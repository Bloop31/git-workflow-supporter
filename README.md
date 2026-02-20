# GitHub Repo Analyzer 📊

A Streamlit dashboard that analyzes GitHub repositories and provides insights into commit activity, productivity, and repository health.

## Features

- 📅 Commits per day visualization
- 📊 Total commits and contributor stats
- 📦 Detect large files in repository
- ⚡ Real-time Git repo analysis using GitPython
- 🎨 Interactive dashboard using Streamlit

## Tech Stack

- Python
- Streamlit
- Pandas
- GitPython

## Project Structure
repo-analyzer/
│
├── app.py
├── core/
│ ├── git_loader.py
│ ├── commit_analyzer.py
│ ├── productivity.py
│ └── repo_health.py
│
├── .streamlit/
│ └── config.toml
│
└── README.md

## Installation

```bash
pip install -r requirements.txt