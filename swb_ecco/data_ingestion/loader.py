from abc import ABC
from pathlib import Path

import pandas as pd


class DataLoaderInterface:
    """Define the methods + kwargs that all data loaders classes should have."""

    def retrieve_normalised_data() -> pd.DataFrame:
        """Retrieve data from this source normalised in the format required by PyPSA."""
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
    """
    Implement the methods common to all child classes.

    Most sources will only need to implement the `format_data` method in their child class.
    """

    def __init__(self, source: str) -> pd.DataFrame:
        self.source = source
        self.raw_df = None
        self.normalised_df = None

    def retrieve_normalised_data(self):
        """Retrieve data from this source normalised in the format required by PyPSA.

        Returns
        -------
        pd.DataFrame
            DataFrame of normalised data, i.e. the source data wrangled into the format required by PyPSA.
        """
        self.raw_df = self.load_raw_data()
        self.normalised_df = self.format_data(self.raw_df)

        return self.normalised_df

    def load_raw_data(self) -> pd.DataFrame:
        """Load raw data from a CSV at the given source URL.

        Data loaders for sources which are not CSV files can overwrite this method in the child class,
        but this will likely be common enough to belong in the base class.

        Returns
        -------
        pd.DataFrame
            The raw data, i.e. a pandas DataFrame of the source data with minimal modifications.
        """
        return pd.read_csv(self.source)

    def write_csv(self, output_filepath: Path, **kwargs) -> None:
        """Write the normalised data to a CSV file.

        Parameters
        ----------
        output_filepath: Path
            Filepath to write the DataFrame to.
        """
        self.normalised_df.to_csv(output_filepath, **kwargs)
