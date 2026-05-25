import json
import os
import argparse
from datetime import datetime, date, timedelta
import textwrap

DIARY_FILE = "diary.json"

def load_data():
    """Load the diary data from the JSON file."""
    if not os.path.exists(DIARY_FILE):
        return {"entries": [], "metadata": {"current_streak": 0, "last_entry_date": None}}
    try:
        with open(DIARY_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"Warning: Could not read {DIARY_FILE}. Initializing new diary.")
        return {"entries": [], "metadata": {"current_streak": 0, "last_entry_date": None}}

def save_data(data):
    """Save the diary data to the JSON file."""
    try:
        with open(DIARY_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"Error: Failed to save diary data. {e}")

def update_streak(data):
    """Calculate and update the writing streak."""
    today = date.today()
    last_date_str = data["metadata"].get("last_entry_date")
    
    if last_date_str is None:
        # First entry ever
        data["metadata"]["current_streak"] = 1
    else:
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
        if today == last_date:
            # Already wrote today, no change to streak
            pass
        elif today == last_date + timedelta(days=1):
            # Consecutive day!
            data["metadata"]["current_streak"] += 1
        else:
            # Missed a day (or more), reset streak
            data["metadata"]["current_streak"] = 1
            
    data["metadata"]["last_entry_date"] = today.strftime("%Y-%m-%d")

def add_entry(content):
    """Add a new entry and update metadata."""
    data = load_data()
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    
    entry = {
        "timestamp": timestamp,
        "content": content
    }
    
    data["entries"].append(entry)
    update_streak(data)
    save_data(data)
    print(f"\nEntry recorded! Current streak: {data['metadata']['current_streak']} days.")

def view_entries(limit=5):
    """Display the most recent entries."""
    data = load_data()
    entries = data.get("entries", [])
    if not entries:
        print("Your diary is empty. Use 'write' to add your first entry!")
        return
    
    recent = entries[-limit:]
    print(f"\n--- Last {len(recent)} entries ---")
    for entry in recent:
        print(f"\n[{entry['timestamp']}]")
        print(textwrap.indent(textwrap.fill(entry['content'], width=70), "  "))
    print("\n" + "-" * 30)

def show_stats():
    """Display writing habits and statistics."""
    data = load_data()
    meta = data.get("metadata", {})
    total = len(data.get("entries", []))
    streak = meta.get("current_streak", 0)
    last_date_str = meta.get("last_entry_date", "Never")
    
    # Check if streak is currently active
    if last_date_str != "Never":
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
        if date.today() > last_date + timedelta(days=1):
            streak = 0 # Streak broken as of today

    print("\n--- Your Writing Stats ---")
    print(f"Total Entries:  {total}")
    print(f"Current Streak: {streak} days")
    print(f"Last Entry:     {last_date_str}")
    print("--------------------------")

def main():
    parser = argparse.ArgumentParser(description="Python Diary: Build a daily writing habit.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # write command
    write_parser = subparsers.add_parser("write", help="Write a new diary entry")
    write_parser.add_argument("content", nargs="?", help="The text of your entry. If omitted, you will be prompted.")

    # view command
    view_parser = subparsers.add_parser("view", help="View recent entries")
    view_parser.add_argument("-n", "--count", type=int, default=5, help="Number of entries to show (default: 5)")

    # stats command
    subparsers.add_parser("stats", help="Check your writing streak and stats")

    args = parser.parse_args()

    if args.command == "write":
        content = args.content
        if not content:
            content = input("What's on your mind today?\n> ")
        
        if content.strip():
            add_entry(content)
        else:
            print("Empty entries are not saved.")
    elif args.command == "view":
        view_entries(args.count)
    elif args.command == "stats":
        show_stats()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()