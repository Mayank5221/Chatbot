import streamlit as st

st.title("👨‍🏫 Contact Faculty")

faculty = {
    "Computer Science": "Dr. Rajeev Kumar (rajeev.kumar@college.edu)",
    "Data Science": "Ms. Kavita Sharma (anjali.sharma@college.edu)",
    "Business Management": "Mr. Arvind Mehta (arvind.mehta@college.edu)",
}

for dept in faculty:
    st.write(f"**{dept}**: {faculty[dept]}")

if st.button("🔙 Go Back"):
    st.switch_page("chatbot_app.py")
