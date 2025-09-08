# Ejercicios Módulo 7: Manejo de Archivos en Python.
"""📄 Crea un archivo de texto llamado saludo.txt y escribe dentro:
Hola, bienvenido al módulo 7 de Python"""

with open("saludo.txt", "w") as archivo:
    archivo.write("Hola, bienvenido al módulo 7 de Python")

# Ejercicio 2:
"""📄 Escribe un programa que pida al usuario su nombre y lo guarde en un archivo usuario.txt.
Después, abre el archivo y muestra el nombre en mayúsculas."""

with open("usuario.txt", "w") as archivo:
    nombre = input("Escribe tu nombre a continuación: ")
    archivo.write(nombre)

with open("usuario.txt", "r") as archivo:
    leer = archivo.read().strip().upper()

print(f"El nombre de la persona es {leer}")

# Ejercicio 3:
"""📄 Dado un archivo numeros.txt que contiene una lista de números (uno por línea),
lee el archivo y calcula la suma total."""

numeros_str = []

for i in range(2):
    numero = input(
        f"Escribe al menos dos números que desees agregar a la lista {i + 1}: "
    )
    numero_separado = numero
    numeros_str.append(numero_separado)

with open("archivo_numeros.txt", "w") as lista:
    lista.writelines(numero + "\n" for numero in numeros_str)

with open("archivo_numeros.txt", "r") as lista:
    leer_lista = lista.readlines()

print(f"Esta es la lista de números: {leer_lista}")


def devuelve_suma_lista(numeros_str):
    lista_int = [int(elemento) for elemento in numeros_str]
    return sum(lista_int)


suma = devuelve_suma_lista(numeros_str)
print(f"La suma de los números contenidos en el archivo de texto es: {suma}")

# Ejercicio 4:
import json

"""📄 Crea un archivo notas.txt donde cada línea tenga el formato:

Alumno, Nota

El programa debe leerlo y calcular el promedio de notas de la clase."""
clase = {}

for i in range(2):
    estudiante = input(f"Agrega el nombre del estudiante '{i + 1}': ")
    promedio = int(input(f"Agrega el promedio del estudiante '{i + 1}' {estudiante}: "))
    clase[estudiante] = promedio

total_alumnos = len(clase)

promedios = clase.values()

suma_promedios = sum(promedios)


def devuelve_promedio(clase):
    with open("clase.json", "w") as archivo:
        json.dump(clase, archivo)
    with open("clase.json", "r") as archivo:
        datos_leidos = json.load(archivo)
    print(f"Los archivos contenidos en clase.json son: {datos_leidos}")
    promedio_final = suma_promedios / total_alumnos
    return promedio_final


resultado_promedio = devuelve_promedio(clase)
print("\nLista de alumnos en la clase con promedios:\n")
for alumno, promedio in clase.items():
    print(f"Alumno: {alumno} - Promedio: {promedio}")
print(f"El promedio general de la clase es: {resultado_promedio}")

# Ejercicio 5:
import datetime

"""📄 Escribe un programa que abra un archivo historial.txt en modo a y vaya agregando cada vez que se ejecute la fecha 
y hora actual (pista: usa datetime.now()).Luego, muestra el contenido completo del archivo."""


def obtiene_fecha_hora_actual():
    # Esta función funciona para escribir la hora en el documento
    with open("Historial.txt", "a") as f:
        fecha_hora_actual = datetime.datetime.now()
        f.write(f"{fecha_hora_actual.strftime('%Y-%m-%d %H:%M:%S')}\n")


def leer_historial():
    # Lee el archivo 'Historial.txt'
    try:
        with open("Historial.txt", "r") as f:
            lectura = f.read()
            print("El historial resultante de 'Historial.txt' es: ")
            print(lectura)
    except FileNotFoundError:
        print("El archivo no se encuentra⚠️")


obtiene_fecha_hora_actual()
leer_historial()

# Ejercicio número 6
"""1. 📊 Leer CSV simple

Crea un archivo personas.csv con este contenido:

nombre,edad
Ana,23
Luis,30
María,27


Luego escribe un programa que lo lea y muestre solo los nombres de las personas mayores de 25 años."""

import csv

with open("personas.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Ana", 23])
    writer.writerow(["Luis", 30])
    writer.writerow(["María", 27])

with open("personas.csv", "r") as archivo:
    reader = csv.DictReader(archivo)
    for row in reader:
        if int(row["Edad"]) > 25:
            print("Nombre", row["Nombre"], "con", row["Edad"])
        else:
            print("No cuentan con +25 años:", row["Nombre"], "con", row["Edad"], "años")

