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

# #Get data
# data_paris , data_ba = get_data()
# #Clean data
# paris_clean = cleaning_paris(data_paris)
# #Preprocess
# paris_preprocess = preprocessor(paris_clean)

st.markdown("""
    ## Focus on the Carbon stock vs the GHG emissions
    Map of Paris

    ## Focus on predictions
            """)


st.markdown("""
    ## Maps Tableau
            """)

def main():
    html_temp_paris = """
                <div class='tableauPlaceholder' id='viz1670421132542' style='position: relative'>
                    <noscript>
                        <a href='#'>
                        <img alt='Tableau de bord 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Th&#47;The_Forest_Paris&#47;Tableaudebord1&#47;1_rss.png' style='border: none' />
                        </a>
                    </noscript>
                    <object class='tableauViz'  style='display:none;'>
                        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                        <param name='embed_code_version' value='3' />
                        <param name='site_root' value='' />
                        <param name='name' value='The_Forest_Paris&#47;Tableaudebord1' />
                        <param name='tabs' value='no' />
                        <param name='toolbar' value='no' />
                        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Th&#47;The_Forest_Paris&#47;Tableaudebord1&#47;1.png' />
                        <param name='animate_transition' value='yes' />
                        <param name='display_static_image' value='yes' />
                        <param name='display_spinner' value='yes' />
                        <param name='display_overlay' value='no' />
                        <param name='display_count' value='yes' />
                        <param name='language' value='fr-FR' />
                        <param name='filter' value='publish=yes' />
                    </object>
                </div>
                <script type='text/javascript'>
                    var divElement = document.getElementById('viz1670421132542');
                    var vizElement = divElement.getElementsByTagName('object')[0];
                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}
                    var scriptElement = document.createElement('script');
                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
                    vizElement.parentNode.insertBefore(scriptElement, vizElement);
                </script>
                """
    components.html(html_temp_paris, height=640, width=900)

    html_temp_ba = """
                <div class='tableauPlaceholder' id='viz1670421652179' style='position: relative'>
                    <noscript>
                        <a href='#'>
                        <img alt='Tableau de bord 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Th&#47;The_Forest_BA&#47;Tableaudebord1&#47;1_rss.png' style='border: none' />
                        </a>
                    </noscript>
                    <object class='tableauViz'  style='display:none;'>
                        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
                        <param name='embed_code_version' value='3' />
                        <param name='site_root' value='' />
                        <param name='name' value='The_Forest_BA&#47;Tableaudebord1' />
                        <param name='tabs' value='no' />
                        <param name='toolbar' value='yes' />
                        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Th&#47;The_Forest_BA&#47;Tableaudebord1&#47;1.png' />
                        <param name='animate_transition' value='yes' />
                        <param name='display_static_image' value='yes' />
                        <param name='display_spinner' value='yes' />
                        <param name='display_overlay' value='yes' />
                        <param name='display_count' value='yes' />
                        <param name='language' value='fr-FR' />
                        <param name='filter' value='publish=yes' />
                    </object>
                </div>
                <script type='text/javascript'>
                    var divElement = document.getElementById('viz1670421652179');
                    var vizElement = divElement.getElementsByTagName('object')[0];
                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}
                    var scriptElement = document.createElement('script');
                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
                    vizElement.parentNode.insertBefore(scriptElement, vizElement);
                </script>
                """
    components.html(html_temp_ba, height=640, width=900)

if __name__ == "__main__":
    main()
