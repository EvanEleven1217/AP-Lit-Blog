import streamlit as st
import base64
from PIL import Image

with st.container():
    st.title("About me")

    left_column, right_column = st.columns(2)

    with left_column:
        st.write(
            """
            Hi! I'm Evan Lee, and I'm a senior at Yorba Linda High School. 
            My favorite thing in life is technology: both hardware and software. 
            Regarding hardware, I enjoy building PCs and dissasembling devices like phones and laptops. 
            I love companies like Apple, and I keep up with leaks so I know every product before it's announced.
            As for software, I love programming. 
            I'm familiar with three programming languages so far: Python, Java, and C#.
            Python is my personal favorite programming language.

            As you can tell, I love technology a lot :D
            """
        )

    with right_column:
     
        image = Image.open('myComputer.jpg')
        st.image(image, caption='I built this computer!')

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

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



      
