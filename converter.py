# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
def celsius_to_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9
