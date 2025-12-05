# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.
import calculator
result_sum = calculator.sumar(10, 5)
result_subtract = calculator.restar(10, 5)
result_multiply = calculator.multiplicar(10, 5)
result_divide = calculator.dividir(10, 5)
print(f"Suma: {result_sum}")
print(f"Resta: {result_subtract}")
print(f"Multiplicación: {result_multiply}")
print(f"División: {result_divide}")

# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C son {fahrenheit}°F")
fahrenheit = 77
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F son {celsius}°C")

# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.
from students_list import print_students
print("Lista de estudiantes:")
print_students()

# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.

from geometry import area_circulo, area_cuadrado
radio = 5
area_circ = area_circulo(radio)
print(f"Área del círculo con radio {radio}: {area_circ}")
lado = 4
area_cuad = area_cuadrado(lado)
print(f"Área del cuadrado con lado {lado}: {area_cuad}")

# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.
import sum
total = sum.sumar_numeros(1, 2, 3, 4, 5)
print(f"La suma de los números es: {total}")

# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".
from Car import Car
mi_auto = Car("Toyota", "Corolla", 2020)
print(f"Mi auto es un {mi_auto.year} {mi_auto.brand} {mi_auto.model}")

# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.
from utils_file import write_to_file, read_from_file
filename = "ejemplo.txt"
data_to_write = "Hola, este es un ejemplo de escritura en un archivo."
write_to_file(filename, data_to_write)
read_data = read_from_file(filename)
print(f"Datos leídos del archivo: {read_data}")

# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.
from stadistics import average, median
numbers = [10, 20, 30, 40, 50]
media = average(numbers)
mediana = median(numbers)
print(f"Media: {media}")
print(f"Mediana: {mediana}")

# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.
from words import word_count
texto = "Hola esto es un texto de ejemplo. Hola a todos. Hola!"
palabra = "hola"
conteo = word_count(texto, palabra)
print(f"La palabra '{palabra}' aparece {conteo} veces en el texto.")


# 10. Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.
from dates import get_current_date, date_difference
from datetime import datetime
fecha_actual = get_current_date()
print(f"Fecha actual: {fecha_actual}")
fecha1 = datetime(2022, 1, 1)
fecha2 = datetime(2023, 1, 1)
diferencia = date_difference(fecha1, fecha2)
print(diferencia)
print(f"Diferencia entre {fecha1.date()} y {fecha2.date()}: {diferencia} días")