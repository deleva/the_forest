import pandas as pd
import numpy as np
import streamlit as st

@st.cache
def tree_stats_df(paris_clean, ba_clean):
    '''
    After cleaning, we get paris_clean and ba_clean.
    This df has columns: ['Paris', 'Buenos Aires']
    And indices:
    ['Number of trees', 'Average height (in m)', 'Average diameter (in cm)', 'Number of species', 'Area of city (in km2)']
    '''

    df = pd.DataFrame(index=['Number of trees', 'Average height (in m)', 'Average diameter (in cm)', 'Number of species', 'Area of city (in km2)'] ,
                  columns=['Paris', 'Buenos Aires'])

    df['Paris'] = [paris_clean.shape[0],
                np.round(paris_clean['hauteur_m'].mean(), 2),
                np.round(paris_clean['diametre_cm'].mean(), 2),
                161,
                105.4]

    df['Buenos Aires'] = [ba_clean.shape[0],
                        np.round(ba_clean['hauteur_m'].mean(),2),
                        np.round(ba_clean['diametre_cm'].mean(), 2),
                        206,
                        203]
    return df

@st.cache
def carbon_stats_df(paris_preprocess, ba_preprocess):
    '''
    After cleaning and preprocessing, we get paris_preprocess, ba_preprocess.
    This df has columns: ['Paris', 'Buenos Aires']
    And indices:
    ['Total Carbon stock (in tons of CO2)', 'Area of city (in km2)', 'Carbon stock/km2']
    '''
    df = pd.DataFrame(index=['Total Carbon stock (in tons of CO2)', 'Area of city (in km2)', 'Carbon stock/km2'] ,
                  columns=['Paris', 'Buenos Aires'])

    df['Paris'] = [np.round(paris_preprocess['remainder__carbon'].sum(), 2),
                105.4,
                np.round(paris_preprocess['remainder__carbon'].sum()/105.4, 2)]

    df['Buenos Aires'] = [np.round(ba_preprocess['remainder__carbon'].sum(), 2),
                        203,
                        np.round(ba_preprocess['remainder__carbon'].sum()/203, 2)]
    return df


# def tree_carbon_stats_df(paris_clean, paris_preprocess, ba_clean, ba_preprocess):
#     '''
#     After cleaning, we get paris_clean and ba_clean.
#     After preprocessing the clean data, we get paris_preprocess, ba_preprocess.
#     This df has columns: ['Paris', 'Buenos Aires']
#     And indices:
#     ['Number of trees', 'Average height (in m)', 'Average diameter (in cm)', 'Number of species',
#         'Total Carbon stock (in tons of CO2)', 'Area of city (in km2)', 'Carbon stock/km2']
#     '''
#     df = pd.DataFrame(index=['Number of trees', 'Average height (in m)', 'Average diameter (in cm)', 'Number of species',
#                          'Total Carbon stock (in tons of CO2)', 'Area of city (in km2)', 'Carbon stock/km2'] ,
#                   columns=['Paris', 'Buenos Aires'])

#     df['Paris'] = [paris_clean.shape[0],
#                 np.round(paris_clean['hauteur_m'].mean(), 2),
#                 np.round(paris_clean['diametre_cm'].mean(), 2),
#                 161,
#                 np.round(paris_preprocess['remainder__carbon'].sum(), 2),
#                 105.4,
#                 np.round(paris_preprocess['remainder__carbon'].sum()/105.4, 2)]

#     df['Buenos Aires'] = [ba_clean.shape[0],
#                         np.round(ba_clean['hauteur_m'].mean(),2),
#                         np.round(ba_clean['diametre_cm'].mean(), 2),
#                         206,
#                         np.round(ba_preprocess['remainder__carbon'].sum(), 2),
#                         203,
#                         np.round(ba_preprocess['remainder__carbon'].sum()/203, 2)]
#     return df

def arrondissements_paris_df(paris_preprocess):
    '''
    After cleaning and preprocessing, we get paris_preprocess.
    This df has columns:
    ['Carbon stock/km2 [in t of CO2]', 'Number of trees', 'GES [in teq. CO2/an]', 'GES-Carbon stock [in teq. CO2/an]']
    And indices:
    the 20 arrondissements
    '''

    arr = list()
    area = [1.83, 0.99, 1.17, 1.60, 2.54, 2.15, 4.09, 3.88, 2.18, 2.89, 3.67, 16.32, 7.15, 5.64, 8.48, 16.37, 5.67, 6.01, 6.79, 5.98]
    ges = [82400, 71500, 67500, 70600, 111400, 130300, 154600, 253900, 170500, 162600, 227300, 362400, 300800, 265200, 496900, 538600, 375900, 307700, 309700, 312800]
    carbon = list()
    carbon_area = list()
    trees= list()

    for n in range(1, 21):
        arr.append(f"{n}e")
        sub_df = paris_preprocess[paris_preprocess['remainder__arrondissement']== n]
        C = np.round(sub_df['remainder__carbon'].sum(), 2)

        carbon.append(C)
        carbon_area.append(round(C/area[n-1], 2))
        trees.append(sub_df.shape[0])

    df = pd.DataFrame(index = arr)
    df['Carbon stock/km2 [in t of CO2]'] = carbon_area
    df['Number of trees'] = trees
    df['GES [in teq. CO2/an]'] = ges
    df['GES-Carbon stock [in teq. CO2/an]'] = df['GES [in teq. CO2/an]'] - df['Carbon stock/km2 [in t of CO2]']
    return df


