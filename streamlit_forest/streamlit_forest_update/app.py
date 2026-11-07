import streamlit as st

# The menu: order, names and icons of the pages are all set here.
pg = st.navigation([
    st.Page("home.py", title="Home", icon=":material/home:", default=True),
    st.Page("views/tree_analysis.py", title="Tree Analysis"),
    st.Page("views/maps.py", title="Maps"),
    st.Page("views/carbon_stock_formula.py", title="Carbon Stock Formula"),
    st.Page("views/prediction_models.py", title="Prediction Models"),
    st.Page("views/calculator.py", title="Calculator"),
])
pg.run()
