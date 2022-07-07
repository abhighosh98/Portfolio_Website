import streamlit as st
from PIL import Image

# Style
st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.biggest-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar.container():
    st.markdown('<p class="big-font"><u>Grades</u></p>', unsafe_allow_html=True)
st.sidebar.markdown("### University of Southern California (Los Angeles, California)")
st.sidebar.write("GPA: 3.85")
st.sidebar.markdown("#")

st.sidebar.markdown("### TOEFL (Score : 116)")
st.sidebar.write("Reading: 30, Listening: 30, Speaking: 28, Writing: 28")
st.sidebar.markdown("#")

st.sidebar.markdown("### GRE (Score: 330)")
st.sidebar.write("Verbal: 164, Quantitative: 166")
st.sidebar.markdown("#")

st.sidebar.markdown("### Xavier Institute of Engineering (Mumbai, India)")
st.sidebar.write("CGPA: 9.12")
st.sidebar.markdown("#")


# Main Text
st.markdown('<p class="biggest-font"><b>➲  University of Southern California</b></p>', unsafe_allow_html=True)
st.markdown("## Master of Science in Applied Data Science")
st.markdown('#### *Important Coursework*')
st.markdown('*Foundations of Data Management, Machine Learning for Data Science, Predictive Analytics*')
st.image(Image.open('Images/personal 3.jpeg'), width = 640)
usc = """text"""
st.write(usc)
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  Xavier Institute of Engineering</b></p>', unsafe_allow_html=True)
st.markdown("## Bachelor of Engineering in Computer Engineering")
st.markdown('#### *Important Coursework*')
st.markdown('*Structured Programming Approach, Data Structures, Analysis of Algorithms, Computer Organization and Architecture, Computer Graphics, Operating System, Advanced Algorithm, Microprocessor, Database Management System, Computer Network, Software Engineering, Data Warehousing & Mining, Machine Leaning, Digital Signal & Image Processing, Artificial Intelligence & Soft Computing, Advanced System Security & Digital Forensics, Natural Language Processing*')
st.image(Image.open('Images/XIE Council.jpeg'), width = 640)
xie = """text"""
st.write(xie)
st.markdown('#')
st.markdown('#')