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
st.sidebar.markdown("Visit my [Github](https://github.com/abhighosh98) for more projects. ")

# Main Text
st.markdown('<p class="biggest-font"><b>➲  AI Pet Robot</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/AI Pet 1.png'), width = 370)
pet = """The primary objective of this project is to make an AI based pet that can interact seamlessly with humans and react based on the inputs it receives from its array of sensors and camera. We aim to make this pet a smart robot with multiple functions and capabilities to keep its human companion engaged. Eventually we hope to fulfill any humans need of a pet with the help of our AI pet without the problems that arise with owing real pets.  """
st.write(pet)
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  AI Stylist</b></p>', unsafe_allow_html=True)
with st.container():
    st.image(Image.open('Images/ai_stylist_snap.png'), width = 640)
ais = """AI Stylist is for people with color blindness which will help them select clothes from their wardrobe and give them the ability to dress better by overcoming the drawbacks due to color blindness. It can also help others save precious time that is wasted daily on choosing an outfit. """
st.write(ais)
st.markdown('#')
st.markdown('#')

