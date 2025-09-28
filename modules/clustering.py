from kneed import KneeLocator
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd


def _find_optimal_k(scaled, n_samples: int) -> int:
    """Determine optimal number of clusters using the elbow method."""
    inertias = []
    K = range(1, min(7, n_samples))
    for k in K:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(scaled)
        inertias.append(km.inertia_)

    knee = KneeLocator(K, inertias, curve='convex', direction='decreasing')
    return knee.knee if knee.knee else 3


class Clustering:
    """
    Apply KMeans clustering on trader performance metrics.

    Responsibilities:
    - Scale features
    - Find optimal number of clusters
    - Assign clusters + labels
    """

    def __init__(self, df: pd.DataFrame, features: list[str] = None):
        if features is None:
            features = ['total_pnl', 'total_volume', 'price_risk']
        self.df = df.copy()
        self.features = features

    def _scale_features(self) -> pd.DataFrame:
        """Standardize numeric features."""
        return StandardScaler().fit_transform(self.df[self.features].fillna(0))

    def fit_kmeans(self) -> pd.DataFrame:
        """Fit KMeans and assign clusters."""
        scaled = self._scale_features()
        n_samples = self.df.shape[0]

        # Edge case: very few samples
        if n_samples < 2:
            self.df['cluster'] = 0
            self.df['cluster_label'] = 'Single Cluster'
            return self.df

        optimal_k = _find_optimal_k(scaled, n_samples)
        km = KMeans(n_clusters=min(optimal_k, n_samples), random_state=42, n_init=10)
        self.df['cluster'] = km.fit_predict(scaled)

        # Assign readable labels
        cluster_labels = {0: "Steady Eddy", 1: "Risk Lover", 2: "Balanced Bob"}
        self.df['cluster_label'] = self.df['cluster'].map(lambda x: cluster_labels.get(x, f"Cluster {x}"))

        return self.df