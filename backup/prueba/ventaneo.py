import tkinter as tk

class Ventana1:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.label = tk.Label(self.window, text="Ventana 1")
        self.label.pack()

    def on_close(self):
        self.parent.show_main_window()
        self.window.destroy()


class Ventana2:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.label = tk.Label(self.window, text="Ventana 2")
        self.label.pack()

    def on_close(self):
        self.parent.show_main_window()
        self.window.destroy()


class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")  # Ajusta el tamaño de la ventana principal
        self.root.title("Ventanas")

        self.ventana1 = Ventana1(self)
        self.ventana2 = Ventana2(self)

        self.show_ventana1()
        self.root.withdraw()
        self.ventana2.window.withdraw()  # Ocultar la ventana 2

        self.main_window = tk.Frame(self.root)
        self.main_window.pack()

    def show_main_window(self):
        self.ventana1.window.withdraw()
        self.ventana2.window.withdraw()
        self.main_window.pack()

    def show_ventana1(self):
        #self.main_window.pack_forget()
        self.ventana1.window.deiconify()

    def show_ventana2(self):
        #self.main_window.pack_forget()
        self.ventana2.window.deiconify()


if __name__ == "__main__":
    app = MainApplication()
    app.root.mainloop()
