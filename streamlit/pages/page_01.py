import streamlit as st
from tables import tree_stats_df
from cleaning import cleaning_ba, cleaning_paris
from interface.main import get_data

#Get data
data_paris , data_ba = get_data()
#Clean data
paris_clean = cleaning_paris(data_paris)
ba_clean = cleaning_ba(data_ba)

st.markdown("""
    # Analysis of the trees in Paris and Buenos Aires

    ## Features
    - Height (in m)
    - Diameter (in cm)
    - Stage of development (Young, Young Adult, Adult, Mature)
    - Species (85 mutual species between Paris and Buenos Aires)
""")

#Dataframe
df = tree_stats_df(paris_clean, ba_clean)

st.write(df)
