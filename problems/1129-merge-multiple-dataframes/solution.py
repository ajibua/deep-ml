import pandas as pd

def solution(df1, df2, df3):
    merged = pd.merge(df1, df2, on='emp_id', how='inner')

    merged_df3 = pd.merge(merged, df3, on='emp_id', how='left')

    return merged_df3