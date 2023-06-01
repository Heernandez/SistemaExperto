import tkinter as tk

class Resultado:
    def __init__(self, parent, seleccionadas, enfermedades):
        self.parent = parent
        self.window = tk.Toplevel(self.parent.root)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.title("Resultados")
        self.window.geometry("500x400")

        if seleccionadas:
            tk.Label(self.window, text="Para los síntomas referidos:", font=("Arial", 14)).pack(pady=20)
            self.list_var = tk.StringVar(value=seleccionadas)
            self.listbox = tk.Listbox(self.window, height=4)
            self.listbox.pack(pady=10)
            for i, opcion in enumerate(seleccionadas):
                self.listbox.insert(i+1, opcion.replace("_", " "))
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
                boton.bind("<Enter>", lambda event, enfermedad=enfermedad: self.mouse_pasa(event, enfermedad))            
        else:
            tk.Label(self.window, text="No se pudo determinar un diagnóstico.", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.window, text="Cerrar", command=self.on_close).pack(pady=20)

    def on_close(self):
        print("Ejecuta close")
        self.parent.show_main_window("FALSE")
        self.window.destroy()
    
    
    def mouse_pasa(self,event, enfermedad):
        print(f"El mouse está pasando por el botón {enfermedad}")


    def hacer_algo(self,color):
        print(f"Se ha seleccionado el color {color}")