from abc import ABC, abstractmethod
import os
import pandas as pd
from life_expectancy.regions import Regions
from life_expectancy.loading_saving import load_data_json, load_data_tsv, save_data
from life_expectancy.cleaning import clean_data, clean_data_json

class FileStrategy(ABC):

    """ Strategy to load, clean and save different types of files. """

    @abstractmethod
    def load_strategy(self, path : str):
        """ Loads the data. """

    def clean_strategy(self, df: pd.DataFrame, region: Regions):
        """ Cleans the data. """

    def save_strategy(self, df: pd.DataFrame, path: str):
        """ Saves the cleaned data. """

class JSONStrategy(FileStrategy):

    """ Class to load clean and save files in json."""

    def load_strategy(self, path):
        """ Function to load the data file in JSON. """
        return load_data_json(path)

    def clean_strategy(self, df: pd.DataFrame, region: Regions):
        """ Function to clean the data file in JSON. """
        return clean_data_json(df, region)

    def save_strategy(self, df, path):
        """ Function to save the data file. """
        save_data(df,path)

class TSVStrategy(FileStrategy):

    """ Class to load clean and savefiles in tsv."""

    def load_strategy(self, path):
        """ Function to load the data file in tsv. """
        return load_data_tsv(path)

    def clean_strategy(self, df: pd.DataFrame, region: Regions):
        """ Function to clean the data file in tsv. """
        return clean_data(df, region )

    def save_strategy(self, df, path):
        """ Function to save the data file. """
        save_data(df, path)

def handle_file(path):
    """Handles file operations (load, clean, save) based on file extension."""
    strategies = {
        '.tsv': TSVStrategy,
        '.json': JSONStrategy
    }

    _, ext = os.path.splitext(path)
    try:
        strategy_class = strategies[ext]
        return strategy_class()
    except KeyError as exc:
        raise ValueError(f"Unsupported file extension: {ext}") from exc
    except TypeError as exc:
        raise ValueError(f"Error initializing strategy for file extension: {ext}") from exc
