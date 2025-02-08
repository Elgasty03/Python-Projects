import tkinter as tk
from tkinter import ttk

conversiones = {
    "km": 1000,
    "hm": 100,
    "dam": 10,
    "m": 1,
    "dm":0.1,
    "cm":0.01,
    "mm":0.001
}

def identificar_tipo(valor):
    try:
        numero = int(valor)
        return "int"
    except ValueError:
        try:
            numero = float(valor)
            return "float"
        except ValueError:
            return "invalido"


def convertirUnidad():
    try:
        if identificar_tipo(entrada1.get())=='int':
            valor=int(entrada1.get())
            unidad_inicial=opciones1.get()
            unidad_final=opciones2.get()
            resultado=valor*conversiones[unidad_inicial]/conversiones[unidad_final]
            entrada2.delete(0,tk.END)
            entrada2.insert(0,resultado)
        elif identificar_tipo(entrada1.get())=='float':
            valor=float(entrada1.get())
            unidad_inicial=opciones1.get()
            unidad_final=opciones2.get()
            resultado=valor*conversiones[unidad_final]/conversiones[unidad_inicial]
            entrada2.delete(0,tk.END)
            entrada2.insert(0,resultado)
    except ValueError:
        return "invalido"


ventana= tk.Tk()
ventana.geometry('500x100')
ventana.title('Conversor de Unidades') 

etiqueta1 = tk.Label(ventana, text="Escribi el valor:")

opciones1=ttk.Combobox(ventana,values=['km','hm','dam','m','dm','cm','mm'])
opciones1.set('Selecciona una unidad')

entrada1=tk.Entry(ventana)

etiqueta2=tk.Label(ventana,text='Resultado:')

opciones2=ttk.Combobox(ventana,values=['km','hm','dam','m','dm','cm','mm'])
opciones2.set('Selecciona una unidad')

entrada2=tk.Entry(ventana)

boton=tk.Button(ventana,text='Convertir',command=convertirUnidad)



etiqueta1.grid(row=0,column=0)
entrada1.grid(row=0,column=1)
opciones1.grid(row=0,column=3)
etiqueta2.grid(row=1,column=0)
entrada2.grid(row=1,column=1)
opciones2.grid(row=1,column=3)
boton.grid(row=2,column=1)


ventana.mainloop()