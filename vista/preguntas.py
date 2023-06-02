import tkinter as tk
import time
from PIL import Image,ImageTk
from functools import partial

class Consulta:
    def __init__(self, parent,sintomas,imagen):
        self.imagen = imagen
        self.parent = parent
        self.window = tk.Toplevel(parent.root,bg="#B0D2E3")
        

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.opciones = sintomas
        self.window.title("Preguntas de rutina.")
        self.window.geometry("500x400") # Fijar el tamaño de la ventana
        self.labelTitle = tk.Label(self.window, text='¿En los últimos días has sentido ...?', font=("Arial", 30), wraplength=400)
        self.labelTitle.pack(side='top', anchor='center')
    
        self.seleccionadas = []

        self.label = tk.Label(self.window, text=self.opciones[0], font=("Arial", 20))
        self.label.pack(pady=20)
        
        self.figuraDoctor = ImageTk.PhotoImage(self.imagen)
        self.labelImagen = tk.Label(self.window,image=self.figuraDoctor,bg="#B0D2E3")
        self.labelImagen.pack()
        self.contenedorBotones = tk.Frame(self.window)
        self.contenedorBotones.pack(anchor=tk.CENTER)
        self.botonSi = tk.Button(self.contenedorBotones, text="Sí", command=partial(self.seleccionar_opcion), font=("Arial", 10), height=2, width=5)
        self.botonNo = tk.Button(self.contenedorBotones, text="No", command=partial(self.siguiente_opcion), font=("Arial", 10), height=2, width=5)
        self.botonSi.grid(row=0,column=0)
        self.botonNo.grid(row=0,column=1)
        # Centrar el contenedor en la pantalla
        #self.contenedorBotones.pack(anchor=tk.CENTER)

    def seleccionar_opcion(self):
        if(len(self.opciones) > 0):
            elegido = self.opciones[0]
            self.seleccionadas.append(elegido)
        else:
            self.botonSi.config(state=tk.DISABLED)
            self.botonNo.config(state=tk.DISABLED)
            #print(f"Lista vacia  len:{len(self.opciones)}  data {self.opciones} ")
        self.siguiente_opcion()
        

    def siguiente_opcion(self):
        #print(self.opciones, len(self.opciones))
        self.opciones = self.opciones[1:]
        if(len(self.opciones) > 0):
            self.label.configure(text=self.opciones[0].replace("_"," "))
            self.window.update()  
        else:
            self.botonSi.config(state=tk.DISABLED)
            self.botonNo.config(state=tk.DISABLED)
            #print(f"No pudo partir mas la lista. len:{len(self.opciones)}  data {self.opciones} ")
            self.label.configure(text="Procesando...")
            time.sleep(3) # Esperar 5 segundos
            self.parent.show_main_window("SIGUIENTE2",self.seleccionadas)
            
            self.window.destroy()
        #self.window.update()
    
    def on_close(self):
        #print("Ejecuta close")
        self.window.destroy()
        self.parent.show_main_window("FALSO")
        