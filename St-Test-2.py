# 
# Env - saenv5
# Import required modules
#
import os
import sys
import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime
import streamlit as st
from PIL import Image
#
# 
st.title(" -- Streamlit testing -- ")

#
st.sidebar.text('Testing starts-1:'+ datetime.today().strftime("%x %H:%M:%S"))

# print version no
st.sidebar.text(' *** Environment Details ***')
st.sidebar.text('Python     : '+sys.version)
st.sidebar.text('Numpy      : '+np.__version__)
st.sidebar.text('Matplotlib : '+matplotlib.__version__)
st.sidebar.text('OpenCV     : '+cv2.__version__)

# Read image using OpenCV
st.sidebar.write(' ** Using OpenCV ** ')

# Get the file from the user using file Uploader
image_file = st.sidebar.file_uploader('Give input file:', type=['jpg'])

if not image_file:
   st.warning('Please input an image file name')
   st.stop()
st.success('Thank you for inputting a name: '+image_file.name)

st.write('Image filename:', image_file)

#
# Read image using PIL, then convert it to OpenCV image format for all processing
pil_image = Image.open(image_file).convert('RGB')  
open_cv_image = np.array(pil_image) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy() 
#

#image = cv2.imread(image_file.name)
image = open_cv_image.copy()

#
d_width = 200
width = st.sidebar.slider('Select image width:', 100, 600, d_width)
st.write('Image width:', width, 'pixels')
st.image(image, caption=image_file.name+' -- Original', width=width, channels = 'BGR')

# Convert to Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
st.image(gray, caption=image_file.name+' -- Gray', width=width)

#
st.write ('Example ends here:', datetime.today().strftime("%x %H:%M:%S"))
st.title(" -- Streamlit testing Ends -- ")
#
