def data_cleaning_ba(data_ba):
  '''
  Permet de nettoyer le dataset de bueno aires
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

  return data_ba
