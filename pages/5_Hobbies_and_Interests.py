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
st.markdown('<p class="biggest-font"><b>➲  Me Time</b></p>', unsafe_allow_html=True)
st.title("Motorbikes")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image(Image.open('Images/bike 2.jpeg'), width = 320)
    with col2:
        st.image(Image.open('Images/bike 1.jpeg'), width = 327)
bike = """As soon as I turned 18, I started learning to drive the car and ride the bike.
The latter became an escape for me. I started going on short rides around my neighbourhood 
between work sessions. Looking back however, I never needed an excuse to go on a ride. 
I undertook several short trips with my friends while I was in India. """
st.write(bike)
st.markdown('#')
st.markdown('#')

st.title("Gaming")
with st.container():
    st.image(Image.open('Images/setup.png'), width = 640)
gaming = """I have played hundreds of games and invested thousands on hours 
into gaming. I firmly believe that games as far better than movies or books
 in delivering a narrative experience. Gaming is one of those things that
  I cannot see myself giving up anytime soon. In fact I would want to delve 
  even deeper into the realm. Having a proper setup also aids in higher 
  productivity when working on it. """
st.write(gaming)
st.markdown('#')
st.markdown('#')

st.title("Exercise")
gym = """Exercising is something I try to do on a daily basis despite 
the amount of work I may have. It has helped me gain a lot of self-confidence
 over the years and helped forged me into the what I am today. """
st.write(gym)
st.markdown('#')
st.markdown('#')