import tkinter as tk
from functools import partial
from PIL import Image,ImageTk
import os

#RUTAS ARCHIVOS
RUTA_IMAGEN_DOCTOR = (os.path.abspath(os.path.join(os.path.dirname(__file__), 'doctor.png'))).replace("\\", "\\\\")
RUTA_IMAGEN_ALERTA = (os.path.abspath(os.path.join(os.path.dirname(__file__), 'alerta.png'))).replace("\\", "\\\\")

#Ventana1
class Home:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        # Cargar la imagen
        self.imagenInicial = Image.open(RUTA_IMAGEN_DOCTOR)
        self.imagenElegida = None
        self.listaSubImagenes = []
        self.recorte_imagen()
        self.imagenElegida = self.listaSubImagenes[0][1]
        self.imagenPantalla2 = self.listaSubImagenes[2][2]
        self.imagenPantalla3 = self.listaSubImagenes[2][1]
        self.imagenPantalla4 = self.listaSubImagenes[2][2]
        self.imagenPantalla5 = self.listaSubImagenes[1][2]
        self.imagenAlerta = Image.open(RUTA_IMAGEN_ALERTA)
        self.imagenAlerta =  self.imagenAlerta.resize((50, 30))
        
        self.inicializa_screen()

    def get_imagen_2(self):
        return self.imagenPantalla2
    def get_imagen_3(self):
        return self.imagenPantalla3
    def get_imagen_4(self):
        return self.imagenPantalla4
    def get_imagen_5(self):
        return self.imagenPantalla5
    def on_close(self):
        print("Ejecuta close")
        self.window.destroy()
        self.parent.root.destroy()

    def inicializa_screen(self):
        self.window.resizable(width=False, height=False)
        self.window.geometry("500x500")
        self.window.title("CompuDoc")
        self.window.configure(background="#FFFFFF")
        #Variables
        estatusCheck = tk.IntVar()
        #Marco A
        marcoA= tk.Frame(self.window,width=500,height=500)
        marcoA.configure(background="#B0D2E3")
        marcoA.pack()
        tituloBienvenido = tk.Label(marcoA,text="CyberDoctor\n\nTu médico en casa",font=("Arial", 20),bg="#B0D2E3")
        self.figuraDoctor = ImageTk.PhotoImage(self.imagenElegida)
        labelImagen = tk.Label(marcoA,image=self.figuraDoctor,bg="#B0D2E3")
        tituloBienvenido.grid(row=0,column=0)
        labelImagen.grid(row=0,column=1)
        #marcoB
        marcoB = tk.Frame(self.window,pady=45)
        marcoB.configure(background="#FFFFFF")
        marcoB.pack()
        self.imagenAlerta = ImageTk.PhotoImage(self.imagenAlerta)
        textoDescriptivo = ("Esta es una aplicación que utiliza conocimientos especializados para ayudar a identificar y diagnosticar "+
                                "problemas o situaciones específicas. Estos sistemas están diseñados para emular el razonamiento humano y "+
                                "ofrecer recomendaciones o soluciones basadas en una serie de reglas o heurísticas predefinidas, "+
                                "sin embargo no reemplaza en su totalidad una consulta directa con un profesional de la salud, "+
                                "y su objetivo es generar, en base a un conocimiento suministrado, "+
                                "un análisis preliminar el cual debe ser verificado por un médico.")

        labelDescripcion = tk.Label(marcoB,text=textoDescriptivo,font=("Arial", 11), bg="white",wraplength=350,image=self.imagenAlerta, compound=tk.LEFT)
        boton = tk.Button(marcoB, text="Continuar",font=("Arial", 11), relief="flat",overrelief="raised",state="disabled", command=partial(self.accionBoton))
        checkAceptarCondiciones = tk.Checkbutton(marcoB, text="Acepto los términos y condiciones",font=("Arial", 11, "underline"), bg="white", command=partial(self.accionCheckButton,estatusCheck,boton),variable=estatusCheck)
        labelDescripcion.pack()
        checkAceptarCondiciones.pack()
        boton.pack()

    def accionBoton(self):
        print("Accion continuar")
        self.parent.show_main_window("SIGUIENTE1")
        self.window.destroy()

    def accionCheckButton(self,estado,boton):
        if(estado.get() == 1):
            boton.configure(state=tk.NORMAL)
        else:
            boton.configure(state=tk.DISABLED)

    def recorte_imagen(self):
        # Tamaño de cada subimagen
        anchoSubImagen = int(self.imagenInicial.width/4)
        altoSubImagen = int(self.imagenInicial.height/3)

        # Generar la lista de listas de subimágenes
        #self.listaSubImagenes = []
        for y in range(0, self.imagenInicial.height, altoSubImagen):
            
            filaSubImagenes = []
            for x in range(0, self.imagenInicial.width, anchoSubImagen):
                print(x,",",y)
                subimagen = self.imagenInicial.crop((x, y, x + anchoSubImagen, y + altoSubImagen))
                filaSubImagenes.append(subimagen)
            self.listaSubImagenes.append(filaSubImagenes)