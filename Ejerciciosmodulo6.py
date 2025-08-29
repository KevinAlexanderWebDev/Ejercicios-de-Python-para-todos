# Modulo 6: funciones
# Ejercicios prácticos
nombre = input("Escribe el nombre de entrada: ")
"""Escribe una función que reciba un nombre y devuelva un saludo."""


def nombre_entrada(nombre):
    apellido = input("Por favor escribe tu apellido: ")
    print(
        f"Hola {nombre} {apellido}, Bienvenido al módulo 6: funciones en python."
    )  # aplicamos una variable local y global para experimentar


nombre_entrada(nombre)
# Ejercicio número 2
"""Crea una función que calcule el área de un círculo (radio como parámetro)."""

radio = float(input("Escribe el radio del círculo: "))


def area_circulo(radio, exponente=2, pi=3.1416):
    return pi * (radio ** 2)


print(f"El área del círculo es: {area_circulo(radio, 2, 3.1416)}")

# Ejercicio númer 3
"""Haz una función que convierta grados Celsius a Fahrenheit."""

grados_celsius = float(input("Por favor ingresa la temperatura en grados celsius: "))


def conversor(grados_celsius):
    return (grados_celsius * 1.8) + 32


print(f"La temperatura convertida a grados Farenheit es: {conversor(grados_celsius)}°F")


# Ejercicio número 4
"""Escribe una función que reciba 2 números y devuelva el mayor."""
num_1 = int(input("Ingresa el primer número: "))

num_2 = int(input("Ingresa el segundo número: "))


def mayor_menor(num_1, num_2):
    if num_1 > num_2:
        return num_1
    elif num_2 == num_1:
        return "Error: Ambos +valores son idénticos"
    else:
        return num_2


resultado = mayor_menor(num_1, num_2)

print(f"El número más grande o mayor es: {resultado}")

# Ejercicio número 5
"""Función que reciba una lista de números y devuelva el promedio.
"""
num_lista = []

for i in range(3):
    numero = int(input(f"Por favor, agrega un número a la lista {i + 1}: "))
    num_lista.append(numero)


def devuelve_promedios(num_lista):
    total_lista = len(num_lista)
    sum_lista = sum(num_lista)
    return sum_lista / total_lista


promedio = devuelve_promedios(num_lista)

print(f"El promedio total de la lista es: {promedio}")

# Modulo 6: funciones
# Ejercicios prácticos
"""Escribe una función que reciba una lista y devuelva otra con los números pares.
"""
lista_numeros = []

for i in range(3):
    numero = int(input(f"Por favor, agrega un número a la lista {i + 1}: "))
    lista_numeros.append(numero)


def devuelve_pares(lista_numeros):
    num_pares = [num for num in lista_numeros if num % 2 == 0]
    return num_pares if num_pares else "No se encontraron números pares"


pares_devueltos = devuelve_pares(lista_numeros)
print(f"Los números pares de la lista son: {pares_devueltos}")

# Ejercicio número 7
"""Crea una función que reciba cualquier cantidad de números y devuelva la suma
"""

numeros = []

for i in range(2):

    cual_num = int(
        input(
            f"Agrega al menos una cantidad de 10 números que desees almacenar en una lista : {i + 1}"
        )
    )
    numeros.append(cual_num)


def recibe_numeros(cual_num):
    return sum(numeros)


# Ejercicio número 7
"""Crea una función que reciba cualquier cantidad de números y devuelva la suma
"""

numeros = []

print(
    "Instrucciones: Agrega un máximo de 10 números cualsea (Incluídos decimales), al final obtendrás su suma. "
)

for i in range(10):

    cual_num = float(input(f"Agregar {i + 1}: "))
    numeros.append(cual_num)


def recibe_numeros(numeros):
    print("Lista de números actual: ")
    for i, numero in enumerate(numeros, start=1):
        print(f"Lista: {i} - Número: {numero}")
    return sum(numeros)


suma = recibe_numeros(numeros)
print(f"La suma total de los números en la lista es: {suma}")

# Ejercicio 8:
"""Haz una función que reciba un texto y devuelva cuántas vocales tiene.
"""
texto = input("Escribe lo que quieras en sl siguiente espacio disponible: ")


def devuelve_vocales(texto):
    palabra = 0
    for letra in texto:
        if letra in "aeiou":
            palabra += 1
    return palabra


print(f"{devuelve_vocales}")

# Ejercicio 8:
"""Haz una función que reciba un texto y devuelva cuántas vocales tiene.
"""
texto = (
    input("Escribe lo que quieras en sl siguiente espacio disponible: ")
    .lower()
    .strip()
    .replace(" ", "")
)


def devuelve_vocales(texto):
    vocales = 0
    consonantes = 0
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío.")
    for letra in texto:
        if letra.isalpha():
            if letra in "aeiou":
                vocales += 1
            else:
                consonantes += 1
        else:
            raise ValueError("Error: Solo se aceptan valores alfabèticos. ")
    return vocales, consonantes


print(
    f"Devolviendo vocales y consonantes (Vocales, Consonantes): {devuelve_vocales(texto)}"
)

# Ejercicio 9
"""Función que reciba un diccionario de alumnos y calificaciones, y devuelva el promedio general."""
dic_alumnos = {}
promedios = dic_alumnos.values()
for i in range(3):
    alumno = input(f"Ingresa al primer alumno correspondiente {i + 1} : ")
    promedio = int(input(f"Ingresa el promedio {i + 1} correspondiente a {alumno}: "))
    dic_alumnos[alumno] = promedio
