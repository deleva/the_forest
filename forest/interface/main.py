from pathlib import Path
import pandas as pd
import streamlit as st
from forest.cleaning import cleaning_ba, cleaning_paris
from forest.preprocessor import preprocessor
from forest.model_age import define_stage_tree

# The raw data now lives in the repo (data/ folder), compressed as .csv.gz.
# It used to come from a Google Cloud bucket that no longer exists.
FILE_PARIS = "les-arbres-paris-2022.csv.gz"
FILE_BA = "arbolado-publico-lineal-2017-2018.csv.gz"

def _data_dir() -> Path:
    """Find the repo's data/ folder, whether the app runs from the repo root
    (Streamlit Cloud) or from a subfolder."""
    for folder in [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parents[2]]:
        if (folder / "data" / FILE_PARIS).exists():
            return folder / "data"
    raise FileNotFoundError(f"Could not find data/{FILE_PARIS} in the repo")

@st.cache_data(show_spinner="Loading tree data...")
def get_data():
    data_dir = _data_dir()
    data_paris = pd.read_csv(data_dir / FILE_PARIS, sep=';', low_memory=False)
    data_ba = pd.read_csv(data_dir / FILE_BA, low_memory=False)
    return data_paris, data_ba

if __name__=='__main__':
    data_paris , data_ba = get_data()
    data_paris = cleaning_paris(data_paris)
    data_ba = cleaning_ba(data_ba)

    data_paris = preprocessor(data_paris)
    data_ba = preprocessor(data_ba)

    data_paris , data_ba = define_stage_tree(data_paris , data_ba)
    print(data_paris)
