from preprocessing.common import DropColumns, BinaryEncoder
from preprocessing.logistic_regression import PreprocessLR
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression


lr_pipeline = Pipeline(
    steps=[
        ("drop_columns", DropColumns()),
        ("binary_encoder", BinaryEncoder),
        ("preprocessor", PreprocessLR()),
        ("smote", SMOTE(random_state=42)),
        ("classifier", LogisticRegression(random_state=0)),
    ]
)
