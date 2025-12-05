# 1. Crea una función que intente dividir dos números proporcionados por el usuario. 
#    Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    else:
        return result
# 2. Crea una función que tome una cadena e intente convertirla en un número entero. 
#    Usa try-except para capturar cualquier error en la conversión (ValueError).

def convert_to_int(string):
    try:
        number = int(string)
    except ValueError:
        return "Error: La cadena no se puede convertir a entero."
    else:
        return number
# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores 
#    (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones 
#    de archivos de forma segura.
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return "Error: Archivo no encontrado."
    else:
        return content

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) 
#    con dos números. Usa try-except-else-finally para manejar errores y asegurar que se 
#    imprima un mensaje final, independientemente de los errores.
def multiple_operations(num1, num2):
    try:
        suma = num1 + num2
        resta = num1 - num2
        division = num1 / num2
        multiplicacion = num1 * num2
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    else:
        return {
            "suma": suma,
            "resta": resta,
            "division": division,
            "multiplicacion": multiplicacion
        }
    finally:
        print("Operaciones completadas.")   

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada 
#    no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada 
#    y lanzar excepciones cuando sea necesario.
def ask_age():
    age_input = input("Por favor, ingresa tu edad: ")   
    try:
        age = int(age_input)
        if age < 0:
            raise ValueError("La edad no puede ser negativa.")
    except ValueError as value_err:
        return f"Error: {value_err}"
    else:
        return f"Tienes {age} años."

# 6. Crea una función que intente acceder a un elemento de una lista por índice. 
#    Usa try-except para manejar el caso donde el índice esté fuera de rango (IndexError).
def access_list_element(my_list, index):
    try:
        element = my_list[index]
    except IndexError:
        return "Error: Índice fuera de rango."
    else:
        return element

# 7. Crea una función que use try-except para manejar múltiples excepciones: 
#    ZeroDivisionError, ValueError y TypeError.
def multiple_excptions(num1, num2):
    try:
        result = num1 / num2
        int_result = int(result)
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except ValueError:
        return "Error: No se puede convertir el resultado a entero."
    except TypeError:
        return "Error: Tipo de dato incorrecto."
    else:
        return int_result

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada 
#    llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.
class InsufficientFundsError(Exception):
    pass
def withdraw_funds(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Fondos insuficientes para completar la transacción.")
    else:
        balance -= amount
        return balance  

# 9. Crea una función que intente convertir una lista de cadenas en enteros. 
#    Maneja cualquier error (ValueError) que surja cuando una cadena no pueda convertirse.
def convert_list_to_int(string_list):
    int_list = []
    for string in string_list:
        try:
            number = int(string)
            int_list.append(number)
        except ValueError:
            return f"Error: La cadena '{string}' no se puede convertir a entero."
    return int_list    

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError 
#     si el número es negativo.
import math
def calculate_square_root(number):
    try:    
        if number < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    except ValueError as ve:
        return f"Error: {ve}"
    else:
        return math.sqrt(number)
