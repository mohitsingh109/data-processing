from pandas import DataFrame

def save_report(df: DataFrame):
    df.to_csv("data/processed/report.csv", index=False)
