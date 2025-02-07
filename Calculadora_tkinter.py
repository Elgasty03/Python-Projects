import tkinter as tk

ventana= tk.Tk()
ventana.geometry("475x630")
ventana.title('Calculadora')

cajaDeTexto=tk.Entry(ventana)
cajaDeTexto.config(width=16,border=5,font=('Arial',50))
cajaDeTexto.grid(row=0,column=0,columnspan=4)

i=0

def obtener_Numeros(n):
    global i
    cajaDeTexto.insert(i,n)
    i+=1

def obtener_Operacion(operador):
    global i
    longitud=len(operador)
    cajaDeTexto.insert(i,operador)
    i+=longitud

def eliminar_Numero():
    cajaDeTexto.delete(len(cajaDeTexto.get())-1)

    
def eliminar_Todo():
    cajaDeTexto.delete(0,tk.END)

def calculo():
    try:
        resultado = eval(cajaDeTexto.get(), {"__builtins__": None}, {})
        eliminar_Todo()
        cajaDeTexto.insert(0, resultado)
    except Exception as e:
        eliminar_Todo()
        cajaDeTexto.insert(0, "Error")
        print("Error:", e)  

#Botones Numericos
boton0=tk.Button(ventana,text='0',command=lambda:obtener_Numeros(0),padx=30,pady=30,fg='black',background='black',font=('Arial',35))

boton1=tk.Button(ventana,text='1',command=lambda:obtener_Numeros(1),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton2=tk.Button(ventana,text='2',command=lambda:obtener_Numeros(2),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton3=tk.Button(ventana,text='3',command=lambda:obtener_Numeros(3),padx=30,pady=30,fg='black',background='black',font=('Arial',35))

boton4=tk.Button(ventana,text='4',command=lambda:obtener_Numeros(4),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton5=tk.Button(ventana,text='5',command=lambda:obtener_Numeros(5),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton6=tk.Button(ventana,text='6',command=lambda:obtener_Numeros(6),padx=30,pady=30,fg='black',background='black',font=('Arial',35))

boton7=tk.Button(ventana,text='7',command=lambda:obtener_Numeros(7),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton8=tk.Button(ventana,text='8',command=lambda:obtener_Numeros(8),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton9=tk.Button(ventana,text='9',command=lambda:obtener_Numeros(9),padx=30,pady=30,fg='black',background='black',font=('Arial',35))

#Botones Operaciones
boton_suma=tk.Button(ventana,text='+',command=lambda:obtener_Operacion('+'),padx=30,pady=30,fg='black',background='black',font=('Arial',35))
boton_resta=tk.Button(ventana,text='-',command=lambda:obtener_Operacion('-'),padx=35,pady=30,fg='black',background='black',font=('Arial',35))
boton_igual=tk.Button(ventana,text='=',command=lambda:calculo(),padx=32,pady=30,fg='black',background='black',font=('Arial',35))
boton_dividir=tk.Button(ventana,text='÷',command=lambda:obtener_Operacion('/'),padx=32,pady=30,fg='black',background='black',font=('Arial',35))
boton_multiplicar=tk.Button(ventana,text='*',command=lambda:obtener_Operacion('*'),padx=35,pady=30,fg='black',background='black',font=('Arial',35))
boton_cuadrado = tk.Button(ventana, text='^2', command=lambda:obtener_Operacion('**2'), padx=23, pady=30, fg='black', background='black', font=('Arial', 35))
boton_eliminar_todo=tk.Button(ventana,text='AC',command=lambda:eliminar_Todo(),padx=15,pady=30,fg='black',background='black',font=('Arial',35))
boton_eliminar_uno_solo=tk.Button(ventana,text='⌫',command=lambda:eliminar_Numero(),padx=25,pady=34,fg='black',background='black',font=('Arial',28))
boton_abrir_parentesis=tk.Button(ventana,text='(',command=lambda:obtener_Operacion('('),padx=35,pady=30,fg='black',background='black',font=('Arial',35))
boton_cerrar_parentesis=tk.Button(ventana,text=')',command=lambda:obtener_Operacion(')'),padx=35,pady=30,fg='black',background='black',font=('Arial',35))


#Ubicacion de botones
boton0.grid(row=5,column=0)
boton1.grid(row=2,column=0)
boton2.grid(row=2,column=1)
boton3.grid(row=2,column=2)
boton4.grid(row=3,column=0)
boton5.grid(row=3,column=1)
boton6.grid(row=3,column=2)
boton7.grid(row=4,column=0)
boton8.grid(row=4,column=1)
boton9.grid(row=4,column=2)
boton_suma.grid(row=1,column=3)
boton_resta.grid(row=2,column=3)
boton_igual.grid(row=5,column=3)
boton_dividir.grid(row=3,column=3)
boton_multiplicar.grid(row=4,column=3)
boton_eliminar_todo.grid(row=5,column=1)
boton_eliminar_uno_solo.grid(row=5,column=2)
boton_cuadrado.grid(row=1,column=2)
boton_abrir_parentesis.grid(row=1,column=0)
boton_cerrar_parentesis.grid(row=1,column=1)

#Mostrar Ventana
ventana.mainloop()
