# 01_varialbes.py
# Ejemplos comentados que cumplen los 10 ejercicios solicitados.

# 1. Declara y asigna valores a las siguientes variables:
name = "Felix"           # una cadena con tu nombre
age = 30                 # un entero con tu edad
height = 1.75            # un flotante con tu altura (metros)

# Imprime cada variable en una línea separada
print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concaténala con texto
age_str = str(age)
print("Tienes " + age_str + " años.")

# 3. Declara una variable booleana is_student e imprímela
is_student = True  # usa True o False según corresponda
print(is_student)

# 4. Usa len() para calcular cuántos caracteres tiene tu nombre completo
full_name = name + " Gonzalez"  # nombre completo (ejemplo)
print(len(full_name))

# 5. Declara tres variables en una sola línea: nombre, apellido y ciudad. Luego imprímelas.
first_name, last_name, city = "Felix", "Gonzalez", "Madrid"
print(first_name)
print(last_name)
print(city)

# 6. Usa input() para solicitar al usuario su color favorito y almacénalo en color; luego imprímelo.
color = input("¿Cuál es tu color favorito? ")
print(color)

# 7. Declara una variable fruit, cámbiala y vuelve a imprimirla.
fruit = "manzana"
print(fruit)
fruit = "pera"
print(fruit)

# 8. Convierte un número decimal (price) a entero y luego imprímelo.
price = 19.99
price_int = int(price)
print(price_int)

# 9. Declara address_len con la cantidad de caracteres de una dirección usando len() e imprímela.
address = "Calle Falsa 123, Madrid"
address_len = len(address)
print(address_len)

# 10. Usa un tipo forzado para declarar phone como número, cámbialo y verifica el tipo con type().
phone = int(600123456)        # forzamos a int
print(phone)
phone = int("700987654")      # cambiamos su valor (también forzado)
print(phone)
print(type(phone))            # debe mostrar <class 'int'>