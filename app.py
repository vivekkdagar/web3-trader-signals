import streamlit as st
from modules.data_loader import DataLoader
from modules.data_processor import DataProcessor
from modules.clustering import Clustering
from modules.regression import RegressionModel
from modules.visualization import Visualization
from modules.insights import Insights


# =====================================
# Streamlit Dashboard
# =====================================
st.set_page_config(layout="wide", page_title="Trader Sentiment Dashboard")
st.title("📈 Trader & Market Sentiment Dashboard")

# 0️⃣ File Uploads
trader_file = st.file_uploader("Upload Trader CSV", type=['csv'])
sentiment_file = st.file_uploader("Upload Fear/Greed CSV", type=['csv'])

# 1️⃣ Load Data
if trader_file and sentiment_file:
    st.success("Files uploaded successfully!")
    loader = DataLoader(trader_file, sentiment_file)
else:
    st.info("Using default CSVs from csv_files folder")
    loader = DataLoader('csv_files/historical_data.csv', 'csv_files/fear_greed_index.csv')

trader_df, sentiment_df = loader.load_data()

# 2️⃣ Process Data
processor = DataProcessor()
merged_df = processor.prepare_data(trader_df, sentiment_df)
filtered_df = merged_df.copy()

st.write(f"Showing data from **{filtered_df['date'].min().date()}** "
         f"to **{filtered_df['date'].max().date()}**")

# 3️⃣ Clustering
clustering = Clustering(filtered_df)
filtered_df = clustering.fit_kmeans()

# 4️⃣ Summary Metrics
avg_pnl = filtered_df['total_pnl'].mean()
avg_volume = filtered_df['total_volume'].mean()
top_cluster = filtered_df['cluster_label'].mode()[0] if 'cluster_label' in filtered_df else 'N/A'

col1, col2, col3 = st.columns(3)
col1.metric("Avg PnL", f"${avg_pnl:,.2f}")
col2.metric("Avg Volume", f"${avg_volume:,.2f}")
col3.metric("Most Profitable Cluster", top_cluster)

# 5️⃣ Buy vs Sell Pie
if 'side' in trader_df.columns:
    st.subheader("Buy vs Sell Trades")
    st.plotly_chart(Visualization.buy_sell_pie(trader_df), use_container_width=True)

# 6️⃣ 3D Cluster Map
st.subheader("3D Trader Cluster Map")
st.plotly_chart(Visualization.cluster_3d(filtered_df), use_container_width=True)

# 7️⃣ Profitability vs Sentiment Time Series
st.subheader("Profitability vs Sentiment")
st.plotly_chart(Visualization.pnl_sentiment_timeseries(filtered_df), use_container_width=True)

# 8️⃣ Regression Model
reg_model = RegressionModel(filtered_df)
model_res = reg_model.fit()
if model_res:
    model, mse, r2 = model_res
    st.subheader("Regression Model Performance")
    st.write(model.summary())
    st.write(f"MSE: {mse:.2f} | R²: {r2:.2f}")
else:
    st.warning("Not enough data for regression model.")

# 9️⃣ Sentiment Gauge
st.subheader("Sentiment Thermometer")
st.plotly_chart(Visualization.sentiment_gauge(filtered_df), use_container_width=True)

# 🔟 Key Insights
st.subheader("Key Insights")
for insight in Insights.compute(filtered_df):
    st.write(f"- {insight}")