def comunas_ba_df(ba_preprocess):
    '''
    After cleaning and preprocessing, we get ba_preprocess.
    This df has columns:
    ['Carbon stock/km2 (in tons of CO2)', 'Number of trees']
    And indices:
    the 15 comunas
    '''

    comunas = list()
    area = [17.4, 6.1, 6.4, 21.6, 6.7, 6.8, 12.4, 21.9, 16.8, 12.7, 14.1, 15.6, 14.6, 15.8, 14.3]
    carbon = list()
    carbon_area = list()
    trees= list()
    for n in range(1, 16):
        comunas.append(n)
        sub_df = ba_preprocess[ba_preprocess['remainder__arrondissement']== n]
        C = np.round(sub_df['remainder__carbon'].sum(), 2)

        carbon.append(C)
        carbon_area.append(round(C/area[n-1], 2))
        trees.append(sub_df.shape[0])

    df = pd.DataFrame(index = comunas, columns=['Carbon stock/km2 (in tons of CO2)', 'Number of trees'])
    df['Carbon stock/km2 (in tons of CO2)'] = carbon_area
    df['Number of trees'] = trees
    return df

def species_carbon_df(paris_preprocess, ba_preprocess):
    '''
    After cleaning and preprocessing, we get paris_preprocess and ba_preprocess.
    This df has columns:
    ['Carbon stock/tree (in tons of CO2) paris', 'Number of trees paris', 'Carbon stock/tree (in tons of CO2) ba', 'Number of trees ba']
    And indices:
    the 85 mutual species
    '''

    species_commun = ['rhus', 'castanea', 'viburnum', 'malus', 'punica', 'carya', 'phoenix', 'cydonia', 'picea', 'pterocarya', 'crataegus', 'paulownia', 'photinia', 'thuja', 'ficus', 'calocedrus', 'albizia', 'araucaria', 'tilia', 'betula', 'cryptomeria', 'populus', 'hovenia', 'ligustrum', 'pyrus', 'butia', 'chamaecyparis', 'cercis', 'magnolia', 'ilex', 'liriodendron', 'platanus', 'poncirus', 'gleditsia', 'acer', 'pinus', 'hibiscus', 'platycladus', 'eriobotrya', 'broussonetia', 'olea', 'fraxinus', 'robinia', 'alnus', 'juniperus', 'carpinus', 'trachycarpus', 'cupressocyparis', 'prunus', 'firmiana', 'lagerstroemia', 'buxus', 'ailanthus', 'koelreuteria', 'fagus', 'ginkgo', 'juglans', 'eucalyptus', 'callistemon', 'melia', 'cinnamomum', 'morus', 'celtis', 'aesculus', 'maclura', 'quercus', 'mespilus', 'laurus', 'catalpa', 'abies', 'cupressus', 'pittosporum', 'cordyline', 'ulmus', 'sambucus', 'cotoneaster', 'carica', 'taxodium', 'euonymus', 'cedrus', 'diospyros', 'acca', 'acacia', 'salix', 'liquidambar']
    species_df = pd.DataFrame(index = species_commun)

    for city in ['paris', 'ba']:
        carbon = list()
        trees= list()
        for s in species_commun:
            if city == 'paris':
                sub_df = paris_preprocess[paris_preprocess[f'species__nom_scientifique_{s}']== 1]
            else:
                sub_df = ba_preprocess[ba_preprocess[f'species__nom_scientifique_{s}']== 1]

            C = np.round(sub_df['remainder__carbon'].mean(), 2)
            carbon.append(C)
            trees.append(sub_df.shape[0])

    species_df[f'Carbon stock/tree (in tons of CO2) {city}'] = carbon
    species_df[f'Number of trees {city}'] = trees
    return species_df


