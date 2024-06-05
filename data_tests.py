import pandas as pd
from pprint import pprint

df = pd.read_csv('data/asx_etp_202401_small.csv')

pprint(df.head())