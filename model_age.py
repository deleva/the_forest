import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.linear_model import LogisticRegression



def define_age_tree(data_paris: pd.DataFrame, data_predict: pd.DataFrame) -> np.ndarray:
    """
    Use the Paris dataset to fit a classification model.
    Model to predict the stage of development of the tree from the hight and circumference.
    The possible stages: 'Jeune (arbre)', 'Jeune (arbre)Adulte', 'Adulte', 'Mature'.
    Stage 'Sénesescent' is not present in data_paris.

    Columns data_paris: ['STADE DE DEVELOPPEMENT', 'HAUTEUR (m)', 'CIRCONFERENCE (cm)'].
    Columns data_predict:['HAUTEUR (m)', 'CIRCONFERENCE (cm)']
    """

    #Removing trees with missing stage of developpement
    data = data_paris.dropna(axis=0, subset=['STADE DE DEVELOPPEMENT'])

    #Setting X and y for the model
    X = data[['HAUTEUR (m)', 'CIRCONFERENCE (cm)']]
    y = data['STADE DE DEVELOPPEMENT']
    X_scaled = MinMaxScaler().fit_transform(X)

    #Balancing the dataset to have same proportion for each of the 4 stages
    undersample = RandomUnderSampler(sampling_strategy='all')
    X_balanced, y_balanced = undersample.fit_resample(X_scaled, y)

    #Model
    model = LogisticRegression(C=200, max_iter=10000)
    model.fit(X_balanced, y_balanced)

    #Predictions
    data_predict = MinMaxScaler().transform(data_predict)
    predictions = model.predict(data_predict)

    return predictions
