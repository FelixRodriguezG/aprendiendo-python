# 1. Crea un diccionario con las claves name, age y country, asignando valores a cada una. 
#    Imprime el diccionario.
my_dict = {"name": "Brais", "age": 37, "country": "Galicia"}
print(my_dict)

# 2. Accede al valor de la clave name en el diccionario.
print(my_dict["name"])
# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior.
#    Imprime el diccionario actualizado.
my_dict["job"] = "Programador"
print(my_dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38.
#    Imprime el diccionario actualizado.
my_dict["age"] = 38
print(my_dict)
# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dict["country"]
print(my_dict)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados
#    (ejemplo: 1: 1, 2: 4, ...).
squares_dict = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares_dict)
# 7. Verifica si la clave age está presente en el diccionario 
#    {"name": "Brais", "age": 37, "country": "Galicia"}. 
print("age" in my_dict)

# 8. Imprime solo las claves del diccionario.
print(my_dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
keys_list = list(my_dict.keys())
print(keys_list)
# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando 
#     fromkeys(), asignando a todas las claves el valor "Desconocido".
new_dict = dict.fromkeys(["name", "age", "job"], "Desconocido")
print(new_dict)
# 11. Elimina el diccionario creado en el punto anterior usando del y luego intenta imprimirlo
#     para ver el resultado.
del new_dict
# print(new_dict)  # Esto generará un error porque new_dict ha sido eliminado
# 12. Usa el método get() para acceder al valor de la clave job en el diccionario
#     {"name": "Brais", "age": 37, "country": "Galicia"}. Imprime el valor obtenido.
print(my_dict.get("job"))
# 13. Usa el método items() para imprimir los pares clave-valor del diccionario.
print(my_dict.items()[0])
# 14. Usa el método clear() para vaciar un diccionario y luego imprime su longitud.
my_dict.clear()
print(len(my_dict))