# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
        
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()