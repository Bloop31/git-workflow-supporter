import pandas as pd
def commits_per_day(df):
    df["date"]=pd.to_datetime(df["date"],utc=True)
    df["day"]=df["date"].dt.date
    return df.groupby("day").size()
def total_stats(df):
    total_commits=len(df)
    total_insertions=df["insertions"].sum()
    total_deletions=df["deletions"].sum()
    return total_commits,total_insertions,total_deletions