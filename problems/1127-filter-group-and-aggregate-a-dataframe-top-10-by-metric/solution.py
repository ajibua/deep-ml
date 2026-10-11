import pandas as pd

def solution(df):
    df = df[df['status']=='completed']
    totals = df.groupby('region', as_index=False)['amount'].sum()
    sort = totals.sort_values('amount', ascending=False).head(10)
    return sort.reset_index(drop=True)