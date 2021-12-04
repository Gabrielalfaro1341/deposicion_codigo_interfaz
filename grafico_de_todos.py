import pandas as pd
from matplotlib import pyplot as plt

def graficadata(lista_data,listatemp,medir):

    fig,ax=plt.subplots()
    for i in range(len(lista_data)):
        df=pd.read_csv(lista_data[i], delimiter=',')
        df['DeltaP(Deg)'] = df['FaradayVoltage(V)'] * 13
        #sacando temperatura
        nombre = lista_data[i].split('/')
        path = [n + '/' for n in nombre[:-1]]
        directorio=''
        for j in path:
            directorio += j
        temperatura=nombre[-1].split('_')[1]
        temperatura=temperatura.replace('.txt','')
        print(listatemp[1][0])

        if medir=='delta':
            # grafico
            ax.plot(df['Time(s)'], df['DeltaP(Deg)'], alpha=1, label=temperatura)
            ax.set_xlabel('Tiempo (s)')
            ax.set_ylabel('Delta P°')
            ax.set_title('Comparacion de Deposiciones')

        elif medir=='temperatura':
            ax.plot(listatemp[i][1],listatemp[i][0], alpha=1, label=temperatura)
            ax.set_ylabel('Delta P°')
            ax.set_xlabel('Temperatura Knudsen (K)')
            ax.set_title('Comparacion DeltaP vs Temperatura_knudsen(K)')

        elif medir=='tiempo':
            ax.plot(df['Time(s)'],listatemp[i][1], alpha=1, label=temperatura)
            ax.set_ylabel('Temperatura Knudsen (K)')
            ax.set_xlabel('Tiempo(s)')
            ax.set_title('Comparacion Temperatura_knudsen(K)')







    ax.legend()
    if medir=='delta':
       plt.savefig(directorio+'Comparacion_de_deposiciones.png',dpi=300)
    elif medir=='temperatura':
            plt.savefig(directorio + 'Comparacion_Knudsen.png', dpi=300)

    elif medir=='tiempo':
            plt.savefig(directorio + 'Comparacion_tiempo_Knudsen.png', dpi=300)
    plt.show()




