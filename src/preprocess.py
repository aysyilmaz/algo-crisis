import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """Preprocesses the raw data by adding features."""
    df['Return'] = df['Adj Close'].pct_change()
    df['Direction'] = (df['Return'] > 0).astype(int)
    for i in range(1, 4):
        df[f'Lag_{i}'] = df['Return'].shift(i)
    df.dropna(inplace=True)
    return df
