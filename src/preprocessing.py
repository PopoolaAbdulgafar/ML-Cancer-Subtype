import pandas as pd
def load_expression_data(file_path):
    expr = pd.read_csv(file_path, sep="\t")
    expr = expr.set_index("sample")
    x = expr.T
    return x


def load_labels(file_path, sample_ids):
    clinical = pd.read_csv(file_path)
    y = clinical.loc[sample_ids, "PAM50Call_RNAseq"]
    return y


def remove_missing_labels(x, y):
    valid = y.notna()
    x = x.loc[valid]
    y = y.loc[valid]
    return x, y
