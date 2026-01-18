# Clase base Persona
# Aquí aplicamos ENCAPSULACIÓN y definimos una clase base

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # atributo privado (encapsulación)

    # Método getter para acceder al atributo privado
    def get_edad(self):
        return self.__edad

    # Método común que será sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.__edad} años."
