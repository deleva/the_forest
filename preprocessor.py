import pandas as pd
import math
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer


def preprocessor(data: pd.DataFrame) -> pd.DataFrame:

    #Creature volume column
    hauteur = data['hauteur_m']
    rayon = data['rayon_cm']
    list_volume = list()

    for h, R in zip(hauteur, rayon):
        r = R/2
        V = (1/3)*math.pi*h*(R**2 + R*r + r**2)/10000
        list_volume.append(V)

    data['volume_m3'] = list_volume

    #Create density column
    data['wood_density'] = 0.5

    #Create BEF column
    list_bef = list()
    diametre = data['diametre_cm']
    for d in diametre:
        if d >= 12.5:
            list_bef.append(1.15)
        else:
            bef= -(2.25/11.5)*d +3.4
            list_bef.append(bef)
    data['bef']= list_bef


    #Pipeline
    preprocessor = ColumnTransformer([
        ('species', OneHotEncoder(sparse = False), ['nom_scientifique']),
        ('stage encoder', LabelEncoder(), ['stade_de_developpement']),
        ('scaler', RobustScaler(), ['hauteur_m', 'diametre_cm', 'rayon_cm'])],
        remainder='passthrough')

    #Fit the pipeline and transform the dataset
    data_preprocessed = preprocessor.fit_transform(data)

    data_preprocessed = pd.DataFrame(
        data_preprocessed,
        columns=preprocessor.get_feature_names_out()
        )

    #Feature engineering


    return data_preprocessed
