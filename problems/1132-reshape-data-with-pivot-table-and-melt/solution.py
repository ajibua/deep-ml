import pandas as pd

def solution(df):
    wide = pd.pivot_table(df, index='date', columns='product', values='sales', aggfunc='sum', fill_value=0)
    lon = wide.reset_index().melt(id_vars='date', var_name='product', value_name='sales')

    return lon.sort_values(['date', 'product']).reset_index(drop=True)