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

# Main Text
st.markdown('<p class="biggest-font"><b>➲  Joan and Frank Trocki Scholarship for Best Student of the 2020 Batch</b></p>', unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image(Image.open('Images/convocation 2.jpeg'), width = 320)
    with col2:
        st.image(Image.open('Images/Scholarship award.jpeg'), width = 370)
best = """"""
st.write(best)
st.markdown('#')
st.markdown('#')


st.markdown('<p class="biggest-font"><b>➲  1st Place in the Xavier Coding Hackathon 2019</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/Hackathon First Prize.jpeg'), width = 640)
hackathon = """"""
st.write(hackathon)
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  1st Place in Project Exhibition</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/Spandan Project Exhibition Prize 2020.jpeg'), width = 640)
spandan = """"""
st.write(spandan)
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  Consolation Prize for National Project Exhibition, Protech 2020</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/SIT Consolation.jpeg'), width = 640)
protech = """[Protech 2020](https://www.sitpune.edu.in/news_protech2020) was a national level project exhibition where more than 300 
student participated in 75+ teams. I participated with 2 of my peers from Xavier 
Institute of Engineering. The project we showcased was the AI Pet Robot. You 
can read more about this in the Projects section. 

We learnt a lot about presentation and how to showcase our project, not just to the 
judges but to everyone interested who came to our booth. Although we did not finish 
on the podium at this prestigious competition, we got exposure to some
great projects. A lot of these were supremely polished products geared towards 
helping the ordinary man. Some of the project were aimed at social good and also
go recognition for same. """
st.write(protech)
st.markdown('#')
st.markdown('#')