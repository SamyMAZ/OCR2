# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:54:38 2021

@author: b.tabet
"""


import streamlit as st
from PIL import Image
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
def display_dataset_page():
    
    with st.container():
        
        
        st.header('Présentation du DataSet')
        st.subheader("Introduction")

        st.write("La reconnaissance optique de caractères (OCR) est une technique",
                     " permettant de transformer le texte présent sur une photographie en fichier texte.")
        st.write("Le système OCR utilise les plus récentes technologies pour collecter les informations d'un document",
                     " (texte, photographie) scanné et le convertit ensuite en un fichier texte. Pour cela, le système OCR ",
                     "compare les couleurs noires et blanches d'un document pour déterminer chaque code alphanumérique.",
                     "Le système reconnaît ensuite chaque caractère, et le convertit en texte ASCII (Code américain normalisé pour ",
                     "l'échange d'information).")
         
        #img = Image.open(dataSetButton_img1)
        #img = img.resize((width_picture, height_picture))
        #st.image(img)
    
        st.subheader("Exploration des données")
        #with st.expander("Voir l'exploration des données", True):
            
        st.write("La banque d’image utilisée est la IAM Handwriting Database. Réalisée avec la participations de 657 personnes "+
                     "ayant rédigés des fichiers manuscrits: \n")
        st.text("▪    1 539 pages de texte scannées \n" + 
                "▪    5 685 phrases isolées et labellisées \n" +
                "▪    13 353 lignes de texte isolées et labellisées \n" +
                "▪    115 320 mots isolés et labellisés  ")
        
        st.write("** Signification des variables : ** \n")
        st.text(     "FileName:     Nom du fichier png \n"+
                     "greyLevel:    Nuance de gris de l'image ( 0 noir -> 255 blanc)\n"+
                     "target:       Détection du mot ( 0 si non, 1 si Oui par l’algorithme source)\n"+
                     "X_Begin:      Position départ abscisse \n"+
                     "Y_Begin:      Position départ ordonnée \n"+
                     "width:        Largeur de l'image \n"+
                     "Height:       Hauteur de l'image \n"+
                     "Tag:          Nature du mot \n"+
                     "Word:         Mot identifié \n"+
                     "Path:         Chemin d'accès à l'image")       
            
        #img = Image.open(dataSetButton_img2)
        #img = img.resize((width_picture, height_picture))
        #st.image(img)
        
        st.subheader("Affichage des Pairplot")
        
        #with st.expander("Visualiser les graphiques", True):
            
        st.write("On constate sur le pairplot la présence de point trés éloignés pour les graphiques de mise",
                 "en relation des variables largeur du mot et nombre de lettre",
                 "Pour cela, nous avons décidé de séparer le DataSet en 2 groupes:")
        
        col1, col2 = st.columns(2)
       
        
        with col1:
            
            
            st.write("**Avec les valeurs abhérentes**")
            img = Image.open(PATH + "Pairplot_avecValAbhe.png")
            # img = img.resize((width_picture, height_picture))
            st.image(img)
            st.text("- Largeur image > 1200 px \n" +
                    "- Longueur mot > 30 lettres \n" )
                
        with col2:
            
            st.write("**Sans les valeurs abhérentes**")
            img = Image.open(PATH + "Pairplot sans valeur abérrant.png")
            #img = img.resize((width_picture, height_picture))
            st.image(img)

                
        #Affichage de la matrice de correlation   
            
           
        #img = Image.open(dataSetButton_img2)
        #img = img.resize((width_picture, height_picture))
        #st.image(img)
            
        st.subheader("Matrice de correlation")
        
        img = Image.open(PATH +  "Matrice de correlation.png")
        img = img.resize((250, 250))
        st.image(img)
        
        st.write("L'analyse des corrélations entre les varaibles ne nous indice pas grand chose",
                 "mise à part un forte corrélation entre le nombre de caractère d'un mot et la largeur de l'image (assez attendu)",
                 "Il semble également y avoir une corrélation entre largeur et hauteur mais pas aussi forte que ce que l'on pourrait intuiter",
                 "Il semblerait que plus le mot contient de caractères plus celui-ci aura une image grande. Cela est du à ",
                 "la plus grande probabilité d'avoir une lettre 'grande' dans un mot si celui-ci est long ( ex : L/ F /G)")
        
                    
        st.subheader("Affichage des images non reconnues")    
        
        
        
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.write("** Image trop large **")
            img = Image.open(PATH + "dataSet_pres_ImageTropLarge.jpeg")
            st.image(img)
            st.write("On peut observer que la présence de ponctuation d'apostrophe ou de point sur des I pourrait ",
                     "avoir une incidence sur la dectection et qui explique parfois les hauteurs plus grandes des mots")
        with col2:
            st.write("** Image trop petite **")
            #Ajouter les images petites
            
            img = Image.open(PATH +"dataSet_pres_ImageTropPetite.jpeg")
            st.image(img)
            st.write("Même après un bon découpage de la ponctuation, celle-ci ne semble pas être correctement",
                     " reconnue. Bien qu'il semble y avoir plusieurs cas d'exemple dans le dataset, le modéle ne ",
                     "semble pas avoir appris à les reconnaitre")
  
        with col3:
            st.write("** Niveau de gris posant problème **")
            ## Affichage des images 
            img = Image.open(PATH +"dataSet_pres_ImageNiveauGris.jpeg")
            st.image(img)
            st.write("On peut voir sur cette échantillion du bruit sur les images ce qui a probablement empêché",
                     " la detection On peut suppose qu'en améliorant le traitement de l'image on pourrait augmenter le taux de reconnaissance")
            
        st.subheader("Conclusion de l’analyse des données")
                    
        st.write("Cette première analyse du Data Set nous ouvre un grand nombre de voies sur la compréhension des méthodes de détection.",
                 "En effet l'analyse de ces résultats et principalement des KO nous apprennent beaucoup sur les cas de figure problématiques ",
                 "rencontrées par le modèle : ")
        st.write(" - Difficulté dans le split des phrases en mots") 
        st.write(" - Bruit de l'image un peu trop fort ")
        st.write(" - Présence de mots raturés ")
        st.write(" - Mots tronqués")
        
        #### inclure le schéma
        
        st.write("Cette dernière nous permet aussi de pouvoir émettre quelques hypothèses à valider pour améliorer les performance du modèle:")
        st.write(" - Lettre 'accidentogène' voir même en poussant le raisonnement des combinaisons du type 'RS'")
        st.write(" - Le ratio w/h pourrait permettre d'identifier des images KO avant traitement - Un traitement du bruit des image pourrait améliorer performance du modèle")
    
    
