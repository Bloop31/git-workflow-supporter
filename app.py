import streamlit as st
import pandas as pd
from core.git_loader import load_repo_data
from core.commit_analyzer import analyze_commit
from core.productivity import commits_per_day, total_stats
from core.repo_health import check_large_files
from utils.helpers import calculate_repo_score, count_short_commits
from config import MIN_COMMIT_LENGTH
st.set_page_config(page_title="Git workflow Supporter",layout="wide")
st.title("Git Workflow Supporter System")
repo_path = st.text_input("Enter repository path", ".")
if "analyze" not in st.session_state:
    st.session_state.analyze = False

if st.button("Analyze Repository"):
    st.session_state.analyze = True

if st.session_state.analyze:
    df = load_repo_data(repo_path)
    st.subheader("Repository Overview")
    total_commits, insertions, deletions = total_stats(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Commits", total_commits)
    col2.metric("Total Insertions", insertions)
    col3.metric("Total Deletions", deletions)
    st.subheader("Commits Per Day")
    stats = commits_per_day(df)
    st.line_chart(stats)
    st.subheader("Commit Quality Check")
    for msg in df["message"].head(10):
        st.write(msg)
        st.write(analyze_commit(msg))
        st.write("---")
    large_files = check_large_files(repo_path)
    st.subheader("Repo Health")
    if large_files:
        st.warning(f"Large Files Detected: {large_files}")
    else:
        st.success("No large files detected!")
    short_commit_count = count_short_commits(df["message"], MIN_COMMIT_LENGTH)
    score = calculate_repo_score(short_commit_count, large_files)
    st.subheader("Repo Health Score")
    st.metric("Health Score", f"{score}/100")