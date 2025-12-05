# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.
import math
def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * radio ** 2

def area_cuadrado(lado):
    """Calcula el área de un cuadrado dado el lado."""
    return lado ** 2  
