import tkinter as tk

ventana = tk.Tk()

# Contenedor principal
contenedor_principal = tk.Frame(ventana)
contenedor_principal.pack()

# Primer Frame con la etiqueta
frame_etiqueta = tk.Frame(contenedor_principal)
frame_etiqueta.grid(row=0, column=0, padx=10, pady=10)

etiqueta = tk.Label(frame_etiqueta, text="Etiqueta")
etiqueta.pack()

# Segundo Frame con los botones
frame_botones = tk.Frame(contenedor_principal)
frame_botones.grid(row=0, column=1, padx=10, pady=10)

boton1 = tk.Button(frame_botones, text="Botón 1")
boton1.grid(row=0, column=0)

boton2 = tk.Button(frame_botones, text="Botón 2")
boton2.grid(row=0, column=1)

boton3 = tk.Button(frame_botones, text="Botón 3")
boton3.grid(row=1, column=0)

# Configurar el contenedor principal para que la columna 1 se expanda más que la columna 0
contenedor_principal.columnconfigure(1, weight=1)

ventana.mainloop()
