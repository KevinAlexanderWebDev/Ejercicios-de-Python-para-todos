# 🔥 15 Ejercicios Finales de Repaso (Módulos 5, 6 y 7)
"""Listas, Diccionarios y Funciones

📌 Escribe una función que reciba una lista de números y devuelva otra lista solo con los números pares.

📌 Crea un programa que use un diccionario para almacenar nombres de productos y precios. Luego pide al usuario un producto y muestra su precio (si existe).

📌 Escribe una función que reciba un texto y devuelva un diccionario con la frecuencia de cada letra.

📌 Dada una lista de nombres, escribe una función que devuelva los nombres que comienzan con vocal.

📌 Crea una función que reciba una lista de números y devuelva un diccionario con el mínimo, máximo y promedio.
"""

# Ejercicio 1
lista_numeros = []

while True:
    numeros = input(
        "Agrega los números que gustes a la lista, oprime 'ENTER' para dejar de agregar números: "
    )
    if not numeros:
        break
    lista_numeros.append(numeros)

lista_num_enteros = [int(elemento) for elemento in lista_numeros]
print("Lista de números completa: ")
for i, numero in enumerate(lista_num_enteros, start=1):
    print(f"{i} - Número: {numero}")


def devuelve_numeros_pares(lista_num_enteros):
    lista_pares = [num for num in lista_num_enteros if num % 2 == 0]
    return lista_pares


def devuelve_numeros_inpares(lista_num_enteros):
    lista_inpares = [num for num in lista_num_enteros if num % 2 != 0]
    return lista_inpares


numeros_pares = devuelve_numeros_pares(lista_num_enteros)
print("Lista de números pares: ")
for i, numero in enumerate(numeros_pares, start=1):
    print(f"{i} - Número: {numero}")

numeros_inpares = devuelve_numeros_inpares(lista_num_enteros)
print("Lista de números inpares: ")
for i, numero in enumerate(numeros_inpares, start=1):
    print(f"{i} -  Número: {numero}")

# Ejercicio 2:
SALIR = "🔽Ok, Saliendo del programa..."

MENSAJE_EXITO = "EL procedimiento se llevó a cabo con éxito👍"

MENSAJE_ERROR = "❌Error: Por favor escoja entre los valores correctos."

VOLVER = "Ok, volviendo al inicio👆"

diccionario_productos = {}

