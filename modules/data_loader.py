import pandas as pd


def _clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names to lowercase and remove duplicate rows.
    """
    df.columns = df.columns.str.lower()
    return df.drop_duplicates()


def _parse_dates(df: pd.DataFrame, column: str, dayfirst: bool = False) -> pd.DataFrame:
    """Convert a column to datetime and drop invalid rows."""
    df[column] = pd.to_datetime(df[column], errors="coerce", dayfirst=dayfirst)
    return df.dropna(subset=[column])


class DataLoader:
    """
    Load and clean trader & sentiment CSV data.

    Responsibilities:
    - Load raw CSVs
    - Standardize column names
    - Remove duplicates
    - Parse date columns
    - Drop invalid rows
    """

    def __init__(self, trader_file: str, sentiment_file: str):
        self.trader_file = trader_file
        self.sentiment_file = sentiment_file

    def load_data(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        """Load and clean trader and sentiment CSV data."""
        # Load raw CSVs
        trader_df = pd.read_csv(self.trader_file)
        sentiment_df = pd.read_csv(self.sentiment_file)

        # Clean trader data
        trader_df = _clean_dataframe(trader_df)
        trader_df = _parse_dates(trader_df, "timestamp ist", dayfirst=True)

        # Clean sentiment data
        sentiment_df = _clean_dataframe(sentiment_df)
        sentiment_df = _parse_dates(sentiment_df, "date")

        return trader_df, sentiment_df