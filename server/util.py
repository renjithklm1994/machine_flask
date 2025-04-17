import json
import pickle
import numpy as np
__locations =None
__data_columns = None
__model = None
def get_location_names():

    return __locations

def predict_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except :
        loc_index = -1
    X = np.zeros(len(__data_columns))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index>=0:
        X[loc_index] = 1

    return round(__model.predict([X])[0],2)

def load_art_data():
    global __locations
    global __data_columns
    global __model
    with open('./art/columns.json','r') as f:
        __data_columns = json.load(f)['data.columns']
        __locations = __data_columns[3:]
    with open('./art/bangalore_home_price_model','rb') as f:
        __model  = pickle.load(f)
    print("loading arteffect done")
    
if __name__ =="__main__":
    load_art_data()
    get_location_names()
    print(predict_price('1st Phase JP Nagar',1000,2,2))

