#!/usr/bin/env python
# coding: utf-8
#
###
#print ("Testing starts-1a:")
###
#
#!pip install clarifai-grpc

# 
# Uses Clarifai APIs for Object Detection in Python - Jupyter Notebook & .py scripts
#
import os
import sys
import numpy as np
import pandas as pd
import cv2
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime
#
import pyttsx3
import streamlit as st
from PIL import Image
#
# 
st.title(" -- Streamlit testing -- ")
#
#
st.sidebar.text('Testing starts-1:'+ datetime.today().strftime("%x %H:%M:%S"))

# print version no
st.sidebar.text(' *** Environment Details ***')
st.sidebar.text('Python     : '+sys.version)
st.sidebar.text('Numpy      : '+np.__version__)
st.sidebar.text('Matplotlib : '+matplotlib.__version__)
st.sidebar.text('OpenCV     : '+cv2.__version__)

# Read image using OpenCV
st.sidebar.write(' ** Using OpenCV n Clarifai API ** ')

# Take a picture using camera

image_file = st.camera_input("Take a picture")

if not image_file:
   st.warning('Please input an image file name')
   st.stop()
st.success('Thank you for inputting a name: '+image_file.name)

#st.write('Image filename:', image_file)
#
# Read the image file as Byte stream

file_bytes = image_file.getvalue()

#
# Set up voice processing stuff
#
engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
#print(type(voices), len(voices), '\n', voices[0], '\n', voices[1])
engineio.setProperty('rate', 130)
engineio.setProperty('voice',voices[0].id)
#
label = 'Voice over testing'
engineio.say(label)
engineio.runAndWait()
#
# Read image using PIL, then convert it to OpenCV image format for all processing
pil_image = Image.open(image_file).convert('RGB')  
open_cv_image = np.array(pil_image) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy() 
#

#image = cv2.imread(image_file.name)
image = open_cv_image.copy()

#image_orig = image.copy() # Copy original image to display later
(H, W) = image.shape[:2]
st.write('Image H, W:', H, W, 'pixels')
#
#d_width = 200
#width = st.sidebar.slider('Select image width:', 100, 600, d_width)
#st.write('Image width:', width, 'pixels')
st.image(image, caption=image_file.name+' -- Original', width=W, channels = 'BGR')

#
#Set Clarifai API key
#key = st.text_input("App Key")

key = "ca2997db54074b768e5b596ed5d5b940"  # --- API key for App-1, General Object Detection
#key = "397dbc4a0d23447a9171650b3ae0ad11" # --- API key for Face-1, Face Detection
#
# Start Clarifai API processing
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# This is how you authenticate.
metadata = (('authorization', 'Key {}'.format(key)),)

request = service_pb2.PostModelOutputsRequest(

# This is the model ID of a publicly available General model. You may use any other public or custom model ID.
#   model_id='aaa03c23b3724a16a56b629203edc62c',
#   model_id='f76196b43bbd45c99b4f3cd8e8b40a8a', for face detection
   model_id = 'general-image-detection', 
   inputs=[
     resources_pb2.Input(
         data=resources_pb2.Data(image=resources_pb2.Image(base64 = file_bytes)))
#         data=resources_pb2.Data(image=resources_pb2.Image(url="https://upload.wikimedia.org/wikipedia/commons/a/a0/Pierre-Person.jpg")))
#         data=resources_pb2.Data(image=resources_pb2.Image(url="https://samples.clarifai.com/metro-north.jpg")))
   ])
response = stub.PostModelOutputs(request, metadata=metadata)

if response.status.code != status_code_pb2.SUCCESS:
   raise Exception("Request failed, status code: " + str(response.status.code))

# Start - Testing for Bounding boxes

for regions in response.outputs[0].data.regions:
    x1 = int(regions.region_info.bounding_box.left_col *W)
    y1 = int(regions.region_info.bounding_box.top_row *H)
    x2 = int(regions.region_info.bounding_box.right_col *W)
    y2 = int(regions.region_info.bounding_box.bottom_row *H)
    #print ("regions :\n", x1, y1, x2, y2)
    cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
    #print ("regions :\n", regions.region_info.bounding_box.top_row)
    # 
    # Voice over the image dertails
    label = regions.data.concepts[0].name
    #print ("regions: ", x1, y1, x2, y2, label)
    engineio.say(label)
    engineio.runAndWait()
# 
# Convert to Gray
image_p = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
st.image(image_p, caption=image_file.name+' -- Processed', width=W)

#
st.write ('Example ends here:', datetime.today().strftime("%x %H:%M:%S"))
st.title(" -- Streamlit testing Ends -- ")
#
############
#
