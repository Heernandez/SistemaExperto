import tkinter as tk
from tkinter import ttk


def mouse_pasa(event, color):
    print(f"El mouse está pasando por el botón {color}")


def hacer_algo(color):
    print(f"Se ha seleccionado el color {color}")


ventana = tk.Tk()

contenedor = tk.Frame(ventana)
contenedor.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(contenedor)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lienzo = tk.Canvas(contenedor, yscrollcommand=scrollbar.set)
lienzo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lienzo.yview)

subventana = tk.Frame(lienzo)
subventana.pack()

colores = ['amarillo', 'azul', 'rojo', 'verde', 'naranja', 'violeta', 'negro', 'blanco']

# Configurar el número de columnas
num_columnas = 3

# Crear botones para cada elemento de la lista
for i, color in enumerate(colores):
    fila = i // num_columnas
    columna = i % num_columnas

    boton = tk.Button(subventana, text=color, command=lambda color=color: hacer_algo(color))
    boton.grid(row=fila, column=columna, padx=5, pady=5)
    boton.bind("<Enter>", lambda event, color=color: mouse_pasa(event, color))

lienzo.create_window(0, 0, anchor=tk.NW, window=subventana)

subventana.update_idletasks()
lienzo.config(scrollregion=lienzo.bbox("all"))

ventana.mainloop()

'''
import tkinter as tk
from tkinter import ttk


def mouse_pasa(event,color):
    print(f"El mouse está pasando por el boton {color} ")


def hacer_algo(color):
    print(f"Se ha seleccionado el color {color}")

ventana = tk.Tk()

# Crear un contenedor para los botones y la barra de desplazamiento
contenedor = tk.Frame(ventana)
contenedor.pack(fill=tk.BOTH, expand=True)

# Crear una barra de desplazamiento vertical
scrollbar = tk.Scrollbar(contenedor)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Crear un lienzo para contener los botones
lienzo = tk.Canvas(contenedor, yscrollcommand=scrollbar.set)
lienzo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configurar la barra de desplazamiento para desplazar el lienzo
scrollbar.config(command=lienzo.yview)

# Crear una subventana dentro del lienzo
subventana = tk.Frame(lienzo)
subventana.pack()

# Lista de colores de ejemplo
colores = ['amarillo', 'azul', 'rojo', 'verde', 'naranja', 'violeta', 'negro', 'blanco']

# Crear botones para cada elemento de la lista
for color in colores:
    boton = tk.Button(subventana, text=color, command=lambda color=color: hacer_algo(color))
    boton.pack(pady=5)
    boton.bind("<Enter>", lambda event,color=color: mouse_pasa(event,color))

# Configurar el lienzo para que contenga la subventana
lienzo.create_window(0, 0, anchor=tk.NW, window=subventana)

# Configurar el desplazamiento del lienzo
subventana.update_idletasks()
lienzo.config(scrollregion=lienzo.bbox("all"))

ventana.mainloop()

'''