while True:

    print(
        "A continuación podrás agregar los productos con sus respectivos precios, oprime dos veces 'ENTER' para dejar de agregar: "
    )
    while True:
        productos = input("Ingresa el nombre del producto: ").strip().replace(" ", "")
        precio = input("Ingresa el precio del producto: $")
        if not productos or not precio:
            break
        precio_int = float(precio)
        diccionario_productos[productos] = precio_int

    print("🔍 Buscar producto...")
    filtro = (
        input("¿Desea buscador el procuto por precio(p) o por nombre(n)?: (p/n) ")
        .lower()
        .strip()
        .replace(" ", "")
    )
    if filtro == "p":
        buscar_por_precio = float(
            input("Ingresa el precio del producto en el buscador: ")
        )
        for nombre, precio in diccionario_productos.items():
            if precio == buscar_por_precio:
                print(f"El producto {nombre} tiene un precio de {precio}")
                print(MENSAJE_EXITO)
                print(SALIR)
                break
        else:
            agregar = input(
                f"El producto con el precio {buscar_por_precio} no se encuentra, ¿Desea agregarlo al diccionario? - (s/n): "
            )
            if agregar == "s":
                nombre_producto = input(
                    "Escribe cuál deseas que sea el nombre del producto que corresponderá al precio: "
                )
                print("Entendido, agregando producto a la Base de datos: ")
                diccionario_productos[nombre_producto] = buscar_por_precio
                print(
                    f"El producto {nombre_producto} ha sido agregado al diccionario corréctamente🤩"
                )
                for nombre, precio in diccionario_productos.items():
                    print(f"Nombre del producto: {nombre} - Precio: {precio}")
                regresar = input(
                    "¿Desea regresar al inicio (r) o salir del programa (s): (r/s) - "
                )
                if regresar == "r":
                    print(VOLVER)
                elif regresar == "s":
                    print(SALIR)
                    break
                else:
                    print(MENSAJE_ERROR)
            elif agregar == "n":
                regresar = input(
                    "¿Desea regresar al inicio (r) o salir del programa (s): (r/s) - "
                )
                if regresar == "r":
                    print(VOLVER)
                elif regresar == "s":
                    print(SALIR)
                    break
                else:
                    print(MENSAJE_ERROR)
            else:
                print(MENSAJE_ERROR)
    if filtro == "n":
        buscar_por_nombre = input("Ingresa el nombre del producto en el buscador: ")
        if buscar_por_nombre in diccionario_productos:
            precio = diccionario_productos[buscar_por_nombre]
            print(f"El producto {buscar_por_nombre} tiene un precio de: {precio}")
            regresar = input(
                "¿Desea regresar al inicio (r) o salir del programa (s): (r/s) - "
            )
            if regresar == "r":
                print(VOLVER)
            elif regresar == "s":
                print(SALIR)
                break
            else:
                print(MENSAJE_ERROR)
        else:
            agregar = input(
                f"El producto con el precio {buscar_por_precio} no se encuentra, ¿Desea agregarlo al diccionario? - (s/n): "
            )
            if agregar == "s":
                nombre_producto = input(
                    "Escribe cuál deseas que sea el nombre del producto que corresponderá al precio: "
                )
                print("Entendido, agregando producto a la Base de datos: ")
                diccionario_productos[nombre_producto] = buscar_por_precio
                print(
                    f"El producto {nombre_producto} ha sido agregado al diccionario corréctamente🤩"
                )
                for nombre, precio in diccionario_productos.items():
                    print(f"Nombre del producto: {nombre} - Precio: {precio}")
                regresar = input(
                    "¿Desea regresar al inicio (r) o salir del programa (s): (r/s) - "
                )
                if regresar == "r":
                    print(VOLVER)
                elif regresar == "s":
                    print(SALIR)
                    break
                else:
                    print(MENSAJE_ERROR)
            elif agregar == "n":
                regresar = input(
                    "¿Desea regresar al inicio (r) o salir del programa (s): (r/s) - "
                )
                if regresar == "r":
                    print(VOLVER)
                elif regresar == "s":
                    print(SALIR)
                    break
                else:
                    print(MENSAJE_ERROR)
            else:
                print(MENSAJE_ERROR)

# Ejercicio número 3:
texto = input("Escribe a continuación un texto cual sea: ")
texto_modificado = texto.strip().replace(" ", "")


def devuelve_frecuencia(texto_modificado):
    """Devuelve diccionario de frecuencia por letra"""
    diccionario_letras = {}
    for letra in texto_modificado:
        diccionario_letras[letra] = (
            diccionario_letras.get(letra, 0) + 1
        )  # Almacena en el diccionario las letras como clave y un número (si hay letras se agruega al valor un número por cada letra)
    return diccionario_letras  # Recordatorio para mí ⚠️Identar al nivel del for un return porque solo captura un valor(al menos reflexiona si hacerlo o no😅)


diccionario_resultante = devuelve_frecuencia(texto)
print(f"Diccionario resultante de la palabra '{texto}': ")
for palabra, cantidad in diccionario_resultante.items():
    print(f"Letra: {palabra} - Cantidad: {cantidad}")

"""📌 Dada una lista de nombres, escribe una función que devuelva los nombres que comienzan con vocal."""

lista_nombres = []

print(
    "A continuación crea una lista de nombres, con los nombres que gustes, oprime '1' para terminar de agregar nombres: "
)

while True:
    nombres = input("Comienza a agregar: ").strip().replace(" ", "")
    if nombres == "1":
        break
    lista_nombres.append(nombres)

print("Lista completa con los nombres: ")
for i, nombre in enumerate(lista_nombres, start=1):
    print(f"{i} - Nombre: {nombre}")


def devuelve_nombresvocales(lista_nombres):
    vocales = "aeiouAEIOU"
    lista_vocales = [
        nombre for nombre in lista_nombres if len(nombre) >= 1 and nombre[0] in vocales
    ]
    print("Esta es la lista con los nombres que comienzan en vocal: ")
    return lista_vocales


def devuelve_nombresconsonantes(lista_nombres):
    vocales = "aeiouAEIOU"
    lista_consonantes = [
        nombre
        for nombre in lista_nombres
        if len(nombre) >= 1 and nombre[0] not in vocales
    ]
    print("Esta es la lista con los nombres que comienzan en consonante: ")
    return lista_consonantes


