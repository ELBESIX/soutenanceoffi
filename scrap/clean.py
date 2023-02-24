import pandas as pd
import numpy as np
import re

data = pd.read_csv('lol.csv')
print(data)


def tests(data,columns):
    print(data.dtypes)
    print(data.isnull().sum())
    data_null = data.isnull().sum()
    print(data_null[data_null>0])
    print(data.loc[data[columns].duplicated(keep=False),:])
tests(data,["name"])

def duplicate(data,columns):
    data.drop_duplicates(subset=columns, inplace=True, ignore_index=True)

def clean(data,columns):
    duplicate(data,columns)
    data.to_csv("cleaned.csv", index=False)

# clean(data,["name"])