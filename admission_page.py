import streamlit as st

st.title("📝 Admission Process")

admission_process = """
1. Fill out the online application form.
2. Submit required documents (marksheets, ID proof).
3. Appear for entrance test (if applicable).
4. Attend counseling session.
5. Pay the admission fee to confirm your seat.
"""

st.write(admission_process)

if st.button("🔙 Go Back"):
    st.switch_page("chatbot_app.py")
