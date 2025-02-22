import tkinter as tk
from imagenes import Imagenes
from helper import verificar_entry
from password import on_focus_in,on_focus_out,mostrar_ocultar_Password
from verificar import verificar_datos_register

def cambiar_tamano(root,ancho,altura):
    if ancho < 370:  # Condición para seguir incrementando el ancho
        ancho += 2  # Aumentar el ancho en 2 píxeles por cada paso
    if altura < 550:  # Condición para seguir incrementando la altura
        altura += 5  # Aumentar la altura en 5 píxeles por cada paso
    
    root.geometry(f"{ancho}x{altura}")  # Cambiar el tamaño de la ventana
    root.update_idletasks()
    # Solo sigue llamando a la función si no hemos alcanzado los límites
    if ancho < 370 or altura < 550:
        root.after(3, cambiar_tamano, root, ancho, altura)


def ventana_register(event,root):
    posx=365
    posy=310
    root.withdraw()
    root_register=tk.Toplevel()
    root_register.geometry('365x310+500+200')
    cambiar_tamano(root_register,posx,posy)
    #root_register.geometry('362x580+500+200')
    root_register.resizable(False,False)
    root_register.title('App')
    root_register.protocol("WM_DELETE_WINDOW", lambda: root_register_close(root_register,root))

    frame_register = tk.Frame(root_register)
    frame_register.grid(row=0, column=0, padx=10, pady=0,columnspan=100,sticky="ew")  
    titulo_register=tk.Label(frame_register,text='REGISTRO DE USUARIO',font=('San Francisco',30,'bold'))
    titulo_register.grid(row=0,column=0,sticky='nsew',pady=5,columnspan=3,padx=4)
    
    nombre_registro=tk.Label(frame_register,text='Nombre:',font=('San Francisco',15,'underline'))
    nombre_registro.grid(row=1,column=0,sticky='w',padx=5)
    n_entry,nombre_r_var=entry_register(frame_register,'',0,2)
    
    apellido_registro=tk.Label(frame_register,text='Apellido:',font=('San Francisco',15,'underline'))
    apellido_registro.grid(row=3,column=0,sticky='w',padx=5)
    a_entry,apellido_r_var=entry_register(frame_register,'',0,4)
    
    usuario_registro=tk.Label(frame_register,text='Usuario:',font=('San Francisco',15,'underline'))
    usuario_registro.grid(row=5,column=0,sticky='w',padx=5)
    u_entry,usuario_r_var=entry_register(frame_register,'',0,6)
    
    mail_registro=tk.Label(frame_register,text='Email:',font=('San Francisco',15,'underline'))
    mail_registro.grid(row=7,column=0,sticky='w',padx=5)
    m_entry,mail_r_var=entry_register(frame_register,'ejemplo@gmail.com',0,8)
    
    password_registro=tk.Label(frame_register,text='Contraseña:',font=('San Francisco',15,'underline'))
    password_registro.grid(row=9,column=0,sticky='w',padx=5)
    p_entry,password_r_var=entry_register(frame_register,'(Mínimo 8 caracteres)',1,10)
    
    password_confirmar=tk.Label(frame_register,text='Confirmar contraseña:',font=('San Francisco',15,'underline'))
    password_confirmar.grid(row=11,column=0,sticky='w',padx=5)
    p_c_entry,password_conf_var=entry_register(frame_register,'',1,12)
    
    register_button=tk.Label(frame_register,text='Registrarse',font=('San Francisco',14),width=2,height=2,background='RoyalBlue2',fg='white',relief='raised',cursor='pointinghand')
    register_button.grid(row=14,column=0,sticky='ew',columnspan=3,pady=5)
    register_button.bind('<ButtonPress-1>',lambda event:register_button.config(width=2,height=2,background='RoyalBlue3', borderwidth=1, relief="raised"))
    register_button.bind('<ButtonRelease-1>',lambda event:verificar_datos_register(event,root_register,register_button,frame_register,nombre_r_var,apellido_r_var,usuario_r_var,mail_r_var,password_r_var,password_conf_var,n_entry,a_entry,u_entry,m_entry,p_entry,p_c_entry))
    register_button.bind('<Enter>',lambda event:register_button.config(background='RoyalBlue1'))
    register_button.bind('<Leave>',lambda event:register_button.config(background='RoyalBlue2'))
    
    
def entry_register(frame, titulo,i,fila):
    var = tk.StringVar()
    if i==1:
        entry = tk.Entry(frame, fg='grey', textvariable=var, width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2')
        entry.insert(0, titulo)
        entry.grid(row=fila, column=0, pady=3, ipady=10,columnspan=2,padx=7,ipadx=5)      
        
        imagen_tk_no_mostrar_pass = Imagenes('Imagenes/Oculta-Password.png')

        boton_mostrar = tk.Button(frame, image=imagen_tk_no_mostrar_pass, width=25, height=25, bd=0,command=lambda:mostrar_ocultar_Password(boton_mostrar,entry))
        boton_mostrar.image = imagen_tk_no_mostrar_pass 
        boton_mostrar.grid(row=fila,column=2,sticky='e',padx=10)
        boton_mostrar.grid_forget()
        entry.bind('<KeyRelease>',lambda event:verificar_entry(event,entry,titulo,boton_mostrar,fila,10))
            
    else:
        entry = tk.Entry(frame, fg='grey', textvariable=var,width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2')
        entry.insert(0, titulo)
        entry.grid(row=fila,column=0,pady=3,ipady=10,columnspan=2,padx=7,ipadx=5)
    entry.bind("<FocusIn>", lambda event: on_focus_in(event, entry, titulo,i))
    entry.bind("<FocusOut>", lambda event: on_focus_out(event, entry, titulo,i))
        
    return entry,var

def root_register_close(root_register,root):
    root_register.destroy()
    root.deiconify()
