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

def paris_predictions(paris_preprocess):
    """
    After cleaning and preprocessing, we get paris_preprocess.
    This df has columns: [Average Carbon stock/tree (in tons of CO2) Paris,
        Average Carbon stock/Young tree,
        Average Carbon stock/Young Adult tree,
        Average Carbon stock/Adult tree,
        Average Carbon stock/Mature tree]
    And indices: top ten species in average carbon stock/tree in Paris.
    """
    #top ten in average carbon stock/tree (in tons of CO2) Paris
    top_ten_species = ['taxodium', 'pterocarya', 'cedrus', 'populus', 'platanus', 'aesculus', 'fagus', 'ailanthus', 'salix', 'calocedrus']
    stages = ['jeune (arbre)', 'jeune (arbre)adulte', 'adulte', 'mature']

    paris_predict_df = pd.DataFrame(index = top_ten_species)

    total_carbon = list()
    stage_lists = [[], [], [], []]

    for s in top_ten_species:
        sub_df = paris_preprocess[paris_preprocess[f'species__nom_scientifique_{s}']== 1]

        C = np.round(sub_df['remainder__carbon'].mean(), 2)
        total_carbon.append(C)

        for ind in range(4):
            sub_sub_df = sub_df[sub_df['remainder__stade_de_developpement']==stages[ind]]
            c = np.round(sub_sub_df['remainder__carbon'].mean(), 2)
            stage_lists[ind].append(c)

    paris_predict_df['Average Carbon stock/tree (in tons of CO2) Paris'] = total_carbon
    paris_predict_df['Average Carbon stock/Young tree'] = stage_lists[0]
    paris_predict_df['Average Carbon stock/Young Adult tree'] = stage_lists[1]
    paris_predict_df['Average Carbon stock/Adult tree'] = stage_lists[2]
    paris_predict_df['Average Carbon stock/Mature tree'] = stage_lists[3]
    return paris_predict_df


# def arrondissements_paris_df(paris_preprocess):
#     '''
#     After cleaning and preprocessing, we get paris_preprocess.
#     This df has columns:
#     ['Carbon stock/km2 [in t of CO2]', 'Number of trees', 'GES [in teq. CO2/an]', 'GES-Carbon stock [in teq. CO2/an]']
#     And indices:
#     the 20 arrondissements
#     '''

#     arr = list()
#     area = [1.83, 0.99, 1.17, 1.60, 2.54, 2.15, 4.09, 3.88, 2.18, 2.89, 3.67, 16.32, 7.15, 5.64, 8.48, 16.37, 5.67, 6.01, 6.79, 5.98]
#     ges = [82400, 71500, 67500, 70600, 111400, 130300, 154600, 253900, 170500, 162600, 227300, 362400, 300800, 265200, 496900, 538600, 375900, 307700, 309700, 312800]
#     carbon = list()
#     carbon_area = list()
#     trees= list()

#     for n in range(1, 21):
#         arr.append(f"{n}e")
#         sub_df = paris_preprocess[paris_preprocess['remainder__arrondissement']== n]
#         C = np.round(sub_df['remainder__carbon'].sum(), 2)

#         carbon.append(C)
#         carbon_area.append(round(C/area[n-1], 2))
#         trees.append(sub_df.shape[0])

#     df = pd.DataFrame(index = arr)
#     df['Carbon stock/km2 [in t of CO2]'] = carbon_area
#     df['Number of trees'] = trees
#     df['GES [in teq. CO2/an]'] = ges
#     df['GES-Carbon stock [in teq. CO2/an]'] = df['GES [in teq. CO2/an]'] - df['Carbon stock/km2 [in t of CO2]']
#     return df


# def comunas_ba_df(ba_preprocess):
#     '''
#     After cleaning and preprocessing, we get ba_preprocess.
#     This df has columns:
#     ['Carbon stock/km2 (in tons of CO2)', 'Number of trees']
#     And indices:
#     the 15 comunas
#     '''

#     comunas = list()
#     area = [17.4, 6.1, 6.4, 21.6, 6.7, 6.8, 12.4, 21.9, 16.8, 12.7, 14.1, 15.6, 14.6, 15.8, 14.3]
#     carbon = list()
#     carbon_area = list()
#     trees= list()
#     for n in range(1, 16):
#         comunas.append(n)
#         sub_df = ba_preprocess[ba_preprocess['remainder__arrondissement']== n]
#         C = np.round(sub_df['remainder__carbon'].sum(), 2)

#         carbon.append(C)
#         carbon_area.append(round(C/area[n-1], 2))
#         trees.append(sub_df.shape[0])

