import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv(".env")

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def capturar_credenciales():
    user = entry_usuario.get()
    password = entry_password.get()
    validar_credenciales(user, password)

def validar_credenciales(usuario, password):
    if usuario == APP_USER and password == APP_PASSWORD:
        mostrar_mensaje("Acceso correcto", "green")
    else:
        mostrar_mensaje("Usuario o contraseña incorrecta", "red")

def mostrar_mensaje(texto, color):
    label_resultado.config(text=texto, fg=color)

ventana = tk.Tk()
ventana.title("Practica 1: Validacion")
ventana.geometry("400x200")

# USANDO GRID

tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_password = tk.Entry(ventana, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

boton = tk.Button(ventana, text="Validar Acceso", command=capturar_credenciales)
boton.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=3, column=0, columnspan=2)

ventana.mainloop()