def stage_carbon_df(paris_stage, ba_stage):
    """
    After cleaning, preprocessing, and the stage model, we get paris_stage and ba_stage.
    This df has columns:
    ['Carbon stock/tree (in tons of CO2) paris', 'Number of trees paris', 'Carbon stock/tree (in tons of CO2) ba', 'Number of trees ba'].
    And indices:
    ['Young', 'Young Adult', 'Adult', 'Mature'].
    """

    stages = ['Young', 'Young Adult', 'Adult', 'Mature']
    s_dict = {'Young':1,
            'Young Adult':2,
            'Adult':0,
            'Mature':3}
    stage_df = pd.DataFrame(index = stages)

    for city in ['paris', 'ba']:
        carbon = list()
        trees= list()
        for stage in stages:
            if city == 'paris':
                sub_df = paris_stage[paris_stage['remainder__stade_de_developpement']== s_dict[stage]]
            else:
                sub_df = ba_stage[ba_stage['remainder__stade_de_developpement']== s_dict[stage]]

            C = np.round(sub_df['remainder__carbon'].mean(), 2)
            carbon.append(C)
            trees.append(sub_df.shape[0])

        stage_df[f'Carbon stock/tree (in tons of CO2) {city}'] = carbon
        stage_df[f'Number of trees {city}'] = trees

    return stage_df


def average_diameter(paris_clean, paris_preprocess):
    '''
    From paris_clean and paris_preprocess.
    Columns: ['Average Carbon stock/tree (in tons of CO2) Paris', 'Number of trees',
        'Average diameter stage Young',
        'Average diameter stage Young Adult',
        'Average diameter stage Adult',
        'Average diameter stage Mature']
    Indices: the 85 commun species
    '''

    species_commun = ['rhus', 'castanea', 'viburnum', 'malus', 'punica', 'carya', 'phoenix', 'cydonia', 'picea', 'pterocarya', 'crataegus', 'paulownia', 'photinia', 'thuja', 'ficus', 'calocedrus', 'albizia', 'araucaria', 'tilia', 'betula', 'cryptomeria', 'populus', 'hovenia', 'ligustrum', 'pyrus', 'butia', 'chamaecyparis', 'cercis', 'magnolia', 'ilex', 'liriodendron', 'platanus', 'poncirus', 'gleditsia', 'acer', 'pinus', 'hibiscus', 'platycladus', 'eriobotrya', 'broussonetia', 'olea', 'fraxinus', 'robinia', 'alnus', 'juniperus', 'carpinus', 'trachycarpus', 'cupressocyparis', 'prunus', 'firmiana', 'lagerstroemia', 'buxus', 'ailanthus', 'koelreuteria', 'fagus', 'ginkgo', 'juglans', 'eucalyptus', 'callistemon', 'melia', 'cinnamomum', 'morus', 'celtis', 'aesculus', 'maclura', 'quercus', 'mespilus', 'laurus', 'catalpa', 'abies', 'cupressus', 'pittosporum', 'cordyline', 'ulmus', 'sambucus', 'cotoneaster', 'carica', 'taxodium', 'euonymus', 'cedrus', 'diospyros', 'acca', 'acacia', 'salix', 'liquidambar']
    stages = ['jeune (arbre)', 'jeune (arbre)adulte', 'adulte', 'mature']

    df = pd.DataFrame(index = species_commun)

    carbon = list()
    trees= list()
    stage_lists = [[], [], [], []]

    for s in species_commun:
        sub_df = paris_preprocess[paris_preprocess[f'species__nom_scientifique_{s}']== 1]
        sub_clean = paris_clean[paris_clean['nom_scientifique']==s]

        C = np.round(sub_df['remainder__carbon'].mean(), 2)
        carbon.append(C)
        trees.append(sub_df.shape[0])

        for ind in range(4):
            stage_clean = sub_clean[sub_clean['stade_de_developpement']==stages[ind]]
            stage_lists[ind].append(stage_clean['diametre_cm'].mean())


    df['Average Carbon stock/tree (in tons of CO2) Paris'] = carbon
    df['Number of trees'] = trees
    df['Average diameter stage Young'] = stage_lists[0]
    df['Average diameter stage Young Adult'] = stage_lists[1]
    df['Average diameter stage Adult'] = stage_lists[2]
    df['Average diameter stage Mature'] = stage_lists[3]

    return df.sort_values(by=['Average Carbon stock/tree (in tons of CO2) Paris'], ascending=False).head(10)

#For API
# dict={
#     'taxodium':{NaN, 37.719722, 69.837189, 92.840383},
#     'pterocarya':{13.658093, 25.012612, 40.400336, 97.977683},
#     'cedrus':{15.962651, 34.536623, 47.128857, 85.862904},
#     'populus':{11.114684, 25.504228, 47.708399, 74.819876},
#     'platanus':{12.607335, 23.014674, 43.153470, 76.363315},
#     'aesculus':{14.140222, 22.449675, 41.805955, 73.966669},
#     'fagus':{10.619080, 25.883469, 38.941035, 87.356965},
#     'ailanthus':{16.446011, 24.182280, 41.078177, 72.825951},
#     'salix':{11.042060, 23.229387, 44.405638, 51.839039},
#     'calocedrus':{11.936621, 19.576058, 36.685214, 66.526766}
# }
