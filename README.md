
# Daily Dev Tracker 🐍

A small Python project that runs automatically using GitHub Actions.

## What it does

Every day, the project:

1. Runs the Python program.
2. Records the current date and time.
3. Records the Python version and operating system.
4. Saves the result to `activity.json`.
5. Commits the updated data back to the repository.

## Running locally

Make sure Python 3.10+ is installed.

```bash
python app.py
```

## Automatic execution

GitHub Actions runs the program automatically every day.

You can also run it manually:

**GitHub → Actions → Daily Dev Tracker → Run workflow**

## Project structure

```text
daily-dev-tracker/
├── app.py
├── activity.json
├── README.md
└── .github/
    └── workflows/
        └── daily.yml
```

## Technologies

* Python
* Git
* GitHub Actions
* JSON
