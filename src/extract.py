import yfinance as yf


def extract_data(ticker="AAPL", period="1y"):
    print(f"Coletando dados do ativo {ticker}")
    df = yf.download(ticker, period=period)
    df.reset_index(inplace=True)
    df.to_csv("data/raw/stock_data.csv", index=False)
    return df
