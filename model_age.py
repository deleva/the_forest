import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler
from sklearn.linear_model import LogisticRegression
from preprocessor import  preprocessor_stage



def define_age_tree(data_paris: pd.DataFrame, data_ba: pd.DataFrame):
    """
    Use the Paris dataset to fit a classification model.
    Model to predict the stage of development of the tree from the hight and circumference.
    The possible stages: 'Jeune (arbre)', 'Jeune (arbre)Adulte', 'Adulte', 'Mature'.
    Stage 'Sénesescent' is not present in data_paris.

    Returns the two dataframes: data_paris, data_ba
    """

    data_paris = preprocessor_stage(data_paris)
    data_ba = preprocessor_stage(data_ba)

    #Removing trees with missing stage of developpement
    data = data_paris.dropna(axis=0, subset=['remainder__stade_de_developpement'])

    #Setting X and y for the model
    X = data[['scaler__hauteur_m', 'scaler__diametre_cm']]
    y = data['remainder__stade_de_developpement']

    #Balancing the dataset to have same proportion for each of the 4 stages
    undersample = RandomUnderSampler(sampling_strategy='all')
    X_balanced, y_balanced = undersample.fit_resample(X, y)

    #Model
    model = LogisticRegression(C=5, max_iter=10000)
    model.fit(X_balanced, y_balanced)

    #Predictions
    predictions = model.predict(data_ba[['scaler__hauteur_m', 'scaler__diametre_cm']])
    predict = pd.DataFrame(predictions, columns=['remainder__stade_de_developpement'])

    data_ba = pd.concat([data_ba, predict], axis=1)

    return data_paris, data_ba
