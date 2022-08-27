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
st.markdown('<p class="biggest-font"><b>➲  University of Southern California, Los Angeles</b></p>', unsafe_allow_html=True)
st.title("Position: Course Producer for DSCI 551: Foundations of Data Mangement")
usc = """As a Course Producer my responsibilities included grading assignments, projects and lab work for students in the Fall 2022 offering of this class. Apart from this I also held weekly office hours to help students in any and all aspects regarding the class. """
st.write(usc)
st.markdown("### Technologies and Concepts Used")
st.write("AWS, MongoDB, SQL, Firestore, ")

st.markdown('<p class="biggest-font"><b>➲  Quantiphi Analytics, Mumbai</b></p>', unsafe_allow_html=True)
st.title("Position: Machine Learning Engineer")
quantiphi = """[Quantiphi](https://quantiphi.com/) is a service based company with 
multiple verticals in the entertainment, consulting, medical, insurance sectors 
to name a few. I worked on 3 projects in the duration of 1 year at Quantiphi. 

My first project was a POC research based project to detect ransomwares using 
ML. This was a novel concept for me; using ML to solve a security problem. I 
worked with a large team where my colleagues had an eclectic set of skills. The team 
had a number of Machine Learning Engineers, Data Engineers, Security Engineers 
and Platform Engineers. We were working on petabytes of data accessible through Google BigQuery. I became 
proficient at writing SQL querries to extract the required data. The data was divided 
into 3 sets based on certain parameters. Through the course of the project, I 
took the lead on one of the sets. Initially, performing extensive EDA and later 
with model development and documentation. I was frequently on calls with the
client explaining the work the team had done and answering questions from them. 

During this time I was also allocated to another project where I mentored a 
colleague on tensorflow and GCP related tasks. 

During my final project at Quantiphi, I worked on an production grade project for 
engine defect detection slated to be deployed on an assembly line. The ML team
consisted of me and one more colleague. We had frequent calls with the client's 
tech team regarding our approach for the problem and our results. We were given an 
in-depth virtual tour of the assembly line, stations and where our model 
will be deployed. Our model took their accuracy from below 10% to 
78%. Improving their model accuracy solved multiple problems for them. 
"""

st.write(quantiphi)
with open("Files/Quantiphi Recommendation Letter.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
st.sidebar.download_button(label = "Download Quantiphi Recommendation Letter",
                    data = PDFbyte,
                    file_name = "Abhishek Ghoshal Quantiphi Letter.pdf",
                    mime = 'application/octet-stream')

st.markdown("### Technologies and Concepts Used")
st.write("Tensorflow, CNN, OpenCV, Model Interpretability, SHAPley, Python, Pandas, Transfer Learning, GCP, AWS, Huggingface Transformers, SOTA Models, SQL, Google BigQuery, Google Cloud Storage, Google AI Platform Notebooks, GCP Compute Instances, Data Analysis, Deep Learning, Anomaly Detection ")

st.markdown("### Challenges")
st.write("The team and I faced some minor issues during the first POC project. The client was not able to deliver the data on time due to security issues. We had to generate gigabytes of logs on our computers. Throughout the project we kept learning about new security concepts such as MITRE framework, ransomware attack vectors and sandboxes for detonating ransomware payloads. Once we had our own data, we had to redo parts of the EDA to ensure that the previously found insights still hold for this newly generated data. There were also continuous changes to the deliverables and the client's requirements which led to the team collborating during crunch times. ")
st.write("Since the ML team was small for the second project, more responsibilities were given to me. My colleague and I had multiple sessions to decide an approach and run experiments even before the project kick off date. This involved significant research to be done in this phase. The main challenge in this project was that the margin of error was very small since one engine prediction was actually made up for several smaller part level predictions. Errors in prediction at the part level would result in the errors propogating for the engine level statistics. ")
st.markdown('#')
st.markdown('#')

st.markdown('<p class="biggest-font"><b>➲  Omniaz, Singapore(Remote)</b></p>', unsafe_allow_html=True)
st.title("Position: Intern")
omniaz = """[Omniaz](https://www.omniaz.io/) is a tech based company that provides AR
 based marketing solutions for a number of industries. I worked as an Intern in the
 Machine Learning R&D Department for a month. I was working with one other colleague to optimise 
 the image matching and image similarity for one of their in-house products of Omniaz.
 
First, I had to familiarise myself with their tech stack and dataset during the onboarding.
. I came across new libraries like imgaug which was used for image augmentation.
. Then I ran extensive tests for SOTA models like Resnet, VGG16 and others on an extensive 
dataset and collated the results. I also had to setup and test [FAISS](https://github.com/facebookresearch/faiss) 
as a sort of baseline for our own pipeline. """
st.write(omniaz)
st.markdown("### Technologies and Concepts Used")
st.write("OpenCV, Tensorflow, CNN, Python, Pandas, Siamese Networks, Contrastive Loss, Transfer Learning, Image Preprocessing and Augmentation")

st.markdown("### Challenges")
st.write("At the time, this was the most advanced project I had worked on. It took time for me to get started with the GCP environment and pipeline setup. While I had some past experience using CNNs in academic projects, I developed a scientific rigor while working on CNNs for Omniaz. I realised the importance of good image preprocessing and augmentation and how the resulting images need to match possible images from the end user. This was also the first time I came across the differences between an ideal environment for testing and the real world; another thing that needs to be taken into account during development. ")

with open("Files/Internship_Certificate_Omniaz.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
st.sidebar.download_button(label = "Download Omniaz Internship Certificate",
                    data = PDFbyte,
                    file_name = "Abhishek Ghoshal Omniaz Internship Certificate.pdf",
                    mime = 'application/octet-stream')
st.markdown('#')
st.markdown('#')