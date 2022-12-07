import streamlit as st

st.markdown("""
    # Models to predict the Carbon Stock

    Through a permutation table, we found that the most relevant features to predict the carbon stock of a tree are
    the **diameter** and the **stage of development** of the tree.

   Hence for our regression models, we define

    X= 'Diameter (in cm)', 'Stage of developement' \\
    y= 'Carbon Stock'

    Using the performance metric R-squared (R²), we fitted and tested 7 different regression models.

    R² represents the proportion of the variance of the target explained by the features.

    Out of the 7 models, the best one is:

    **GradientBoosting Regressor** with a R-squared of 0.86:\\
        GradientBoostingRegressor(learning_rate= 0.6, loss= 'huber', n_estimators= 50)

""")
