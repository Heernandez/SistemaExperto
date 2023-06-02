import tkinter as tk
from PIL import Image,ImageTk
class VentanaEmergente:
    def __init__(self, parent, title, cuidados, recomendaciones):
        self.window = tk.Toplevel(parent,bg="#B0D2E3")
        self.window.title(title)
        
        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=10)

        # Parte de los cuidados
        tk.Label(frame, text="Cuidados", font=("Arial", 14)).pack(pady=10)
        cuidados_text = tk.Message(frame, text="\n".join(cuidados), width=300)
        cuidados_text.pack(pady=5)

        # Parte de las recomendaciones
        tk.Label(frame, text="Recomendaciones", font=("Arial", 14)).pack(pady=10)
        recomendaciones_text = tk.Message(frame, text="\n".join(recomendaciones), width=300)
        recomendaciones_text.pack(pady=5)

        # Redimensionar la ventana en altura según el contenido
        self.window.geometry(f"400x{self.window.winfo_reqheight()+100}")

class Resultado:
    def __init__(self, parent, seleccionadas, enfermedades,cuidados,recomendaciones,imagen,imagen2,imagen3):
        self.imagen = imagen
        self.imagen2 = imagen2
        self.imagen3 = imagen3
        self.parent = parent
        self.window = tk.Toplevel(self.parent.root,bg="#B0D2E3")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.title("Resultados")
        self.window.geometry("500x400")
        self.cu = cuidados
        self.rec = recomendaciones
        #print(enfermedades)

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
            tk.Label(self.window, text="Se muestran las posibles enfermedades", font=("Arial", 14)).pack(pady=20)
            
            # Contenedor principal
            self.contenedor_principal = tk.Frame(self.window,bg="#B0D2E3")
            self.contenedor_principal.pack()

            self.frame_imagen = tk.Frame(self.contenedor_principal)
            self.frame_imagen.grid(row=0, column=0, padx=10, pady=10)

            self.figuraDoctor = ImageTk.PhotoImage(self.imagen)
            self.labelImagen = tk.Label(self.frame_imagen,image=self.figuraDoctor,bg="#B0D2E3")
            self.labelImagen.pack()


            self.frame_enfermedades = tk.Frame(self.contenedor_principal,bg="#B0D2E3")
            self.frame_enfermedades.grid(row=0, column=1, padx=10, pady=10)
            # Calcular el número de filas y columnas para los botones
            num_enfermedades = len(enfermedades)
            num_filas = (num_enfermedades + 2) // 3
            num_columnas = min(num_enfermedades, 3)
            
            # Crear los botones de enfermedades
            for i, enfermedad in enumerate(enfermedades):
                fila = i // num_columnas
                columna = i % num_columnas
                boton = tk.Button(self.frame_enfermedades,command=lambda enfermedad=enfermedad: self.onclickBoton(enfermedad), text=enfermedad.replace("_", " "))
                boton.grid(row=fila, column=columna, padx=5, pady=5)
                #boton.bind("<Enter>", lambda event, enfermedad=enfermedad: self.mostrar_ventana(event, enfermedad))
                #boton.bind("<Leave>", lambda event, enfermedad=enfermedad: self.cerrar_ventana(event, enfermedad))
            
            self.contenedor_principal.columnconfigure(1, weight=1)
        else:
            if seleccionadas:
                tk.Label(self.window, text="No se pudo determinar un diagnóstico.", font=("Arial", 14)).pack(pady=20)
                self.figuraDoctor = ImageTk.PhotoImage(self.imagen3)
                self.labelImagen = tk.Label(self.window,image=self.figuraDoctor,bg="#B0D2E3")
                self.labelImagen.pack()
            else:
                #tk.Label(self.window, text="No se pudo determinar un diagnóstico.", font=("Arial", 14)).pack(pady=20)
                self.figuraDoctor = ImageTk.PhotoImage(self.imagen2)
                self.labelImagen = tk.Label(self.window,image=self.figuraDoctor,bg="#B0D2E3")
                self.labelImagen.pack()

        tk.Button(self.window, text="Cerrar", command=self.on_close).pack(pady=20)

    def on_close(self):
        #print("Ejecuta close")
        self.parent.show_main_window("FALSE")
        self.window.destroy()
    
    def mostrar_ventana(self, event,enfermedad):
        #cuidados = ["Descansar", "Tomar medicamentos", "Mantenerse hidratado"]
        #recomendaciones = ["Evitar actividades extenuantes", "Seguir las indicaciones del médico"]
        cuidados = self.cu[enfermedad]
        recomendaciones = self.rec[enfermedad]
        titulo = f"Recomendaciones para {enfermedad}"
        self.ventana_emergente = VentanaEmergente(self.window,titulo,cuidados,recomendaciones)
    
    def onclickBoton(self,enfermedad):
        #cuidados = ["Descansar", "Tomar medicamentos", "Mantenerse hidratado","Dormir a buena hora","Descansar", "Tomar medicamentos", "Mantenerse hidratado","Dormir a buena hora"]
        #recomendaciones = ["Evitar actividades extenuantes", "Seguir las indicaciones del médico","Tomar medicamento a la hora","Evitar actividades extenuantes", "Seguir las indicaciones del médico","Tomar medicamento a la hora"]
        cuidados = self.cu[enfermedad]
        recomendaciones = self.rec[enfermedad]
        titulo = f"Recomendaciones para {enfermedad}"
        self.ventana_emergente = VentanaEmergente(self.window,titulo,cuidados,recomendaciones)

    def cerrar_ventana(self, event,enfermedad):
        if hasattr(self, 'ventana_emergente'):
            self.ventana_emergente.window.destroy()
            del self.ventana_emergente

    def hacer_algo(self,color):
        print(f"Se ha seleccionado el color {color}")