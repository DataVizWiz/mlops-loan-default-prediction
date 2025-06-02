from control import config
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer


class PreprocessLR:
    """Preprocess Logistic Regression"""

    def __init__(self):
        pass

    def set_numerical_transformer():
        """Use standard scaling to scale numerical values"""
        return Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="mean")),
                ("scaler", StandardScaler()),
            ]
        )

    def set_dtir_transformer():
        """Normalize DTIRation as values are between 0 and 1"""
        return Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="mean")),
                ("minmax", MinMaxScaler()),
            ]
        )

    def set_categorical_transformer():
        """One-hot encode categorical variables"""
        return Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore")),
            ]
        )

    def fit(self):
        return self

    def transform(self):
        return ColumnTransformer(
            transformers=[
                ("num", self.set_numerical_transformer(), config.NUMERICAL_FEATURES),
                ("dtir", self.set_dtir_transformer(), config.DTIR_FEATURES),
                (
                    "cat",
                    self.set_categorical_transformer(),
                    config.CATEGORICAL_FEATURES,
                ),
            ],
            remainder="passthrough",
        )
