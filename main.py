# Archivo principal para ejecutar el programa

from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import mostrar_presentacion

def main():
    persona1 = Persona("Carlos", 40)
    estudiante1 = Estudiante("Valentina", 20, "Programación")

    mostrar_presentacion(persona1)
    mostrar_presentacion(estudiante1)

if __name__ == "__main__":
    main()
