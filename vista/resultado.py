import tkinter as tk

class VentanaEmergente:
    def __init__(self, parent,title):
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry("200x100")
        self.label = tk.Label(self.window, text="¡Hola, soy una ventana emergente!")
        self.label.pack(pady=20)

class Resultado:
    def __init__(self, parent, seleccionadas, enfermedades):
        self.parent = parent
        self.window = tk.Toplevel(self.parent.root)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.title("Resultados")
        self.window.geometry("500x400")

        if seleccionadas:
            tk.Label(self.window, text="Para los síntomas referidos:", font=("Arial", 14)).pack(pady=20)
            self.frame_seleccionadas = tk.Frame(self.window)
            self.frame_seleccionadas.pack(pady=10)

            # Crear un frame para contener la lista de síntomas seleccionados y la barra de desplazamiento
            frame_scroll = tk.Frame(self.frame_seleccionadas)
            frame_scroll.pack(side=tk.LEFT)

            # Crear un scrollbar para la lista
            scrollbar = tk.Scrollbar(frame_scroll)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Crear el Listbox para los síntomas seleccionados
            self.listbox_seleccionadas = tk.Listbox(frame_scroll, height=4, yscrollcommand=scrollbar.set)
            self.listbox_seleccionadas.pack(side=tk.LEFT, fill=tk.BOTH)
            scrollbar.config(command=self.listbox_seleccionadas.yview)

            # Agregar las etiquetas a la lista de síntomas seleccionados
            for i, opcion in enumerate(seleccionadas):
                self.listbox_seleccionadas.insert(i + 1, opcion.replace("_", " "))

        else:
            tk.Label(self.window, text="No referiste ningún síntoma", font=("Arial", 14)).pack(pady=20)


        if enfermedades:
            tk.Label(self.window, text="Se muestran las posibles enfermedades:", font=("Arial", 14)).pack(pady=20)
            self.frame_enfermedades = tk.Frame(self.window)
            self.frame_enfermedades.pack(pady=10)
            
            # Calcular el número de filas y columnas para los botones
            num_enfermedades = len(enfermedades)
            num_filas = (num_enfermedades + 2) // 3
            num_columnas = min(num_enfermedades, 3)
            
            # Crear los botones de enfermedades
            for i, enfermedad in enumerate(enfermedades):
                fila = i // num_columnas
                columna = i % num_columnas
                boton = tk.Button(self.frame_enfermedades, text=enfermedad.replace("_", " "))
                boton.grid(row=fila, column=columna, padx=5, pady=5)
                boton.bind("<Enter>", lambda event, enfermedad=enfermedad: self.mostrar_ventana(event, enfermedad))
                boton.bind("<Leave>", lambda event, enfermedad=enfermedad: self.cerrar_ventana(event, enfermedad))
        else:
            tk.Label(self.window, text="No se pudo determinar un diagnóstico.", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Cerrar", command=self.on_close).pack(pady=20)

    def on_close(self):
        print("Ejecuta close")
        self.parent.show_main_window("FALSE")
        self.window.destroy()
    
    def mostrar_ventana(self, event,enfermedad):
        titulo = f"Recomendaciones para {enfermedad}"
        self.ventana_emergente = VentanaEmergente(self.window,titulo)

    def cerrar_ventana(self, event,enfermedad):
        if hasattr(self, 'ventana_emergente'):
            self.ventana_emergente.window.destroy()
            del self.ventana_emergente

    def hacer_algo(self,color):
        print(f"Se ha seleccionado el color {color}")