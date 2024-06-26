# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:54:38 2021

@author: b.tabet
"""


import streamlit as st
from PIL import Image

#CONSTANT:

PATH     = "C:/Users/benja/Documents/Data Science/PyOCaRe/utils/images/"


def display_modelPres_page():
    
    st.header('Présentation du Model')
    img = Image.open(PATH + 'Schema Model.PNG')
    st.image(img)
    
    st.subheader("Zoom sur le CNN")
    
    img = Image.open(PATH + "model_presentation_1.png")
    st.image(img)
    
    st.subheader("Zoom sur le RNN")
    
    img = Image.open(PATH + "Schema CTC.PNG")
    st.image(img)
    
    
    st.subheader("Les couches utilisées")
    
    st.write("**Couche Conv2D**")
    st.write("Découpage d'une image en morceau et analyse de chaque partie")

    st.write("**Couche BatchNormalization:**")
    st.write("Réduxtion de la dispersion dans un interval donnée, permet d'améliorer les performances du model")
    
    st.write("**Couche LeakyRlu**")
    st.write("Permet l'ajout de variante pour les valeurs négatives de façon à ce que les neuronnes soit toujours présents")
    
    st.write("**Couche MaxPooling:**")
    st.write("Compresse le tenseur d’entrée pour n’en garder que l’information pertinente. Cette couche va conserver en fonction des parametre seulement certaines parties d'un morceau.")
    
    st.write("**Couche RNN:**")
    st.write("Analyse plusieurs fois chaque parties pour en gardant en mémoire l'analyse précédente")
    
    st.write("**Couche Dense:**")
    st.write("Application d'une transformation basique avec fonction d'activation sur une entrée.")    
    
