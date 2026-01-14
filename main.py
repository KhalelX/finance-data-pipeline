from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.analysis import analyze_data


def main():
    print("Iniciando Finance Data Pipeline 🚀")

    extract_data("AAPL")
    transform_data()
    load_data()
    analyze_data()

    print("Pipeline finalizado com sucesso ✅")


if __name__ == "__main__":
    main()