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
            More on software, I always use the unreleased iOS versions because I have access to developer beta content. 
            I get to test features before everyone else and it's always exciting. 
            For example, I've had iOS 16 since June when everyone got it in September.

            As you can tell, I love technology a lot :D
            """
        )

    with right_column:
     
        image = Image.open('myComputer.jpg')
        st.image(image, caption='I built this computer!')
      
