import streamlit as st
from interface.main import get_data
from cleaning import cleaning_ba, cleaning_paris

st.markdown("""
    # Maps

    ## Distribution of the trees
""")

#Get data
data_paris , data_ba = get_data()
#Clean data
paris_clean = cleaning_paris(data_paris)
ba_clean = cleaning_ba(data_ba)

@st.cache
def get_map_paris():
    return paris_clean[['lat', 'lon']]

@st.cache
def get_map_ba():
    return ba_clean[['lat', 'lon']]

map_paris = get_map_paris()
map_ba = get_map_ba()

st.map(map_paris)
st.map(map_ba)

st.markdown("""
    ## Focus on the Carbon stock vs the GHG emissions
    Map of Paris

    ## Focus on predictions
    Planting trees of a certain species (=> average diameter): the carbon stock at a certain stage of development. \\
    -> API
            """)
