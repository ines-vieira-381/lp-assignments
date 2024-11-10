"""Tests for the cleaning module"""
import os
import sys
from unittest.mock import patch
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cleaning import clean_data
from loading_saving import load_data, save_data

def test_clean_data(eu_life_expectancy_raw_sample, eu_life_expectancy_raw_sample_expected):
    """ 
    Function to test if the clean_data function cleans the data correctly.
    """

    data_to_test = eu_life_expectancy_raw_sample
    expected_result = eu_life_expectancy_raw_sample_expected
    cleaned_data = clean_data(data_to_test)
    cleaned_data.reset_index(drop=True, inplace=True)

    pd.testing.assert_frame_equal(
        cleaned_data, expected_result)

def test_load_data(eu_life_expectancy_raw_sample):
    """ 
    Function to test if the load_data function correctly loads the data.
    """

    with patch('pandas.read_csv', return_value=eu_life_expectancy_raw_sample):
        data = load_data("the_data_path.csv")
        assert data.equals(eu_life_expectancy_raw_sample)

def test_save_data():
    """ 
    Function to test if the load_data function correctly saves the data.
    """

    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        save_data(df, "the_data_path.csv")
        mock_to_csv.assert_called_once_with("the_data_path.csv", index=False)
