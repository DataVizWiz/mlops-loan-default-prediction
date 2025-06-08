NUM_FEATS = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "MonthsEmployed",
    "NumCreditLines",
    "InterestRate",
    "DTIRatio",
]

CAT_FEATS = ["Education", "EmploymentType", "MaritalStatus", "LoanPurpose"]

BIN_FEATS = ["HasMortgage", "HasDependents", "HasCoSigner"]

DROP_FEATS = ["LoanID"]

REGISTRY = "models"
