import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

DATA_FILE = Path("activity.json")
STATS_FILE = Path("statistics.json")
SYSTEM_FILE = Path("system_info.json")
SUMMARY_FILE = Path("daily_summary.json")
VALIDATION_FILE = Path("validation.json")
STATUS_FILE = Path("status.json")


def load_json(path, default):
    if not path.exists():
        return default

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(path, data):
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
        file.write("\n")


def record_activity():
    activity = load_json(DATA_FILE, [])
    now = datetime.now(timezone.utc)

    entry = {
        "run_number": len(activity) + 1,
        "date": now.strftime("%Y-%m-%d"),
        "time_utc": now.strftime("%H:%M:%S"),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "status": "success"
    }

    activity.append(entry)
    save_json(DATA_FILE, activity)

    print(f"Recorded activity #{entry['run_number']}")


def update_statistics():
    activity = load_json(DATA_FILE, [])

    total = len(activity)

    successful = sum(
        1 for item in activity
        if item.get("status") == "success"
    )

    failed = total - successful

    statistics = {
        "total_runs": total,
        "successful_runs": successful,
        "failed_runs": failed,
        "success_rate": round(
            (successful / total) * 100, 2
        ) if total else 0,
        "last_run": activity[-1] if activity else None
    }

    save_json(STATS_FILE, statistics)

    print("Statistics updated.")


def update_system():
    system_info = {
        "collected_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor()
    }

    save_json(SYSTEM_FILE, system_info)

    print("System information updated.")


def generate_summary():
    activity = load_json(DATA_FILE, [])

    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    today_runs = [
        item for item in activity
        if item.get("date") == today
    ]

    successful = sum(
        1 for item in today_runs
        if item.get("status") == "success"
    )

    summary = {
        "date": today,
        "runs_today": len(today_runs),
        "successful_runs_today": successful,
        "failed_runs_today": len(today_runs) - successful,
        "latest_run": today_runs[-1] if today_runs else None
    }

    save_json(SUMMARY_FILE, summary)

    print("Daily summary generated.")


def validate_data():
    activity = load_json(DATA_FILE, [])

    required_fields = [
        "run_number",
        "date",
        "time_utc",
        "python_version",
        "platform",
        "status"
    ]

    issues = []

    for index, entry in enumerate(activity, start=1):
        missing = [
            field
            for field in required_fields
            if field not in entry
        ]

        if missing:
            issues.append({
                "record": index,
                "missing_fields": missing
            })

    validation = {
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "valid": len(issues) == 0,
        "records_checked": len(activity),
        "issues": issues
    }

    save_json(VALIDATION_FILE, validation)

    if issues:
        raise ValueError("Validation failed.")

    print("Validation successful.")


def update_status():
    activity = load_json(DATA_FILE, [])

    status = {
        "project": "Daily Dev Tracker",
        "status": "operational",
        "total_runs": len(activity),
        "last_updated_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": platform.python_version(),
        "python_executable": sys.executable
    }

    save_json(STATUS_FILE, status)

    print("Project status updated.")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python app.py activity")
        print("  python app.py statistics")
        print("  python app.py system")
        print("  python app.py summary")
        print("  python app.py validate")
        print("  python app.py status")
        return

    command = sys.argv[1].lower()

    commands = {
        "activity": record_activity,
        "statistics": update_statistics,
        "system": update_system,
        "summary": generate_summary,
        "validate": validate_data,
        "status": update_status
    }

    if command not in commands:
        raise ValueError(f"Unknown command: {command}")

    commands[command]()


if __name__ == "__main__":
    main()