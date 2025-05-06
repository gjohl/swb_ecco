from abc import ABC
from pathlib import Path

import pandas as pd


class DataLoaderInterface:
    """Define the methods + kwargs that all data loaders classes should have"""

    def retrieve_normalised_data() -> pd.DataFrame:
        """Retrieve data from this source normalised into the format required by PyPSA."""
        raise NotImplementedError()

    def load_raw_data() -> pd.DataFrame:
        """Load raw data from the given source."""
        raise NotImplementedError()

    @staticmethod
    def format_data(raw_data: pd.DataFrame) -> pd.DataFrame:
        """Wrangle the raw data to the required output format."""
        raise NotImplementedError()

    def write_csv(self, output_filepath: Path, **kwargs) -> None:
        """Write the normalised data to a CSV file."""
        raise NotImplementedError()


class AbstractDataLoader(DataLoaderInterface, ABC):
    """Implement the methods common to all child classes."""

    def __init__(self, source: str) -> pd.DataFrame:
        self.source = source
        self.raw_df = None
        self.normalised_df = None

    def retrieve_normalised_data(self):
        """Retrieve the normalised data by loading the raw data and then applying any necessary formatting."""
        self.raw_df = self.load_raw_data()
        self.normalised_df = self.format_data(self.raw_df)

        return self.normalised_df

    def write_csv(self, output_filepath: Path, **kwargs) -> None:
        """Write the normalised data to a CSV file."""
        self.normalised_df.to_csv(output_filepath, **kwargs)


class DataLoaderOPSD(AbstractDataLoader):
    """Data loader for Open Power System Data.

    Example
    -------
    from swb_ecco.data_ingestion.loader import DataLoaderOPSD

    # Create the data loader
    SOURCE_URL = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv"
    opsd_loader = DataLoaderOPSD(SOURCE_URL)

    # Load normalised data
    df = opsd_loader.retrieve_normalised_data()

    # Save the output to CSV
    opsd_loader.write_csv('/path/to/file.csv')
    """

    def load_raw_data(self) -> pd.DataFrame:
        """Load raw data from the given source."""
        return pd.read_csv(self.source)

    @staticmethod
    def format_data(raw_data: pd.DataFrame) -> pd.DataFrame:
        """Format the raw OPSD data.

        For this first iteration we'll just filter on the `load_actual_entsoe_transparency`.
        This is just an arbitrary placeholder until we know which data is actually useful;
        it's easy enough to change `base_field_name` to some other column.
        """
        base_field_name = 'load_actual_entsoe_transparency'
        timestamp_col = 'utc_timestamp'

        # Filter on the required columns plus a timestamp column
        data_cols = [k for k in raw_data.columns if base_field_name in k]
        filter_cols = [timestamp_col] + data_cols
        col_name_mapping = {k: k.replace(f"_{base_field_name}", "") for k in data_cols}

        output_df = (raw_data[filter_cols]
                     .rename(columns=col_name_mapping)
                     .set_index(timestamp_col))

        return output_df
