import pickle

def load_model():
    # load the model from disk
    filename = 'GradientBoostingRegressor_model.pkl'
    model = pickle.load(open(filename, 'rb'))

    return model
