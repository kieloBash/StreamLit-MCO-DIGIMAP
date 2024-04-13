import numpy as np
import streamlit as st
import image_stitching as ist

st.set_page_config(page_title="GRP6 DIGIMAP - IMAGE STITCHING", layout="wide", page_icon="🤖")

"""
# Welcome to ImageStitching!

Make your dream pics into one whole story! Upload images you want to make into a Panoramic Image.

Disclaimer: Due to the paper used as the reference for the project, the website can only stitch pictures
            that follow the ff rules:
            1. pictures uploaded should be overlapping and not straight cuts/crops.
            2. Please upload small sized pictures around up to 500px for the width and height.
            3. Please upload up to 2 images at a time.
"""
st.subheader("CALVIN CORONADO | MICHELLE MARTINEZ | KIELO BASH MERCADO | GHRAZIELLE DE RAMOS | VALEN SALIG")

# Upload multiple image files
uploaded_files = st.file_uploader("Upload two images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# Check if there are two or more uploaded images
if uploaded_files is not None and len(uploaded_files) >= 2:
    # Create a button
    if st.button('Start Stitching'):
        # st.write("Clicked")
        # Call the function when the button is clicked
        ist.stitch_images(uploaded_files)
else:
    st.warning("Please upload two images to start stitching.")
    
if uploaded_files is not None:
    # Display each uploaded image
    for uploaded_file in uploaded_files:
        st.image(uploaded_file)
