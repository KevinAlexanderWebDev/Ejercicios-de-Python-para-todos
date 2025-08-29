# Ejercicios Finales del modulo 6.

nombre = input("Escribe a continuación tu nombre completo: ").strip().replace(" ", "")


def devuelve_saludo(nombre):
    saludo = f"¡Hola {nombre} bienvenido a los ejercicios finales del módulo 6 de Python 'Funciones'!"
    return saludo


print(devuelve_saludo(nombre))

# Ejercicio Número 2 "Suma con función".
"""Crea una función suma(a, b) que reciba dos números y regrese su suma. Pide al usuario los dos números y muestra el resultado."""
print("Operadora de sumas")
a = int(input("Escribe un número entero: "))
b = int(input("Escribe el segundo número a sumar: "))


def devuelve_suma(a, b):
    print("Iniciando operación➕ ")
    return a + b


suma = devuelve_suma(a, b)
print(f"La suma total de los números ingresados es: {suma}")

# Ejercicio Número 3 "Factorial".
"""Escribe una función factorial(n) que reciba un número entero positivo y regrese su factorial.
(Ejemplo: factorial(5) → 120)."""

numero_n = int(
    input("Escribe un nùmero entero cualquiera que desees saber su factorial: ")
)


def factorial(numero_n):
    if numero_n == 0 or numero_n == 1:
        return 1
    else:
        return numero_n * factorial(numero_n - 1)


resultado = factorial(numero_n)
print(f"El número factorial de {numero_n} es {resultado}")

# Ejercicio Número 4 "Números pares".

"""Crea una función pares(lista) que reciba una lista de números y regrese otra lista solo con los números pares."""

lista_numeros = []

for i in range(10):
    numero = int(input(f"Escribe el número {i + 1}: "))
    lista_numeros.append(numero)


def devuelve_pares(lista_numeros):
    print("Limpiando la lista de inpares⚠️")
    lista_sinpares = [numero for numero in lista_numeros if numero % 2 == 0]
    return lista_sinpares


lista_limpia = devuelve_pares(lista_numeros)

print("\n📊 Lista con pares:\n")
for i, numero in enumerate(lista_limpia, start=1):
    print(f"{i} - Número: {numero}")

# Ejercicio Número 5 "Conversor de temperatura".

"""Crea una función celsius_a_fahrenheit(celsius) que convierta de °C a °F.
Fórmula: F = C * 9/5 + 32."""

celsius = float(
    input("Inserta la temperatura que desees convertir a grados Farenheit: ")
)


def celsius_a_farenheit(celsius):
    print(f"Convirtiendo {celsius} a temperatura en grados Farenheit👍")
    F = celsius * 9 / 5 + 32
    return F


F = celsius_a_farenheit(celsius)

print(f"La temperatura resultante es {F} °F")

# Ejercicio Número 6: Contador de palabras

oracion = input(
    "Inserte una cadena de texto, el programa desglozará cuántas palabras tiene en total: "
).replace(" ", "")

conteo = []


def devuelve_conteo_palabras(oracion):
    print("Contando la cantidad de palabras en el texto🟰")
    conteo.append(oracion)
    palabras_totales = len(oracion)
    return palabras_totales


palabras_totales = devuelve_conteo_palabras(oracion)

print(f"La cantidad de palabras en la oración es: {palabras_totales}")

# Ejercicio número 7: Máximo de una lista
"""Crea una función maximo(lista) que reciba una lista y regrese el valor máximo sin usar la función max()."""

lista_num = []

for i in range(4):
    numero = int(input(f"Escriben el número {i + 1}: "))
    lista_num.append(numero)


def devuelve_max_lista(lista_num):
    print("Ordenando la lista y obteniendo el valor más alto👍")
    lista_ordenada = sorted(lista_num)
    lista_ordenada.reverse()
    print("\n📊 Lista ordenada:\n")
    for i, numero in enumerate(lista_ordenada, start=1):
        print(f"{i} - Número: {numero}")
    alto = lista_ordenada[0]
    return alto


maximo_lista = devuelve_max_lista(lista_num)
print(f"El máximo de la lista es: {maximo_lista}")

#Ejercicio número 9: Promedio. 
"""Crea una función promedio(lista) que reciba una lista de números y regrese el promedio."""

lista_promedios= {}

for i in range(3):
    alumno= input(f"Ingresa el nombre del alumno {i + 1}: ")
    promedios= float(int(f"Ingresa el promedio del alumno {alumno} '{i + 1}' a continuación: "))
    lista_promedios[alumno]= promedios
    
claves= lista_promedios.keys()

valor= lista_promedios.values()

def devuelve_promedio(claves, valor):
    suma_promedios= sum(valor)
    total_alumnos= len(claves)
    
    return suma_promedios / total_alumnos
       
promedio_general= devuelve_promedio(claves, valor)
for clave, valor in lista_promedios.items():
    print(f"Alumno: {clave} - Promedio: {valor}")
print(f"Promedio general: {promedio_general}")

#Ejercicio número 9: Promedio. 
import math
"""Crea una función promedio(lista) que reciba una lista de números y regrese el promedio."""

lista_promedios= {}

for i in range(3):
    alumno= input(f"Ingresa el nombre del alumno {i + 1}: ")
    promedios= float(input(f"Ingresa el promedio del alumno {alumno} '{i + 1}' a continuación: "))
    lista_promedios[alumno]= promedios
    
claves= lista_promedios.keys()

valor= lista_promedios.values()

def devuelve_promedio(claves, valor):
    suma_promedios= sum(valor)
    total_alumnos= len(claves)
    
    return suma_promedios / total_alumnos
       
promedio_general= devuelve_promedio(claves, valor)
promedio_redondeado= math.floor(promedio_general)
for clave, valor in lista_promedios.items():
    print(f"Alumno: {clave} - Promedio: {valor}")
print(f"Promedio general: {promedio_general}, promedio final: {promedio_redondeado}")

if promedio_redondeado <= 7: 
    print("El grupo ha reprobado❌")
elif promedio_redondeado <= 8:
    print("El grupo tuvo un desempeño promedio⚠️")
else: 
    print("El grupo obtuvo un promedio satisfactorio👍🤩")
    
#Ejercicio número 10: Calculadora. 
"""Escribe una función calculadora(a, b, operacion) que reciba dos números y una operación ("suma", "resta", "multiplicacion", "division") 
y devuelva el resultado correspondiente."""

operacion= input("""
Escoge del siguiente menú la operación que desees hacer: 
1) Suma
2) Resta
3) Multiplicación
4) División
5) Potenciación 
: """)

a= int(input("Ingresa el primer número: "))

b= int(input("Ingresa el segundo número: "))

def calculadora(a, b, operacion): 
    print(f"Tu escogiste la operación {operacion}: ")
    if operacion == "1":
        print("Suma")
        return a + b 
    elif operacion == "2":
        print("Resta")
        return a - b
    elif operacion == "3":
        print("Multiplicación")
        return a * b
    elif operacion == "4":
        print("División")
        return a / b
    elif operacion == "5":
        print("Potenciación")
        return a ** b
    else: 
        return ValueError

resultado= calculadora(a, b, operacion)

print(f"El resultado de la operación entre {a} y {b} es: {resultado}. ")    
    