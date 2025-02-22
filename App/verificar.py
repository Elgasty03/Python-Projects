import tkinter as tk
from base_de_datos import conectar
from imagenes import Imagenes

def verificar_datos_inicio(event,mail,password,
                    boton,error,
                    entry_mail,entry_pass,
                    root,ubicacion,
                    boton_pass,
                    pass_title,mail_title):
    root.focus_set()
    boton.config(width=2,height=2,background='RoyalBlue2', borderwidth=1.9,relief='raised')
    conn,cursor=conectar()
    #inicio sesion
    if ubicacion==1:
        mail=mail.get().strip()
        cursor.execute('SELECT * FROM usuarios WHERE email=?',(mail,))
        usuario_encontrado=cursor.fetchone()
        if usuario_encontrado is None or usuario_encontrado[5]!=password.get().strip():
            root.geometry('365x315')
            if pass_title==entry_pass.get() or len(entry_pass.get())<8:
                entry_pass.config(fg='grey', width=35,relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0,insertbackground='black')
            else:
                entry_pass.config(fg='black', width=35,relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0,insertbackground='black')
            if mail_title==entry_mail.get():
                entry_mail.config(fg='grey', width=35,relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0,insertbackground='black')
            else:
                entry_mail.config(fg='black', width=35,relief='raised', background='gray99',
                        highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                        borderwidth=0,insertbackground='black')
            error.grid(row=5,column=0,sticky='ew',columnspan=3)
        else:
            boton_pass.grid_forget()
            error.grid_forget()
            # Resetear entry_mail
            entry_mail.delete(0, tk.END)
            titulo_m = 'ej: ejemplo@gmail.com'
            entry_mail.insert(0, titulo_m)
            entry_mail.config(fg='grey', width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2')

            # Resetear entry_pass
            entry_pass.delete(0, tk.END)
            titulo_p = '(Mínimo 8 caracteres)'
            entry_pass.insert(0, titulo_p)
            entry_pass.config(fg='grey', width=35,relief='raised', background='gray99',
                 highlightthickness=0.6, highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0,insertbackground='DodgerBlue2', show="")
            
            imagen_tk_mostrar_pass = Imagenes('Imagenes/Oculta-Password.png')
            boton_pass.config(image=imagen_tk_mostrar_pass)
            boton_pass.image = imagen_tk_mostrar_pass
            
            root.geometry('365x300')
            print('Iniciaste sesión correctamente.')
        
    conn.close()

def verificar_datos_register(event, root, boton, frame,
                              nombre, apellido, usuario, mail, password, confirm_password,
                              n_entry, a_entry, u_entry, m_entry, p_entry, p_c_entry):

    # Inicialización de errores
    conn, cursor = conectar()
    Error = False  # Variable para verificar si hay algún error
    
    # Crear el label de error fuera de la grilla, en la fila 2
    error_label = tk.Label(frame, text='', fg='red')
    error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Colocamos el label en la fila 2
    error_label.grid_forget()  # Ocultarlo inicialmente

    # Obtener los datos de los Entry
    nombre = nombre.get().strip()
    apellido = apellido.get().strip()
    usuario = usuario.get().strip()
    mail = mail.get().strip()
    password = password.get().strip()
    confirm_password = confirm_password.get().strip()

    # Verificación de nombre
    if nombre == '':
        Error = True
        n_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Campo vacío en nombre.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    else:
        reset_entry(n_entry)

    # Verificación de apellido
    if apellido == '':
        Error = True
        a_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Campo vacío en apellido.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    else:
        reset_entry(a_entry)

    # Verificación de usuario
    cursor.execute('SELECT * from usuarios WHERE usuario=?', (usuario,))
    usuario_obtenido = cursor.fetchone()
    if usuario_obtenido is not None:
        Error = True
        u_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Nombre de usuario ya existente.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    elif usuario == '':
        Error = True
        u_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Campo vacío en usuario.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    else:
        reset_entry(u_entry)

    # Verificación de email
    cursor.execute('SELECT * from usuarios WHERE email=?', (mail,))
    mail_obtenido = cursor.fetchone()
    if mail_obtenido is not None:
        Error = True
        m_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Email ya registrado.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    elif mail != 'ejemplo@gmail.com' and (mail[-10:] != '@gmail.com' and mail[-12:] != '@hotmail.com'):
        Error = True
        m_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Dominio incorrecto en email.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    elif mail == 'ejemplo@gmail.com':
        Error = True
        m_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Campo vacío en email.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    else:
        reset_entry(m_entry)

    # Verificación de contraseña
    if password != '(Mínimo 8 caracteres)' and len(password) < 8:
        Error = True
        p_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Contraseña muy corta.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    elif password != '(Mínimo 8 caracteres)' and password != confirm_password:
        Error = True
        p_c_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Las contraseñas no coinciden.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    elif password == '(Mínimo 8 caracteres)' and confirm_password == '':
        Error = True
        p_c_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Campo vacío en confirmar contraseña.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
        p_entry.config(fg='black', width=35, relief='raised', background='gray99',
                    highlightthickness=0.6, highlightbackground='red', highlightcolor='black',
                    borderwidth=0, insertbackground='black')
        error_label.config(text='Campo vacío en contraseña.', fg='red')
        error_label.grid(row=13, column=0, columnspan=2, sticky='w')  # Mostrar error
    else:
        reset_entry(p_entry)
        reset_entry(p_c_entry)

    # Si no hay errores y las contraseñas coinciden
    if not Error and password == confirm_password:
        cursor.execute('INSERT INTO usuarios (nombre, apellido, usuario, email, contraseña) VALUES (?,?,?,?,?)',
                       (nombre, apellido, usuario, mail, password))
        print('Registro Completado.')
        reset_entry(n_entry)
        reset_entry(a_entry)
        reset_entry(u_entry)
        reset_entry(m_entry)
        reset_entry(p_entry)
        reset_entry(p_c_entry)
        conn.commit()

    conn.close()


def reset_entry(entry):
    # Restablece la apariencia del Entry
    entry.config(fg='black', width=35, relief='raised', highlightbackground='gray77', highlightcolor='DodgerBlue2',
                 borderwidth=0, insertbackground='DodgerBlue2')
