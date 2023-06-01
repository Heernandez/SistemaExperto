from pyswip import Prolog
import os,sys

# Obtiene la ruta absoluta del archivo base.pl
RUTA_BASE_CONOCIMIENTO = os.path.abspath(os.path.join(os.path.dirname(__file__), 'base.pl'))
# Reemplaza las barras invertidas con dobles barras invertidas
RUTA_BASE_CONOCIMIENTO = RUTA_BASE_CONOCIMIENTO.replace("\\", "\\\\")
class SistemaExperto:
    
    def __init__(self):
        # Carga el archivo de conocimiento en Prolog
        self.prolog = Prolog()
        self.prolog.consult(RUTA_BASE_CONOCIMIENTO)
    # Función para preguntar al usuario sobre un síntoma
    def preguntar_sintoma(self,sintoma):
        while True:
            respuesta = input(f"¿Tienes {sintoma}? (s/n) ")
            if respuesta.lower() == "s":
                return True
            elif respuesta.lower() == "n":
                return False
            else:
                print("Respuesta inválida. Intente de nuevo.")
                
    # Función para hacer en base  lista de sintomas obtener una posible enfermedad
    def preguntar_enfermedad(self,sintomas):
        # Busca una posible enfermedad que coincida con los síntomas
        consultaProlog = f"enfermedades_coincidentes({sintomas},EnfermedadesF)."
        for enfermedad in self.prolog.query(consultaProlog):
            resultadoA = enfermedad['EnfermedadesF']
            resultadoB = []
            for i in resultadoA:
                resultadoB.append(str(i.value))
            print(resultadoB)
            return resultadoB
        return None
    
    def preguntar_enfermedad_2(self):
        # Función para hacer preguntas al usuario y obtener una posible enfermedad
        sintomas = []
        for sintoma in self.prolog.query("sintoma(X)"):
            if self.preguntar_sintoma(sintoma["X"]):
                sintomas.append(sintoma["X"])
        # Busca una posible enfermedad que coincida con los síntomas
        consultaProlog = f"enfermedades_coincidentes({sintomas},EnfermedadesF)."
        for enfermedad in self.prolog.query(consultaProlog):
            resultadoA = enfermedad['EnfermedadesF']
            resultadoB = []
            for i in resultadoA:
                resultadoB.append(str(i.value))
            print(resultadoB)
            return resultadoB
        return None

    def obtenerSintomas(self):
        sintomas = []
        for sintoma in self.prolog.query("sintoma(X)"):
            sintomas.append(sintoma["X"])
        return sintomas

    def iniciarInferencia(self):
        a = self.prolog.query('iniciar_inferencia.')
        for e in a:
            print(a)
            break
        a.close()
        

#a = SistemaExperto()
#a.iniciarInferencia()
#sintomas = a.obtenerSintomas()
#a.preguntar_enfermedad_2()
