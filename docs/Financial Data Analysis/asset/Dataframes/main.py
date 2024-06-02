import dataframe_image as dfi
import pandas as pd

df = pd.read_csv("asx_etp_202401.csv")
dfi.export(df, '1.png'
           ,max_rows = 10)


