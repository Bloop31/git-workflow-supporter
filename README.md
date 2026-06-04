# GitHub Repository Analyzer

A web-based analytics dashboard that evaluates GitHub repositories and provides actionable insights into development activity, contributor engagement, and repository health. The application leverages Git metadata to generate visualizations and metrics that help developers monitor project progress and identify potential maintenance concerns.

## Features

* Analyze commit activity and trends over time
* Visualize commits on a daily basis through interactive charts
* Track repository statistics, including total commits and contributor metrics
* Identify large files that may impact repository performance and maintainability
* Perform real-time repository analysis using GitPython
* Interactive dashboard interface built with Streamlit

## Technology Stack

* Python
* Streamlit
* Pandas
* GitPython

## Project Structure

```text
repo-analyzer/
│
├── app.py
├── core/
│   ├── git_loader.py
│   ├── commit_analyzer.py
│   ├── productivity.py
│   └── repo_health.py
│
├── .streamlit/
│   └── config.toml
│
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Use Cases

* Repository activity monitoring
* Contributor productivity analysis
* Open-source project evaluation
* Repository health assessment
* Software engineering analytics
