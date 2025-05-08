# swb_ecco

## 0. Background
This repository contains for data ingestion and modelling of energy systems in Europe and northern Africa.


## 1. Dev Environment Setup
Create an environment.

```shell
conda create -n ecco python=3.11
conda activate ecco
pip install -e .
pip install -r requirements-dev.txt
```

Recompile requirements. 
This is only required if you are adding new dependencies to the project or upgrading existing libraries.

```shell
pip install pip-tools
pip-compile requirements.in --upgrade
pip-compile requirements-dev.in --upgrade
```

## 2. Style and Testing
Testing is done using `pytest`.

Docstrings conform to the [numpy docstring style guide](https://numpydoc.readthedocs.io/en/latest/format.html) 
and `flake8` is used to lint.


## 3. Repo Structure

There is a broad split between `modelling` and `data_ingestion`.

### 3.1. Data Ingestion

The `data_ingestion` subdirectory has the data loader classes to ingest data from different sources.
The general idea (this is a work-in-progress subject to change as we discover more about the data requirements) is to have a common API for the different sources. 


The typical use case for each would be to call the `retrieve_normalised_data` method.

As an example, there is an implementation to load data from Open Power System Data (OPSD).

```python
from swb_ecco.data_ingestion.loader import DataLoaderOPSD

SOURCE_URL = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"
opsd_loader = DataLoaderOPSD(source=SOURCE_URL)
opsd_df = opsd_loader.retrieve_normalised_data()
opsd_loader.write_csv('/path/to/file.csv')
```


The idea is that as we add more sources, there will be a common interface for each. So, say we add Scigrid data. The code from the user's point of view would be almost identical:

```python
from swb_ecco.data_ingestion.loader import DataLoaderScigrid

# Create the data loader
SOURCE_URL = "some/source/url/goes/here"
scigrid_loader = DataLoaderScigrid(source=SOURCE_URL)
scigrid_df = scigrid_loader.retrieve_normalised_data()
scigrid_loader.write_csv('/path/to/file.csv')
```

If we want to implement a new data loader, say from some new source called "XYZ", we create a class inheriting from `AbstractDataLoader` and implement the methods below. 
In most cases, we'd only actually need to implement `format_data` to handle the logic specific to this source; the `load_raw_data` and `write_csv` methods are handled in the parent class and are pretty generic.

```python
from swb_ecco.data_ingestion.loader import AbstractDataLoader

class DataLoaderXYZ(AbstractDataLoader):

    def load_raw_data():
        # Load raw data from the source. 
        # If this is just reading a CSV file from some URL, that's already implemented in the base class,
        # so you can skip this method
        pass

    def format_data():
        # This is where the source-specific logic goes, to wrangle the data into a format that is compatible with PyPSA
        pass

```

We can also extend the interface if we need to. Say, for example, we later decide we want files in parquet format rather than csv. We could add a `write_parquet` method to `DataLoaderInterface` and implement it in `AbstractDataLoader` as:

```python
def write_parquet():
    self.normalised_df.to_parquet(output_filepath, **kwargs)
```


### 3.2. Modelling

This has code and config related to modelling scenarios using [PyPSA-Earth](https://github.com/pypsa-meets-earth/pypsa-earth/tree/main)