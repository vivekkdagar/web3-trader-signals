import pandas as pd


class DataProcessor:
    """
    Prepare trader & sentiment data for analysis.

    Responsibilities:
    - Aggregate trader data daily
    - Merge with sentiment scores
    - Normalize sentiment
    """

    @staticmethod
    def _aggregate_trader(trader_df: pd.DataFrame) -> pd.DataFrame:
        """Aggregate trader data into daily totals."""
        trader_daily = trader_df.groupby(trader_df['timestamp ist'].dt.date).agg({
            'closed pnl': 'sum',
            'size usd': 'sum',
            'execution price': 'std'
        }).reset_index()

        trader_daily.columns = ['date', 'total_pnl', 'total_volume', 'price_risk']
        trader_daily['date'] = pd.to_datetime(trader_daily['date'])
        return trader_daily

    @staticmethod
    def _normalize_sentiment(df: pd.DataFrame) -> pd.DataFrame:
        """Min-max normalize sentiment values to [0, 1]."""
        df['sentiment_norm'] = (
            (df['sentiment_score'] - df['sentiment_score'].min()) /
            (df['sentiment_score'].max() - df['sentiment_score'].min())
        )
        return df

    @classmethod
    def prepare_data(cls, trader_df: pd.DataFrame, sentiment_df: pd.DataFrame) -> pd.DataFrame:
        """Aggregate trader data and merge with sentiment index."""
        trader_daily = cls._aggregate_trader(trader_df)

        # Merge sentiment
        merged_df = pd.merge(trader_daily, sentiment_df[['date', 'value']], on='date', how='inner')
        merged_df.rename(columns={'value': 'sentiment_score'}, inplace=True)

        # Normalize sentiment
        merged_df = cls._normalize_sentiment(merged_df)
        return merged_df