"""Tests for the cleaning module"""
import pandas as pd
from life_expectancy.cleaning import clean_data

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
