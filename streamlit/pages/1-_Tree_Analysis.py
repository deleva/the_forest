import streamlit as st
from tables import tree_stats_df
from cleaning import cleaning_ba, cleaning_paris
from interface.main import get_data


st.markdown("""
    # Analysis of the trees in Paris and Buenos Aires

    The trees can be classified into 4 stages of developement: Young, Adult, Mature and Senescent. \\
    In Paris, there aren't any scenescent trees. Hence we have redefined our four classes as: \\
        Young, Young Adult, Adult, Mature.

    Paris and Buenos Aires have 85 mutual species of trees.
""")

#Get data
data_paris , data_ba = get_data()
#Clean data
paris_clean = cleaning_paris(data_paris)
ba_clean = cleaning_ba(data_ba)
#Dataframe
df = tree_stats_df(paris_clean, ba_clean)
st.write(df)
