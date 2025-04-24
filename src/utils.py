import pandas as pd

def split_periods(df: pd.DataFrame):
    """Split data into pre-crisis, crisis, and post-crisis periods."""
    return {
        'Pre-Crisis': df.loc['2005-01-01':'2007-12-31'],
        'Crisis': df.loc['2008-01-01':'2009-12-31'],
        'Post-Crisis': df.loc['2010-01-01':'2023-12-31'],
    }
