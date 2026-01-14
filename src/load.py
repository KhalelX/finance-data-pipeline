import pandas as pd
import sqlite3


def load_data():
    print("Carregando dados no banco SQLite")
    df = pd.read_csv("data/processed/stock_data_processed.csv")

    conn = sqlite3.connect("data/finance.db")
    df.to_sql("stocks", conn, if_exists="replace", index=False)
    conn.close()
