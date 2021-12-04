import numpy as np
import pandas as pd

def pendiente_suavizado(x,y,puntos):
    listax=list()
    listay=list()
    for i in range(1,len(x)):
        if i%puntos==0 and i!=0:

            promedio=x[i-puntos:i].mean()

            listax.append(promedio)

    for i in range(1,len(y)):
        if i%puntos==0 and i!=0:
            promedio=y[i-puntos:i].mean()

            listay.append(promedio)

    return listax,listay