alumnos = dic_alumnos.keys()
alumnos_totales = len(alumnos)
print(alumnos_totales)


def devuelve_promedio(promedios):
    suma_general = sum(promedios)
    promedio_general = suma_general / alumnos_totales
    return promedio_general


promedio_general = devuelve_promedio(promedios)
print("\n📊 Para los alumnos registrados en la clase:\n")
for alumno, promedio in dic_alumnos.items():
    print(f"Alumno: {alumno} - Promedio: {promedio}")
print(f"Poseen un promedio como grupo de: {promedio_general}")

for i in range(3):
    alumno = input(f"Ingresa al primer alumno correspondiente {i + 1} : ")
    promedio = int(input(f"Ingresa el promedio correspondiente a {alumno} {i + 1}: "))
    dic_alumnos[alumno] = promedio
print(dic_alumnos)

# Ejercicio 10
"""Escribe una función que convierta una palabra a “mayúsculas alternadas”"""

palabra = input("Ingresa una palabra, cuál gustes: ").replace(" ", "").strip()


def convierte_mayusculasalternadas(palabra):
    resultado = ""
    for i, letra in enumerate(palabra):
        if i % 2 == 0:
            resultado += letra.upper()
        else:
            resultado += letra.lower()
    return resultado


palabra_alternada = convierte_mayusculasalternadas(palabra)
print(f"La palabra alteranda queda así: {palabra_alternada}")

# Ejercicio 11
"""Crea una función que reciba una lista de números y devuelva otra con los números sin repetir (sin usar set)."""

lista_numeros = []


def devuelve_sinrepetidos(lista_numeros):
    lista_sinrepetidos = []
    for numero in lista_numeros:
        if numero not in lista_sinrepetidos:
            lista_sinrepetidos.append(numero)
    return lista_sinrepetidos


for i in range(10):
    numero = int(
        input(f"A continuación, escribe un número entero cual sea -> {i + 1}: ")
    )
    lista_numeros.append(numero)

lista_unica = devuelve_sinrepetidos(lista_numeros)
print("\n📊 Lista sin repetidos:\n")
for i, numero in enumerate(lista_unica, start=1):
    print(f"{i} - Número: {numero}")


# Ejercicio 12
"""Escribe una función que reciba un número entero y devuelva si es primo o no."""

numero = int(input("Anota un número entero a continuación: "))


def devuelve_primoonoprimo(numero):
    if numero % 2 == 0:
        print("El número es primo👆")
    else:
        print("El número que proporcionas NO es primo❌")
    return numero


resultado = devuelve_primoonoprimo(numero)
print(resultado)

# Ejercicio 13
"""Función que reciba una frase y devuelva un diccionario con cada palabra y cuántas veces aparece.
"""

frase = input("Escribe una frase u oración, cual gustes: ").lower().strip()


def devuelve_diccionario(frase):
    signos = ",.;:¡!¿?()[]{}\"'"
    for s in signos:
        frase = frase.replace(s, "")  # Eliminamos signos
    palabras = frase.split()  # Separa la oración/frase en palabras
    diccionario_frase = {}

    for palabra in palabras:
        if palabra in diccionario_frase:
            diccionario_frase[palabra] += 1
        else:
            diccionario_frase[palabra] = 1
    return diccionario_frase


diccionario_devuelto = devuelve_diccionario(frase)
print("\n📊 Frecuencia de palabras:\n")
for palabra, cantidad in diccionario_devuelto.items():
    print(f"Palabra: {palabra} - Cantidad: {cantidad}")

# Ejercicio 14:
"""Haz una función que simule una calculadora básica: recibe 2 números y la operación ("suma", "resta", etc.).
"""


def devuelve_mensaje():
    print("¡Procedimiento realizado con éxito!🤩🥳")


lista_denumeros = []

diccionario_operaciones = {}

for i in range(2):
    números = float(
        input(
            "Anota dos números, los que quieras (incluídos decimales) y escoge qué operación deseas hacer: "
        )
    )
    lista_denumeros.append(números)


def calculadora_sencilla(lista_denumeros):
    suma = sum(lista_denumeros)
    diccionario_operaciones["Suma"] = suma
    resta = lista_denumeros[0] - lista_denumeros[1]
    diccionario_operaciones["Resta"] = resta
    multiplicacion = lista_denumeros[0] * lista_denumeros[1]
    diccionario_operaciones["Multiplicación"] = multiplicacion
    division = lista_denumeros[0] / lista_denumeros[1]
    diccionario_operaciones["División"] = division
    return diccionario_operaciones


resultados_devueltos = calculadora_sencilla(lista_denumeros)
devuelve_mensaje()
print("\n📊 Operaciones realizadas:\n")
for operacion, resultado in diccionario_operaciones.items():
    print(f"Operación: {operacion} - Resultado: {resultado}")

#Ejercicio 15
"""Escribe una función que reciba **kwargs de una persona (nombre, edad, ciudad, etc.) y lo muestre en formato bonito."""
usuario1= {}

nombre= input("Escribe el nombre del usuario: ")
usuario1["Nombre"]= nombre
edad= int(input("Escirbe la edad el usuario: "))
usuario1["Edad"]= edad
pais= input("Ingresa el país de origen de la persona: ")
usuario1["Pais"]= pais 

def devuelve_buenformato(**kwargs):
    print("\n📊 Información del usuario:\n")
    for clave, valor in kwargs.items(): 
        print(f"{clave} - {valor}")
        
formato_bonito= devuelve_buenformato(**usuario1)



        