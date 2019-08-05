import pandas as pd
from keras import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.preprocessing import RobustScaler
import joblib

scale_l = joblib.load('static/NN Files/prices.pkl')


def model():
    nn = Sequential()
    nn.add(Dense(1687, activation ='relu', input_shape=(1687,)))
    nn.add(Dense(1687*2, activation ='relu'))
    nn.add(Dense(1687*2, activation ='relu'))
    nn.add(Dense(1687*4, activation ='relu'))
    nn.add(Dense(1687, activation ='relu'))
    nn.add(Dense(1687, activation ='relu'))
    nn.add(Dense(1200, activation ='relu'))
    nn.add(Dense(1000, activation ='relu'))
    nn.add(Dense(800, activation ='relu'))
    nn.add(Dense(400, activation ='relu'))
    nn.add(Dense(200, activation = 'relu'))
    nn.add(Dense(50, activation = 'relu'))
    nn.add(Dense(1, activation = 'linear'))
    nn.load_weights('static/NN Files/model_weights.hdf5')
    return nn


def format_data(zip, age, sqft, city, beds, baths,
                levels, lotsize, remarks,
                proptype):
    zip = int(str(zip).lstrip('0'))
    columns = pd.read_csv('static/NN Files/column_names.csv')
    data = pd.DataFrame(columns=columns['0'])
    pls = pd.Series(0, index=columns['0'])
    data = data.append(pls, ignore_index=True)
    data.loc[0]["AGE"] = age
    data.loc[0]["BATHS"] = baths
    data.loc[0]["BEDS"] = beds
    data.loc[0]["LOTSIZE"] = lotsize
    if ("CITY_" + city) in data.columns:
        data.loc[0]["CITY_" + city] = 1
    data.loc[0]["SQFT"] = sqft
    if "pool" in remarks:
        data.loc[0]["POOL"] = 1
    if "granite" in remarks:
        data.loc[0]["GRANITE"] = 1
    if "cellar" in remarks:
        data.loc[0]["CELLAR"] = 1
    if "theatre" in remarks:
        data.loc[0]["THEATRE"] = 1
    if "chandelier" in remarks:
        data.loc[0]["CHANDELIER"] = 1
    if "tennis court" in remarks:
        data.loc[0]["TENNIS"] = 1
    if "walk-in closet" in remarks:
        data.loc[0]["CLOSET"] = 1
    if "waterfront" in remarks:
        data.loc[0]["WATERFRONT"] = 1
    if "gym" in remarks:
        data.loc[0]["GYM"] =1
    if "garden" in remarks:
        data.loc[0]["GARDEN"] = 1
    if "balcony" in remarks:
        data.loc[0]["BALCONY"] = 1
    if "terrace" in remarks:
        data.loc[0]["TERRACE"] = 1
    if "duplex" in remarks:
        data.loc[0]["duplex"] = 1
    if "luxury" in remarks:
        data.loc[0]["luxury"] = 1
    if "view" in remarks:
        data.loc[0]["view"] = 1
    if "ocean" in remarks:
        data.loc[0]["ocean"] = 1
    if ("PROPTYPE_" + proptype) in data.columns:
        data.loc[0]["PROPTYPE_"+proptype] = 1
    if ("LEVEL_" + levels) in data.columns:
        data.loc[0]["LEVEL_" + levels] = 1
    zip_data = pd.read_csv('static/NN Files/ZIP data.csv')
    for i in range(520):
        zip_data.rename(index={i: int(zip_data.iloc[i]["ZIP CODE"])},
                        inplace=True)
    if zip in zip_data["ZIP CODE"]:
        data.loc[0]["MED_AGE"] = zip_data.loc[zip]["MEDIAN_AGE"]
        data.loc[0]["MED_PRICE"] = zip_data.loc[zip]["MEDIAN_HOME_PRICE"]
        data.loc[0]["INCOME"] = zip_data.loc[zip]["MEDIAN_INCOME"]
        data.loc[0]["RATIO"] = zip_data.loc[zip]["STUDENT_RATIO"]
        data.loc[0]["SCHOOL_SPEND"] = zip_data.loc[zip]["SCHOOL_SPENDATURE"]
    else:
        data.loc[0]["MED_AGE"] = 41
        data.loc[0]["MED_PRICE"] = 400000
        data.loc[0]["INCOME"] = 60000
        data.loc[0]["RATIO"] = 12
        data.loc[0]["SCHOOL_SPEND"] = 12500
    scale_f = joblib.load('static/NN Files/features.pkl')
    data[['AGE', 'BATHS', 'BEDS', 'DOM', 'LOTSIZE', 'SQFT', 'GARAGE', 'MED_AGE', 'MED_PRICE', 'INCOME', 'RATIO',
             'SCHOOL_SPEND']] = scale_f.transform(data[['AGE', 'BATHS', 'BEDS', 'DOM', 'LOTSIZE', 'SQFT',
                                                                       'GARAGE', 'MED_AGE', 'MED_PRICE', 'INCOME',
                                                                       'RATIO', 'SCHOOL_SPEND']])
    return data
