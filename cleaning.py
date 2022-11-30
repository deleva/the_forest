import re
import math
import pandas as pd


def cleaning_ba(data_ba : pd.DataFrame) -> pd.DataFrame:
    '''
    Allows you to clean Bueno Aires trees dataset.
    Takes the dataframe as an input to return a dataframe with the columns :
    ['long', 'lat', 'id', 'arrondissement', 'nom_scientifique', 'diametre_cm', 'hauteur_m']
    This function is specific to Buenos Aires
    '''
    #Drop columns
    columns_to_drop = [ 'tipo_activ','manzana','calle_nombre', 'calle_altura', 'calle_chapa', 'direccion_normalizada',
                        'ubicacion',  'ancho_acera', 'estado_plantera','ubicacion_plantera', 'nivel_plantera']
    data_ba = data_ba.drop(columns=columns_to_drop)

    #rename columns
    data_ba.columns = ['long', 'lat', 'id', 'arrondissement', 'nom_scientifique', 'diametre_cm', 'hauteur_m']

    #Compute radius
    data_ba['rayon_cm'] = data_ba['diametre_cm'].apply(lambda x: x/2)

    #Remove 'No identificado'
    data_ba = data_ba[data_ba['nom_scientifique'] != 'No identificado']

    # Remove trees that have null/NaN height or diameter
    data_ba = data_ba[(data_ba['hauteur_m'] > 0) & (data_ba['diametre_cm'] > 0)]
    data_ba = data_ba.dropna(axis=0, subset=['diametre_cm', 'hauteur_m'], how='any')

    # Reduce the number of species
    species_list = list(data_ba['nom_scientifique'].unique())
    species_list.sort()
    pattern  = ' ' + ".*"
    data_ba['nom_scientifique'] = data_ba['nom_scientifique'].apply(lambda x: re.sub(pattern, '', x))

    #Nettoyage des valeurs
    data_ba['nom_scientifique'] = data_ba['nom_scientifique'].str.lower()
    data_ba['nom_scientifique'] = data_ba['nom_scientifique'].str.strip()

    #Modifier le type de données
    data_ba['id'] = data_ba['id'].replace('}','37') #Remplacement de la valeur de la ligne 203145
    data_ba['id'] = data_ba['id'].astype(str).astype(int)

    return data_ba


def cleaning_paris(data_pa : pd.DataFrame) -> pd.DataFrame :
    '''
    Allows you to clean Paris trees dataset.
    Takes the dataframe as an input to return a dataframe with the columns :
    ['long', 'lat', 'id', 'arrondissement', 'nom_scientifique',
        'stade_de_developpement', 'diametre_cm', 'hauteur_m', 'rayon_cm']
    This function is specific to Paris
    '''

    # Separate Longitudes and Latitudes
    data_pa[['Long','Lat']] = data_pa['geo_point_2d'].str.split(",", expand=True)

    # Transform Circonférence to Diamètre
    data_pa['CIRCONFERENCE (cm)'] = data_pa['CIRCONFERENCE (cm)'].apply(lambda x : x/math.pi)

    # Insert new radius Column
    data_pa['rayon_cm'] = data_pa['CIRCONFERENCE (cm)'].apply(lambda x : x/2)

    # Drop all trees with no measurable size
    data_pa = data_pa[(data_pa['HAUTEUR (m)'] > 0) & (data_pa['CIRCONFERENCE (cm)'] > 0)]

    # Drop unecessary columns and re-order them
    data_pa = data_pa[['IDBASE', 'ARRONDISSEMENT', 'GENRE', 'STADE DE DEVELOPPEMENT',
                             'CIRCONFERENCE (cm)', 'HAUTEUR (m)', 'Long', 'Lat', 'rayon_cm']]
    data_pa = data_pa.iloc[:, [6, 7, 0, 1, 2, 3, 4, 5, 8]]

    #Re-name to match other Dataset
    data_pa.columns = ['long', 'lat', 'id', 'arrondissement', 'nom_scientifique',
                            'stade_de_developpement', 'diametre_cm', 'hauteur_m', 'rayon_cm']

    # Drop Non-specified Trees
    data_pa = data_pa.loc[(data_pa["nom_scientifique"] != 'Non spécifié')]

    # Clean Tree Type entirely
    data_pa['nom_scientifique'] = data_pa['nom_scientifique'].replace('x Cupressocyparis','Cupressocyparis')
    data_pa['nom_scientifique'] = data_pa['nom_scientifique'].replace('x Chitalpa','Chitalpa')

    # Selecting only Trees in Paris
    data_pa = data_pa.loc[(data_pa["arrondissement"] != 'SEINE-SAINT-DENIS') & (data_pa["arrondissement"] != 'VAL-DE-MARNE') &
                 (data_pa["arrondissement"] != 'HAUTS-DE-SEINE')]

    # Modify arrondissement so that it shows only numbers
    arrdt = {'PARIS 8E ARRDT' : '8', 'PARIS 11E ARRDT': '11',
         'PARIS 18E ARRDT' : '18', 'PARIS 16E ARRDT' : '16',
         'PARIS 20E ARRDT' : '20', 'PARIS 15E ARRDT' : '15',
         'PARIS 17E ARRDT' : '17', 'PARIS 4E ARRDT' : '4',
         'PARIS 12E ARRDT' : '12', 'PARIS 10E ARRDT' : '10',
         'PARIS 14E ARRDT' : '14', 'PARIS 7E ARRDT' : '7',
         'PARIS 13E ARRDT' : '13', 'BOIS DE VINCENNES' : '12',
         'PARIS 9E ARRDT' : '9', 'PARIS 5E ARRDT' : '5',
         'PARIS 19E ARRDT' : '19', 'PARIS 3E ARRDT' : '3',
         'PARIS 6E ARRDT' : '6', 'BOIS DE BOULOGNE' : '16',
         'PARIS 1ER ARRDT' : '1', 'PARIS 2E ARRDT' : '2'
         }

    data_pa = data_pa.replace({"arrondissement": arrdt})

    # Lower casing and strip string
    data_pa['nom_scientifique'] = data_pa['nom_scientifique'].str.lower()
    data_pa['stade_de_developpement'] = data_pa['stade_de_developpement'].str.lower()
    data_pa['nom_scientifique'] = data_pa['nom_scientifique'].str.strip()
    data_pa['stade_de_developpement'] = data_pa['stade_de_developpement'].str.strip()

    # Transform columns in integers or floats
    cols = ['hauteur_m', 'long', 'lat']
    data_pa[cols] = data_pa[cols].apply(pd.to_numeric, downcast = 'float')
    data_pa['arrondissement'] = data_pa['arrondissement'].astype('int64')

    return data_pa
