# Clase derivada Estudiante
# Aplica HERENCIA y POLIMORFISMO

from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Método sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre}, estudio {self.carrera} y tengo {self.get_edad()} años."
