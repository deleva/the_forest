import pandas as pd
import math
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer
import streamlit as st

@st.cache(allow_output_mutation=True)
def preprocessor(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function to use after the cleaning for both Paris and BA,
    and before the model_age function.
    """

    #Nom scientifique: keep only species in commun between paris and BA
    species_commun = ['rhus', 'castanea', 'viburnum', 'malus', 'punica', 'carya', 'phoenix', 'cydonia', 'picea', 'pterocarya', 'crataegus', 'paulownia', 'photinia', 'thuja', 'ficus', 'calocedrus', 'albizia', 'araucaria', 'tilia', 'betula', 'cryptomeria', 'populus', 'hovenia', 'ligustrum', 'pyrus', 'butia', 'chamaecyparis', 'cercis', 'magnolia', 'ilex', 'liriodendron', 'platanus', 'poncirus', 'gleditsia', 'acer', 'pinus', 'hibiscus', 'platycladus', 'eriobotrya', 'broussonetia', 'olea', 'fraxinus', 'robinia', 'alnus', 'juniperus', 'carpinus', 'trachycarpus', 'cupressocyparis', 'prunus', 'firmiana', 'lagerstroemia', 'buxus', 'ailanthus', 'koelreuteria', 'fagus', 'ginkgo', 'juglans', 'eucalyptus', 'callistemon', 'melia', 'cinnamomum', 'morus', 'celtis', 'aesculus', 'maclura', 'quercus', 'mespilus', 'laurus', 'catalpa', 'abies', 'cupressus', 'pittosporum', 'cordyline', 'ulmus', 'sambucus', 'cotoneaster', 'carica', 'taxodium', 'euonymus', 'cedrus', 'diospyros', 'acca', 'acacia', 'salix', 'liquidambar']
    def good_species(s):
        if s in species_commun:
            return s
        else:
            return 'other_species'
    data['nom_scientifique'] = data['nom_scientifique'].map(good_species)

    #Creature volume column
    hauteur = data['hauteur_m']
    rayon = data['rayon_cm']
    list_volume = list()

    for h, R in zip(hauteur, rayon):
        r = R/2
        V = (1/3)*math.pi*h*(R**2 + R*r + r**2)/10000
        list_volume.append(V)

    data['volume_m3'] = list_volume

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

    #Create Rj column (Root-shoot ratio for tree)
    hauteur = data['hauteur_m']
    list_rj = list()
    for element in hauteur:
        if element <= 5:
            list_rj.append(0.45)
        elif element > 11:
            list_rj.append(0.2)
        else:
            list_rj.append(0.35)
    data['Rj'] = list_rj

    #Estimation of tree biomass using the BEF method
    volume = data['volume_m3']
    rj = data['Rj']
    bef = data['bef']

    list_biomass = []

    for V, Rj , BEF in zip(volume , rj , bef):
        Btree = V * 0.5* (1+Rj) * BEF
        list_biomass.append(Btree)

    data['Btree'] = list_biomass

    #Carbon stock in tree biomass
    list_carbon = []
    Btree_result = data['Btree']
    for Btree in Btree_result :
        CFtree = 0.55
        C=(44/12)*CFtree*Btree
        list_carbon.append(C)

    data['carbon'] = list_carbon

    #Pipeline
    preprocessor = ColumnTransformer([
        ('species', OneHotEncoder(sparse = False), ['nom_scientifique']),
        ('scaler', RobustScaler(), ['hauteur_m', 'diametre_cm', 'rayon_cm'])],
        remainder='passthrough')

    #Fit the pipeline and transform the dataset
    data_preprocessed = preprocessor.fit_transform(data)

    data_preprocessed = pd.DataFrame(
        data_preprocessed,
        columns=preprocessor.get_feature_names_out()
        )

    return data_preprocessed
