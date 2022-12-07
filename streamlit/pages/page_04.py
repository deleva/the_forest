import streamlit as st
from interface.main import get_data
from cleaning import cleaning_paris
from preprocessor import preprocessor
from tables import paris_predictions
import tableauserverclient as TSC
import pandas as pd
#import io.StringIO
import streamlit.components.v1 as components

st.markdown("""
    # Maps

    ## Distribution of the trees
""")

#Get data
data_paris , data_ba = get_data()
#Clean data
paris_clean = cleaning_paris(data_paris)
#Preprocess
paris_preprocess = preprocessor(paris_clean)

st.markdown("""
    ## Focus on the Carbon stock vs the GHG emissions
    Map of Paris

    ## Focus on predictions
            """)

#Dataframe predictions
df = paris_predictions(paris_preprocess)
st.write(df)

st.markdown("""
    ## Maps Tableau
            """)

def main():
    html_temp_paris = """
                <script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'>
                </script><tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/theforest/views/The_Forest_Paris_16703359220950/Tableaudebord1' width='900' height='640' hide-tabs toolbar='hidden'>
                </tableau-viz>
                """
    components.html(html_temp_paris, height=640, width=900)

    html_temp_ba = """
                <script type='module' src='https://prod-uk-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'>
                </script>
                <tableau-viz id='tableau-viz' src='https://prod-uk-a.online.tableau.com/t/theforest/views/The_Forest_BA/Tableaudebord1' width='900' height='640' hide-tabs toolbar='hidden'>
                </tableau-viz>
    """
    components.html(html_temp_ba, height=640, width=900)

if __name__ == "__main__":
    main()
