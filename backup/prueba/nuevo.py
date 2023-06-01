import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
# Crear un Canvas como contenedor
canvas = tk.Canvas(root, width=200, height=500)
canvas.pack()

# Crear un Frame dentro del Canvas
frame = tk.Frame(canvas, bg="red")
canvas.create_window(0, 0,  window=frame)

# Establecer el tamaño del Frame
frame.config(width=1500, height=1500)

root.mainloop()

'''
import tkinter as tk
from functools import partial
from PIL import Image, ImageTk

# Cargar la imagen
imagen_inicial = Image.open("doctor.png")

# Tamaño de cada subimagen
ancho_subimagen = int(imagen_inicial.width / 4)
alto_subimagen = int(imagen_inicial.height / 3)

# Generar la lista de listas de subimágenes
lista_subimagenes = []
for y in range(0, imagen_inicial.height, alto_subimagen):
    fila_subimagenes = []
    for x in range(0, imagen_inicial.width, ancho_subimagen):
        subimagen = imagen_inicial.crop((x, y, x + ancho_subimagen, y + alto_subimagen))
        fila_subimagenes.append(subimagen)
    lista_subimagenes.append(fila_subimagenes)

def actualizar_imagen(fila, columna):
    subimagen_seleccionada = lista_subimagenes[fila][columna]
    imagen_tk = ImageTk.PhotoImage(subimagen_seleccionada)
    label_imagen.configure(image=imagen_tk)
    label_imagen.image = imagen_tk  # Mantener referencia al objeto PhotoImage

def accionBoton(parametro):
    print(parametro.get())
    return 10

def accionBotonExperimento(parametro):
    # parametro.icursor(2)
    print(parametro.index(tk.INSERT))

def accionCheckButton(estado, boton):
    if estado.get() == 1:
        boton.configure(state=tk.NORMAL)
    else:
        boton.configure(state=tk.DISABLED)

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("500x500")
root.title("CompuDoc")

# Variables
estatusCheck = tk.IntVar()

# Definición de widgets
tituloBienvenido = tk.Label(root, text="Bienvenido")
subtituloBienvenido = tk.Label(root, text="Este es tu médico en casa")
label_imagen = tk.Label(root)
campoNombre = tk.Entry(root)
boton = tk.Button(root, text="Continuar", relief="flat", overrelief="raised", state="disabled",
                  command=partial(accionBoton, campoNombre))
botonExperimento = tk.Button(root, text="Experimento", relief="groove",
                             command=partial(accionBotonExperimento, campoNombre))
checkAceptarCondiciones = tk.Checkbutton(root, text="Acepto los términos y condiciones",
                                         command=partial(accionCheckButton, estatusCheck, boton),
                                         variable=estatusCheck)

# Mostrar la subimagen inicial
imagen_inicial_tk = ImageTk.PhotoImage(lista_subimagenes[0][1])
label_imagen.configure(image=imagen_inicial_tk)
#label_imagen.image = imagen_inicial_tk  # Mantener referencia al objeto PhotoImage

# Agregar los widgets al área visual
tituloBienvenido.pack()
subtituloBienvenido.pack()
label_imagen.pack()
campoNombre.pack()
boton.pack()
botonExperimento.pack()
checkAceptarCondiciones.pack()

root.mainloop()
'''