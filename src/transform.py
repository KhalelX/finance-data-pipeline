import pandas as pd


def transform_data():
    print("Transformando dados")

    df = pd.read_csv("data/raw/stock_data.csv")

    # Converter Close para número (força erro virar NaN)
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Calcular retorno diário
    df["daily_return"] = df["Close"].pct_change()

    # Remover linhas inválidas
    df.dropna(inplace=True)

    df.to_csv("data/processed/stock_data_processed.csv", index=False)
    return df
