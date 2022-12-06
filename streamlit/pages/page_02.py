import streamlit as st
from cleaning import cleaning_ba, cleaning_paris
from interface.main import get_data
from preprocessor import preprocessor
from tables import carbon_stats_df

st.markdown("""
    # The Carbon Stock

    ## Tree biomass

    The biomass of a tree of species *j* at a point of time in year *t* is estimated as:
""")

st.latex(r'''
         B_{TREE, j, t} = V_{TREE, j, t} * D_j * BEF_j * (1+R_j)
    ''')

st.markdown('''
            With:

        - $V_{TREE, j, t}$: Volume of the tree (in $m^3$) \n
        - $D_j$: Basic wood density of tree species $j$ \n
        - $BEF_j$: Biomass expansion factor (for conversion of stem biomass to above-ground tree
        biomass), for tree species $j$ \n
        - $R_j$: Root-shoot ratio for tree species $j$.

        ## Carbon Stock in tree biomass
            ''')

st.latex(r'''
         C_{TREE, t} =  \frac{44}{12} * B_{TREE, t} * CF_{TREE}
    ''')

st.markdown('''
            With:

        - $B_{TREE, t}$: Total tree biomass \n
        - $CF_{TREE}$: Carbon fraction of tree biomass. A default value of 0.50 is used. \n
            ''')

#Get data
data_paris , data_ba = get_data()
#Clean data
paris_clean = cleaning_paris(data_paris)
ba_clean = cleaning_ba(data_ba)
#Preprocess data
paris_preprocess = preprocessor(paris_clean)
ba_preprocess = preprocessor(ba_clean)
#DataFrame
df = carbon_stats_df(paris_preprocess, ba_preprocess)

st.write(df)
