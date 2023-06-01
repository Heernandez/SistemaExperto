import tkinter as tk
import time, sys,os

#RUTAS ARCHIVOS
RUTA_IMAGEN_DOCTOR = (os.path.abspath(os.path.join(os.path.dirname(__file__), 'doctor.png'))).replace("\\", "\\\\")
RUTA_IMAGEN_ALERTA = (os.path.abspath(os.path.join(os.path.dirname(__file__), 'alerta.png'))).replace("\\", "\\\\")
class MainView:
    def __init__(self,sisExp,sintomas):
        self.sisExp = sisExp
        self.opciones = sintomas
        self.root = tk.Tk()
        self.root.title("Doctor OnLine")
        self.root.geometry("500x400") # Fijar el tamaño de la ventana
        self.labelTitle = tk.Label(self.root, text='En Consulta con tu Doctor Virtual', font=("Arial", 40), wraplength=400)
        self.labelTitle.pack(side='top', anchor='center')
    
        self.seleccionadas = []

        self.label = tk.Label(self.root, text=self.opciones[0], font=("Arial", 20))
        self.label.pack(pady=20)
    
        self.contenedorBotones = tk.Frame(self.root)
        #self.contenedorBotones.pack()
        tk.Button(self.contenedorBotones, text="Sí", command=self.seleccionar_opcion, font=("Arial", 10), height=2, width=5).grid(row=0,column=0)
        tk.Button(self.contenedorBotones, text="No", command=self.siguiente_opcion, font=("Arial", 10), height=2, width=5).grid(row=0,column=1)
        # Centrar el contenedor en la pantalla
        self.contenedorBotones.pack(anchor=tk.CENTER)

        self.root.mainloop()

    def seleccionar_opcion(self):
        self.seleccionadas.append(self.opciones[0])
        print(self.opciones[0])
        self.siguiente_opcion()

    def siguiente_opcion(self):
        self.opciones = self.opciones[1:]
        if self.opciones:
            self.label.configure(text=self.opciones[0].replace("_"," "))
        else:
            self.label.configure(text="Procesando...")
            self.root.update()
            time.sleep(5) # Esperar 5 segundos
            self.root.withdraw()
            enfermedades = self.sisExp.preguntar_enfermedad(self.seleccionadas)
            ResultadosView(self.seleccionadas,enfermedades)

        self.root.update()


class ResultadosView:
    def __init__(self, seleccionadas, enfermedades):
        self.root = tk.Tk()
        self.root.title("Resultados")
        self.root.geometry("500x400") # Fijar el tamaño de la ventana
        if seleccionadas:
            tk.Label(self.root, text="Para los sintomas referidos:", font=("Arial", 14)).pack(pady=20)
            # Variable de control de la lista
            self.list_var = tk.StringVar(value=seleccionadas)
            # Lista
            self.listbox = tk.Listbox(self.root,  height=4)
            self.listbox.pack(pady=10)

            # Agregar elementos a la lista
            for i, opcion in enumerate(seleccionadas):
                self.listbox.insert(i+1, opcion.replace("_"," "))
        else:
            tk.Label(self.root, text="No referiste ningún sintoma", font=("Arial", 14)).pack(pady=20)
        # Mostrar lista de enfermedades o mensaje de error
        if enfermedades:
            tk.Label(self.root, text="Se muestran las posibles enfermedades:", font=("Arial", 14)).pack(pady=20)

            # Lista de enfermedades
            self.listbox_enfermedades = tk.Listbox(self.root, width=40, height=4)
            self.listbox_enfermedades.pack(pady=10)

            # Agregar elementos a la lista de enfermedades
            for i, enfermedad in enumerate(enfermedades):
                self.listbox_enfermedades.insert(i+1, enfermedad.replace("_"," "))

            # Definir ancho de las columnas
            
            # Desactivar selección de elementos de la lista
            # Deshabilitar la selección de elementos
            self.listbox_enfermedades.configure(selectmode="none")

        else:
            tk.Label(self.root, text="No se pudo determinar un diagnóstico.", font=("Arial", 14)).pack(pady=20)

        # Botón de cerrar
        tk.Button(self.root, text="Cerrar", command=self.cerrar).pack(pady=20)

        

        
    def cerrar(self):
        self.root.mainloop()
        self.root.destroy()
        sys.exit(0)
