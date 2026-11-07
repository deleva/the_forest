import streamlit as st

st.markdown("""# THE FOREST
## 🌳 Calculating the CARBON STOCK in trees
📍 **Paris and Buenos Aires**
""")

# Navigation
col_prev, col_next = st.columns(2)
col_next.page_link("views/tree_analysis.py", label="Next page", icon=":material/arrow_forward:")
