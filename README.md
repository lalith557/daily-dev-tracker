# Daily Dev Tracker 🐍

A Python automation project that runs through GitHub Actions and maintains a structured history of development activity.

## What it does

The project automatically performs six stages during each daily workflow:

1. Records execution activity.
2. Updates project statistics.
3. Records the execution environment.
4. Generates a daily summary.
5. Validates stored activity data.
6. Updates project status.

Each stage produces a separate change and is committed independently.

## Automatic execution

GitHub Actions runs the tracker automatically every day.

The workflow can also be started manually:

**GitHub → Actions → Daily Dev Tracker → Run workflow**

## Running locally

Python 3.10+ is recommended.

```bash
python app.py activity
python app.py statistics
python app.py system
python app.py summary
python app.py validate
python app.py status
```

## Project structure

```text
daily-dev-tracker/
│
├── app.py
├── activity.json
├── statistics.json
├── system_info.json
├── daily_summary.json
├── validation.json
├── status.json
├── README.md
│
└── .github/
    └── workflows/
        └── daily.yml
```

## Technologies

* Python
* Git
* GitHub Actions
* JSON

## Purpose

This project demonstrates Python scripting, JSON data processing, Git automation, continuous integration workflows, scheduled execution, environment detection, validation, and automated repository updates.
