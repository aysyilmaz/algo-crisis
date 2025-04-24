import yfinance as yf

def load_data(ticker: str, start: str, end: str):
    """Downloads data from Yahoo Finance."""
    data = yf.download(ticker, start=start, end=end)
    return data
