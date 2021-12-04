from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



def entrenar(df):
    mlr=MLPRegressor(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(100,100),
                     random_state=1,max_iter=10000)

    datos= pd.read_csv('/home/gabriel/Escritorio/deposicion codigo/temperature_mv.csv',sep=',')

    datos['mv']=pd.to_numeric(datos['mv'].str.replace(',','.'))*(10**-3)
    datos['c'] = pd.to_numeric(datos['c'])



    c=datos['c'].to_numpy().reshape(-1,1)
    mv = datos['mv'].to_numpy().reshape(-1,1)
    mlr.fit(mv,c.ravel())


    resultado=mlr.predict(df['Temp_knudsen(K)'].to_numpy().reshape(-1,1))






    return resultado




