import streamlit as st

st.markdown("""
    # The Carbon Stock

    ## Tree biomass
    Using the biomass expansion factor (BEF) method.

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
