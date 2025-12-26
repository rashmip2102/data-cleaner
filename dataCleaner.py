import pandas as pd
import numpy as np

def data_cleaner(file):
    df=pd.read_csv(file)
    df.info()
    df.describe()
    sumDupRows=df.duplicated().sum()
    df=df.fillna('Unknown')
    df=df.replace('',np.nan)
    df=df.replace('nan',np.nan)
    df.replace(r'!@#$%^&\*',np.nan,regex=True)

file_path=input('Enter the path of the file you want to clean the data of:')
file_path = file_path.strip(' "')
data_cleaner(file_path)

