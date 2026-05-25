Please maintain the stripped-down, lightweight version of `app.py` matching the current functional scope.

Key Deployment Constraints:
1. Ensure the user interface is completely pristine, relying on Streamlit's core native layouts without any arbitrary or custom CSS injection wrappers.
2. Keep the backend data integration reading and writing cleanly to `diary.json` using the existing backend functions (`load_data`, `add_entry`).
3. Preserve the dynamic text template pre-population (`YYYY-MM-DD HH:MM` \n `Dear Diary,`) inside the entry creation container.
4. Ensure the keyword text-filtering search engine and reverse-chronological expander loops under the "Past Entries" log display data seamlessly without throwing visual or logical errors.