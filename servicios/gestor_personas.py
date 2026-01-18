# Lógica del sistema
# Aquí se manejan las personas y estudiantes

def mostrar_presentacion(persona):
    # Polimorfismo: no importa el tipo de objeto,
    # el método presentarse se comporta según la clase
    print(persona.presentarse())
