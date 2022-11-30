import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler
from sklearn.linear_model import LogisticRegression
from preprocessor import  preprocessor_stage
from sklearn.preprocessing import LabelEncoder


def define_stage_tree(data_paris: pd.DataFrame, data_ba: pd.DataFrame):
    """
    Use the Paris dataset to fit a classification model.
    Model to predict the stage of development of the tree from the hight and circumference.

    The possible stages encoded:
    'Jeune (arbre)':0 ,
    'Jeune (arbre)Adulte':1,
    'Adulte':2,
    'Mature':3.
    Stage 'Sénesescent' is not present in data_paris.

    Returns the two dataframes: data_paris, data_ba
    """

    #Removing trees with missing stage of developpement
    data_paris = data_paris.dropna(axis=0, subset=['remainder__stade_de_developpement'])

    #Setting X and y for the model
    X = data_paris[['scaler__hauteur_m', 'scaler__diametre_cm']]
    y = data_paris['remainder__stade_de_developpement']

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

    #Label encoding 'stade_de_developpement'
    stage_encoder = LabelEncoder().fit(data_paris['remainder__stade_de_developpement'])
    data_paris['remainder__stade_de_developpement'] = stage_encoder.transform(data_paris['remainder__stade_de_developpement'])
    data_ba['remainder__stade_de_developpement'] = stage_encoder.transform(data_ba['remainder__stade_de_developpement'])

    return data_paris, data_ba
