import tkinter as tk
from base_de_datos import conectar
from password import on_focus_in,on_focus_out,mostrar_ocultar_Password
from imagenes import Imagenes
from registrar_usuario import ventana_register
from helper import verificar_entry,ocultar_error
from verificar import verificar_datos_inicio

def ventana_Inicio(frame,root):
    email=tk.Label(frame,text='Email:',font=('San Francisco',15,'underline'))
    email.grid(row=1,column=0,sticky='w',padx=5)
    entry_mail,mail_var,mail_title=entry_inicio(frame,'ej: ejemplo@gmail.com',2,0)
    
    contra=tk.Label(frame,text='Contraseña:',font=('San Francisco',15,'underline'))
    contra.grid(row=3,column=0,sticky='w',padx=5)
    entry_pass,pass_var,pass_title=entry_inicio(frame,'(Mínimo 8 caracteres)',4,1)
    
    error_label=tk.Label(frame,text='Email o contraseña incorrecta',fg='red')
    error_label.grid(row=5,column=0,sticky='ew',columnspan=3)
    error_label.grid_forget()
    
    inicio_button=tk.Label(frame,text='Iniciar sesión',font=('San Francisco',14),width=2,height=2,background='RoyalBlue2',fg='white',relief='raised',cursor='pointinghand')
    inicio_button.grid(row=6,column=0,sticky='ew',columnspan=3)
    inicio_button.bind('<ButtonPress-1>',lambda event:inicio_button.config(width=2,height=2,background='RoyalBlue3', borderwidth=1, relief="raised"))
    inicio_button.bind('<ButtonRelease-1>',lambda event:verificar_datos_inicio(event,mail_var,pass_var,inicio_button,error_label,entry_mail,entry_pass,root,1))
    inicio_button.bind('<Enter>',lambda event:inicio_button.config(background='RoyalBlue1'))
    inicio_button.bind('<Leave>',lambda event:inicio_button.config(background='RoyalBlue2'))
    
    pregunta=tk.Label(frame,text='¿No tenés una cuenta?')
    pregunta.grid(row=7,column=0,columnspan=3)
    
    registro_label=tk.Label(frame,text='Registrarse',font=('San Francisco',13),fg='RoyalBlue4',cursor='pointinghand')
    registro_label.grid(row=8,column=0,columnspan=3)
    registro_label.bind('<ButtonRelease-1>',lambda event:ventana_register(event,root))
    registro_label.bind('<ButtonRelease-1>',lambda event:ocultar_error(event,error_label,entry_mail,entry_pass),add='+')
    registro_label.bind('<Enter>',lambda event:registro_label.config(font=('San Francisco',14,'underline')))
    registro_label.bind('<Leave>',lambda event:registro_label.config(font=('San Francisco',13)))
    
    imagen_pass=Imagenes('Imagenes/Oculta-Password.png')
    
    boton_pass_inicio=tk.Button(frame,image=imagen_pass,width=25, height=25,command=lambda:mostrar_ocultar_Password(boton_pass_inicio,entry_pass))
    boton_pass_inicio.image=imagen_pass
    boton_pass_inicio.grid(row=4,column=1,sticky='e',padx=10)
    boton_pass_inicio.grid_forget()
    entry_pass.bind('<KeyRelease>',lambda event:verificar_entry(event,entry_pass,pass_title,boton_pass_inicio,4,10))
    
    inicio_button.bind('<ButtonRelease-1>',lambda event:verificar_datos_inicio(event,mail_var,pass_var,inicio_button,error_label,entry_mail,entry_pass,root,1,boton_pass_inicio,pass_title,mail_title))

def entry_inicio(frame,titulo,fila,i):
    var=tk.StringVar()
    entry=tk.Entry(frame,fg='grey',textvariable=var, width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2')
    entry.insert(0,titulo)
    entry.grid(row=fila,column=0,pady=5,ipady=10,columnspan=2,padx=7,ipadx=5)
    entry.bind('<FocusIn>',lambda event:on_focus_in(event,entry,titulo,i))
    entry.bind('<FocusOut>',lambda event:on_focus_out(event,entry,titulo,i))
    return  entry,var,titulo 





