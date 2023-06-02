import tkinter as tk

class VentanaEmergente:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Ventana Emergente")
        self.window.geometry("200x100")
        self.label = tk.Label(self.window, text="¡Hola, soy una ventana emergente!")
        self.label.pack(pady=20)

class Resultado:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Resultados")
        self.window.geometry("500x400")

        self.boton = tk.Button(self.window, text="Mostrar Ventana", width=15)
        self.boton.pack(pady=20)
        self.boton.bind("<Enter>", self.mostrar_ventana)
        self.boton.bind("<Leave>", self.cerrar_ventana)

    def mostrar_ventana(self, event):
        self.ventana_emergente = VentanaEmergente(self.window)

    def cerrar_ventana(self, event):
        if hasattr(self, 'ventana_emergente'):
            self.ventana_emergente.window.destroy()
            del self.ventana_emergente

    def run(self):
        self.window.mainloop()

resultado = Resultado()
resultado.run()
