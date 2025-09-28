import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class Visualization:
    """
    All Plotly visualization functions.
    """

    @staticmethod
    def buy_sell_pie(trader_df: pd.DataFrame):
        """Pie chart of Buy vs Sell trades."""
        trader_df['side_clean'] = trader_df['side'].str.strip().str.capitalize()
        buy_count = (trader_df['side_clean'] == 'Buy').sum()
        sell_count = (trader_df['side_clean'] == 'Sell').sum()

        return px.pie(
            names=['Buy', 'Sell'],
            values=[buy_count, sell_count],
            color_discrete_sequence=['green', 'red'],
            title="Trade Side Distribution"
        )

    @staticmethod
    def cluster_3d(df: pd.DataFrame):
        """3D scatter plot of clusters."""
        return px.scatter_3d(
            df,
            x='total_pnl', y='total_volume', z='price_risk',
            color='cluster_label',
            hover_data=['date'],
            title="Clusters: PnL vs Volume vs Risk"
        )

    @staticmethod
    def pnl_sentiment_timeseries(df: pd.DataFrame):
        """Time series of PnL vs sentiment index."""
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['date'], y=df['total_pnl'], name='Total PnL', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=df['date'], y=df['sentiment_norm'], name='Sentiment Index',
                                 line=dict(color='blue'), yaxis='y2'))
        fig.update_layout(
            yaxis=dict(title='Total PnL'),
            yaxis2=dict(title='Sentiment Index', overlaying='y', side='right'),
            title="PnL vs Sentiment Over Time"
        )
        return fig

    @staticmethod
    def sentiment_gauge(df: pd.DataFrame):
        """Gauge chart of latest sentiment value."""
        latest_sentiment = df['sentiment_norm'].iloc[-1] if not df.empty else 0
        return go.Figure(go.Indicator(
            mode="gauge+number",
            value=float(latest_sentiment * 100),
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "darkblue"},
                   'steps': [
                       {'range': [0, 50], 'color': "red"},
                       {'range': [50, 100], 'color': "green"}]},
            title={'text': "Market Sentiment"}
        ))