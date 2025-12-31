import pandas as pd
import numpy as np

def data_cleaner(file):
    df=pd.read_csv(file)
    df.info()
    df.describe()
    sumDupRows=df.duplicated().sum()
    if sumDupRows>0:
        df.drop_duplicates()
    df=df.fillna('Unknown')
    df=df.replace('',np.nan)
    df=df.replace('nan',np.nan)
    df.replace(r'!@#$%^&\*',np.nan,regex=True)
    
    columnToNum=input('Are there any columns with numbers taken as string. If yes, how many? Else, enter \'0\'')
    for i in columnToNum:
        nameCol=input('Name of the column as it is:')
        df[nameCol]=pd.to_numeric(df[columnToNum],errors='coerce')
    
    columnToDate=input('Are there any columns with dates and (or) times taken as string. If yes, how many? Else, enter \'0\'')
    for i in columnToDate:
        nameCol=input('Name of the column as it is:')
        df[nameCol]=pd.to_datetime(df[columnToNum],errors='coerce')
    print(df)

file_path=input('Enter the path of the file you want to clean the data of:')
df=pd.read_csv(file_path)
file_path = file_path.strip(' "')


data_cleaner(file_path)

