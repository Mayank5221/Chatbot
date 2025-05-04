import streamlit as st

def courses_page():
    st.title("Courses Offered")
    
    # Define the courses with details, including course time and fees
    courses = {
        "BCA": {
            "description": "Bachelor of Computer Applications - Learn the fundamentals of computer science, programming, and software development.",
            "time": "3 years",
            "fees": "₹50,000 per year"
        },
        "BBA": {
            "description": "Bachelor of Business Administration - Focus on business principles, marketing, management, and leadership skills.",
            "time": "3 years",
            "fees": "₹40,000 per year"
        },
        "MBA": {
            "description": "Master of Business Administration - Advanced business management, strategy, finance, and leadership training.",
            "time": "2 years",
            "fees": "₹1,00,000 per year"
        },
        "B.Ed": {
            "description": "Bachelor of Education - A professional course for those interested in teaching, focusing on education theory and practice.",
            "time": "2 years",
            "fees": "₹30,000 per year"
        },
        "B.Com": {
            "description": "Bachelor of Commerce - In-depth study of commerce, accounting, finance, and economics.",
            "time": "3 years",
            "fees": "₹35,000 per year"
        },
        "M.Com": {
            "description": "Master of Commerce - Advanced study in areas such as accounting, finance, and economic theory.",
            "time": "2 years",
            "fees": "₹70,000 per year"
        },
    }

    # Display each course with description, time, and fees
    for course, details in courses.items():
        with st.expander(course):
            st.write(f"**Description**: {details['description']}")
            st.write(f"**Duration**: {details['time']}")
            st.write(f"**Fees**: {details['fees']}")

    if st.button("Go Back"):
        st.session_state.page = 'main'
