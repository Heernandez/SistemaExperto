import tkinter as tk
import time

class Consulta:
    def __init__(self, parent,sintomas):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.opciones = sintomas
        self.window.title("Doctor OnLine")
        self.window.geometry("500x400") # Fijar el tamaño de la ventana
        self.labelTitle = tk.Label(self.window, text='En Consulta con tu Doctor Virtual', font=("Arial", 40), wraplength=400)
        self.labelTitle.pack(side='top', anchor='center')
    
        self.seleccionadas = []

        self.label = tk.Label(self.window, text=self.opciones[0], font=("Arial", 20))
        self.label.pack(pady=20)
    
        self.contenedorBotones = tk.Frame(self.window)
        #self.contenedorBotones.pack()
        tk.Button(self.contenedorBotones, text="Sí", command=self.seleccionar_opcion, font=("Arial", 10), height=2, width=5).grid(row=0,column=0)
        tk.Button(self.contenedorBotones, text="No", command=self.siguiente_opcion, font=("Arial", 10), height=2, width=5).grid(row=0,column=1)
        # Centrar el contenedor en la pantalla
        self.contenedorBotones.pack(anchor=tk.CENTER)

    def seleccionar_opcion(self):
        self.seleccionadas.append(self.opciones[0])
        print(self.opciones[0])
        self.siguiente_opcion()

    def siguiente_opcion(self):
        self.opciones = self.opciones[1:]
        if self.opciones:
            self.label.configure(text=self.opciones[0].replace("_"," "))
            self.window.update()
        else:
            self.label.configure(text="Procesando...")
            time.sleep(1) # Esperar 5 segundos
            self.parent.show_main_window("SIGUIENTE2",self.seleccionadas)
            
            self.window.destroy()
        #self.window.update()
    
    def on_close(self):
        print("Ejecuta close")
        self.window.destroy()
        self.parent.show_main_window("FALSO")
        