# Ejercicio número 7
"""2. 📄 Contar palabras en un texto

Crea un archivo cuento.txt con un párrafo cualquiera.
Haz un programa que lo lea y:

Cuente cuántas palabras hay en total.

Muestre las 5 palabras más usadas.

(Pista: usa .split() y un diccionario para contar)."""

palabra = input(
    "A continuación, crea un texto inventado referente a lo que tú gustes: "
)
with open("cuento.txt", "w") as f:
    f.write(palabra)

with open("cuento.txt", "r") as f:
    texto = f.read()
    texto_limpio = texto.lower().strip().replace(" ", "")
    texto_agrupado = (
        texto.lower().split()
    )  # Devuelve un texto separado por texto, por ejemplo: Kevin --> Solo es un texto
    contador_palabras = len(texto_limpio)
    print(f"La cantidad total de palabras en el texto es: {contador_palabras}")

oracion = {}
for palabra in texto_agrupado:
    if palabra in oracion:
        oracion[palabra] += 1
    else:
        oracion[palabra] = 1

palabras_masusadas = sorted(oracion.items(), key=lambda x: x[1], reverse=True)
print("La 5 palabras más usadas son: ")
for i in range(5):
    print(f"{palabras_masusadas[i] [0]}: {palabras_masusadas[i] [1]}")

# Ejercicio número 8
"""Escribe un programa que abra un archivo original.txt y cree una copia exacta en copia.txt.
(Pista: puedes leer con .read() y luego escribir, o usar un bucle línea por línea)."""

with open("original.txt", "w") as f:
    f.write("Texto a ser copiado")
with open("original.txt", "r") as f:
    a_original = f.read()
print(f"Archivo original: {a_original}")

with open("copia.txt", "w") as f:
    f.write(a_original)
with open("copia.txt", "r") as f:
    a_copia = f.read()
print(f"Archivo copia: {a_copia}")


# Ejercicio 9: +
"""4. 🗂️ Separar datos

Crea un archivo alumnos.txt con líneas así:

Juan,8
Ana,10
Pedro,6
Marta,9


Haz un programa que cree dos archivos nuevos:

aprobados.txt (notas >= 7)

reprobados.txt (notas < 7)"""

CERRAR = "Entendido, cerrando proceso...👋"

RETORNAR = "Ok, regresando al inicio👆"

ERROR = "Error: Por favor escoge entre las opciones disponibles"

MENSAJE_CONFIRMACION = "Entendido, realizando proceso"

MENSAJE_EXITO = "Procedimiento realizado satisfactoriamente y sin errores👍"

alumnos = []

