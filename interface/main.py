from google.cloud import storage
import pandas as pd
from cleaning import cleaning_ba , cleaning_paris
from preprocessor import preprocessor
from model_age import define_age_tree

def get_data():
    # The ID of your GCS bucket
    bucket_name = "bucket-the-forest"

    # The ID of your GCS object
    name_csv_ba = "arbolado-publico-lineal-2017-2018.csv"
    name_csv_paris = "les-arbres-paris-2022.csv"

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blob1 = bucket.blob(name_csv_ba)
    path_1 = "gs://bucket-the-forest/data/arbolado-publico-lineal-2017-2018.csv"
    data_ba = pd.read_csv(path_1)

    blob2 = bucket.blob(name_csv_paris)
    path_2 = "gs://bucket-the-forest/data/les-arbres-paris-2022.csv"
    data_paris= pd.read_csv(path_2 , sep=';')

    return data_paris , data_ba

if 'name'=='__main__':
    data_paris , data_ba = get_data()
    data_paris = cleaning_paris(data_paris)
    data_ba = cleaning_ba(data_ba)

    data_paris = preprocessor(data_paris)
    data_ba = preprocessor(data_ba)

    data_paris , data_ba = define_age_tree(data_paris , data_ba)
