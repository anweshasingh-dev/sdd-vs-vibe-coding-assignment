import streamlit as st
from datetime import datetime, date, timedelta
from diary import load_data, add_entry
import re

# Page Configuration
st.set_page_config(
    page_title="Anwesha's Secret Diary",
    page_icon="📔", # Updated to diary icon
    layout="centered"
)

# --- Sidebar Features ---
st.sidebar.title("📔 Anwesha's Secret Diary")
st.sidebar.markdown("---")
st.sidebar.subheader("Dashboard")

def get_stats():
    """Calculates statistics for the sidebar display."""
    data = load_data()
    entries = data.get("entries", [])
    meta = data.get("metadata", {})
    
    total_count = len(entries)
    streak = meta.get("current_streak", 0)
    last_date_str = meta.get("last_entry_date", "Never")
    
    # Check if streak is still active (matches logic in diary.py show_stats)
    if last_date_str != "Never":
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
        if date.today() > last_date + timedelta(days=1):
            streak = 0
            
    return total_count, streak

total, current_streak = get_stats()

st.sidebar.metric(label="Total Reflections Logged", value=total) # Updated label
st.sidebar.markdown(f"### Current Habit Streak: {current_streak} 🔥") # Updated label

# --- Main Interface: Tabs ---
tab_write, tab_view = st.tabs(["📝 Write Entry", "📖 Past Entries"]) # Updated tab titles

with tab_write:
    st.header("New Diary Entry")
    
    # Auto-Generated Template
    default_content = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nDear Diary,\n\n"
    entry_content = st.text_area(
        "What's on your mind today?",
        value=default_content, # Pre-populate with template
        height=300,
        placeholder="Start writing here...",
        key="new_entry_content"
    )
    
    # Mood Selector
    mood_options = ["😃 Happy", "🛠️ Productive", "😴 Tired", "🧠 Reflective", "😐 Neutral", "😔 Sad"]
    selected_mood = st.radio(
        "How are you feeling?",
        mood_options,
        horizontal=True,
        key="mood_selector"
    )
    
    if st.button("Save to JSON", type="primary"): # Updated button text
        if entry_content.strip():
            # Combine mood and song into content for storage in diary.py
            combined_content = f"[MOOD: {selected_mood}]\n\n{entry_content.strip()}"
            
            # Use backend function to save data
            add_entry(combined_content)
            
            # Success message with timestamp and balloons
            st.balloons()
            timestamp = datetime.now().strftime("%H:%M:%S")
            st.success(f"Entry saved successfully with timestamp: {timestamp}!")
            
            # Force refresh to update stats and view list
            st.rerun()
        else:
            st.warning("Please enter some text before saving.")

with tab_view:
    st.header("Journal History")

    search_query = st.text_input("Search entries by keyword:", placeholder="e.g., 'project', 'meeting', 'feeling'", key="search_bar")

    data = load_data()
    entries = data.get("entries", [])
    
    if not entries:
        st.info("Your diary is currently empty. Head over to the 'Log Reflection' tab to create your first entry!")
    else:
        # Filter entries based on search query
        filtered_entries = [
            entry for entry in entries
            if search_query.lower() in entry['content'].lower()
        ]

        if not filtered_entries:
            st.info("No entries found matching your search query.")
        else:
            # Display entries in reverse-chronological order
            for entry in reversed(filtered_entries):
                with st.expander(f"**{entry['timestamp']}**"): # Use expander
                    content = entry['content']

                    # Extract Mood and Song using regex
                    mood_match = re.search(r"\[MOOD: (.*?)\]", content) # Keep mood extraction
                    display_mood = mood_match.group(1) if mood_match else "N/A" # Keep mood display

                    # Remove mood and song tags from the main content for cleaner display
                    clean_content = re.sub(r"\[MOOD: .*?\]", "", content)
                    clean_content = clean_content.strip()
                    st.markdown("---")
                    st.markdown(clean_content) # Display cleaned content