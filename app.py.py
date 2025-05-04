import streamlit as st

# Sample Data
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

faculty = {
    "B.C.A": "Dr. Rajeev Kumar (rajeev.kumar@college.edu)",
    "B.B.A": "Ms. Kavita Sharma (anjali.sharma@college.edu)",
    "M.B.A": "Mr. Arvind Mehta (arvind.mehta@college.edu)",
    "B.COM": "Mr. Arvind Mehta (arvind.mehta@college.edu)",
    "M.COM": "Mr. Arvind Mehta (arvind.mehta@college.edu)",
    "B.EDs": "Mr. Arvind Mehta (arvind.mehta@college.edu)",
    
}

admission_process = """
1. Fill out the online application form.
2. Submit required documents (marksheets, ID proof).
3. Appear for entrance test (if applicable).
4. Attend counseling session.
5. Pay the admission fee to confirm your seat.
"""

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Sidebar Navigation
def navigate():
    page = st.sidebar.selectbox("Navigate", ["Home", "Courses", "Admission Process", "Contact Faculty"])
    return page

# Home Page
def home_page():
    st.title("🎓 College Info Chatbot")
    if not st.session_state.submitted:
        st.write("Please fill your details to continue:")
        with st.form("user_form"):
            name = st.text_input("Your Name")
            contact = st.text_input("Your Contact Number")
            interest = st.text_input("Your Area of Interest")
            submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.submitted = True
            st.session_state.name = name
            st.success(f"Welcome, {name}! 👋")

    if st.session_state.submitted:
        st.success(f"Welcome, {st.session_state.name}! 👋")

# Courses Page
def courses_page():
    st.title("📚 Courses Offered")
    for course in courses:
        with st.expander(course):
            st.write(courses[course])

# Admission Process Page
def admission_page():
    st.title("📝 Admission Process")
    st.write(admission_process)

# Faculty Page
def faculty_page():
    st.title("👨‍🏫 Contact Faculty")
    for dept in faculty:
        st.write(f"**{dept}**: {faculty[dept]}")

# App Router
page = navigate()

if page == "Home":
    home_page()
elif page == "Courses":
    courses_page()
elif page == "Admission Process":
    admission_page()
elif page == "Contact Faculty":
    faculty_page()
