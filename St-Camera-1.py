# 
# Env - saenv5
# Import required modules
#
import os
import sys
#import cv2
import numpy as np
#import matplotlib
#from matplotlib import pyplot as plt
from datetime import datetime
import streamlit as st
from PIL import Image
#
#st.write ("Testing starts-1:", datetime.today().strftime("%x %H:%M:%S"))

#print version no
#st.write ('Python     : {}'.format(sys.version))
#st.write ('Numpy      : {}'.format(np.__version__))
#st.write ('Matplotlib : {}'.format(matplotlib.__version__))
#st.write ('OpenCV     : {}'.format(cv2.__version__))

# 
st.title(" -- Streamlit testing -- ")

# Get the file from the user using file Uploader
image_file = st.file_uploader('Give input file:', type=['jpg'])

#image_file = st.camera_input("Take a picture")

if not image_file:
   st.warning('Please input an image file name')
   st.stop()
st.success('Thank you for inputting a name: '+image_file.name)
#st.write('Image file:', image_file.name)
#st.write('Image file type:', image_file.type)

#
image = Image.open(image_file)
#st.image(image, caption=image_file.name, width=500)

#
d_width = 200
width = st.sidebar.slider('Select image width:', 100, 600, d_width)
st.write('Image width:', width, 'pixels')
st.image(image, caption=image_file.name, width=width, channels = 'RGB')
#

st.write ('Example ends here:', datetime.today().strftime("%x %H:%M:%S"))
st.title(" -- Streamlit testing Ends -- ")
# 
