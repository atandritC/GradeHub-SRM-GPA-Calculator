import streamlit as st

# Frontend Title and Description
st.title('GradeHub - SRM GPA Calculator')
st.markdown("This project is created by [Atandrit Chatterjee](https://github.com/atandritC).")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f0f0f0;
            color: #333333;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            color: #0066ff;
            font-size: 2em;
            margin-bottom: 1em;
        }
        .button {
            background-color: #0066ff;
            color: white;
            padding: 0.5em 1em;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            margin-top: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# Frontend Interface
st.header('SRM University GPA Calculator')

# Input Form
st.subheader('Enter Your Grades and Credits:')
courses = st.number_input('Number of Courses', min_value=1, max_value=10, value=6)

# Initialize data storage
credits = []
grades = []

# Collect user input
for i in range(courses):
    credits.append(st.number_input(f'Course {i+1} Credits', min_value=1))
    grades.append(st.selectbox(f'Course {i+1} Grade', ['O', 'A+', 'A', 'B+', 'B', 'C', 'W', 'F', 'Ab', 'I', '*']))

# Calculate GPA
if st.button('Calculate GPA'):
    total_credits = sum(credits)
    total_points = sum([credits[i] * {
        'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5.5, 'W': 0, 'F': 0, 'Ab': 0, 'I': 0, '*': 0
    }[grades[i]] for i in range(courses)])
    
    gpa = total_points / total_credits
    st.success(f'Your CGPA is: {gpa:.2f}')

# Footer
st.markdown('---')
st.markdown('Source Code: [GradeHub on GitHub](https://github.com/atandritC)')
st.markdown('© 2024, Atandrit Chatterjee.')