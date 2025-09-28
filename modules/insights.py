import pandas as pd


class Insights:
    """
    Generate insights from trader and sentiment data.

    Responsibilities:
    - Correlation analysis
    - Fear vs Greed profitability
    - Lead/lag relationships
    """

    @staticmethod
    def compute(df: pd.DataFrame) -> list[str]:
        if df.empty:
            return ["No data available"]

        insights = []

        # Correlation analysis
        corr = df[['total_pnl', 'total_volume', 'price_risk', 'sentiment_norm']].corr()
        top_metric = corr['sentiment_norm'].drop('sentiment_norm').idxmax()
        insights.append(
            f"Strongest correlation with sentiment: {top_metric} "
            f"(corr={corr['sentiment_norm'][top_metric]:.2f})"
        )

        # Fear vs Greed profitability
        fear_periods = df[df['sentiment_score'] < 50]
        greed_periods = df[df['sentiment_score'] >= 50]
        avg_pnl_fear = fear_periods['total_pnl'].mean()
        avg_pnl_greed = greed_periods['total_pnl'].mean()

        if avg_pnl_fear > avg_pnl_greed:
            insights.append(f"Traders more profitable during FEAR (Avg PnL {avg_pnl_fear:.2f}) vs GREED ({avg_pnl_greed:.2f})")
        else:
            insights.append(f"Traders earn more during GREED (Avg PnL {avg_pnl_greed:.2f}) vs FEAR ({avg_pnl_fear:.2f})")

        # Price risk correlation
        lead_corr = df[['price_risk', 'sentiment_norm']].corr().iloc[0, 1]
        if abs(lead_corr) > 0.3:
            insights.append(f"Price risk leads sentiment (corr={lead_corr:.2f})")

        return insights