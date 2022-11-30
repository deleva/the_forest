import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer


def preprocessor(data: pd.DataFrame) -> pd.DataFrame:

    preprocessor = ColumnTransformer([
        ('species', OneHotEncoder(sparse = False), ['nom_scientifique']),
        ('stage encoder', LabelEncoder(), ['stade_de_developpement']),
        ('scaler', RobustScaler(), ['hauteur_m', 'diametre_cm', 'rayon_cm'])
    ])
