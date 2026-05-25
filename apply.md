Please update the `app.py` file to include the following two specific features:

1. Personalized Branding: Change all references of "Python Diary" to my custom name: "Anwesha's Secret Ledger".
2. Automatic Timestamp Template: When initializing the 'Write Entry' text area, pre-populate the value property with a dynamic timestamp string using `datetime.now().strftime("%Y-%m-%d %H:%M")` followed by a new line and "Dear Diary,\n\n". Ensure the user can still freely type after it or edit it.