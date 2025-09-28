# web3-trading-behavior-dashboard
# 📈 Web3 Trader Behavior Dashboard

> **Decoding Profitability:** An Analysis of Trader Behavior and Bitcoin Sentiment

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)  
[![License](https://img.shields.io/github/license/vivekkdagar/web3-trader-signals)](https://github.com/vivekkdagar/web3-trader-signals/blob/main/LICENSE)  
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Framework-38bdf8?logo=tailwind-css)](https://tailwindcss.com/)  
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)](https://scikit-learn.org/stable/modules/clustering.html)

---

## 📑 Table of Contents
- [🎯 Project Overview (STAR Methodology)](#-project-overview-star-methodology)
- [⚙️ Technical Deep Dive (Modules)](#️-technical-deep-dive-the-docs--modules)
- [📊 Datasets](#-datasets)
- [💻 Skills Utilized](#-skills-utilized)
- [🚀 How to Run It](#-how-to-run-it)

---

## [🎯 Project Overview (STAR Methodology)](#-project-overview-star-methodology)

This project leverages **advanced data science techniques** to statistically analyze the relationship between **daily trader performance** and **market sentiment** in the Bitcoin ecosystem.  

The aim: go beyond simple correlation and uncover **actionable, data-driven factors** that drive **daily profitability**.

---

<details>
<summary><b>⭐ Situation</b></summary>

The **DeFi/Web3 trading space** is defined by **high volatility** and **emotional decision-making**.  
Most traders rely on intuition or basic indicators without understanding **non-linear relationships** between **market sentiment** and **profitability**.
</details>

---

<details>
<summary><b>🌟 Task</b></summary>

Build a robust **data pipeline + analytical dashboard** capable of:
1. Integrating **200K+ trader transactions** with the **daily Fear & Greed Index**.
2. Applying **OLS Regression** to quantify the impact of **sentiment, volume, and risk** on PnL.
3. Using **K-Means Clustering** to segment trading days into behavioral profiles.
</details>

---

<details>
<summary><b>✨ Action</b></summary>

| Step | Action | Tools/Techniques |
| :--- | :--- | :--- |
| **Data Ingestion** | Load & clean CSVs, standardize columns, validate dates | `pandas`, Custom `DataLoader` |
| **Feature Engineering** | Aggregate trades daily → compute `total_pnl`, `total_volume`, `price_risk` | `pandas`, `DataProcessor` |
| **Statistical Modeling** | Apply OLS Regression with lagged sentiment feature | `statsmodels` |
| **Behavioral Segmentation** | Use K-Means ($k=3$) on scaled features → clusters | `scikit-learn`, `kneed` |
| **Deployment** | Build interactive dashboard | `Streamlit` |
</details>

---

<details open>
<summary><b>💡 Result</b></summary>

- 📊 **Volume is King** → **Total Volume** = **only statistically significant predictor** of daily PnL (p ≈ 0.000).  
- 😮 **Sentiment ≠ Profitability** → **Fear & Greed Index** (current + lagged) = **insignificant** (p > 0.17).  
- 🧑‍🤝‍🧑 **Three Trader Profiles Identified** via clustering:
  1. **Risk Lover** → High Volume, High Risk  
  2. **Balanced Bob** → Moderate Metrics  
  3. **Steady Eddy** → Low PnL, Low Risk, Low Volume  
</details>

---

## [⚙️ Technical Deep Dive (The `docs` & Modules)](#️-technical-deep-dive-the-docs--modules)

<details open>
<summary><b>Click to Expand Module Details</b></summary>

| Module | Description | Key Components |
| :--- | :--- | :--- |
| `data_loader.py` | Loads & cleans raw CSVs, parses dates | `_clean_dataframe`, `DataLoader` |
| `data_processor.py` | Aggregates 200K+ rows into daily metrics, merges with sentiment | `_aggregate_trader`, `_normalize_sentiment` |
| `regression.py` | Builds OLS Regression, includes `sentiment_lag1` | `_prepare_features`, `RegressionModel` |
| `clustering.py` | Implements K-Means, finds optimal $k$ with Elbow Method | `_find_optimal_k`, `Clustering` |
| `streamlit_app.py` | Main dashboard → runs models + renders plots | `st.file_uploader`, `Visualization` |
</details>

---

## [📊 Datasets](#-datasets)

<details>
<summary><b>Show Dataset Links</b></summary>

- 📂 **Trader Transactions (200K+ rows):**  
  [🔗 Google Drive Link](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing)  

- 📂 **Fear & Greed Index:**  
  [🔗 Google Drive Link](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing)  
</details>

---

## [💻 Skills Utilized](#-skills-utilized)

<details open>
<summary><b>Click to Expand</b></summary>

| Category | Skills & Tools |
| :--- | :--- |
| **Data Science** | OLS Regression, K-Means, Feature Engineering, Time Series Analysis, EDA, Significance Testing |
| **Python Ecosystem** | `pandas`, `numpy`, `scikit-learn`, `statsmodels`, `kneed` |
| **Visualization & Deployment** | `Streamlit`, `Plotly`, Modular Programming, Tailwind CSS, Chart.js |
</details>

---

## [🚀 How to Run It](#-how-to-run-it)

<details open>
<summary><b>Setup & Installation</b></summary>

### 🔧 Prerequisites
- **Python 3.9+** installed  
- Recommended: use a **virtual environment**

---

### 1. Clone the Repo
```bash
git clone https://github.com/vivekkdagar/web3-trader-signals.git
cd web3-trader-signals
