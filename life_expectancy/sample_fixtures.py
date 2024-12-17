import argparse
import os
import pandas as pd
from cleaning import clean_data, clean_data_json
from life_expectancy.regions import Regions

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_PATH, 'data')
FIXTURES_PATH = os.path.join(BASE_PATH, 'tests\\fixtures\\')

def creating_new_fixtures(country: Regions = Regions.PT):
    '''
    Function to create new fixtures.
    '''
    data_to_sample = pd.read_csv(DATA_PATH + '/eu_life_expectancy_raw.tsv', sep='\t')
    sample_data_input = data_to_sample.sample(n=400, random_state= 4)
    sample_data_input.to_csv(FIXTURES_PATH + 'eu_life_expectancy_raw_sample.tsv', sep='\t', index=False)

    sample_data_cleaned = clean_data(sample_data_input,country)
    sample_data_cleaned.to_csv(FIXTURES_PATH + 'eu_life_expectancy_raw_sample_expected.csv', index=False)

def json_fixtures(country: Regions = Regions.PT):
    """
    Function to create new json fixtures.
    """
    data_to_sample = pd.read_json(DATA_PATH + '/eurostat_life_expect.json')
    sample_data_input = data_to_sample.sample(n=1400, random_state= 4)
    sample_data_input.to_json(FIXTURES_PATH + 'eurostat_json_sample.json', orient='records')

    sample_data_cleaned = clean_data_json(sample_data_input,country)
    sample_data_cleaned.to_csv(FIXTURES_PATH + 'eurostat_json_sample_expected.csv', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=lambda x: Regions[x], default=Regions.PT,
                        help='Country code to filter data (default: PT)')
    args = parser.parse_args()
    creating_new_fixtures(args.country)
    json_fixtures(args.country)
