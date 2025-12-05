# 1. Usa un bucle while para imprimir los números del 1 al 10.
number = 1
while number <= 10:
    print(number)
    number += 1


# 2. Usa un bucle for para recorrer la lista [10, 20, 30, 40, 50] e imprime cada número.
for num in [10, 20, 30, 40, 50]:
    print(num)
# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

i = 1
while i <= 100:
    print(i)    
    i += 1
# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
for char in "Python":
    print(char)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
num = 1
while num <= 50:
    if num % 7 == 0:
        print(num)
        break # Sale del bucle cuando encuentra el primer número divisible por 7
    num += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
for key in {"name": "Brais", "age": 37, "country": "Galicia"}:
    print(key)
# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.:
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista [30, 10, 30, 20, 30, 40].
count = 0
for num in [30, 10, 30, 20, 30, 40]:
    if num == 30:
        count += 1
print(count)
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
names = ["Ana", "Luis", "Brais", "Marta", "Carlos"]
for name in names:
    if name == "Brais":
        break
    print(name)