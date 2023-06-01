import tkinter as tk

class Resultado:

    def __init__(self, parent,seleccionadas,enfermedades):
        self.parent = parent
        self.window = tk.Toplevel(self.parent.root)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.title("Resultados")
        self.window.geometry("500x400") # Fijar el tamaño de la ventana
        if seleccionadas:
            tk.Label(self.window, text="Para los sintomas referidos:", font=("Arial", 14)).pack(pady=20)
            # Variable de control de la lista
            self.list_var = tk.StringVar(value=seleccionadas)
            # Lista
            self.listbox = tk.Listbox(self.window,  height=4)
            self.listbox.pack(pady=10)

            # Agregar elementos a la lista
            for i, opcion in enumerate(seleccionadas):
                self.listbox.insert(i+1, opcion.replace("_"," "))
        else:
            tk.Label(self.window, text="No referiste ningún sintoma", font=("Arial", 14)).pack(pady=20)
        # Mostrar lista de enfermedades o mensaje de error
        if enfermedades:
            tk.Label(self.window, text="Se muestran las posibles enfermedades:", font=("Arial", 14)).pack(pady=20)

            # Lista de enfermedades
            self.listbox_enfermedades = tk.Listbox(self.window, width=40, height=4)
            self.listbox_enfermedades.pack(pady=10)

            # Agregar elementos a la lista de enfermedades
            for i, enfermedad in enumerate(enfermedades):
                self.listbox_enfermedades.insert(i+1, enfermedad.replace("_"," "))

            # Definir ancho de las columnas
            
            # Desactivar selección de elementos de la lista
            # Deshabilitar la selección de elementos
            self.listbox_enfermedades.configure(selectmode="none")

        else:
            tk.Label(self.window, text="No se pudo determinar un diagnóstico.", font=("Arial", 14)).pack(pady=20)

        # Botón de cerrar
        tk.Button(self.window, text="Cerrar", command=self.on_close).pack(pady=20)


    def on_close(self):
        print("Ejecuta close")
        self.parent.show_main_window("FALSE")
        self.window.destroy()