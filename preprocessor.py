import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler

def preprocessor(data: pd.DataFrame) -> pd.DataFrame:

    #One hot encoding the species
    ohe = OneHotEncoder(sparse = False)
    ohe.fit(data[['nom_scientifique']])
    species_encoded = ohe.transform(data[['nom_scientifique']])
    data[ohe.categories_[0]] = species_encoded

    #Label encoder of the 'stade_de_developement'
    stage_encoder = LabelEncoder().fit(data['stade_de_developpement'])
    data['stade_de_developpement'] = stage_encoder.transform(data['stade_de_developpement'])

    #Scaling ['hauteur_m', 'diametre_cm', 'rayon_cm']
    r_scaler = RobustScaler()
    r_scaler.fit(data['hauteur_m'])
    data['hauteur_m'] = r_scaler.transform(data[['hauteur_m']])

    #Pipeline
    preprocessor = ColumnTransformer([
        ('num_tr', num_transformer, ['age', 'bmi']),
        ('cat_tr', cat_transformer, ['smoker', 'region'])
    ])
