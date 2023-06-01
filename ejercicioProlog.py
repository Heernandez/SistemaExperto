from modelo.model import SistemaExperto
from vista.view import MainApplication
# Programa principal

if __name__ == '__main__':

    print("Bienvenido al sistema experto de diagnóstico de enfermedades.")
    sisExp = SistemaExperto()
    app = MainApplication(sisExp)
    app.root.mainloop()


