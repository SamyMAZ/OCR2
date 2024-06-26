# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:31:07 2021

@author: b.tabet
"""
import streamlit as st


def display_conclusion_page():
    
    st.header("Conclusion")
    st.subheader("Cas d’utilisation du projet :")
    st.write(" -  Lecture automatique et repérage de CV par mots clés permettant un tri rapide et efficace",
                "des candidatures (étape coûteuse en termes de temps dans les processus de recrutement") 
    st.write(" - Lecture automatique de note de frais:  Détection de ligne comptables") 
    st.write(" - Détection de montant - Détection de TVA ")
    st.write(" - Traitement documentaire dans le cadre de la gestion éditique de document.",
             " Cela permet l’enregistrement de data en base de données afin d’améliorer la traçabilité et la recherche")
    st.write("Traçabilité/décryptage de documents d’époques : aide pour décrypter les documents anciens/abimés par le ",
             "temps. ")
    
    st.subheader("Perspectives d’amélioration du code :")
    st.write(" - Nous avons donc un modèle qui répond à notre problématique. Celui-ci détecte le texte en alphabet latin et le reconnais.")
    st.write(" - Le modèle n'inclut pas de caractères spéciaux et la ponctuation. Pour inclure ces caractères,",
             "une possibilité serait d'augmenter le dataset en incluant plus de caractères spéciaux. L'autre ",
             "possibilité serait de créer un modèle spécifique prenant en compte ces caractères et que ce modèle ",
             "soit additionné au modèle développé dans notre projet ...")
    st.write(" - Pour améliorer les performances, on pourrait aussi augmenter les données (91 992 images ne suffisent ",
             "pas forcément), ou réaliser la même méthode mais en partant sur un apprentissage des phrases/expression ",
             "plutôt que les mots, voir additionner les 2 méthodes.")
    st.write(" - Une des grandes difficultés de ce type de problématique vient directement du poids des données utilisées ",
             "et de la puissance de calcul disponible pour entraîner nos modèles sur des machines non dimensionnées ",
             "pour ça. Une des pistes d’améliorations possible de notre projet en travaillant sur un meilleur ",
             "traitement des images en termes de performance et de passer par des services comme google collab ",
             "pour aller chercher plus de puissance de calcul.")
    st.write(" - Enfin une dernière piste serait de se servir des règles de la langue anglaise. On pourrait recenser ",
             "les mots les plus utilisés dans la langue et ainsi associé à la reconnaissance une probabilité d'avoir ",
             "tel mot. On pourrait à partir de correcteur de grammaire, et d’orthographe, rajouter une probabilité que ",
             "le mot à reconnaître soit d'une telle nature et ainsi filtrer les choix de reconnaissance. Cependant ",
             "toutes ces pistes nécessitent énormément de ressources de calcul et pourrait ne pas être viable.")