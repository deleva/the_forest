from fastapi import FastAPI
import pandas as pd
from models.GradientBoostingRegressor import
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

app.state.model = load_model()

@app.get("/predict")
def predict(nb_arbres: list,
            arrondissement: str,
            espece: list ):

    stade_diametre_info =  {'espece_1':{'Jeune(arbre)':1 ,'Jeune(arbre)Adulte':2,'Adulte':0,'Mature':3},
               'taxodium':{'Jeune(arbre)':Nan ,'Jeune(arbre)Adulte':37.719722,'Adulte':69.837189,'Mature':92.840383},
               'pterocarya':{'Jeune(arbre)':13.658093 ,'Jeune(arbre)Adulte':25.012612,'Adulte':40.400336,'Mature':97.977683},
               'cedrus':{'Jeune(arbre)':15.962651 ,'Jeune(arbre)Adulte':34.536623,'Adulte':47.128857,'Mature':85.862904},
               'populus':{'Jeune(arbre)':11.114684 ,'Jeune(arbre)Adulte':25.504228,'Adulte':47.708399,'Mature':74.819876},
               'platanus':{'Jeune(arbre)':12.607335 ,'Jeune(arbre)Adulte':23.014674,'Adulte':43.153470,'Mature':76.363315},
               'aesculus':{'Jeune(arbre)':14.140222 ,'Jeune(arbre)Adulte':22.449675,'Adulte':41.805955,'Mature':73.966669},
               'fagus':{'Jeune(arbre)':10.619080 ,'Jeune(arbre)Adulte':25.883469,'Adulte':38.941035,'Mature':87.356965},
               'ailanthus':{'Jeune(arbre)':16.446011 ,'Jeune(arbre)Adulte':24.182280,'Adulte':41.078177,'Mature':72.825951},
               'salix':{'Jeune(arbre)':11.042060 ,'Jeune(arbre)Adulte':23.229387,'Adulte':44.405638,'Mature':51.839039},
               'calocedrus':{'Jeune(arbre)':11.936621 ,'Jeune(arbre)Adulte':19.576058,'Adulte':36.685214,'Mature':66.526766}


               }

    #data_list = []
    X_pred = pd.DataFrame()

    for e in espece:

        diametre_cm_j = stade_diametre_info[espece]['Jeune(arbre)']

        diametre_cm_ja = stade_diametre_info[espece]['Jeune(arbre)Adulte']

        diametre_cm_a = stade_diametre_info[espece]['Adulte']

        diametre_cm_m = stade_diametre_info[espece]['Mature']

        X_pred['diametre_cm'] = [diametre_cm_j ,diametre_cm_ja ,diametre_cm_a ,diametre_cm_m ]
        X_pred['espece'] = e

    X_pred


    #create a dataframe with the given info (stade, espece)
    #complete the df with the average diameter thanks to the dictionnary
    # this gives a X_pred

    X_pred = pd.DataFrame(dict(
        stade_de_developpement=['Jeune(arbre)', 'Jeune(arbre)Adulte', 'Adulte','Mature'],
        espece=[espece],
        diametre_cm=[data_list]))

    X_pred_final = X_pred.copy()

    #preprocess the X_pred (label encoding, OHE, scaling, etc)

    X_pred['diametre_cm'] = MinMaxScaler().fit_transform(X_pred['diametre_cm'])
    X_pred['stade_de_developpement'] = LabelEncoder().fit_tranform(X_pred['stade_de_developpement'])

    model = app.state.model

    # get a y_pred with the loaded model
    X_processed = X_pred.drop(columns='espece')

    y_pred = model.predict(X_processed)

    #merge it with the arrondissement to return the wanted graph

    X_pred_final['y_pred'] = y_pred



    X_pred_final[Today] = nb_arbres[nb] * y_pred[0]

    Tomorrow = nb_arbres[nb] * y_pred[1]

    The_day_after_tomorrow = nb_arbres[nb] * y_pred[2]

    Many_years_later = nb_arbres[nb] * y_pred[3]

    data_prediction_list.append(Today ,Tomorrow, The_day_after_tomorrow ,Many_years_later )

    data_prediction_list = pd.DataFrame(data_prediction_list)

    return


# Endpoint
@app.get('/')
def index():
    return {'ok': True}

@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello")
    # $CHA_END
