import tkinter as tk
from tkinter import ttk
import time

# Variables globales para controlar la velocidad y la pausa
velocidad = 1.0  # Velocidad predeterminada
pausa = False

def mostrar_palabras():
    global pausa
    texto = entrada_texto.get("1.0", "end-1c")
    palabras = texto.split()
    
    for palabra in palabras:
        if pausa:
            while pausa:  # Espera hasta que se reanude
                ventana.update()
                time.sleep(0.1)
        etiqueta.config(text=palabra)
        ventana.update()
        time.sleep(1 / velocidad)  # Usar velocidad personalizada

def pausar_o_reanudar():
    global pausa
    pausa = not pausa
    if pausa:
        boton_pausar.config(text="Reanudar")
    else:
        boton_pausar.config(text="Pausar")

def actualizar_velocidad():
    global velocidad
    velocidad = float(velocidad_var.get())

ventana = tk.Tk()
ventana.geometry("600x500")
ventana.title("Lector de Texto")

etiqueta = tk.Label(ventana, text="", font=("Helvetica", 34))
etiqueta.pack(pady=20)

entrada_texto = tk.Text(ventana, height=15, width=60)
entrada_texto.pack(pady=10)

boton_mostrar = tk.Button(ventana, text="Mostrar Palabras", command=mostrar_palabras)
boton_mostrar.pack()

boton_pausar = tk.Button(ventana, text="Pausar", command=pausar_o_reanudar)
boton_pausar.pack()

# Configuración de la ventana de velocidad
etiqueta_velocidad = tk.Label(ventana, text="Velocidad:")
etiqueta_velocidad.pack()

velocidad_var = tk.StringVar(value=str(velocidad))
entrada_velocidad = ttk.Entry(ventana, textvariable=velocidad_var)
entrada_velocidad.pack()

boton_actualizar_velocidad = ttk.Button(ventana, text="Actualizar", command=actualizar_velocidad)
boton_actualizar_velocidad.pack()

texto_a_mostrar = """
# Tu texto aquí...
"""

entrada_texto.insert("1.0", texto_a_mostrar)

ventana.mainloop()

#presionar f5 para ejecutar la aplicacion.