#     df = pd.DataFrame(index = comunas, columns=['Carbon stock/km2 (in tons of CO2)', 'Number of trees'])
#     df['Carbon stock/km2 (in tons of CO2)'] = carbon_area
#     df['Number of trees'] = trees
#     return df

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

    stages = ['Young', 'Young adult', 'Adult', 'Mature']
    s_dict = {'Young':1,
            'Young adult':2,
            'Adult':0,
            'Mature':3}
    stage_df = pd.DataFrame(columns = stages)

    for city in ['Paris', 'BA']:
        carbon = list()
        trees= list()
        for stage in stages:
            if city == 'Paris':
                sub_df = paris_stage[paris_stage['remainder__stade_de_developpement']== s_dict[stage]]
            else:
                sub_df = ba_stage[ba_stage['remainder__stade_de_developpement']== s_dict[stage]]

            C = np.round(sub_df['remainder__carbon'].mean(), 2)
            carbon.append(C)
            trees.append(sub_df.shape[0])

        stage_df.loc[f'Carbon stock/tree (in tons of CO2) {city}'] = carbon
        stage_df.loc[f'Number of trees {city}']= trees

    return stage_df


def dev_stage_mean_diameter(paris_clean, ba_clean, ba_stage):

    '''
    Starting from three distinct data sets, paris and buenos aires cleaned but also the dataset from buenos aires passed through cleaning, preprocess and stage.
    We loop over these datasets in order to create/extract three columns:
    ['mean_diametre_cm', 'stade_de_developpement', 'villes'] for each stage of the tree in each city

    '''

    df = pd.DataFrame(columns = ['stade_de_developpement','mean_diametre_cm', 'ville'])
    stades = ['jeune (arbre)', 'jeune (arbre)adulte', 'adulte', 'mature']
    dict_stade = {'jeune (arbre)':1 ,
        'jeune (arbre)adulte':2,
        'adulte':0,
        'mature':3}
    villes = ['paris', 'buenos aires']
    cities = []
    diametres = []
    for city in villes:
        for stade in stades:
            cities.append(city)
            if city == 'paris':
                sub_data = paris_clean[paris_clean['stade_de_developpement'] == stade]
            else:
                sub_sub_data = ba_clean.merge(ba_stage, right_on = 'remainder__id', left_on = 'id')
                sub_data = sub_sub_data[sub_sub_data['remainder__stade_de_developpement'] == dict_stade[stade]]
            mean = sub_data['diametre_cm'].mean()
            diametres.append(mean)

    df['mean_diametre_cm'] = diametres
    df['stade_de_developpement'] = [1, 2, 3, 4, 1, 2, 3, 4]
    df['ville'] = cities
    return df

def height_city(paris_clean, ba_clean):

    '''
    Starting from the two datasets cleaned, we select 2 columns ['hauteur_m', 'villes']. Then we concatenate them. To get a dataset to create a simple kdeplot.

    '''

    paris_clean['ville'] = 'paris'
    data_paris_graph1 = paris_clean[['hauteur_m', 'ville']]
    ba_clean['ville'] = 'buenos aires'
    data_ba_graph1 = ba_clean[['hauteur_m', 'ville']]

    df = pd.concat([data_paris_graph1, data_ba_graph1], axis = 0)
    df = df.reset_index()
    df = df.drop(columns = 'index')

    return df

def two_sampled_frames(paris_clean, ba_clean):

    '''
    Starting from the two datasets cleaned, we select the 10 most important species for each.
    Following this we sample these datasets to make them easier to read in graphs.

    '''
    top_ten_pa_dict = {'platanus': 'platane', 'aesculus': 'marronnier', 'tilia' : 'tilleul', 'acer': 'erable', 'prunus': 'prunier',
                   'fraxinus': 'frene', 'celtis': 'micocoulier', 'pyrus': 'poirier de chine', 'quercus': 'chene', 'pinus': 'pin'}
    top_ten_ba_dict = {'fraxinus': 'frene', 'platanus': 'platane', 'ficus': 'ficus', 'tilia': 'tilleul', 'ligustrum': 'troene', 'melia': 'margousier',
                   'lagerstroemia': 'lilas', 'acer': 'erable', 'liquidambar': 'liquidambar', 'populus': 'peuplier'}

    data_pa_top_10 = paris_clean[paris_clean['nom_scientifique'].isin(top_ten_pa_dict)].replace({'nom_scientifique': top_ten_pa_dict})
    data_ba_top_10 = ba_clean[ba_clean['nom_scientifique'].isin(top_ten_ba_dict)].replace({'nom_scientifique': top_ten_ba_dict})
    data_paris_graph = pd.DataFrame()
    data_ba_graph = pd.DataFrame()

    for species in set(data_pa_top_10['nom_scientifique']):
        sub_species = data_pa_top_10[data_pa_top_10['nom_scientifique']==species]
        data_pa_sampled = sub_species.sample(frac = 0.5, axis = 0)
        data_paris_graph = pd.concat([data_paris_graph, data_pa_sampled], axis = 0)

    for species in set(data_ba_top_10['nom_scientifique']):
        sub_species = data_ba_top_10[data_ba_top_10['nom_scientifique'] == species]
        data_ba_sampled = sub_species.sample(frac = 0.25, axis = 0)
        data_ba_graph = pd.concat([data_ba_graph, data_ba_sampled], axis = 0)

    return data_paris_graph, data_ba_graph
