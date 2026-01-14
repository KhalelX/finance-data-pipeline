import pandas as pd
import matplotlib.pyplot as plt


def analyze_data():
    print("Gerando análise de dados")
    df = pd.read_csv("data/processed/stock_data_processed.csv")

    df["Close"].plot(title="Preço de Fechamento do Ativo")
    plt.savefig("data/processed/close_price.png")
    plt.close()
