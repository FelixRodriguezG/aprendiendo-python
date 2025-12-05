# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
num = int(input("Ingresa un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad (18 años o más) o menor de edad.
age = int(input("Ingresa tu edad: "))
if age >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")    
# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
string = input("Ingresa una cadena de texto: ")
if string == "":
    print("La cadena está vacía.")
else:
    print("La cadena no está vacía.")
# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2:
    print("El primer número es mayor.")
elif num2 > num1:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
num = int(input("Ingresa un número: "))
if num2 % 3 == 0 and num % 5 == 0:
    print("El número es divisible por 3 y por 5.")
else:
    print("El número no es divisible por 3 y por 5.")
# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
num= int(input("Ingresa un número: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
# 7. Escribe un programa que determine si una persona puede votar en función de su edad (mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.

age = int(input("Ingresa tu edad: "))
if age >= 18:
    print("Puedes votar.")
elif age == 16 or age == 17:
    print("Puedes votar con permiso especial.")
else:
    print("No puedes votar.")
    
# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
predefined_password = "pass12345"
user_password = input("Ingresa la contraseña: ")
if user_password == predefined_password:
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
num = int(input("Ingresa un número: "))
if 10 <= num <= 20:
    print("El número está entre 10 y 20.")
else:
    print("El número no está entre 10 y 20.")

# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color (rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
color = input("Ingresa un color (rojo, amarillo, verde): ").lower()
if color == "rojo":
    print("Detente.")
elif color == "amarillo":
    print("Está alerta.")
elif color == "verde":
    print("Avanza.")
else:
    print("Color no válido.")
