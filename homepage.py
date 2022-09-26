import streamlit as st
import base64

st.set_page_config(
    page_title="Evan's Blog"
)

st.title("Evan's Blog")
st.sidebar.success("Select a page")




def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('wallpaper.png') 
