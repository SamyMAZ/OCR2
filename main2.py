# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:48:35 2021

@author: b.tabet
"""

import pandas as pd
from PIL import Image
import streamlit as st


import utils.functions as functions
from utils.SamplePreprocessor import preprocess
import utils.team_page as team_page
import utils.dataset_page as dataset_page
import utils.objectDetection_page as ObjectDetection_page
import utils.conclusion_page as conclusion_page
import utils.modelPres_page as modelPres_page
import numpy as np
import tensorflow as tf
from tensorflow import keras
import string
import matplotlib.pyplot as plt
import cv2
import seaborn as sns



#CONSTANTS
DIR_PATH = "C:/Users/mazou/AppData/Local/Packages"
PATH     = "C:/Users/mazou/OneDrive/Documents/PyOCaRe_DemoStreamlit/utils/images"

##### SIDEBAR #####

sidebar_title = st.sidebar.title("👌 OCR Project 👌 ")
team_button =       st.sidebar.button("➡ Team______________ _")
dataset_button =    st.sidebar.button("➡ DataSet___________ _")
#modelPres_button =  st.sidebar.button("➡ Présentation du model _")



# Traitement et détection d'objet
with st.sidebar.expander("Détection d'objet", True):
    with st.form(key ='Form1'):
        
        select_form = st.selectbox("Choix du formulaire", 
                                   ["Manuscrit 1",
                                    "Manuscrit 2",
                                    "Manuscrit 3"])
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Traitement**")
            chbox_treat_1 = st.checkbox('1', key='chbox_treat_1')
            chbox_treat_2 = st.checkbox('2', key = "chbox_treat_2")
            chbox_treat_3 = st.checkbox('3', key = "chbox_treat_3")
            chbox_treat_4 = st.checkbox('4', key = "chbox_treat_4")
        
        with col2: 
            st.write("**Bounding Box**")
            chbox_Tessereact    =    st.checkbox('1', key = "chbox_Tessereact")
            chbox_Initial       =    st.checkbox('2', key = "chbox_Tessereact")
            
        submitted1 = st.form_submit_button(label = 'Charger le formulaire 🔎')
        
if submitted1:
    
    ObjectDetection_page.display_objectDetection(select_form,
                                                 chbox_Tessereact,
                                                 chbox_Initial, 
                                                 chbox_treat_1,
                                                 chbox_treat_2,
                                                 chbox_treat_3, 
                                                 chbox_treat_4)


modelPres_button =  st.sidebar.button("➡ Présentation du model _")    

# SideBar détection d'objet en live
with st.sidebar.expander("Détection d'objet EN LIVE", False):
    with st.form(key ='Form2'):
        
        select_form = st.selectbox("Choix du formulaire", 
                                   ["Manuscrit 1",
                                    "Manuscrit 2",
                                    "Manuscrit 3"])
        
        st.write("Preprocessing des formulaires et des images")
     
            
        submitted2 = st.form_submit_button(label = 'Charger le formulaire 🔎')


if submitted2:
    
    ObjectDetection_page.display_ModelDetection(select_form)
    

conclusion_button =         st.sidebar.button("➡ Conclusion_____ _")


subheader_project_role =        "Role within the project"
subheader_current_position =    "Current professional position"
fp_benjaminTabet_picture =      PATH + "benjamin tabet.jpg"
fp_samyMazouz_picture =         PATH + "samy.jfif"
fp_ariSekar_picture =           PATH + "ari-vinoth.jfif"



dataSetButton_img1 =            PATH + "dataSetButton_img_1"
dataSetButton_img2=             PATH + "dataSetButton_img_2"




width_picture =170
height_picture = 190

#Page to present Team 
if team_button:
    team_page.display_team_page()


if dataset_button :
    dataset_page.display_dataset_page()
    
if conclusion_button:
    conclusion_page.display_conclusion_page()
    
if modelPres_button:
    modelPres_page.display_modelPres_page()
        
        
        #st.write("** DataSet extract **")
        # df_words = pd.read_csv('word.csv')
        # st.write(df_words.head())
        # #Afficage aléatoire des images du DF
        # fig=plt.figure(figsize=(100, 100))
        # columns = 5
        # rows = min(len(df_words)/5,4)
        # #for i in range(1, columns*rows +1): 
        # for i in range(1, 11): 
        #     img = DIR_PATH + df_words.iloc[i,11]
        #     pil_im = Image.open(img)
        #     fig.add_subplot(rows, columns, i)
        #     plt.imshow(np.asarray(pil_im))
        # #Affichage de la figure matplotlib chargée de toutes les images
        # st.write("** Images extracted from DataSet **")
        # st.pyplot(fig)
            
       
        #Pairplot
        # st.write("** Répartition des images reconnues ou non par le modèle en fonction des paramètres ** ")
        # st.write("Nous pouvons observer sur ce pairplot que les images non reconnues par le modèle, ",
        #          "se concentrent à certains endroit en fonction des paramètres.")
        # img = Image.open("pairplotDfClean.png")
        # st.image(img)
        
        # #### Code pour charger le paiplot
        # # #Affichage d'un pairplot sur le DF contenant les varibales propres
        # # dfClean= df_words[(df_words['len']<30)& (df_words['width']<1200) & (df_words['width']!=-1)]
        # # fig = plt.figure()
        # # sns.pairplot(dfClean, hue = 'target',hue_order=[1,0]) 
        # # #Code pour enregistrer la figure au format image
        # # fig = swarm_plot.fig
        # # fig.savefig('output.png') 
        # # st.pyplot(fig)

        # #photo
        # st.write("This is inside the container")
        
   
# if test_button :

#     array_pictures = []
    
#     # Specify canvas parameters in application
#     stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
#     stroke_color = st.sidebar.color_picker("Stroke color hex: ")
#     bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
#     bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
#     drawing_mode = st.sidebar.selectbox(
#         "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
#     )
#     realtime_update = st.sidebar.checkbox("Update in realtime", True)
    
#     add_selectbox = st.sidebar.selectbox(
#         "How would you like to be contacted?",
#         ("Email", "Home phone", "Mobile phone")
#     )
    
#     button = st.sidebar.button("click here!")
    
#     # Create a canvas component
#     canvas_result = st_canvas(
#         fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
#         stroke_width=stroke_width,
#         stroke_color=stroke_color,
#         background_color=bg_color,
#         background_image=Image.open(bg_image) if bg_image else None,
#         update_streamlit=realtime_update,
#         height=150,
#         drawing_mode=drawing_mode,
#         key="canvas",
#     )



#     # import requests
    
#     # f = open('Ntest1.png','wb')
#     # #response = requests.get(canvaImg)
#     # img = Image.open(bg_image)
#     # f.write(img)
#     # f.close()
    
#     #st.title(bg_image)
    
#     IMG_SIZE = (128, 32)
    
#     # st.title('test new')
#     # image = Image.open('test2.png')
#     # image = np.array(image)
#     # st.image(image, caption='Sunrise by the mountains')
#     # st.title(image.shape)
#     # #image = np.int64(np.all(image[:, :, :3] == 0, axis=2))
#     # #image = np.array(image)
#     # st.image(image, caption='Sunrise by the mountains')




#     if bg_image is not None:
        
    
        
        
#         st.title('Décodage d\' une image charger')
#         st.text('Image au chargement')
#         img = Image.open(bg_image)
#         img = np.array(img)
#         st.text('dimension de image : ' + str(img.shape))
#         #img = np.int64(np.all(img[:, :, :3] == 0, axis=2))
#         #print(img)
#         #st.text(img)
#         st.image(img)
#         #img = Image.fromarray(img)
#         #st.title(img)
#         img = np.array(img, dtype='uint8')
    
#         img = preprocess(img, IMG_SIZE)    
#         st.text('dimension de image après le preprocessing' + str(img.shape))
#         #st.image(img, clamp=True, channels='BGR')
#         #st.image(img)
#         st.title('1')
#         array_pictures = []
#         array_pictures.append(img)
#         array_pictures = np.array(array_pictures)
#         img = tf.expand_dims(array_pictures, axis = 3) 
#         st.text(img.shape)
#         PRETRAINED_MODEL = 'model_08112021_allData_final'
#         model = keras.models.load_model(PRETRAINED_MODEL)
#         #st.text(model.summary())
#         mod = model.predict(img)
#         charList = list(string.ascii_letters)+[' ']
#         decodage = functions.greedy_decoder(mod, charList)
#         st.title( decodage[0])
    
    
#     st.title('---------------------------------------------------------')
    
#     # Do something interesting with the image data and paths
#     if canvas_result.image_data is not None:
    
#         st.title(canvas_result.image_data.shape)
#         #Recuperation de mon image
#         st.title('test')
#         st.image(canvas_result.image_data)
#         img = canvas_result.image_data
#         st.text(str(img.shape))
#         #img = np.int64(np.all(img[:, :, :3] == 0, axis=2))
#         img = img.mean(axis = 2)
#         #st.image(img)
#         st.text(str(img.shape))
#         img = np.array(img, dtype='uint8')
#         st.image(img)
#         img = preprocess(img, IMG_SIZE)   
#         st.image(img,clamp=True)
#         st.title('after preprocess :' + str(img.shape)     )
#         st.title('1')
#         array_pictures = []
#         array_pictures.append(img)
#         array_pictures = np.array(array_pictures)
#         img = tf.expand_dims(array_pictures, axis = 3) 
#         PRETRAINED_MODEL = 'model_08112021_allData_final'
#         model = keras.models.load_model(PRETRAINED_MODEL)
#         mod = model.predict(img)
#         charList = list(string.ascii_letters)+[' ']
#         decodage = functions.greedy_decoder(mod, charList)
#         st.title( decodage)
#         st.title('fin')
            
        
#     # if canvas_result.json_data is not None:
#     #     objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
#     #     for col in objects.select_dtypes(include=['object']).columns:
#     #         objects[col] = objects[col].astype("str")
#     #     st.dataframe(objects)
