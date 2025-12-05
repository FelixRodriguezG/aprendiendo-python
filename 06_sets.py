# 1. Crea un set con los números del 1 al 5 e imprímelo.
my_set = {1, 2, 3, 4, 5} 
print(my_set)
# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
my_set.add(6)
print(my_set)
# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5}
# nuevamente. ¿Qué sucede?
my_set.add(5)  # No se añade porque los sets no permiten duplicados
print(my_set)
# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e
# imprime el resultado.
print(3 in my_set)
# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el
# set resultante.
my_set.remove(4)
print(my_set)
# 6. Usa el método clear() para vaciar un set y luego imprime
# su longitud.
my_set.clear()
print(len(my_set))
# 7. Convierte el set {"manzana", "naranja", "plátano"} en
# una lista e imprime el primer elemento de la lista.
fruit_set = {"manzana", "naranja", "plátano"}
fruit_list = list(fruit_set)
print(fruit_list[0])
# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e
# imprime el set resultante.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print(union_set)
# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3,
# 4, 5, 6} e imprime el resultado.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
difference_set = set_a.difference(set_b)
print(difference_set)
# 10. Elimina un set llamado my_set usando del y luego
# intenta imprimirlo para ver el resultado.
del my_set
# print(my_set)  # Esto generará un error porque my_set ha sido eliminado