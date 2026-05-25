# Specification: Ultimate Custom Diary App Dashboard

## 1. Objective
Build an elegant, highly customizable, and interactive web dashboard for the Python Diary App that combines robust data metrics with personal aesthetic customization.

## 2. Comprehensive Feature Layout

### Sidebar Features:
* **App Title & Branding:** Clean header using a diary icon (📔 **Personal Analytics Diary**).
* **Metrics Dashboard:** Real-time statistics blocks showing total reflections logged and current habit streak 🔥.
* **Visual Customization (Theme Selector):** A dropdown with options: `Default White`, `Midnight Black`, `Baby Pink`, `Vintage Sepia`, `Space Odyssey`, and `Pop Art`. Custom CSS will inject the matching background and text colors dynamically.

### Main Panel Features (Styled Multi-Tab Layout):

* **Tab 1: 📝 Log Reflection**
  * **Auto-Generated Template:** Pre-populates the text box with the current date/time string and a `"Dear Diary, "` greeting (fully editable by the user).
  * **Mood Selector:** A dropdown or horizontal radio row (😃 Happy, 🛠️ Productive, 😴 Tired, 🧠 Reflective).
  * **Favorite Song of the Day Section:** A text input field to log a song name, Google link, or Spotify URL for that day, which can play every time you open that entry, you can turn off if you want.
  * **Rich Text Editing Support:** Standard text area allowing standard Markdown text formatting like emojis, bold (`**`), italics (`*`), and headings (`#`).
  * **Save Actions:** Clicking "Save to JSON" triggers a success balloon animation (`st.balloons()`).

* **Tab 2: 📖 Historical Ledger**
  * A search/filter bar to find past reflections.
  * Beautiful expandable containers (`st.expander`) displaying historical entries in reverse-chronological order, showcasing the timestamp, mood badge, saved song link, and formatted markdown reflections.