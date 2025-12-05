# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
    # *args permite recibir un número variable de argumentos y los trata como una tupla.
def sumar_numeros(*args): 
    """Devuelve la suma de todos los argumentos proporcionados."""
# sum es una función incorporada de Python que suma los elementos de un iterable.
    return sum(args) 