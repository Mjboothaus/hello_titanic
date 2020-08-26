# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_datapipe.ipynb (unless otherwise specified).

__all__ = ['load_and_cache_raw_data']

# Internal Cell
import os.path
import pandas as pd
#from dateutil.parser import parse
#import datetime as dt

# Cell

# TODO: use st.cache() and also look to pre-load and cache/feather data (or similar) - NB: use of @st.cache() below didn't work
def load_and_cache_raw_data():
    """ Load and/or cache Titanic data set (with known errors) fromm CSV file

    Returns:
        pandas.core.frame.DataFrame: 14 columns
    """
    DATA_PATH = '/Users/mjboothaus/iCloud/Code/Github/titanic-nbdev/data/'
    DATA_FILE = 'titanic3.csv'
    CACHE_FILE = DATA_PATH + 'cache/' + DATA_FILE.replace('.csv', '.feather')

    if os.path.isfile(CACHE_FILE):
        df = pd.read_feather(CACHE_FILE)
        print('Using cached data file...')
    else:
        df = pd.read_csv(DATA_PATH + DATA_FILE)
        df.to_feather(CACHE_FILE)
    return df