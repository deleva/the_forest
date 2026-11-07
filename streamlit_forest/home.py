import streamlit as st

st.markdown("""# THE FOREST
## 🌳 Calculating the CARBON STOCK in trees
📍 **Paris and Buenos Aires**
""")

# Navigation
st.space("large")
nav = st.container(horizontal=True, horizontal_alignment="right")
nav.page_link("views/tree_analysis.py", label="Next page", icon=":material/arrow_forward:", icon_position="right")
