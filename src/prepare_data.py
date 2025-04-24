import os
from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.models import train_logistic, train_linear
from src.evaluate import evaluate_classification, evaluate_regression
from src.utils import split_periods

# Parameters
tickers = ["^GSPC", "^GDAXI", "^N225", "XU100.IS", "^BVSP", "^BSESN", "NGE", "PAK"]
start_date = "2005-01-01"
end_date = "2023-12-31"

# Make folders
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

for ticker in tickers:
    print(f"📥 Downloading {ticker}...")
    data = load_data(ticker, start_date, end_date)

    if data.empty:
        print(f"⚠️ Skipping {ticker}: download returned empty data.")
        continue

    # Save raw data
    clean_name = ticker.replace("^", "")
    raw_path = f"data/raw/{clean_name}_{start_date[:4]}_{end_date[:4]}.csv"
    data.to_csv(raw_path, index_label="Date")

    # Preprocess data
    df = preprocess_data(data)

    # Split data by periods
    periods = split_periods(df)

    # You can now proceed with training and evaluating models
    # Example: Train logistic regression on 'Pre-Crisis'
    X = periods['Pre-Crisis'][['Lag_1', 'Lag_2', 'Lag_3']]
    y = periods['Pre-Crisis']['Direction']
    model_logistic = train_logistic(X, y)
    acc = evaluate_classification(model_logistic, X, y)
    print(f"Accuracy for {ticker} (Pre-Crisis): {acc}")
    
    # Save processed data
    processed_path = f"data/processed/{clean_name}_processed.csv"
    df.to_csv(processed_path, index_label="Date")

print("All tickers downloaded, processed, and saved.")
