import datetime
from config import BASE_SCORE, SHORT_COMMIT_PENALTY, LARGE_FILE_PENALTY
def calculate_repo_score(short_commit_count, large_files):
    score = BASE_SCORE
    if short_commit_count > 5:
        score -= SHORT_COMMIT_PENALTY
    if large_files:
        score -= LARGE_FILE_PENALTY
    return max(score, 0)

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M")

def count_short_commits(messages, min_length):
    return sum(len(msg) < min_length for msg in messages)