import tkinter as tk
from .principal import Home
from .preguntas import Consulta
from .resultado import Resultado


class MainApplication:
    def __init__(self,sisExp):
        self.root = tk.Tk()
        self.root.geometry("400x300")  # Ajusta el tamaño de la ventana principal
        self.root.title("Ventanas")
        self.main_window = tk.Frame(self.root)

        self.sisExp = sisExp

        self.ventana1 = Home(self)
        self.ventana2 = None
        self.ventana3 = None
        #self.show_ventana1()
        self.root.withdraw()

        self.main_window = tk.Frame(self.root)
        self.main_window.pack()
        

    def show_main_window(self,accion="FALSO",seleccion=[]):
        print("Se ejecuta principal : {}".format(accion))
        if(accion =="FALSO"):
            self.show_ventana1()
            
        elif(accion =="SIGUIENTE1"):
            self.show_ventana2()

        elif(accion == "SIGUIENTE2"):
            print("respondió todo")
            self.show_ventana3(seleccion)
        else:
            self.show_ventana1()



    def show_ventana1(self):
        print("Se ejecuta ventana 1")
        try:
            self.main_window.pack_forget()
            self.ventana2.window.withdraw()
            self.ventana3.window.withdraw()
        except:
            print("rompe 1")
        self.ventana1 = Home(self)  # Crea una nueva instancia de Ventana2
        self.ventana1.window.deiconify()

    def show_ventana2(self):
        print("Se ejecuta ventana 2")
        try:
            self.main_window.pack_forget()
            self.ventana1.window.withdraw()
            self.ventana3.window.withdraw()
        except:
            print("rompe 2")
        self.ventana2 = Consulta(self,self.sisExp.obtenerSintomas())  # Crea una nueva instancia de Ventana2
        self.ventana2.window.deiconify()

    def show_ventana3(self,seleccion):
        print("Se ejecuta ventana 3")
        try:
            self.main_window.pack_forget()
            self.ventana1.window.withdraw()
            self.ventana2.window.withdraw()
        except:
            print("rompe 3")
        
        enf = self.sisExp.preguntar_enfermedad(seleccion)
        cu  = self.sisExp.obtenerListaCuidados(enf)
        rec = self.sisExp.obtenerListaRecomendaciones(enf)
        self.ventana3 = Resultado(self,seleccion,enfermedades=enf,cuidados=cu,recomendaciones=rec)  # Crea una nueva instancia de Ventana2
        self.ventana3.window.deiconify()
        

if __name__ == "__main__":
    app = MainApplication()
    app.root.mainloop()
