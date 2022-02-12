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
st.write ("Testing starts-1: Shyam", datetime.today().strftime("%x %H:%M:%S"))

#print version no
st.write ('Python     : {}'.format(sys.version))
st.write ('Numpy      : {}'.format(np.__version__))
#st.write ('Matplotlib : {}'.format(matplotlib.__version__))
#st.write ('OpenCV     : {}'.format(cv2.__version__))

# 
st.title(" -- Streamlit testing -- ")

#
st.title(" -- Streamlit testing example for mobile -- ")
st.write ('Example ends here:', datetime.today().strftime("%x %H:%M:%S"))
st.title(" -- Streamlit testing Ends -- ")
# 
