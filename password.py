import tkinter as tk
from imagenes import Imagenes

def on_focus_in(event, entry, placeholder,i):
    """Si el usuario hace clic y el texto es el placeholder, lo borra."""
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        if i==1:
            entry.config(fg='black',show='*')
        else:
            entry.config(fg='black')
def on_focus_out(event, entry, placeholder,i):
    """Si el usuario hace clic fuera y no ha escrito nada, muestra el placeholder."""
    if entry.get() == "":
        entry.config(fg='grey')
        if i==1:
            entry.config(show="")
        entry.insert(0,placeholder)

def mostrar_ocultar_Password(boton_mostrar,entry):
    if entry.cget('show') == '*':
        entry.config(show="")
        imagen_tk_mostrar_pass = Imagenes('Imagenes/Ver-Password.png')
        boton_mostrar.config(image=imagen_tk_mostrar_pass)
        boton_mostrar.image = imagen_tk_mostrar_pass
    else:
        entry.config(show="*")
        imagen_oculta_pass = Imagenes('Imagenes/Oculta-Password.png')
        boton_mostrar.config(image=imagen_oculta_pass)
        boton_mostrar.image = imagen_oculta_pass

