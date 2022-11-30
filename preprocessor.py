def data_cleaning_ba(data_ba):
    '''
    Allow you to clean Bueno Aires trees dataset.
    Take the dataframe as an input to return a dataframe with the
    This function is specific

    Difficile de généraliser la fonction à cause des colonnes qui sont différentes dans les différents df (paris par exemple)
    '''
    #Drop columns
    columns_to_drop = [ 'tipo_activ','manzana','calle_nombre', 'calle_altura', 'calle_chapa', 'direccion_normalizada',
                        'ubicacion',  'ancho_acera', 'estado_plantera','ubicacion_plantera', 'nivel_plantera']
    data_ba = data_ba.drop(columns=columns_to_drop)

    #rename columns
    data_ba.columns = ['long', 'lat', 'id', 'arrondissement', 'nom_scientifique', 'diametre_cm', 'hauteur_m']

    #Compute radius
    data_ba['rayon'] = data_ba['diametre_cm'].apply(lambda x: x/2)

    #Remove 'No identificado'
    data_ba = data_ba[data_ba['nom_scientifique'] != 'No identificado']

    # Remove trees that are
    data_ba = data_ba[(data_ba['hauteur_m'] > 0) & (data_ba['diametre_cm'] > 0)]

    return data_ba

def clean(df):
    '''
    Allow you to clean the dataframe with the right columns
    '''
    #Suppression des NaNs
    df = df[['diametre_cm', 'hauteur_cm']].dropna()

    #Nettoyage des valeurs
    df['nom_scientifique'] = df['nom_scientifique'].str.lower()
    df['nom_scientifique'] = df['nom_scientifique'].str.strip()

    #Sélection des arbres
    #df[(df['hauteur_m'] >= 1) & (df['diametre_cm'] >= 1)]

    return df
