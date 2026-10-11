import pandas as pd

def solution(df):
    df = df[df['status']=='completed']
    totals = df.groupby('region', as_index=False)['amount'].sum()
    sort = totals.sort_values(by='region')
    larg = sort.head(10)
    return larg.reset_index(drop=True)