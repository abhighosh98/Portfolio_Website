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
st.markdown('<p class="biggest-font"><b>➲  Quantiphi Analytics, Mumbai</b></p>', unsafe_allow_html=True)
st.title("Machine Learning Engineer")
# with st.container():
#     col1, col2 = st.columns(2)
#     with col1:
#         st.image(Image.open('Images/convocation 2.jpeg'), width = 320)
#     with col2:
#         st.image(Image.open('Images/Scholarship award.jpeg'), width = 370)
quantiphi = """https://quantiphi.com/"""
st.write(quantiphi)
with open("Files/Quantiphi Recommendation Letter.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
st.sidebar.download_button(label = "Download Quantiphi Recommendation Letter",
                    data = PDFbyte,
                    file_name = "Abhishek Ghoshal Quantiphi Letter.pdf",
                    mime = 'application/octet-stream')
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  Omniaz, Singapore(Remote)</b></p>', unsafe_allow_html=True)
st.title("Intern")
# with st.container():
#     col1, col2 = st.columns(2)
#     with col1:
#         st.image(Image.open('Images/convocation 2.jpeg'), width = 320)
#     with col2:
#         st.image(Image.open('Images/Scholarship award.jpeg'), width = 370)
omniaz = """[Omniaz](https://www.omniaz.io/) is a tech based company that provides AR
 based marketing solutions for a number of industries. I worked as an Intern in the
 Machine Learning R&D Department. I was working with one other colleague to optimise 
 the image matching and image similarity for one of the in-house products of Omniaz.
 
"""
st.write(omniaz)
with open("Files/Internship_Certificate_Omniaz.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
st.sidebar.download_button(label = "Download Omniaz Internship Certificate",
                    data = PDFbyte,
                    file_name = "Abhishek Ghoshal Omniaz Internship Certificate.pdf",
                    mime = 'application/octet-stream')
st.markdown('#')
st.markdown('#')