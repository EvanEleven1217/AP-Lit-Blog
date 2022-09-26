import streamlit as st
import base64
from PIL import Image

st.set_page_config(page_title="Evan's Blog")

st.title("Evan's Blog")
st.subheader("Welcome! :wave: ")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Fun fact, I spent much more time making this website than I should have, 
            reason being because I did not use a website builder. 
            Instead, this website is made purely by Python: a programming language.
            Because of this, everything takes more time and effort,
            but in the end, I'm fine with it because I love Python and I am able to put my skills to good use.
            This blog will look relatively simple as it is time consuming and complicated to manage.
            I will also be learning more from this experience!
            """
            )
    with right_column:
        python = Image.open('pythonLogo.png')
        st.image(python, caption='Python Logo!')

    codeEx = Image.open('codeExample.png')
    st.image(codeEx, caption='Behind the scenes of this website! (obviously only a fraction of it)')
    
st.sidebar.success("Select a page")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('mountainBackground.jpg') 
