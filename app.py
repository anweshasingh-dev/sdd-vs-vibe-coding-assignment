import streamlit as st
from datetime import datetime, date, timedelta
from diary import load_data, add_entry
import re

# Page Configuration
st.set_page_config(
    page_title="Anwesha's Secret Diary",
    page_icon="📔", 
    layout="centered"
)

# --- PASSWORD PROTECTION (Vibe Coding Feature) ---
# We use diary data to check if a password has been initialized
data_check = load_data()
if "profile" not in data_check:
    data_check["profile"] = {}
profile_data = data_check["profile"]

if "password" not in profile_data:
    st.title("🔒 Secure Your Thoughts")
    st.subheader("Welcome to your vibe coding playground!")
    st.write("Let's initialize a master password to keep your diary completely secret.")
    
    new_pass = st.text_input("Create your secret password", type="password")
    confirm_pass = st.text_input("Confirm your password", type="password")
    
    if st.button("Set Master Key 🔑", use_container_width=True):
        if new_pass and new_pass == confirm_pass:
            # We save it into our storage profile
            import json
            import os
            # Simple direct update to the backend storage with a safety check
            if "profile" not in data_check:
                data_check["profile"] = {}

            data_check["profile"]["password"] = new_pass
            # Just writing it directly to the JSON file being used by diary.py
            with open("diary_db.json" if os.path.exists("diary_db.json") else "diary.json", "w") as f:
                json.dump(data_check, f, indent=4)
            st.success("Password secured perfectly! Reloading...")
            st.rerun()
        else:
            st.error("Passwords don't match or are empty. Give it another shot!")
    st.stop()

else:
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.title("🔒 Diary Encrypted")
        input_pass = st.text_input("Enter password to unlock your secrets:", type="password")
        
        if st.button("Unlock Diary 🔓", use_container_width=True):
            if input_pass == profile_data["password"]:
                st.session_state["authenticated"] = True
                st.success("Access Granted! Welcome back.")
                st.rerun()
            else:
                st.error("Access Denied. Wrong password vibe.")
        st.stop()


# --- SIDEBAR THEME SELECTOR & STATS ---
st.sidebar.title("📔 Anwesha's Secret Diary")
st.sidebar.markdown("---")

# VIBE FEATURE: DYNAMIC CUSTOM THEME INJECTOR
st.sidebar.subheader("🎨 Visual Vibe")
theme_choice = st.sidebar.selectbox(
    "Choose your style mood", 
    ["Default Dark 🌌", "Cyberpunk Neon 💜", "Pastel Dream 🌸"]
)

# Custom CSS theme engines
if theme_choice == "Cyberpunk Neon 💜":
    st.markdown("""
        <style>
        .stApp { background-color: #0d0116; color: #00ffcc; }
        h1, h2, h3, label, p { color: #ff007f !important; text-shadow: 0 0 10px #ff007f; }
        .stButton>button { background-color: #ff007f !important; color: white !important; border-radius: 8px; border: 1px solid #00ffcc; }
        </style>
    """, unsafe_html=True)
    
elif theme_choice == "Pastel Dream 🌸":
    st.markdown("""
        <style>
        .stApp { background-color: #fff0f5; color: #4a4a4a; }
        h1, h2, h3 { color: #ffb6c1 !important; }
        .stButton>button { background-color: #ffb6c1 !important; color: white !important; border-radius: 20px; }
        </style>
    """, unsafe_html=True)

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
    
    if last_date_str != "Never":
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
        if date.today() > last_date + timedelta(days=1):
            streak = 0
            
    return total_count, streak

total, current_streak = get_stats()

st.sidebar.metric(label="Total Reflections Logged", value=total) 
st.sidebar.markdown(f"### Current Habit Streak: {current_streak} 🔥") 

# --- Main Interface: Tabs ---
tab_write, tab_view = st.tabs(["📝 Write Entry", "📖 Past Entries"]) 

with tab_write:
    st.header("New Diary Entry")
    
    default_content = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nDear Diary,\n\n"
    entry_content = st.text_area(
        "What's on your mind today?",
        value=default_content, 
        height=250,
        placeholder="Start writing here...",
        key="new_entry_content"
    )
    
    # Mood Selector & Track of the Day Side-by-Side
    col1, col2 = st.columns([2, 1])
    with col1:
        mood_options = ["😃 Happy", "🛠️ Productive", "😴 Tired", "🧠 Reflective", "😐 Neutral", "😔 Sad"]
        selected_mood = st.selectbox("How are you feeling?", mood_options, key="mood_selector")
    with col2:
        selected_song = st.text_input("🎵 Track of the Day", placeholder="Song - Artist", key="song_selector")
    
    if st.button("Save to JSON", type="primary", use_container_width=True): 
        if entry_content.strip():
            # Combine mood and song strings into data for clean storage extraction
            song_tag = f" | 🎵 Jamming to: {selected_song}" if selected_song else ""
            combined_content = f"[MOOD: {selected_mood}{song_tag}]\n\n{entry_content.strip()}"
            
            add_entry(combined_content)
            st.balloons()
            timestamp = datetime.now().strftime("%H:%M:%S")
            st.success(f"Entry saved successfully with timestamp: {timestamp}!")
            st.rerun()
        else:
            st.warning("Please enter some text before saving.")

with tab_view:
    st.header("Journal History")

    search_query = st.text_input("Search entries by keyword:", placeholder="e.g., 'project', 'meeting', 'feeling'", key="search_bar")

    data = load_data()
    entries = data.get("entries", [])
    
    if not entries:
        st.info("Your diary is currently empty. Head over to the '📝 Write Entry' tab to create your first entry!")
    else:
        filtered_entries = [
            entry for entry in entries
            if search_query.lower() in entry['content'].lower()
        ]

        if not filtered_entries:
            st.info("No entries found matching your search query.")
        else:
            for entry in reversed(filtered_entries):
                content = entry['content']

                # Clean layout details: parsing mood/songs
                mood_match = re.search(r"\[MOOD: (.*?)\]", content) 
                display_details = mood_match.group(1) if mood_match else "N/A" 

                with st.expander(f"📅 **{entry['timestamp']}** | Mood & Music: {display_details}"):
                    clean_content = re.sub(r"\[MOOD: .*?\]", "", content).strip()
                    st.markdown("---")
                    st.markdown(clean_content)