nombres_iniciavocal = devuelve_nombresvocales(lista_nombres)
for i, nombre in enumerate(nombres_iniciavocal, start=1):
    print(f"{i} - Nombre: {nombre}")

nombres_inicioconsonante = devuelve_nombresconsonantes(lista_nombres)
for i, nombre in enumerate(nombres_inicioconsonante, start=1):
    print(f"{i} - Nombre: {nombre}")

# Ejercicio 5:
lista_numeros = []

while True:
    numeros = input("Escribe los números que desees agregar a la lista: ")
    if not numeros:
        break
    lista_numeros.append(numeros)

lista_numeros = [
    int(elemento) for elemento in lista_numeros
]  # Cambia los elementos de tipo strg a tipo int


def devuelve_dictminmaxprom(lista_numeros):
    dict_numeros = {}
    num_minimo = min(lista_numeros)
    num_maximo = max(lista_numeros)
    cantidad_num = len(lista_numeros)
    sum_numeros = sum(lista_numeros)
    promedio = sum_numeros / cantidad_num

    dict_numeros["Número máximo"] = num_maximo
    dict_numeros["Número mínimo"] = num_minimo
    dict_numeros["Promedio"] = promedio

    return dict_numeros


def devuelve_listaordenada(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    return lista_ordenada


lista_ordenada = devuelve_listaordenada(lista_numeros)
diccionario_retornado = devuelve_dictminmaxprom(lista_numeros)
print("Esta es la lista ordenada completa (Menor a Mayor): ")
for i, numero in enumerate(lista_ordenada, start=1):
    print(f"{i} - Número: {numero}")
print("Estos son los datos resultantes: ")
for clave, valor in diccionario_retornado.items():
    print(f"{clave} - Valor: {valor}")

"""Funciones más complejas

📌 Escribe una función que simule una calculadora básica (suma, resta, multiplicación, división) usando parámetros a, b y operación.

📌 Escribe una función que convierta una lista de temperaturas en grados Celsius a Fahrenheit.

📌 Dado un diccionario con alumnos y sus calificaciones, escribe una función que devuelva una lista con los aprobados (nota >= 6).

📌 Crea una función que reciba un string y devuelva True si es palíndromo y False en caso contrario.

📌 Implementa una función que reciba una lista de tuplas con (nombre, edad) y devuelva el nombre del más joven."""

# Ejercicio 6:
# Calculadora arimética
print("Calculadora de operaciones básicas")
print("Escribe dos números para poder proceder con las operaciones: ")

numeros_operar = []
for i in range(2):
    numeros = int(input(f"Agrega el número {i + 1} para la operación: "))
    numeros_operar.append(numeros)


def calculadora_arimetica(numeros_operar):
    operacion = input(
        """➕➖ Calculadora de operaciones básicas ✖️➗
    -Suma: +
    -Resta: -
    -Multiplicación: x
    -División: /
    -Potencia: **
    Tú escoges: """
    )
    primer_numero = numeros_operar[0]
    segundo_numero = numeros_operar[1]
    if operacion == "+":
        suma = sum(numeros_operar)
        return "Suma", suma
    elif operacion == "-":
        resta = primer_numero - segundo_numero
        return "Resta", resta
    elif operacion == "x":
        multiplicacion = primer_numero * segundo_numero
        return "Multiplicación", multiplicacion
    elif operacion == "/":
        division = primer_numero / segundo_numero
        return "División", division
    elif operacion == "**":
        potenciacion = primer_numero**segundo_numero
        return "Potenciacion", potenciacion
    else:
        return TypeError


resultado_operacion = calculadora_arimetica(numeros_operar)

for resultado in resultado_operacion:
    print(f"Resultado de la operacion: {resultado}")

# Ejercicio 7:
# lista de temperaturas: Conversor de °C a °F --> (°C x 9/5) + 32 =°F y (°F - 32) x 5/9 =°C

lista_centigrados = []

print(
    "A continuación escribe las temperaturas que desees agregar a la lista, presiona 'ENTER' para parar de agregar"
)
while True:
    centigrados = input(
        "Escribe una lista con diferentes temperaturas en grados centígrados: "
    )
    if not centigrados:
        break
    lista_centigrados.append(centigrados)

lista_centigrados = [int(temperatura) for temperatura in lista_centigrados]


def devuelve_listafarenheit(lista_centigrados):
    lista_farenheit = [
        ((temperatura * 9 / 5) + 32) for temperatura in lista_centigrados
    ]
    return lista_farenheit


print("\n")

resultado_farenheit = devuelve_listafarenheit(lista_centigrados)
print("Lista original en grados centígrados: ")
for i, temperatura in enumerate(lista_centigrados, start=1):
    print(f"{i} - Temperatura: {temperatura}°C")
print("\n")

print("Lista con temperaturas en Farenheit: ")
for i, temperatura in enumerate(resultado_farenheit, start=1):
    print(f"{i} - Temperatura: {temperatura}°F")
print("\n")


# Hice una extra solo porque se me ocurrió😅
def devuelve_alta(lista_centigrados):
    temperatura_masalta = max(lista_centigrados)

    return temperatura_masalta


def devuelve_baja(lista_centigrados):
    temperatura_masbaja = min(lista_centigrados)

    return temperatura_masbaja


temperatura_mas_alta = devuelve_alta(lista_centigrados)
temperatura_mas_baja = devuelve_baja(lista_centigrados)

print(f"La temperatura más alta en la lista es: {temperatura_mas_alta}°C🥵☀️ \n")
print(f"La temperatura más baja es: {temperatura_mas_baja}°C🥶😖 \n")

# Ejercicio 8:
diccionario_calificaciones = {}

docente = input("Escribe tu nombre de docente: ").strip().replace(" ", "")

print(f"🫡👋Hola {docente}. Bienvenido al registro de alumnos por calificaciones")

print(
    "Escribe los nombres con los promedios de los alumnos, presiona '*' para dejar de agregar: "
)
while True:
    alumno = input("Escribe el nombre del alumno a continuación: ")
    if alumno == "*" or not alumno:
        break
    calificacion = int(input(f"Escribe el promedio del alumno '{alumno}': "))
    diccionario_calificaciones[alumno] = calificacion

lista_tuplas_calificaciones = diccionario_calificaciones.items()


def devuelve_aprobados(lista_tuplas_calificaciones):
    lista_aprobados = [
        alumno for alumno, cal in lista_tuplas_calificaciones if cal >= 6
    ]
    return lista_aprobados


def devuelve_reprobados(lista_tuplas_calificaciones):
    lista_reprobados = [
        alumno for alumno, cal in lista_tuplas_calificaciones if cal < 6
    ]
    return lista_reprobados


reprobados = devuelve_reprobados(lista_tuplas_calificaciones)

aprobados = devuelve_aprobados(lista_tuplas_calificaciones)


if not aprobados:
    print("No hubo alumnos aprobados😭❌")
else:
    print("Lista de alumnos aprobados🍾: ")
    for alumno in aprobados:
        print(f"Alumno: {alumno} 🥳")

if not reprobados:
    print(f"Felicidades {docente}, no hubo alumno reprobados🍾🥳")
else:
    print("Lista de alumno reprobados❌: ")
    for alumno in reprobados:
        print(f"Alumno: {alumno} 😭")

# Ejercicio 9:

frase = input("Escribe una frase cualquiera: ")

frase_minusucla = frase.lower()


def devuelve_palindromo(frase_minuscula):
    print("Detector de palíndromos: ")
    print(
        "Un palíndromo es una frase que se lee igual tantoa al derecho como al revés🫡"
    )
    if frase_minuscula == frase_minuscula[::-1]:
        return "¿Es palíndromo?:", True
    else:
        return "¿Es palíndromo?:", False


palindromo = devuelve_palindromo(frase)

print(f"La frase '{frase}' - {palindromo}")

# Ejercicio 10:

lista_personas = []

print(
    "Instrucciones: Para agregar personas a la lista, por favor hazlo con el siguiente formato (nombre, edad), para dejar de agregar teclea '*'."
)

while True:
    datos_persona = input(
        "Escribe el nombre de las personas con el siguiente formato (nombre, edad): "
    )
    if datos_persona == "*" or not datos_persona:
        break
    nombre, edad = datos_persona.strip().split(",")
    lista_personas.append((nombre, int(edad)))


def devuelve_masjoven(lista_personas):
    if not lista_personas:
        return "No hay personas en la lista, valor:", None
    persona_mas_joven = min(lista_personas, key=lambda x: x[1])
    return persona_mas_joven


persona_masjoven = devuelve_masjoven(lista_personas)

print("La persona más joven de la lista es: ")
print(f"Nombre: {persona_masjoven[0]} - Edad: {persona_masjoven[1]}")

"""Archivos: 

11. 📌 Escribe un programa que cree un archivo numeros.txt con números del 1 al 20 (uno por línea), luego lo lea y calcule la suma.

12. 📌 Escribe un programa que pida al usuario frases y las vaya guardando en un archivo frases.txt. Luego, muéstralo todo en mayúsculas.

13. 📌 Crea un programa que lea un archivo empleados.txt con formato:

nombre, salario


y devuelva el empleado con el mayor salario.
14. 📌 Escribe un programa que lea un archivo palabras.txt y cuente cuántas veces aparece cada palabra (usa un diccionario para almacenar las frecuencias).
15. 📌 (Incluye try y except): Haz un programa que intente leer un archivo llamado config.txt.

Si existe, muestra su contenido.

Si no existe, captura el error con FileNotFoundError y crea el archivo con un mensaje por defecto: "Archivo de configuración creado automáticamente."."""

# Ejercicio 11:
total = 0

NOMBRE_ARCHIVO = "numeros.txt"
with open(NOMBRE_ARCHIVO, "w") as f:
    for num in range(1, 21):
        f.write(str(num) + "\n")

with open(NOMBRE_ARCHIVO, "r") as f:
    print("La lista de números es: ")
    for i, numero in enumerate(f, start=1):
        print(f"{i} - Número: {numero}")

with open(NOMBRE_ARCHIVO, "r") as f:
    for line in f:
        total += int(line.strip())
print(f"La suma de los números en el archivo es: {total}")

# Ejercicio 12:
print(
    "Escribe las frases que gustes en la entrada siguiente, si deseas dejar de agregar teclea '+'."
)

ARCHIVO_FRASES = "frases.txt"

lista_frases = []

while True:
    frases = input("Por favor introduce la o las frases: ").strip()
    if frases == "+" or not frases:
        break
    lista_frases.append(frases)

with open(ARCHIVO_FRASES, "w") as f:
    for i, frase in enumerate(lista_frases, start=1):
        f.write(f"{i} - Frase: {frase} \n")


def devuelve_textomay():
    with open(ARCHIVO_FRASES, "r") as f:
        lectura = f.read().upper()
    return lectura


frases_mayusculas = devuelve_textomay()

print("Esta es la lista de frases en mayúsculas: ")
print(frases_mayusculas)

# Ejercicio 13:

ARCHIVO_EMPLEADOS = "empleados.txt"

datos_empleados = []

print(
    "Para agregar empleados al archivo, por favor hagalo respetando el formato nombre, sueldo, para dejar de agregar oprima la tecla '+': "
)
while True:
    empleados = input(
        "Por favor agrega los datos del empleado con el siguiente formato --> nombre, sueldo: "
    )
    if empleados == "+" or not empleados:
        break
    nombre, sueldo = empleados.strip().split(",")
    datos_empleados.append((nombre, int(sueldo)))

with open(ARCHIVO_EMPLEADOS, "w") as file:
    for nombre, sueldo in datos_empleados:
        file.write(f"Empleado_Nombre: {nombre} - Salario: {sueldo}\n")


def devuelve_lectura():
    with open(ARCHIVO_EMPLEADOS) as file:
        print("Lista de empleados con salarios: ")
        lectura = file.read()
    return lectura


empleados_salarios = devuelve_lectura()
print(empleados_salarios)

# Ejercicio 14:
ARCHIVO_CONFIG = "config.txt"

diccionario_frecuenicas = {}

lista_texto = []
while True:
    texto = input(
        "En el siguiente espacio, proporciona una lista de palabras de la temática que gustes: "
    )
    if texto == "+" or not texto:
        break
    lista_texto.append(texto)

for palabra in lista_texto:
    diccionario_frecuenicas[palabra] = diccionario_frecuenicas.get(palabra, 0) + 1

with open(ARCHIVO_CONFIG, "w") as file:
    for palabra, valor in diccionario_frecuenicas.items():
        file.write(f"Letra: {palabra} - Frecuencia: {valor}\n")


def devuelve_frecuencia():
    with open(ARCHIVO_CONFIG, "r") as file:
        lectura = file.read()
    return lectura


lectura_archivo = devuelve_frecuencia()

print("Lista original: \n")
for i, texto in enumerate(lista_texto, start=1):
    print(f"{i} - Texto: {texto}")

print("\n")
print("Lista de palabras con frecuencia: \n")
print(lectura_archivo)
