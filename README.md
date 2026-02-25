# Finance Data Pipeline (ETL + SQLite + Análise de Dados)

Pipeline de dados financeiros desenvolvido em Python, simulando um fluxo real de **extração, transformação e carga (ETL)** para análise de dados e geração de insights.

O projeto demonstra na prática conceitos de **Data Engineering, automação de dados e análise financeira**, com armazenamento estruturado e preparação para BI.

---

## 🎯 Objetivo

Construir um pipeline de dados que:

✔️ Extrai dados financeiros (simulados ou reais)  
✔️ Realiza limpeza e transformação dos dados  
✔️ Armazena os dados em banco SQLite  
✔️ Permite análise e geração de insights  
✔️ Simula um fluxo real de dados financeiros  

---

## 🧠 Arquitetura do Projeto

Fluxo da pipeline:

Fonte de Dados → extract.py → transform.py → load.py (SQLite) → Análise

- **extract.py**: coleta dados financeiros  
- **transform.py**: limpeza, padronização e cálculo de métricas  
- **load.py**: carga dos dados no banco SQLite  
- **analysis.py** (opcional): análise e geração de insights  

Este fluxo segue o padrão ETL amplamente utilizado em pipelines de dados :contentReference[oaicite:0]{index=0}

---

## ⚙️ Tecnologias Utilizadas

| Ferramenta | Finalidade |
|------------|------------|
| Python | Orquestração do pipeline |
| Pandas | Manipulação e transformação de dados |
| SQLAlchemy | Integração com banco de dados |
| SQLite | Armazenamento estruturado |
| Matplotlib / Pandas | Análise e visualização |

---

## 🔄 Etapas do Pipeline

### 🟢 1. Extração (extract.py)
- Coleta dados financeiros  
- Leitura de fontes (CSV/API/simulação)  

### 🟡 2. Transformação (transform.py)
- Limpeza de dados  
- Conversão de tipos  
- Cálculo de métricas financeiras  
- Padronização de colunas  

### 🔵 3. Carga (load.py)
- Inserção dos dados no SQLite  
- Criação de tabelas estruturadas  

### 🟣 4. Análise (analysis.py)
- Geração de insights  
- Visualização de dados financeiros  

---

## 🚀 Resultados

- Estruturação de pipeline ETL completo  
- Organização de dados financeiros para análise  
- Redução de inconsistências e melhoria da qualidade dos dados  
- Base pronta para dashboards e KPIs  
- Simulação de cenário real de Data Engineering  

---

## 🚀 Como Executar o Projeto

### 1. Criar ambiente virtual

#### Windows
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
