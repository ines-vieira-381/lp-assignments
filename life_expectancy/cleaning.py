import argparse
import pandas as pd

def clean_data(region='PT'):
    '''
    THIS IS A DOCSTRING Load and clean data
    '''

    df = pd.read_csv("life_expectancy\\data\\eu_life_expectancy_raw.tsv", sep='\t')

    df[['unit', 'sex', 'age', 'region']] = df['unit,sex,age,geo\\time'].str.split(',', expand=True)

    df=df.drop('unit,sex,age,geo\\time', axis=1)

    y_columns = df.columns.to_list()

    df = pd.melt(df,
                    id_vars=['unit', 'sex', 'age', 'region'],
                    value_vars=y_columns,
                    var_name='year',
                    value_name='value'
                    )

    df['year'] = df['year'].astype(int)

    df['value'] = df['value'].replace(': ', pd.NA)
    df['value'] = df['value'].str.replace(r'[^\d.-]', '', regex=True)
    df = df.dropna(subset=['value'])

    df['value'] = df['value'].astype(float)
    df = df[df['region'] == region]

    df.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean data for a specific country.")
    parser.add_argument('--country', type=str, default='PT', help="Country code (default: PT).")
    args = parser.parse_args()
    clean_data(args.country)