while True:
    print(
        "Para almacenar alumnos con sus promedios, por favor escriba de la siguiente forma (alumno, calificación)❕⚠️"
    )

    eleccion_acceso = input(
        """
Menú interactivo: 
1: Agregar datos de alumnos (nombre, nota)
2: Eliminar la lista actual (Deben haber datos de por medio)
3: Ordenar lista por nombre
4: Salir
Tú escoges: """
    )
    if eleccion_acceso == "1":
        while True:
            entrada = input(
                "Escriba los datos del Alumno (nombre,nota) o Enter para terminar de agregar: "
            )
            if not entrada:
                break
            nombre, nota = entrada.strip().split(",")
            alumnos.append((nombre, int(nota)))

        with open("alumnos.txt", "w") as f:
            for nombre, nota in alumnos:
                f.write(f"{nombre}, {nota}\n")

        with open("alumnos.txt", "r") as f:
            leer = f.read()
        print("Esta es la lista de alumnos y promedios totales: ")
        print(leer)

        alumn_reprobados = []
        alum_aprobados = []
        for nombre, nota in alumnos:
            if nota >= 7:
                alum_aprobados.append((nombre, nota))
            else:
                alumn_reprobados.append((nombre, nota))

        visualizar_lista = (
            input(
                "¿Desea visializar la lista de alumnos aprobad(a)s y reprobad(a)s: (s/n) - "
            )
            .lower()
            .strip()
            .replace(" ", "")
        )
        if visualizar_lista == "s":
            if not alum_aprobados:
                print("No hay alumnos aprobados")
            else:
                with open("aprobados.txt", "w") as f:
                    for nombre, nota in alum_aprobados:
                        f.write(f"Nombre: {nombre} - Nota: {nota}" + "\n")
                with open("aprobados.txt", "r") as f:
                    lista_aprobados = f.read()
                print("Esta es la lista de alumnos aprobados: ")
                print(lista_aprobados)

            if not alumn_reprobados:
                print("No hay alumnos reprobados")

            else:
                with open("reprobados.txt", "w") as f:
                    for nombre, nota in alumn_reprobados:
                        f.write(f"Nombre: {nombre} - Nota: {nota}" + "\n")
                with open("reprobados.txt", "r") as f:
                    lista_reprobados = f.read()
                print("Esta es la lista de alumnos reprobados: ")
                print(lista_reprobados)

            continuar = (
                input("¿Desea agregar más alumnos? (s/n): ")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if continuar == "s":
                print(RETORNAR)
            elif continuar == "n":
                print(CERRAR)
                break
            else:
                print(ERROR)
        elif visualizar_lista == "n":
            retornar = (
                input("¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) -")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if retornar == "r":
                print(RETORNAR)
            elif retornar == "s":
                print(CERRAR)
                break
            else:
                print(ERROR)
        else:
            print(ERROR)
    elif eleccion_acceso == "2":
        if not alumnos:
            print(
                "La lista de alumnos está vacía, no hay nada que eliminar. Volviendo ⬆️"
            )
        else:
            continuar = input(
                """Para proceder con la eliminación de la lista oprima '1' para confirmar o cualquier otra tecla para abortar
                            ⚠️Esta acción no tiene retorno⚠️"""
            )
            if continuar == "1":
                print(MENSAJE_CONFIRMACION)
                alumnos.clear()
                print(MENSAJE_EXITO)
                retornar = input(
                    "¿Desea regresar al inicio(r) o salir del programa(s): (r/s) - "
                )
                if retornar == "r":
                    print(RETORNAR)
                elif retornar == "s":
                    print(CERRAR)
                    break
                else:
                    print(ERROR)
            else:
                print(RETORNAR)
    elif eleccion_acceso == "3":
        if not alumnos:
            print(
                "La lista de alumnos está vacía, no hay nada que ordenar. Volviendo ⬆️"
            )
        else:
            ordenar = input(
                "¿Desea ordenar la lista de forma permanente(p) o solo momentánemanete(m)?: (p/m) -"
            )
            if ordenar == "p":
                print(MENSAJE_CONFIRMACION)
                alumnos.sort()
                print("Lista ordenada: ")
                for nombre, nota in alumnos:
                    print(f"Nombre: {nombre} - Nota: {nota}" + "\n")
                retornar = input(
                    "¿Desea regresar al inicio(r) o salir del programa(s): (r/s) - "
                )
                if retornar == "r":
                    print(RETORNAR)
                elif retornar == "s":
                    print(CERRAR)
                    break
                else:
                    print(ERROR)
            elif ordenar == "m":
                print("lista ordenada momentáneamente: ")
                print(MENSAJE_CONFIRMACION)
                for nombre, nota in alumnos:
                    print(f"Nombre: {nombre} - Nota: {nota}" + "\n")
                retornar = input(
                    "¿Desea regresar al inicio(r) o salir del programa(s): (r/s) - "
                )
                if retornar == "r":
                    print(RETORNAR)
                elif retornar == "s":
                    print(CERRAR)
                    break
                else:
                    print(ERROR)
            else:
                print(ERROR)
    elif eleccion_acceso == "4":
        print(CERRAR)
        break
    else:
        print(ERROR)

# Ejercicio 10
"""🔍 Buscar en un archivo

Crea un archivo libro.txt con varias líneas de texto.
Haz un programa que pida una palabra al usuario y muestre en qué líneas aparece.
(Pista: usa enumerate() para saber el número de línea).
"""
with open("archivo_libro.txt", "w") as f:
    f.write("El gato maullaba en la ventana.\n")
    f.write("El perro ladraba en el patio.\n")
    f.write("La niña jugaba con sus muñecas.\n")
    f.write("El anciano leía un libro en el parque.\n")
    f.write("El viento soplaba entre las hojas de los árboles.\n")

buscar_palabra = input("Ingresa la palabra que desees sea buscada en el texto: ")

with open("archivo_libro.txt", "r") as f:
    for i, palabra_en_linea in enumerate(
        f, start=1
    ):  # i representa la línea y palabra_en_linea la palabra en una lista.
        if buscar_palabra.lower() in palabra_en_linea.lower():
            print(f"La palabra '{buscar_palabra}' se encuentra en la línea: {i}")
