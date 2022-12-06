from fastapi import FastAPI
import pandas as pd
from models.GradientBoostingRegressor import load_model

app = FastAPI()

app.state.model = load_model()

@app.get("/predict")
def predict(arrondissement: str,  #
            stade_de_developpement: float,    #
            espece: str     #
            )

    key = "2013-07-06 17:18:00.000000119"

    X_pred = pd.DataFrame(dict(
        key=[key],  # useless but the pipeline requires it
        arrondissement=[arrondissement],
        stade_de_developpement=[stade_de_developpement],
        espece=[espece],
        diametre_cm=[diametre_cm]))

    model = app.state.model
    X_processed = preprocess_features(X_pred)
    y_pred = model.predict(X_processed)

    return y_pred


# Endpoint
@app.get('/')
def index():
    return {'ok': True}

@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Hello")
    # $CHA_END
