from tkinter import *
from tkinter import filedialog
from graficador import graficador_crecimiento
from grafico_de_todos import graficadata
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


raiz=Tk()
raiz.wm_title('Graficador de rampas')
listadata=list()
listatemp=list()

cantidad=int(input('cantidad de archivo:'))
f=0
def abrirarchivo():
    global cantidad
    global f
    if len(listadata)!=cantidad:
           archivo=filedialog.askopenfilename(title='abrir',initialdir='/home/gabriel/Escritorio/nico/dep_var_temp')
           listadata.append(archivo)
           x,y,delta,temperatura=graficador_crecimiento(archivo)
           listatemp.append([delta,temperatura])

           abrirarchivo()
    else:

        graficadata(listadata,listatemp,'delta')
        graficadata(listadata, listatemp, 'temperatura')
        graficadata(listadata, listatemp, 'tiempo')


Button(raiz, text='Ingrese archivo para rampa',command=abrirarchivo).pack()




raiz.mainloop()