import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
DB_PATH = os.path.join(BASE_DIR, "mi_base.db")

def conectar():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    return conn, cursor

def crear_tabla():
    print(f"La base de datos se creará en: {DB_PATH}")  
    conn,cursor=conectar()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        usuario TEXT UNIQUE,
        email TEXT UNIQUE,
        contraseña TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def ingresar_usuario(nombre,apellido,usuario,email,password):
    conn,cursor=conectar()
    cursor.execute("INSERT INTO usuarios (nombre,apellido,usuario,email,contraseña) VALUES(?,?,?,?,?)",(nombre,apellido,usuario,email,password))
    conn.commit()
    cursor.close()

# conn,cursor=conectar()
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre TEXT NOT NULL,
#     apellido TEXT NOT NULL,
#     usuario TEXT UNIQUE,
#     email TEXT UNIQUE,
#     contraseña TEXT NOT NULL
# )
# """)

# conn.commit()
# conn.close()
# print("Base de datos creada correctamente")