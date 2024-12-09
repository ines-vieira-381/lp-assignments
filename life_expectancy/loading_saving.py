import pandas as pd

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
