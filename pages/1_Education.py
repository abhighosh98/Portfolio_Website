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
usc = """I came to LA to pursue my graduate degree in the Spring 2022 semester. 
For this semester, I decided to prioritize coursework along with being comfortable 
with the student life in another country. Getting to know my peers and LA itself was 
a great start to my Masters program. 

 During my first semester I took Foundations of Data Management and Machine 
 Learning for Data Science as my courses. Both of these courses helped me learn
  new technologies like Firestore and PySpark and strenghten my basics in 
  SQL and Machine Learning. It was during this semester that I worked on a 
  couple projects; AI Stylist and 5DayMLP. More details about these are listed 
  in the projects section. 
  
  In Summer 2022 I took up another course; Predictive Analytics. Along with this 
  I also started searching for an internship for Summer 2023 and prepping for the 
  interviews. """
st.write(usc)
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  Xavier Institute of Engineering</b></p>', unsafe_allow_html=True)
st.markdown('## Bachelor of Engineering in Computer Engineering')
st.markdown('#### *Important Coursework*')
st.markdown('*Structured Programming Approach, Data Structures, Analysis of Algorithms, Computer Organization and Architecture, Computer Graphics, Operating System, Advanced Algorithm, Microprocessor, Database Management System, Computer Network, Software Engineering, Data Warehousing & Mining, Machine Leaning, Digital Signal & Image Processing, Artificial Intelligence & Soft Computing, Advanced System Security & Digital Forensics, Natural Language Processing*')
xie = """It was during the second half of my undergraduate degree that I started 
finding interest in the field of Machine Learning. I came across through coursework, 
however I learned about it extensively from online learning platforms. 
I worked on multiple projects during this time which were based on ML. The most prominent one 
was the AI Pet Robot. I also participated in multiple hackathons and project exhibitions showcasing 
my projects. More details about these are given in the Projects and Achievements sections. 

By the end of my undergraduate degree I was adept in skills required by the tech industry such as Python, 
deep learning, machine learning, SQL, image processing, tensorflow, etc. I joined Quantiphi Analytics as
 a Machine Learning Engineer where I worked on a varied set of projects with some of the biggest 
 companies in the world as clients. 
"""
st.write(xie)
st.markdown('#')
st.markdown('#')