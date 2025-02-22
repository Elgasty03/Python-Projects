
def verificar_entry(event,entry,titulo,boton_mostrar,fila,pad):
    if entry.get() and entry.get() != titulo:  # Si tiene contenido válido
        boton_mostrar.grid(row=fila, column=1, padx=pad,sticky='e')
    else:
        boton_mostrar.grid_forget()

def ocultar_error(event,error,entry_mail,entry_pass):
    error.grid_forget()
    entry_pass.config(fg='grey', width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2')
    entry_mail.config(fg='grey', width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2')
    