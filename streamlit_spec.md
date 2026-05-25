# Specification: Interactive Personal Diary Dashboard

## 1. Objective
Build a lightweight, clean, and interactive personal diary web application using Streamlit. The application allows the user to write formatted daily journal entries with automatic metadata capturing and view them through a searchable history ledger.

## 2. Core App Layout & Architecture

### A. Sidebar Features (The Dashboard)
* **Branding Header:** Displays the personalized title: *"📔 Anwesha's Secret Diary"*.
* **Real-time Metrics:** * Displays the total count of reflections permanently saved to the database.
  * Tracks and displays the user's current habit streak 🔥 calculated dynamically from their save history.

### B. Main Application Interface (Two-Tab Navigation)

#### Tab 1: 📝 Write Entry
* **Dynamic Content Template:** The input area pre-populates automatically with a live, real-time date-time stamp string followed by *"Dear Diary,"* to ease user friction.
* **Text Area:** A large text area input for writing daily reflections.
* **Mood Tagging Selector:** A horizontal radio button selection row containing quick mood emojis (`😃 Happy`, `🛠️ Productive`, etc.) to track daily emotional status.
* **Action Button:** A prominent *"Save to JSON"* primary execution button that commits the entry and mood tags directly to the backend database file, fires off visual celebrations (balloons), and reloads the display dashboard seamlessly.

#### Tab 2: 📖 Past Entries
* **Search Filtering:** Features an active keyword search bar that queries and screens the historical diary records on the fly.
* **Reverse-Chronological History Ledger:** Displays entries inside collapsable structural modules (expanders) headered by their original submission dates, displaying cleaned textual data clearly.