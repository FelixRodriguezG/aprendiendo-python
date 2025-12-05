# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)
# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
print((100, 200, 300, 400, 500)[1])
# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
    # my_tuple[0] = 40  # Esto generará un error porque las tuplas son inmutables
# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
count_3 = (1, 2, 3, 3, 4, 5, 3).count(3)
print(count_3)
# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
find_index = ("Java", "Python", "JavaScript", "Python").index("Python")
print(find_index)
# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
concat_tuple = (1, 2, 3) + (4, 5, 6)
print(concat_tuple)
# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
sub_tuple = my_tuple[2:4]
# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
my_tuple2 = ("rojo", "verde", "azul")
my_list = list(my_tuple2)
my_list[1] = "amarillo"
my_tuple2 = tuple(my_list)
print(my_tuple2)
# 9. Elimina una tupla llamada `my_tuple` usando `del` y luego intenta imprimirla para ver el resultado.
del my_tuple
# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
single_element_tuple = (100,)  # tupla de un elemento; la coma es obligatoria, si no es una expresión entre paréntesis y devuelve un entero.    
print(type(single_element_tuple))