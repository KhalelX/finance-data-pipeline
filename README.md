# Finance Data Pipeline
![CI](https://github.com/KhalelX/finance-data-pipeline/actions/workflows/pipeline.yml/badge.svg)

Pipeline automatizado para **coleta, transformação, armazenamento e análise de dados financeiros**, desenvolvido em Python com foco em **Análise de Dados e DevOps**.

---

##  Visão Geral
Este projeto implementa um **pipeline ETL financeiro** que:
- Coleta dados de mercado via API
- Realiza limpeza e transformação dos dados
- Armazena os dados em banco SQLite
- Gera análises e visualizações automatizadas

O objetivo é demonstrar habilidades práticas em **Python, dados financeiros e automação**, com boas práticas de **DevOps** (CI/CD e Docker).

---

##  Tecnologias Utilizadas
- Python 3.10
- Pandas
- NumPy
- yFinance
- Matplotlib
- SQLite
- Git / GitHub
- GitHub Actions (CI/CD)
- Docker

---

##  Estrutura do Projeto

```text
Finance-data-pipeline/
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── finance.db
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── analysis.py
├── tests/
├── .dockerignore
├── Dockerfile
├── main.py
├── requirements.txt
├── requirements-lock.txt
└── README.md
