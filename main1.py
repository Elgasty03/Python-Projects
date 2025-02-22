import tkinter as tk
from iniciar_sesion_app import ventana_Inicio
from base_de_datos import crear_tabla

crear_tabla()
root=tk.Tk()
root.geometry('365x300+500+200')
root.resizable(False,False)
root.title('App')

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=0,columnspan=100,sticky="ew")

titulo_inicio_sesion=tk.Label(frame,text='INICIAR SESIÓN',font=('San Francisco',30,'bold'))
titulo_inicio_sesion.grid(row=0,column=0,sticky='nsew',pady=5,columnspan=3)

ventana_sesion=ventana_Inicio(frame,root)

root.mainloop()

