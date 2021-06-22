
# 
# Env - saenv7
#

#Import required modules
#
import os
import sys
#import cv2
import numpy as np
#import matplotlib
#from matplotlib import pyplot as plt
from datetime import datetime
import streamlit as st
#from PIL import Image
#
st.title ('Testing Streamlit Deployment - 2')
st.write ("Testing starts-1:", datetime.today().strftime("%x %H:%M:%S"))

#print version no
st.write ('Python     : {}'.format(sys.version))
st.write ('Numpy      : {}'.format(np.__version__))
#st.write ('Matplotlib : {}'.format(matplotlib.__version__))
#print ('OpenCV     : {}'.format(cv2.__version__))
# 
st.write("Streamlit testing - 1")

#
#image = Image.open('Sumi-Aru-1.jpg')
#st.image(image, caption='Sumi & Aru near the water fall', width=500)

#
age = st.slider('How old are you?', 0, 100, 10)
st.write("I'm ", age, 'years old')

salary = st.slider('What is your salary?', 1000, 100000, 5000)
st.write("My salary INR", salary, 'per month')

#
st.write ('Example ends here:', datetime.today().strftime("%x %H:%M:%S"))

# 
