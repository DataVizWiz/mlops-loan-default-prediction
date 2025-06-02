import pandas as pd

from typing import List
from sklearn.base import BaseEstimator, TransformerMixin


class DropColumns(BaseEstimator, TransformerMixin):
    """Custom transformer to drop columns"""

    def __init__(self, to_drop: List[str] = None):
        self.to_drop = to_drop

    def fit(self):
        return self

    def transform(self, X: pd.DataFrame):
        return X.drop(columns=self.to_drop)
