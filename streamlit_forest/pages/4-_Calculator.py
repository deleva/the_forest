import streamlit as st
import numpy as np
import pandas as pd


st.markdown("""# The Carbon Stock calculator🖩
### Choose how many 🌳 you want to plant and see how much carbon they will store
""")

with st.form(key='params_for_pred'):


    arrondissement_paris= st.selectbox('Choose your arrondissement',('1e','2e','3e','4e','5e','6e','7e','8e','9e','10e','11e','12e','13e','14e','15e','16e','17e','18e','19e','20e'))

    number_of_trees= st.number_input('🌱 How many trees are you planning to plant? ', value=1)
    #st.form_submit_button('Number of trees')

    tree_species= st.selectbox('Choose your kind of tree',('Cyprès','Noyer','Cèdre','Peuplier','Erable','Marronnier','Hêtre','Ailante Glanduleux','Saule','Calocèdre'))


    #st.write('text',tree_species)

    #st.form_submit_button('Name of species')



    st.form_submit_button('Carbon calculation 🌳 ')


def carbon_stock(number_of_trees,tree_species):
    #carbon_tree = {}
    #for nb , tr in zip(number_of_trees,tree_species):
    df_tree = pd.read_csv('data/paris_predict.csv' , index_col='Unnamed: 0')
    #tr = []
    Young = (number_of_trees * (df_tree.loc[tree_species , 'Young']))
    Young_adult = (number_of_trees * (df_tree.loc[tree_species , 'Young adult']))
    Adult = number_of_trees * (df_tree.loc[tree_species, 'Adult'])
    Mature = number_of_trees * (df_tree.loc[tree_species , 'Mature'])

    carbon_tree = [Young ,Young_adult , Adult,Mature ]

    return carbon_tree

carbon_tree = carbon_stock(number_of_trees,tree_species)


def your_arrondissement(arrondissement_paris):
    df_ar = pd.read_csv('data/carbon_arrondissement.csv',index_col='Unnamed: 0' )
    carbon_arrondissement = df_ar.loc[arrondissement_paris , 'Total Carbon stock']

    return carbon_arrondissement

carbon_arrondissement_paris_1 = your_arrondissement(arrondissement_paris)

#st.write()
#col1 = st.columns(1)
st.markdown(f"<h1 style='text-align: center; color: grey; font-size:200%;'>Your current carbon stock in the {arrondissement_paris} arrondissement is <span style='color:green;'>{your_arrondissement(arrondissement_paris)} Tons of CO2</span></h1>", unsafe_allow_html=True)
# st.markdown(f"Your current carbon stock in the {arrondissement_paris} is {your_arrondissement(arrondissement_paris)} Tons of CO2")
st.markdown("""###
### Metrics results in Tons of CO2 for the new trees

""")



col1, col2, col3, col4 = st.columns(4)
col1.metric("Young", f'{round((carbon_tree[0]),2)} ', f'{round((carbon_tree[0]*100/carbon_tree[3]),2)}%')
col2.metric("Young adult", f'{round((carbon_tree[1]),2)} ', f'{round((carbon_tree[1]*100/carbon_tree[3]),2)}%')
col3.metric("Adult", f'{round((carbon_tree[2]),2)}',f'{round((carbon_tree[2]*100/carbon_tree[3]),2)}%')
col4.metric("Mature",f'{round((carbon_tree[3]),2)}', f'{round((carbon_tree[3]*100/carbon_tree[3]),2)}%' )
