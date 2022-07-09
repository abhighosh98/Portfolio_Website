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
best = """This is an award that I had been eyeing for about 4 years; ever 
since I heard about it in the first year of my undergraduate degree. Awarded to 
the best student amongst all engineering branches. This award took into account 
not just grades but also techincal skills, social responsibilities, positions of 
leadership and many more facets of an individual. """
st.write(best)
st.markdown('#')
st.markdown('#')


st.markdown('<p class="biggest-font"><b>➲  1st Place in the Xavier Coding Hackathon 2019</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/Hackathon First Prize.jpeg'), width = 640)
hackathon = """The Xavier Coding Hackathon was a coding competition which attracted 
the best students from many colleges in the city. It had 3 rounds with increasingly 
levels of difficulty and took place over the course of a day, rounding off with the 
prize distribution. Dr. Frank Trocki, Chancellor at Montana State University 
felicated the winners of this competiton. """
st.write(hackathon)
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  1st Place in Spandan Project Exhibition</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/Spandan Project Exhibition Prize.jpeg'), width = 640)
spandan = """Spandan is an annual college festival organized by the student council 
at Xavier Institute of Engineering. The project exhibition was an event under the
technical side of the festival; Transmission. The judges were industry professionals 
from CapGemini with years of experience under their belt. """
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

st.markdown('<p class="biggest-font"><b>➲  1st Place in Final Year Project Exhibition</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/final year exhibition.JPG'), width = 640)
final = """This competition was held online in July 2020 during the lockdown brought 
about due to Covid 19. Industry experts were brought in as the panelists to judge our 
projects. After a grueling day of presentations and demos, our team came out of top 
amognst all the engineering branches. """
st.write(final)
st.markdown('#')
st.markdown('#')

