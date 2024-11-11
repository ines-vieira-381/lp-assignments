import argparse
import os
import pandas as pd

from life_expectancy.cleaning import clean_data

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, 'data')

def load_data(path: str) -> pd.DataFrame:
    '''
    Function to load data.
    '''

    return pd.read_csv(path, sep='\t')

def save_data(df: pd.DataFrame, path: str) -> None:
    '''
    Function that saves the data in a csv file.
    '''
    return df.to_csv(path, index=False)

def main(country: str = 'PT') -> None:
    '''
    Function that loads, cleans and saves the pretended data using the
    functions: load_data, clean_data and save_data.

    Parameters:
        country (str): Country code to filter by.
    '''

    input_path = os.path.join(DATA_DIR, 'eu_life_expectancy_raw.tsv')
    output_file_name = f'{country.lower()}_life_expectancy.csv'
    output_path = os.path.join(DATA_DIR, output_file_name)

    data_loaded = load_data(path=input_path)
    data_cleaned = clean_data(df=data_loaded, region=country)
    save_data(df=data_cleaned, path=output_path)

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str,
                        default='PT',
                        help="Country code (default: PT).")
    args = parser.parse_args()
    main(args.country)
