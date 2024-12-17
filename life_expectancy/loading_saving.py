import pandas as pd

def load_data_tsv(path: str) -> pd.DataFrame:
    '''
    Function to load data that is in tsv.
    '''
    return pd.read_csv(path, sep='\t')

def load_data_json(path: str) -> pd.DataFrame:
    '''
    Function to load data that is in json.
    '''
    return pd.read_json(path)

def save_data(df: pd.DataFrame, path: str) -> None:
    '''
    Function that saves the data in a csv file.
    '''
    return df.to_csv(path, index=False)
