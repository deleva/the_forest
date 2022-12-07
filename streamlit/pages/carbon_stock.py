import streamlit as st
import numpy as np
import pandas as pd

st.markdown("""# The Carbon Stock calculator🖩
### Choose how many 🌳 you want to plant and see how much carbon they will store
""")

with st.form(key='params_for_pred'):


    number_of_trees= st.number_input('🌱 Number of trees ', value=1)
    #st.form_submit_button('Number of trees')

    tree_species= st.selectbox('Kind of species',('bald cypress','Chinese wingnut', 'cedar','poplar','sycamore','horsechestnut', 'European beech', 'tree of heaven', 'Willows','incense cedar'))

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

st.markdown("""
### Metrics results in Tons of CO2
""")



col1, col2, col3, col4 = st.columns(4)
col1.metric("Young", f'{round((carbon_tree[0]),2)} ', f'{round((carbon_tree[0]*100/carbon_tree[3]),2)}%')
col2.metric("Young adult", f'{round((carbon_tree[1]),2)} ', f'{round((carbon_tree[1]*100/carbon_tree[3]),2)}%')
col3.metric("Adult", f'{round((carbon_tree[2]),2)}',f'{round((carbon_tree[2]*100/carbon_tree[3]),2)}%')
col4.metric("Mature",f'{round((carbon_tree[3]),2)}', f'{round((carbon_tree[3]*100/carbon_tree[3]),2)}%' )
