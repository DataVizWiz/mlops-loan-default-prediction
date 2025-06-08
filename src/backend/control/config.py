NUMERICAL_FEATURES = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "MonthsEmployed",
    "NumCreditLines",
    "InterestRate",
    "DTIRatio",
]

CATEGORICAL_FEATURES = ["Education", "EmploymentType", "MaritalStatus", "LoanPurpose"]

BINARY_FEATURES = ["HasMortgage", "HasDependents", "HasCoSigner"]

DROP_FEATURES = ["LoanID"]

MODELS_DIR = "models"
