# Design: Python Diary App

## Architecture
The application will be a standalone Python script using `argparse` for command handling and the standard `json` library for data persistence.

## Data Storage
Entries will be stored in `diary.json` with the following structure:
```json
{
  "entries": [
    {
      "timestamp": "2023-10-27T10:00:00",
      "content": "Today I started working on my OpenSpec project."
    }
  ],
  "metadata": {
    "current_streak": 1,
    "last_entry_date": "2023-10-27"
  }
}
```

## Key Components
1.  **Entry Manager**: Handles reading and writing to the JSON file.
2.  **CLI Interface**: Commands for `write` and `stats`.
3.  **Habit Engine**: Logic to calculate if a streak is active or has been broken based on the `last_entry_date`.

## Implementation Details
- Use `datetime` for timestamping.
- Use `textwrap` for formatting long entries in the terminal.