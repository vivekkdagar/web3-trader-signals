import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


class RegressionModel:
    """
    Fit regression model of PnL vs sentiment and features.

    Responsibilities:
    - Add lagged sentiment
    - Fit OLS model
    - Return performance metrics
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.model = None
        self.reg_df = None

    def _prepare_features(self) -> pd.DataFrame:
        """Create lagged features and drop missing rows."""
        reg_df = self.df[['total_pnl', 'sentiment_norm', 'total_volume', 'price_risk']].copy()
        reg_df['sentiment_lag1'] = reg_df['sentiment_norm'].shift(1)
        reg_df.dropna(inplace=True)
        return reg_df

    def fit(self):
        """Fit OLS regression model."""
        self.reg_df = self._prepare_features()
        if self.reg_df.shape[0] < 2:
            return None

        X = self.reg_df[['sentiment_norm', 'sentiment_lag1', 'total_volume', 'price_risk']]
        y = self.reg_df['total_pnl']
        X_sm = sm.add_constant(X)

        self.model = sm.OLS(y, X_sm).fit()
        self.reg_df['predicted_pnl'] = self.model.predict(X_sm)

        mse = mean_squared_error(y, self.reg_df['predicted_pnl'])
        r2 = r2_score(y, self.reg_df['predicted_pnl'])
        return self.model, mse, r2