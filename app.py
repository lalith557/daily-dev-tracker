import json
import platform
from datetime import datetime, timezone
from pathlib import Path

DATA_FILE = Path("activity.json")


def load_activity():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_activity(activity):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(activity, file, indent=2)


def main():
    activity = load_activity()

    now = datetime.now(timezone.utc)

    entry = {
        "run_number": len(activity) + 1,
        "date": now.strftime("%Y-%m-%d"),
        "time_utc": now.strftime("%H:%M:%S"),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "status": "success",
    }

    activity.append(entry)
    save_activity(activity)

    print("Daily Dev Tracker ran successfully.")
    print(f"Run number: {entry['run_number']}")
    print(f"Date: {entry['date']}")
    print(f"Python: {entry['python_version']}")


if __name__ == "__main__":
    main()