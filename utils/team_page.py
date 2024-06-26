# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:45:18 2021

@author: b.tabet
"""

import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

import utils.functions as functions
from utils.SamplePreprocessor import preprocess
import numpy as np
import tensorflow as tf
from tensorflow import keras
import string
import matplotlib.pyplot as plt
import cv2
import seaborn as sns



#CONSTANTS
DIR_PATH = "C:/Users/b.tabet/Documents/PRIVE/Projet/PyOCaRe/Package/"
PATH     = "C:/Users/benja/Documents/Data Science/PyOCaRe/utils/images/"


subheader_project_role =        "Role within the project"
subheader_current_position =    "Current professional position"
fp_benjaminTabet_picture =      PATH + "benjamin tabet.jpg"
fp_samyMazouz_picture =         PATH + "samy.jfif"
fp_ariSekar_picture =           PATH + "ari-vinoth.jfif"



dataSetButton_img1 =            PATH + "dataSetButton_img_1"
dataSetButton_img2=             PATH + "dataSetButton_img_2"



width_picture =170
height_picture = 190

#@st.cache(suppress_st_warning=True)
def display_team_page():
    
    st.header("Présentation de l'équipe projet")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Benjamin Tabet")
        #photo
        img = Image.open(fp_benjaminTabet_picture)
        
        img = img.resize((width_picture, height_picture))
        st.image(img)
        st.subheader("")
        st.subheader("Data Scientist")
        #role within the project
        st.write("**", subheader_project_role, "**")
        st.write("In charge of the implementation of  **deep learning model** to recognise word in a picture")
        #current professional position
        st.write("**", subheader_current_position, "**")
        st.write("Business Data Analyst / Scientist")
    
    with col2:
        st.subheader("Samy Mazouz")
        #photo
        img = Image.open(fp_samyMazouz_picture)
        img = img.resize((width_picture, height_picture))
        st.image(img)
        st.subheader("")
        st.subheader("Data Scientist")
        #role within the project
        st.write("**", subheader_project_role, "**")
        st.write("In charge of the implementation of  **bounding box model** to isolate words in handwritten forms")
        #current professional position
        st.write("**", subheader_current_position, "**")
        st.write("PMO")

    
    with col3:
        st.subheader("Ari-Vinoth Sekar")
        #photo
        img = Image.open(fp_ariSekar_picture)
        img = img.resize((width_picture, height_picture))
        st.image(img)
        st.subheader("")
        st.subheader("Data Scientist")
        #role within the project
        st.write("**", subheader_project_role, "**")
        st.write("In charge of analysing the dataset, finding the OCR's usecases and helping at improving the models")
        #current professional position
        st.write("**", subheader_current_position, "**")
        st.write("Nuclear process engineer in data reconversion")