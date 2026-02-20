from git import Repo
import pandas as pd
def load_repo_data(path="."):
    repo=Repo(path)
    commits = repo.iter_commits(max_count=200)
    data=[]
    for commit in commits:
        data.append({
            "message": commit.message.strip(),
            "author": commit.author.name,
            "date": commit.committed_datetime,
            "insertions": commit.stats.total["insertions"],
            "deletions": commit.stats.total["deletions"]
        })
    df=pd.DataFrame(data)
    return df
