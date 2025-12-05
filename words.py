# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.

def word_count(text, word):
    """Cuenta cuántas veces aparece una palabra en un texto."""
    words = text.split() # Divide el texto en palabras en una lista
    return words.count(word) # Cuenta las apariciones de la palabra en la lista