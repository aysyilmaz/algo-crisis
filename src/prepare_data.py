
import yfinance as yf
import pandas as pd
import os

tickers = ["^GSPC", "^GDAXI", "^N225", "XU100.IS", "^BVSP", "^BSESN", "NGE", "PAK"]
start_date = "2005-01-01"
end_date = "2023-12-31"

# Make folders
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

for ticker in tickers:
    print(f"📥 Downloading {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print(f"⚠️ Skipping {ticker}: download returned empty data.")
        continue

    # Save raw file
    clean_name = ticker.replace("^", "")
    raw_path = f"data/raw/{clean_name}_{start_date[:4]}_{end_date[:4]}.csv"
    data.to_csv(raw_path, index_label="Date")

    # Check column before processing
    if 'Close' not in data.columns:
        print(f"⚠️ Skipping {ticker}: 'Close' column not found.")
        continue

    # Preprocess
    df = data.copy()
    df['Return'] = df['Close'].pct_change()
    df['Direction'] = (df['Return'] > 0).astype(int)
    for i in range(1, 4):
        df[f'Lag_{i}'] = df['Return'].shift(i)
    df.dropna(inplace=True)

    # Save processed
    processed_path = f"data/processed/{clean_name}_processed.csv"
    df.to_csv(processed_path, index_label="Date")
    print(f"✅ Finished {ticker}")

print("All tickers downloaded and processed.")
