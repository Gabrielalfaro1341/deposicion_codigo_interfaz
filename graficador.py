import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from eliminar_datos_erroneos import eliminar_datos
from sumar import suma
import statsmodels.api as sm
from calculo_pendiente import calculo_pendiente
from exponencial_fit import fiteo, func
import seaborn as sns
from suvi import pendiente_suavizado
from red_neuronal import entrenar



def graficador_crecimiento(directorio):
    nombre = directorio.split('/')
    path = [n + '/' for n in nombre[:-1]]
    direccion = ''

    # Editar data frame

    for i in path:
        direccion += i

    df = pd.read_csv(directorio, delimiter=',')
    fig, (ax, ax2) = plt.subplots(2, 1, sharex=True)


    df['DeltaP(Deg)'] = df['FaradayVoltage(V)'] * 13



    # graficar data frame

    ax.scatter(df['Time(s)'], df['DeltaP(Deg)'], alpha=0.015)
    ax.set_ylabel('Delta P°')
    ax2.set_xlabel('Tiempo (s)')
    ax.set_title('Crecimiento de pelicula para ' + nombre[-1].replace('.txt', ''))
    calculo_pendiente(df, ax)
    ax2.plot(df['Time(s)'], df['StraylightVoltage(V)'] * 1000, alpha=0.5)
    fig.subplots_adjust(hspace=0)
    ax2.set_ylabel('StraylightVoltage(mV)')
    ax2.xaxis.grid(linestyle='--')
    ax.xaxis.grid(linestyle='--')
    ax.legend()

    # suavizado straylight

    lowes1 = sm.nonparametric.lowess(df.loc[:, 'StraylightVoltage(V)'] * 1000,
                                     df.loc[:, 'Time(s)'], frac=0.01)

    ax2.plot(lowes1[:, 0], lowes1[:, 1], color='blue')

    fiteo(df, ax, func)

    plt.savefig(direccion + nombre[-1].replace('.txt', '.png'), dpi=300)

    plt.show()

    # dif data pendiente

    diff = df.diff()
    diff = diff[diff['Time(s)'].notna()]

    diff['pendiente'] = diff['DeltaP(Deg)'] / diff['Time(s)']

    info = diff.describe()

    sns.kdeplot(data=df, x=diff.pendiente, fill=True, alpha=0.5,
                linewidth=0, palette='viridis')

    plt.show()

    # suavizado de pendiente

    fig, ax = plt.subplots()

    x, y = pendiente_suavizado(df.loc[1:, 'Time(s)'], diff.pendiente, 30)

    ax.plot(x, y, color='blue')
    ax.set_title('pendiente suavizada ' + nombre[-1].replace('.txt', ''))
    plt.savefig(direccion + nombre[-1].replace('.txt', '-pendiente_suavizada.png'), dpi=300)


    plt.show()


    #gradicar temperatura

    mv_temperatura=df['Temp_knudsen(K)']+0.919*(10**-3)
    df['Temperatura_knudsen(C)']=entrenar(df)
    df['Temperatura_knudsen(K)']=df['Temperatura_knudsen(C)']+273













    return x,y,df['DeltaP(Deg)'],df['Temperatura_knudsen(K)']


