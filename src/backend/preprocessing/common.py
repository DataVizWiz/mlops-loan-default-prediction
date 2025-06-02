import pandas as pd
from control import config


class DropColumns:
    """Custom transformer to drop columns"""

    def __init__(self):
        pass

    def fit(self):
        return self

    def transform(self, X: pd.DataFrame):
        return X.drop(columns=config.DROP_FEATURES)


class BinaryEncoder:
    """Custom binary encoder"""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def fit(self):
        return self

    def transform(self):
        bin_cols = config.BINARY_FEATURES
        self.df[bin_cols] = self.df[bin_cols].replace({"Yes": 1, "No": 0}).astype(int)
