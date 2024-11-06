import argparse
import os
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(SCRIPT_DIR, 'data')

def load_data(path: str) -> pd.DataFrame:
    '''
    Function to load data.

    Parameters: 
        path (str): path of the data to be loaded.

    Returns:
        pd.DataFrame: dataframe of the loaded data.
    '''

    return pd.read_csv(path, sep='\t')

def clean_data(df: pd.DataFrame, region: str = 'PT') -> pd.DataFrame:
    '''
    Function to clean the data. Unpivots the data, ensures that year is an int,
    ensures value is a float, removes the Nan values and
    filters the data by the country code (default = 'PT').

    Parameters:
        df (pd.DataFrame): dataframe of the data to be cleaned.
        region (str): country code to filter the data by, the default is 'PT'.

    Returns:
        pd.DataFrame: dataframe of the cleaned data.
    '''

    # Unpivoting the data
    df[['unit', 'sex', 'age', 'region']] = df['unit,sex,age,geo\\time'].str.split(',', expand=True)

    df=df.drop('unit,sex,age,geo\\time', axis=1)

    y_columns = df.columns.to_list()

    df = pd.melt(df,
                    id_vars=['unit', 'sex', 'age', 'region'],
                    value_vars=y_columns,
                    var_name='year',
                    value_name='value'
                    )

    # Making sure year is of int type
    df['year'] = df['year'].astype(int)

    # Taking care of the Nan values and guaranteeing that value is of float type
    df['value'] = df['value'].replace(': ', pd.NA)
    df['value'] = df['value'].str.replace(r'[^\d.-]', '', regex=True)
    df = df.dropna(subset=['value'])

    df['value'] = df['value'].astype(float)

    # Filtering the data by the chosen country
    return df[df['region'] == region]

def save_data(df: pd.DataFrame, path: str) -> None:
    '''
    Function that saves the data in a csv file.

    Parameters:
        df (pd.dataFrame): dataframe of the data that will be saved in a csv file.
        path (str): path to save the data on.
    '''
    return df.to_csv(path, index=False)

def main(country: str = 'PT') -> None:
    '''

    Function that loads, cleans and saves the pretended data using the
    functions: load_data, clean_data and save_data.

    Parameters:
        country (str): Country code to filter by.
    '''

    input_path = os.path.join(DATA_PATH, 'eu_life_expectancy_raw.tsv')
    output_file_name = f'{country.lower()}_life_expectancy.csv'
    output_path = os.path.join(DATA_PATH, output_file_name)

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
