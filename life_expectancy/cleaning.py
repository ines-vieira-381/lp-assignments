import pandas as pd
from life_expectancy.regions import Regions

def clean_data(df: pd.DataFrame, region: Regions = Regions.PT) -> pd.DataFrame:
    '''
    Function to clean the data. Unpivots the data, ensures that year is an int,
    ensures value is a float, removes the Nan values and
    filters the data by the country code (default = 'PT').
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
    return df[df['region'] == region.name]

def clean_data_json(df: pd.DataFrame, region: Regions = Regions.PT) -> pd.DataFrame:
    '''
    Function to clean the data. Unpivots the data, ensures that year is an int,
    ensures value is a float, removes the Nan values and
    filters the data by the country code (default = 'PT').
    '''

    # Changing the columns names and erasing the ones not needed
    df.rename(columns={'country': 'region'}, inplace = True)
    df.rename(columns={'life_expectancy': 'value'}, inplace = True)
    df.drop(columns=['flag', 'flag_detail'], inplace = True)

    # Making sure year is of int type and that the value is a float
    df['year'] = df['year'].astype(int)
    df['value'] = df['value'].astype(float)

    # Filtering the data by the chosen country
    return df[df['region'] == region.name]
