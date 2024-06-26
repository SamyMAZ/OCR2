# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 16:25:27 2021

@author: b.tabet
"""

import streamlit as st
from PIL import Image


PATH     = "C:/Users/benja/Documents/Data Science/PyOCaRe/utils/images/"

def display_ModelDetection(select_form):
    if select_form == 'Manuscrit 1':
        img = Image.open(PATH + "Formulaire N06-175.png")
        st.image(img)
    elif select_form == 'Manuscrit 2':
        img = Image.open(PATH + "Formulaire L04-098.png")
        st.image(img)
    elif select_form == 'Manuscrit 3':
        img = Image.open(PATH + "Formulaire H06-096.png")
        st.image(img)
        
        


@st.cache(suppress_st_warning=True)
def display_objectDetection(select_form, chbox_Tessereact,chbox_Initial, chbox_treat_1,chbox_treat_2,chbox_treat_3, chbox_treat_4):

    if chbox_Tessereact and chbox_Initial:
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACTet Initial ET TOUS LES TRAITEMENTS 1,2, 3, 4")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1+2+3+4.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMENT 1, 2, 3")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1+2+3.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 1 et 2")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1+2.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 1 et 3")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1+3.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and  chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 1 et 4")  
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1+4.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_3 and  chbox_treat_4 and not chbox_treat_2 and chbox_treat_3 and  chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 1, 3 et 4") 
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1+3+4.png")
            st.image(img)
                         
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 1")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat1.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 2")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat2.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 2, 3")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat2+3.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 2, 4")   
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat2+4.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 2, 3, 4")  
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat2+3+4.png")
            st.image(img)
                        
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 3")
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat3.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 3, 4") 
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat3+4.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACTet Initial  et TRAITEMNT 4")  
            
            img = Image.open(PATH + "Forms_Boxintial&BoxTesseract_Treat4.png")
            st.image(img)
            
    
    if chbox_Tessereact and not chbox_Initial:
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACT ET TOUS LES TRAITEMENTS 1,2, 3, 4")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1+2+3+4.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT et TRAITEMENT 1, 2, 3")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1+2+3.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 1 et 2")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1+2.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 1 et 3")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1+3.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and  chbox_treat_4:
            st.write(" TESSEREACT et TRAITEMNT 1 et 4")  
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1+4.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and  chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 1, 3 et 4")   
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1+3+4.png")
            st.image(img)
                       
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 1")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat1.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 2")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat2.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 2, 3")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat2+3.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 2, 4") 
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat2+4.png")
            st.image(img)
              
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 2, 3, 4")   
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat2+3+4.png")
            st.image(img)
                       
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 3")
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat3.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 3, 4") 
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat3+4.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" TESSEREACT  et TRAITEMNT 4")        
            
            img = Image.open(PATH + "Forms_BoxTesseract_Treat4.png")
            st.image(img)
                  
    
    if chbox_Initial and not chbox_Tessereact:
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" Initial ET TOUS LES TRAITEMENTS 1,2, 3, 4")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1+2+3+4.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMENT 1, 2, 3")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1+2+3.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMNT 1 et 2")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1+2.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMNT 1 et 3")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1+3.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and  chbox_treat_4:
            st.write(" Initial et TRAITEMNT 1 et 4")  
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1+4.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and  chbox_treat_4:
            st.write(" Initial et TRAITEMNT 1, 3 et 4")    
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1+3+4.png")
            st.image(img)
                      
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMNT 1")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat1.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMNT 2")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat2.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMNT 2, 3")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat2+3.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" Initial et TRAITEMNT 2, 4")   
            
            img = Image.open(PATH + "Forms_Boxintial_Treat2+4.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" Initial et TRAITEMNT 2, 3, 4")  
            
            img = Image.open(PATH + "Forms_Boxintial_Treat2+3+4.png")
            st.image(img)
                        
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" Initial et TRAITEMNT 3")
            
            img = Image.open(PATH + "Forms_Boxintial_Treat3.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" Initial et TRAITEMNT 3, 4") 
            
            img = Image.open(PATH + "Forms_Boxintial_Treat3+4.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" Initial et TRAITEMNT 4")   
            
            img = Image.open(PATH + "Forms_Boxintial_Treat4.png")
            st.image(img)
            

    if not chbox_Initial and not chbox_Tessereact:
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write(" TOUS LES TRAITEMENTS 1,2, 3, 4")
            
            img = Image.open(PATH + "Forms_raw_Treat1+2+3+4.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TRAITEMENT 1, 2, 3")
            
            img = Image.open(PATH + "Forms_raw_Treat1+2+3.png")
            st.image(img)
            
        if chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write(" TRAITEMNT 1 et 2")
            
            img = Image.open(PATH + "Forms_raw_Treat1+2.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write(" TRAITEMNT 1 et 3")
            
            img = Image.open(PATH + "Forms_raw_Treat1+3.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and  chbox_treat_4:
            st.write("  TRAITEMNT 1 et 4")  
            
            img = Image.open(PATH + "Forms_raw_Treat1+4.png")
            st.image(img)
            
        if chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and  chbox_treat_4:
            st.write("  TRAITEMNT 1, 3 et 4")     
            
            img = Image.open(PATH + "Forms_raw_Treat1+3+4.png")
            st.image(img)
                     
        if chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write("  TRAITEMNT 1")
            
            img = Image.open(PATH + "Forms_raw_Treat1.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and not chbox_treat_4:
            st.write("  TRAITEMNT 2")
            
            img = Image.open(PATH + "Forms_raw_Treat2.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write("  TRAITEMNT 2, 3")
            
            img = Image.open(PATH + "Forms_raw_Treat2+3.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write("  TRAITEMNT 2, 4")   
            
            img = Image.open(PATH + "Forms_raw_Treat2+4.png")
            st.image(img)
            
        if not chbox_treat_1 and chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write("  TRAITEMNT 2, 3, 4")     
            
            img = Image.open(PATH + "Forms_raw_Treat2+3+4.png")
            st.image(img)
                     
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and not chbox_treat_4:
            st.write("  TRAITEMNT 3")
            
            img = Image.open(PATH + "Forms_raw_Treat3.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and chbox_treat_3 and chbox_treat_4:
            st.write("  TRAITEMNT 3, 4") 
            
            img = Image.open(PATH + "Forms_raw_Treat3+4.png")
            st.image(img)
            
        if not chbox_treat_1 and not chbox_treat_2 and not chbox_treat_3 and chbox_treat_4:
            st.write(" TRAITEMNT 4")  
            
            img = Image.open(PATH + "Forms_raw_Treat4.png")
            st.image(img)
                       