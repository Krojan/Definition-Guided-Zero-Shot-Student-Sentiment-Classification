import pandas as pd


def read_data():
    df = pd.read_csv("smile-college-dataset.csv")
    df = df.drop(df.columns[0], axis=1)
    df = df.drop("School", axis=1)
    df["Validated_Labels"] = df["Validated_Labels"].str.lower()
    return df
