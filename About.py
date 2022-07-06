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
st.sidebar.image(Image.open('Images/personal 1-modified.png'))
with st.sidebar.container():
    st.markdown('<p class="big-font"><u>Abhishek Ghoshal</u></p>', unsafe_allow_html=True)
st.sidebar.markdown("# Contact Me At")
st.sidebar.write("Gmail : [abhighosh98@gmail.com](https://abhighosh98@gmail.com)")
st.sidebar.write("LinkedIn : [abhishek-m-ghoshal](https://www.linkedin.com/in/abhishek-m-ghoshal)")
st.sidebar.write("Github : [abhighosh98](https://github.com/abhighosh98)")
with open("Files/Resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
st.sidebar.download_button(label = "Download Resume",
                    data = PDFbyte,
                    file_name = "Abhishek Ghoshal Resume.pdf",
                    mime = 'application/octet-stream')
st.sidebar.markdown("#")
st.sidebar.markdown("#")

# Main Text
st.markdown('<p class="biggest-font"><b>➲  Where am I from?</b></p>', unsafe_allow_html=True)
where_am_i_from = """I was born and raised in Mumbai, India and completed 
my education all the way through to an undergraduate degree here. After this, 
I worked as a Machine Learning Engineer at Quantiphi Analytics for a year. 
You can read more about this in the Experience and Projects sections. 
"""
st.write(where_am_i_from)
st.markdown('#')
st.markdown('#')


st.markdown('<p class="biggest-font"><b>➲  What am I doing now?</b></p>', unsafe_allow_html=True)
what_am_i_doing_now = """Currently I am pursuing a 
[Master of Science in Applied Data Science](https://datascience.usc.edu/academics/master-of-science-in-applied-data-science/)
degree from [University of Southern California](https://viterbischool.usc.edu/).
For the Fall 2022 semester, along with finishing my courses I will also be 
one of the course graders for DSCI 551: Foundations of Data Management. I am 
presently searching for Summer 2023 Internships.
"""
st.write(what_am_i_doing_now)
st.markdown('#')
st.markdown('#')


st.markdown('<p class="biggest-font"><b>➲  What are some of my interests?</b></p>', unsafe_allow_html=True)
what_are_some_of_my_interests = """I am avid gamer and regularly play on my PC, PS4 
and PS5. I find video games to be my escape from reality and my place of solace. While
 I am not a "fitness freak" I do ensure I spent some time at the gym daily working on 
 my physical health. Apart from this, I play a lot of sports like football, badminton 
 and table tennis. You can read about these and more in the Hobbies and Interests 
 section. 
"""
st.write(what_are_some_of_my_interests)
st.markdown('#')
st.markdown('#')
