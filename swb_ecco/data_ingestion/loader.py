from abc import ABC
from pathlib import Path

import pandas as pd


class DataLoaderInterface:
    """Define the methods + kwargs that all data loaders classes should have"""

    def retrieve_data() -> pd.DataFrame:
        """Retrieve data from the given source."""
        raise NotImplementedError()
    
    def write_csv() -> None:
        
        raise NotImplementedError()
    

class AbstractDataLoader(DataLoaderInterface, ABC):
    """Implement the methods common to all child classes."""

    def __init__(self, source: str) -> pd.DataFrame:
        self.source = source

    def write_csv(output_df: pd.DataFrame, output_filepath: Path):
        output_df.to_csv(output_filepath)


class DataLoaderOPSD(AbstractDataLoader):

    pass