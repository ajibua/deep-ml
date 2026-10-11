import pandas as pd
def solution(df):
    keep_cols = [c for c in df.columns if df[c].isna().mean() <= 0.5]
    df = df[keep_cols]

    nan_row = df.isna().mean(axis=1)
    df = df[nan_row <= 0.5].copy()
    for c in df.columns:
        if pd.api.types.is_numeric_dtype(df[c]) is True:
            df[c] = df[c].fillna(df[c].mean())
        else:
            df[c] = df[c].fillna(df[c].mode()[0])
    return df 