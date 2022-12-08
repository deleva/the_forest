import streamlit as st
from PIL import Image
import re
import uuid

st.markdown("""
    # Models to predict the Carbon Stock

    Through a permutation table, we found that the most relevant features to predict the carbon stock of a 🌳 are
    its **diameter** and its **stage of development**.
""")
#Ajouter le tableau de permutation

st.markdown("""
   Hence for our regression models, we define :

    ✨ Features -> 'Diameter (in cm)', 'Stage of developement' \\
    🎯 Target -> 'Carbon Stock'


    Using the performance metric R-squared (R²), we fitted and tested 7 different regression models.

    R² measures the strength of the model. The closer to 1, the better the model 🥇

    Out of the 7 models, the best one is:

    ⚡ **GradientBoosting Regressor** with a R-squared of 0.86:\\
        GradientBoostingRegressor(learning_rate= 0.6, loss= 'huber', n_estimators= 50)

    Gradient Boosting is an ensemble learning method which creates predictions using previous erronious predictions :
""")

# Explication sur le GradientBoostingRegressor
image = Image.open('data/images/gradientboostmodel.png')

st.image(image, caption='This is how the GradientBoosting model works')

button_uuid = str(uuid.uuid4()).replace('-', '')
button_id = re.sub('\d+', '', button_uuid)

custom_css = f"""
    <style>
        #{button_id} {{
            background-color: rgb(255, 255, 255);
            color: rgb(38, 39, 48);
            padding: 0.25em 0.38em;
            position: relative;
            text-decoration: none;
            border-radius: 4px;
            border-width: 1px;
            border-style: solid;
            border-color: rgb(230, 234, 241);
            border-image: initial;

        }}
        #{button_id}:hover {{
            border-color: rgb(53,172,122);
            color: rgb(53,172,122);
        }}
        #{button_id}:active {{
            box-shadow: none;
            background-color: rgb(53,172,122);
            color: white;
            }}
    </style> """

button_link = custom_css + f'<a href="/Maps" target="_self" style="text-align: right;" id="{button_id}">Next page</a>'
st.markdown(button_link, unsafe_allow_html=True)
