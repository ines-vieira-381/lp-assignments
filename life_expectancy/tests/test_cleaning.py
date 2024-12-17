"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data, clean_data_json

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

def test_clean_data_json(eurostat_json_sample, eurostat_json_sample_expected):
    
    data_to_test = eurostat_json_sample
    expected_result = eurostat_json_sample_expected
    cleaned_data = clean_data_json(data_to_test)
    cleaned_data.reset_index(drop=True, inplace=True)

    pd.testing.assert_frame_equal(
        cleaned_data, expected_result)