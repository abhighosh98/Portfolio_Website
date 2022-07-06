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
    font-size:75px !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar 
st.sidebar.image(Image.open('Images/personal 1-modified.png'))
with st.sidebar.container():
    # col1, col2, col3 = st.columns(3)
    # with col2:
    st.markdown('<p class="big-font"><u>Abhishek Ghoshal</u></p>', unsafe_allow_html=True)
st.sidebar.markdown("# Contact Me At")
st.sidebar.write("Gmail : [abhighosh98@gmail.com](https://abhighosh98@gmail.com)")
st.sidebar.write("LinkedIn : [abhishek-m-ghoshal](https://www.linkedin.com/in/abhishek-m-ghoshal)")
st.sidebar.write("Github : [abhighosh98](https://github.com/abhighosh98)")

# Main Text
st.markdown('<p class="biggest-font"><b>asdf</b></p>', unsafe_allow_html=True)
st.write("I've always been interested in")
