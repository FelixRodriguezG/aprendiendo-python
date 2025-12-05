# 1. Declara una variable `text` con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando `len()`.
text = "Aprendiendo Python"
print(len(text))
# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
greeting = "Hola" + " " + "Python"
print(greeting)
# 3. Crea una cadena que incluya un salto de línea y luego imprímela para ver el resultado.
multi_line = "Primera línea\nSegunda línea"
print(multi_line)
# 4. Usa el formateo de cadenas con *f-strings* para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre = "Felix"
apellido = "Gonzalez"
edad = 43
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años.")
# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
a, b, c, d, e, f = "Python"
print(a)
print(b) 
print(c)
print(d)
print(e)
print(f)       
# 6. Extrae un *slice* de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
slice_text = "Programacion"[3:8]
print(slice_text)
# 7. Invierte la cadena “Python” usando *slicing* y muestra el resultado.
inverted = "Python"[::-1]
print(inverted)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela. 
upper_text = "aprendiendo python".upper()
print(upper_text)

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
count_n = "Programación en Python".count("n")
print(count_n)

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resu=ltado.
is_numeric = "12345".isnumeric()
print(is_numeric)