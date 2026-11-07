import streamlit as st
import numpy as np
import pandas as pd


st.markdown("""# The Carbon Stock calculator :material/calculate:
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
st.markdown(f"<h3 style='color: darkgreen; font-weight: 400; padding-bottom:0;'>Your current carbon stock in the {arrondissement_paris} arrondissement is</h3>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: green; font-size:200%; padding-top:0;'>{your_arrondissement(arrondissement_paris)} tons of CO2</h1>", unsafe_allow_html=True)

st.markdown("### Metrics results in Tons of CO2 for the new trees")

def pct_of_today(value):
    # New trees' carbon as a % of the arrondissement's current carbon stock
    pct = value * 100 / carbon_arrondissement_paris_1
    if pct >= 0.01:
        return f"+{pct:.2f}% vs today"
    return f"+{pct:.2g}% vs today"  # keeps very small numbers readable instead of showing 0.00%

col1, col2, col3, col4 = st.columns(4)
col1.metric("Young", f'{round((carbon_tree[0]),2)} t', pct_of_today(carbon_tree[0]))
col2.metric("Young adult", f'{round((carbon_tree[1]),2)} t', pct_of_today(carbon_tree[1]))
col3.metric("Adult", f'{round((carbon_tree[2]),2)} t', pct_of_today(carbon_tree[2]))
col4.metric("Mature", f'{round((carbon_tree[3]),2)} t', pct_of_today(carbon_tree[3]))

# Navigation
nav = st.container(horizontal=True)
nav.page_link("views/prediction_models.py", label="Previous page", icon=":material/arrow_back:")
