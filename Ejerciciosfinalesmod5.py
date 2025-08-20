# Ejercicios finales del módulo 5:
"""📌 Problema:
Crea una lista de 10 números enteros aleatorios entre 1 y 100.

Muestra la lista original.

Ordena la lista de menor a mayor y muéstrala.

Elimina los números repetidos manteniendo el orden.

Muestra la suma y el promedio de los elementos.

👉 Pista: sorted(), set(), sum(), len()."""

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

VACIO = "Error encontrado, no puedes dejar vacío."

SINVALOR = "Error: La colección y lista actual se encuentra actualmente vacía."

randoms_list = []

while True:
    print("Menú principal:")
    menu = input(
        """
    -Oprime 1 para agregar números a la lista (10 por elección)
    -Oprime 2 para eliminar números repetidos de la lista
    -Oprime 3 para ordenar la lista de forma permanente
    -Oprime 4 para sumar y promediar los valores de la base de datos
    -Oprime 5 para eliminar la lista entera (No recomendado)
    -Oprime 6 para imprimir la lista actual.
    -Oprime 7 para salir del programa
    Escoge un número en la lista: """
    )

    if menu == "1":
        print("Ejercicio con listas final: Módulo 5. ")
        for i in range(10):
            randoms = int(
                input(
                    f"Ingresa una lista de 10 números aleatorios entre 1 y 100. {i + 1}: "
                )
            )
            randoms_list.append(randoms)
        print("Esta es la lista creada: ")
        for i, numero in enumerate(randoms_list, start=1):
            print(f"Número: {i} - {numero}")
        volver = input(
            "¿Desea regresar al menú(r), salir del programa(s) o ver la vista ordenada de la lista (o)?: (r/s) "
        )
        if volver == "r":
            print(REGRESAR)
        elif volver == "s":
            print(SALIDA)
            break
        elif volver == "o":
            print("Vista de lista ordenada: ")
            for i, numero in enumerate(sorted(randoms_list), start=1):
                print(f"Numero: {i} - {numero}")
            volver = input("¿Desea volver al menú o salir?: (v/s) ")
            if volver == "v":
                print(REGRESAR)
            elif volver == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)
        else:
            print(ERROR)
    elif menu == "2":
        if not randoms_list:
            print(SINVALOR)
        else:
            print("Eliminar valores repetidos en la lista. ")
            eliminar_duplicados = set(randoms_list)
            print("Lista actualizada sin duplicados: ")
            for i, numero in enumerate(eliminar_duplicados, start=1):
                print(f"Número: {i} - {numero}")
            regresar = input(
                "¿Desea regresar al menú(r) o salir del programa(s)?:(r/s) "
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)
    elif menu == "3":
        if not randoms_list:
            print(SINVALOR)
        else:
            ordenar = input(
                "Por favor ingresa 'o' para ordenar la lista de forma definitiva. "
            )
            if ordenar == "o":
                print("Entendido, ordenando la lista actual...👍")
                randoms_list.sort()
                print("Lista ordenada con éxito. ")
                proceder = input(
                    "¿Desea proceder con los cambios(p) o desea revertirlos(r)?: (p/r) "
                )
                if proceder == "p":
                    print("Excelente: Aquí está la lista ordenada: ")
                    for i, numero in enumerate(randoms_list, start=1):
                        print(f"Número:{i} - {numero}")
                        proceder = input(
                            "¿Desea ir al menú y continuar(c) con los cambios o revertirlos(r)?: (c/r) "
                        )
                        if proceder == "c":
                            print(REGRESAR)
                        elif proceder == "r":
                            print("Entendido, revirtiendo los cambios...")
                            print("Cambios revertidos con éxito💯")
                            lista_invertida = reversed(randoms_list)
                            for i, numero in enumerate(lista_invertida, start=1):
                                print(f"{i} - {numero}")
                                volver = input(
                                    "¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                                )
                                if volver == "r":
                                    print(REGRESAR)
                                elif volver == "s":
                                    print(SALIDA)
                                else:
                                    print(ERROR)
                        else:
                            print(ERROR)
    elif menu == "4":
        if not randoms_list:
            print(SINVALOR)
        else:
            print("Sumador de elementos en la lista: ")
            suma_num = sum(randoms_list)
            print(f"La suma de los números encontrados en la lista es: {suma_num}.")
            total_elementos = len(randoms_list)
            print(
                f"Y, el promedio de los números en la lista es: {suma_num/total_elementos}"
            )
            regresar = input(
                "¿Desea regresar al menú (r) o salir del programa(s): (r/s) "
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
            else:
                print(ERROR)
    elif menu == "5":
        if not randoms_list:
            print(SINVALOR)
        else:
            print("Eliminar lista entera: ")
            eliminar = input(
                "¿Está seguro que desea eliminar la lista de forma permanente? (Una vez hecho esto los cambios no pueden ser revertidos): (s/n) "
            )
            if eliminar == "s":
                print("Entendido, eliminando lista...👍")
                randoms_list.clear()
                print("¡Lista eliminada con éxito!")
                regresar = input(
                    "¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eliminar == "n":
                print(REGRESAR)
            else:
                print(ERROR)

    elif menu == "6":
        if not randoms_list:
            print(SINVALOR)
        else:
            print("Lista actual impresa: ")
            for i, numero in enumerate(randoms_list, start=1):
                print(f"Número: {i} - {numero}")
                regresar = input(
                    "¿Desea volver al menú(r) o salir del programa(s)?: (r/s) "
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                else:
                    print(ERROR)
    elif menu == "7":
        print(SALIDA)
        break
    else:
        print(ERROR)

# Ejercicios finales del módulo 5.
"""📌 Problema:
Tienes la siguiente tupla de productos con precios:

productos = (
    ("manzana", 12),
    ("plátano", 8),
    ("naranja", 15),
    ("pera", 10),
    ("uva", 25)
)


Recorre la tupla e imprime cada producto con su precio.

Convierte la tupla en lista, agrega un producto nuevo con precio, y vuelve a convertirla en tupla.

Obtén el producto más caro y el más barato.

👉 Pista: usa max(), min() con key=lambda."""

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

VACIO = "Error encontrado, no puedes dejar vacío."

SINVALOR = "Error: La colección y lista actual se encuentra actualmente vacía."

print("Tienda de Abarrotes 'Don Mario'🧺")

tupla_productos = (
    ("manzana", 12),
    ("plátano", 8),
    ("naranja", 15),
    ("pera", 10),
    ("uva", 25),
)

lista_productos = list(tupla_productos)

print("Ejercicio con tuplas final: Módulo 5. ")

while True:
    print("Menú principal:")
    menu = input(
        """
    -Oprime 1 para agregar números a la lista (10 por elección)
    -Oprime 2 para eliminar números repetidos de la lista
    -Oprime 3 para ordenar la lista de forma permanente
    -Oprime 4 para obtener el producto con mayor existencia o menor existencia
    -Oprime 5 para eliminar la lista entera (No recomendado)
    -Oprime 6 para imprimir la lista actual.
    -Oprime 7 para salir del programa
    Escoge un número en la lista: """
    )

    if menu == "1":
        print("Informe de operaciòn: Tupla convertida a lista👆")
        for i in range(3):
            productos = input(
                f"Ingresa un total de 3 productos más a la tupla. {i + 1}: "
            )
            numeros = int(
                input(f"Ingresa la cantidad de acuerdo al producto. {i + 1}: ")
            )
            lista_productos.append(
                (productos, numeros)
            )  # Creando listas a partir de tuplas, esto permite datos clave valor asì...
        print("Esta es la lista creada: ")
        conv_diccio = dict(lista_productos)
        for productos, numeros in conv_diccio.items():
            print(f"Producto: {productos} - Cantidad: {numeros}")
        tupla_productos = tuple(lista_productos)
        print(tupla_productos)
        volver = input(
            "¿Desea regresar al menú(r), salir del programa(s) o ver la vista ordenada de la tupla (o)?: (r/s) "
        )
        if volver == "r":
            print(REGRESAR)
        elif volver == "s":
            print(SALIDA)
            break
        elif volver == "o":
            print("Vista de lista ordenada: ")
            for i, numero in enumerate(sorted(lista_productos), start=1):
                print(f"Numero: {i} - {numero}")
            volver = input("¿Desea volver al menú o salir?: (v/s) ")
            if volver == "v":
                print(REGRESAR)
            elif volver == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)
        else:
            print(ERROR)
    elif menu == "2":
        if not lista_productos and not tupla_productos:
            print(SINVALOR)
        else:
            print("Eliminar valores repetidos en la lista. ")
            eliminar_duplicados = set(lista_productos)
            print("Lista actualizada sin duplicados: ")
            for i, numero in enumerate(eliminar_duplicados, start=1):
                print(f"Número: {i} - {numero}")
            regresar = input(
                "¿Desea regresar al menú(r) o salir del programa(s)?:(r/s) "
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)
    elif menu == "3":
        if not lista_productos and not tupla_productos:
            print(SINVALOR)
        else:
            ordenar = input(
                "Por favor ingresa 'o' para ordenar la lista de forma definitiva. "
            )
            if ordenar == "o":
                print("Entendido, ordenando la lista actual...👍")
                lista_productos.sort()
                print("Lista ordenada con éxito. ")
                proceder = input(
                    "¿Desea proceder con los cambios(p) o desea revertirlos(r)?: (p/r) "
                )
                if proceder == "p":
                    print("Excelente: Aquí está la lista ordenada: ")
                    for i, numero in enumerate(lista_productos, start=1):
                        print(f"Número:{i} - {numero}")
                        proceder = input(
                            "¿Desea ir al menú y continuar(c) con los cambios o revertirlos(r)?: (c/r) "
                        )
                        if proceder == "c":
                            tupla_productos = tuple(lista_productos)
                            print(REGRESAR)
                        elif proceder == "r":
                            print("Entendido, revirtiendo los cambios...")
                            print("Cambios revertidos con éxito💯")
                            lista_invertida = reversed(lista_productos)
                            for i, numero in enumerate(lista_invertida, start=1):
                                print(f"{i} - {numero}")
                                volver = input(
                                    "¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                                )
                                if volver == "r":
                                    print(REGRESAR)
                                elif volver == "s":
                                    print(SALIDA)
                                else:
                                    print(ERROR)
                        else:
                            print(ERROR)
    elif menu == "4":
        if not lista_productos and not tupla_productos:
            print(SINVALOR)
        else:
            Mayor_menor = input(
                "Escoge (+) para ver el producto con mayor existencia en la lista o (-) para ver el menor. "
            )
            if Mayor_menor == "+":
                mayor = max(lista_productos)
                print(f"El producto con mayor cantidad es: {mayor}")
            elif Mayor_menor == "-":
                min_producto = min(lista_productos)
                print(f"El producto con menor cantidad es: {min_producto}")
            else:
                print(ERROR)
            regresar = input(
                "¿Desea regresar al menú (r) o salir del programa(s): (r/s) "
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
            else:
                print(ERROR)
    elif menu == "5":
        if not lista_productos and not tupla_productos:
            print(SINVALOR)
        else:
            print("Eliminar lista entera: ")
            eliminar = input(
                "¿Está seguro que desea eliminar la lista de forma permanente? (Una vez hecho esto los cambios no pueden ser revertidos): (s/n) "
            )
            if eliminar == "s":
                print("Entendido, eliminando lista...👍")
                lista_productos.clear()
                tupla_productos = tuple(lista_productos)
                print("¡Lista eliminada con éxito!")
                regresar = input(
                    "¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eliminar == "n":
                print(REGRESAR)
            else:
                print(ERROR)

    elif menu == "6":
        if not lista_productos and not tupla_productos:
            print(SINVALOR)
        else:
            print("Lista actual impresa: ")
            for i, numero in enumerate(lista_productos, start=1):
                print(f"Número: {i} - {numero}")
                regresar = input(
                    "¿Desea volver al menú(r) o salir del programa(s)?: (r/s) "
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                else:
                    print(ERROR)
    elif menu == "7":
        print(SALIDA)
        break
    else:
        print(ERROR)

    # Ejercicios finales módulo 5: Conjuntos.
    """📌 Problema:
Supón que tienes dos conjuntos de estudiantes que toman diferentes clases:

matematicas = {"Ana", "Luis", "Pedro", "Carla"}
programacion = {"Pedro", "Maria", "Luis", "Sofía"}


Encuentra los estudiantes que toman ambas clases.

Encuentra los estudiantes que solo toman una clase.

Encuentra el conjunto total de estudiantes sin duplicados.

Agrega un nuevo estudiante a programación y elimina a uno de matemáticas.

👉 Pista: usa operaciones &, |, -, .add(), .remove().
    """

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

VACIO = "Error encontrado, no puedes dejar vacío."

SINVALOR = "Error: La colección y lista actual se encuentra actualmente vacía."

matemáticas = set()

ciencias = set()

print("Alumnado por clase.📚")

while True:
    print("Menú principal:")
    menu = input(
        """
    -Oprime 1 para agregar números a la lista (10 por elección)
    -Oprime 2 para eliminar alumnos de la lista por materias
    -Oprime 3 para ordenar la lista por nombre de manera permanente
    -Oprime 4 para obtener a los estudiantes que comparten clases, los que solo toman una o para encontrar el conjunto 
    total sin duplicados
    -Oprime 5 para eliminar la lista entera (No recomendado)
    -Oprime 6 para imprimir la lista actual.
    -Oprime 7 para salir del programa
    Escoge un número en la lista: """
    )

    if menu == "1":
        for i in range(5):
            clase1 = (
                input(
                    f"Ingresa los alumnos correspondientes a la clase de matemáticas {i + 1}: "
                )
                .strip()
                .replace(" ", "")
            )
            matemáticas.add(clase1)
        print("Alumnos asignados a la clase: ")
        for i, numero in enumerate(matemáticas, start=1):
            print(f"Número: {i} - Alumno: {numero}")
        for i in range(5):
            clase2 = (
                input(
                    f"Ingresa los alumnos correspondientes a la clase de ciencias {i + 1}: "
                )
                .strip()
                .replace(" ", "")
            )
            ciencias.add(clase2)
        print("Alumnos asignados a la clase: ")
        for i, numero in enumerate(ciencias, start=1):
            print(f"Número: {i} - Alumno: {numero}")

    elif menu == "2":
        if not ciencias and not matemáticas:
            print(VACIO)
        else:
            print("Eliminador de alumnos por lista.")
            materia = input(
                "Escoge matemáticas (m) o ciencias (c) para eliminar al alumno: (m/c) "
            )
            if materia == "m":
                alumno = (
                    input("¿Qué alumno deseas eliminar de la lista?: ")
                    .strip()
                    .replace(" ", "")
                )
                if alumno in matemáticas:
                    print(f"Entendido, vas a eliminar a {alumno} de la lista.")
                    proceder = (
                        input("¿Está seguro que desea proceder?: (s/n) ")
                        .strip()
                        .replace(" ", "")
                        .lower()
                    )
                    if proceder == "s":
                        matemáticas.remove(alumno)
                        print(f"{alumno} removido de la lista con éxito.")
                        print("¡Lista actualizada!")
                        for i, alumnado in enumerate(matemáticas, start=1):
                            print(f"Número: {i} - Alumno: {alumnado}")
                    elif proceder == "n":
                        regresar = (
                            input(
                                "Entendido. ¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                            )
                            .strip()
                            .replace(" ", "")
                            .lower()
                        )
                        if regresar == "r":
                            print(REGRESAR)
                        elif regresar == "s":
                            print(SALIDA)
                            break
                        else:
                            print(ERROR)
                    else:
                        print(ERROR)
                elif alumno not in matemáticas:
                    print("Error: Alumno no encontrado en la lista.❌")
                    regresar = (
                        input(
                            "¿Qué desea hacer?: (a) para agregarlo a la lista o (v) para volver al menú?."
                        )
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "a":
                        matemáticas.add(alumno)
                        print(EXITO)
                        for i, alumnado in enumerate(matemáticas, start=1):
                            print(f"Número: {i} - Alumno: {alumnado}")
                    elif regresar == "v":
                        print(REGRESAR)
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

            elif materia == "c":
                alumno = (
                    input("¿Qué alumno deseas eliminar de la lista?: ")
                    .replace(" ", "")
                    .strip()
                )
                if alumno in ciencias:
                    print(f"Entendido, vas a eliminar a {alumno} de la lista.")
                    proceder = (
                        input("¿Está seguro que desea proceder?: (s/n) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if proceder == "s":
                        ciencias.remove(alumno)
                        print(f"{alumno} removido de la lista con éxito.")
                        print("¡Lista actualizada!")
                        for i, alumnado in enumerate(ciencias, start=1):
                            print(f"Número: {i} - Alumno: {alumnado}")
                    elif proceder == "n":
                        regresar = (
                            input(
                                "Entendido. ¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                            )
                            .lower()
                            .strip()
                            .replace(" ", "")
                        )
                        if regresar == "r":
                            print(REGRESAR)
                        elif regresar == "s":
                            print(SALIDA)
                            break
                        else:
                            print(ERROR)
                    else:
                        print(ERROR)
                elif alumno not in ciencias:
                    print("Error: Alumno no encontrado en la lista.❌")
                    regresar = (
                        input(
                            "¿Qué desea hacer?: (a) para agregarlo a la lista o (v) para volver al menú?."
                        )
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "a":
                        ciencias.add(alumno)
                        print(EXITO)
                        for i, alumnado in enumerate(ciencias, start=1):
                            print(f"Número: {i} - Alumno: {alumnado}")
                    elif regresar == "v":
                        print(REGRESAR)
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

    elif menu == "3":
        if not matemáticas and not ciencias:
            print(VACIO)
        else:
            matemáticas_lista = list(matemáticas)
            ciencias_lista = list(ciencias)
            matemáticas_lista.sort()
            ciencias_lista.sort()
            print("Lista de alumnado ordenada por nombre: Clase de ciencias 👨‍🔬")
            for alumnado in ciencias_lista:
                print(f"Alumno: {alumnado}")
            print("Lista de alumnado ordenada por nombre: Clase de matemáticas 🧮")
            for alumnado in matemáticas_lista:
                print(f"Alumno: {alumnado}")
            regresar = (
                input(
                    "¿Qué desea hacer ahora?: (r)regresar al menú o (s)salir del programa "
                )
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)

    elif menu == "4":
        if not matemáticas and not ciencias:
            print(VACIO)
        else:
            eleccion = input(
                """
            Elige (1) para obtener a los estudiantes que comparten clase
            Elige (2) para obtener los que solo toman una
            Elige (3) para encontrar el conjunto total sin duplicados
            Escoge un número: """
            )
            if eleccion == "1":
                print("Éstos son los alumnos que comparten clase: ")
                compartidos = (matemáticas).intersection(ciencias)
                for i, alumnado in enumerate(compartidos, start=1):
                    print(f"Número: {i} - Alumno: {alumnado}")
                regresar = (
                    input(
                        "¿Qué desea hacer ahora?: (v)para volver al menú o (s)para salir del programa? "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "v":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eleccion == "2":
                print("Estos son los alumnos que solo toman una clase: ")
                no_compartidos = (matemáticas).difference(ciencias)
                print("Alumnos que solo toman una clase: ")
                for i, alumnado in enumerate(no_compartidos, start=1):
                    print(f"Número {i} - Alumno: {alumnado}")
                regresar = (
                    input(
                        "¿Qué desea hacer ahora?: (v) para volver al menú o (s) para salir del programa? "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "v":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eleccion == "3":
                print(
                    "Este es el conjunto total de elementos sin duplicados (unión de las dos clases): "
                )
                conjunto_total = (matemáticas).union(ciencias)
                print("Union de las dos clases: ")
                for i, alumnado in enumerate(conjunto_total, start=1):
                    print(f"Número: {i} - Alumno: {alumnado}")
                regresar = (
                    input(
                        "¿Qué desea hacer ahora?: (v) para volver al menú o (s) para salir del programa? "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "v":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)

    elif menu == "5":
        if not matemáticas and not ciencias:
            print(SINVALOR)
        else:
            print("Eliminar lista entera: ")
            eliminar = (
                input(
                    "¿Está seguro que desea eliminar la lista de forma permanente? (Una vez hecho esto los cambios no pueden ser revertidos): (s/n) "
                )
                .lower()
                .strip()
                .replace(" ", "")
            )
            if eliminar == "s":
                print("Entendido, eliminando lista...👍")
                matemáticas.clear()
                ciencias.clear()
                print("¡Lista eliminada con éxito!")
                regresar = (
                    input("¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) ")
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eliminar == "n":
                print(REGRESAR)
            else:
                print(ERROR)

    elif menu == "6":
        if not matemáticas and not ciencias:
            print(SINVALOR)
        else:
            print("Lista actual impresa: Ciencias")
            for i, numero in enumerate(ciencias, start=1):
                print(f"Número: {i} - {numero}")
            print("Lista actual impresa: Matemáticas")
            for i, numero in enumerate(matemáticas, start=1):
                print(f"Número: {i} - {numero}")
                regresar = (
                    input("¿Desea volver al menú(r) o salir del programa(s)?: (r/s) ")
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                else:
                    print(ERROR)
    elif menu == "7":
        print(SALIDA)
        break
    else:
        print(ERROR)

    # Ejercicios finales módulo 5: Conjuntos.
    """📌 Problema:
Crea un diccionario para almacenar calificaciones de alumnos:

calificaciones = {
    "Ana": 85,
    "Luis": 90,
    "Pedro": 72,
    "Carla": 95,
    "Maria": 88
}


Imprime todos los alumnos con sus calificaciones.

Agrega un nuevo alumno con su calificación.

Modifica la calificación de un alumno existente.

Encuentra al alumno con la calificación más alta y al de la más baja.

Calcula el promedio del grupo.

👉 Pista: usa dict.items(), max(), min(), sum().
    """

from collections import defaultdict

grupos = defaultdict(
    list
)  # Diccionario para agrupar por letra inicial (A - Armando, B - Beto, etc...)

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

VACIO = "Error encontrado, no puedes dejar vacío."

SINVALOR = "Error: La colección y lista actual se encuentra actualmente vacía."

calificaciones_finales = {}

print("Calificaciones por alumno.🟰")

while True:
    print("Menú principal:")
    menu = input(
        """
    -Oprime 1 para agregar números a la lista (5 por elección)
    -Oprime 2 para eliminar alumnos o actualizar un promedio de la lista por materias
    -Oprime 3 para ordenar la lista por nombre de manera permanente
    -Oprime 4 para obtener a el o los estudiantes con los mejores y peores promedios 
    -Oprime 5 para eliminar la lista entera (No recomendado)
    -Oprime 6 para imprimir la lista actual.
    -Oprime 7 para obtener el promedio general del grupo
    -Oprime 8 para salir del programa
    Escoge un número en la lista: """
    )

    if menu == "1":
        print(
            "Instrucciones: Ingresa el nombre del alumno, posteriormente se le pedirá su respectiva calificación. "
        )
        for i in range(2):
            alumno = input(f"Ingresa al alumno {i + 1}: ").strip().replace(" ", "")
            calificacion = float(
                input(
                    f"Ingresa la calificación correspondiente al alumno número {i + 1} - {alumno}: "
                )
            )
            calificaciones_finales[alumno] = calificacion

        for alumno, calificacion in calificaciones_finales.items():
            print(f"Alumno: {alumno} - Calificacion: {calificacion}")

        regresar = (
            input(
                "¿Qué desea hacer ahora?: regresar al menú(r) o salir del programa(s) "
            )
            .lower()
            .strip()
            .replace(" ", "")
        )
        if regresar == "r":
            print(REGRESAR)
        elif regresar == "s":
            print(SALIDA)
            break
        else:
            print(ERROR)

    elif menu == "2":
        if not calificaciones_finales:
            print(VACIO)
        else:
            print("Eliminador de alumnos por lista.")
            materia = (
                input(
                    "Deseas eliminar(e) o actualizar una calificación en la lista(a): (e/a) "
                )
                .lower()
                .strip()
                .replace(" ", "")
            )
            if materia == "e":
                alumno = (
                    input("¿Qué alumno deseas eliminar de la lista?: ")
                    .strip()
                    .replace(" ", "")
                )
                if alumno in calificaciones_finales:
                    print(f"Entendido, vas a eliminar a {alumno} de la lista.")
                    proceder = (
                        input("¿Está seguro que desea proceder?: (s/n) ")
                        .strip()
                        .replace(" ", "")
                        .lower()
                    )
                    if proceder == "s":
                        calificaciones_finales.pop(alumno)
                        print(f"{alumno} removido de la lista con éxito.")
                        print("¡Lista actualizada!")
                        for alumno, calificacion in calificaciones_finales.items():
                            print(f"Alumno: {alumno} - Calificación: {calificacion}")
                    elif proceder == "n":
                        regresar = (
                            input(
                                "Entendido. ¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                            )
                            .strip()
                            .replace(" ", "")
                            .lower()
                        )
                        if regresar == "r":
                            print(REGRESAR)
                        elif regresar == "s":
                            print(SALIDA)
                            break
                        else:
                            print(ERROR)
                    else:
                        print(ERROR)
                elif alumno not in calificaciones_finales:
                    print(f"Error: El alumno {alumno} no fue encontrado en la lista.❌")
                    regresar = (
                        input(
                            "¿Qué desea hacer?: (a) para agregarlo a la lista o (v) para volver al menú?."
                        )
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "a":
                        calificacion = float(
                            input(
                                f"Agrega la calificación que tiene el alumno {alumno}: "
                            )
                        )
                        calificaciones_finales[alumno] = calificacion
                        print(EXITO)
                        for alumno, calificacion in calificaciones_finales.items():
                            print(f"Alumno: {alumno} -  Calificación: {calificacion}")
                    elif regresar == "v":
                        print(REGRESAR)
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

            elif materia == "a":
                alumno = (
                    input("¿De qué alumno deseas actualizar su calificación?: ")
                    .replace(" ", "")
                    .strip()
                )
                if alumno in calificaciones_finales:
                    print(f"Entendido, vas a actualizar el promedio de {alumno}.")
                    proceder = (
                        input("¿Está seguro que desea proceder?: (s/n) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if proceder == "s":
                        calificacion = float(
                            input(f"Ingresa el promedio nuevo del alumno {alumno}: ")
                        )
                        calificaciones_finales[alumno] = calificacion
                        print(EXITO)
                        print("¡Promedio actualizado!")
                        for alumno, calificacion in calificaciones_finales.items():
                            print(f"Alumno: {alumno} - Calificación: {calificacion}")
                    elif proceder == "n":
                        regresar = (
                            input(
                                "Entendido. ¿Desea regresar al menú(r) o salir del programa(s)?: (r/s) "
                            )
                            .lower()
                            .strip()
                            .replace(" ", "")
                        )
                        if regresar == "r":
                            print(REGRESAR)
                        elif regresar == "s":
                            print(SALIDA)
                            break
                        else:
                            print(ERROR)
                    else:
                        print(ERROR)
                elif alumno not in calificaciones_finales:
                    print(f"Error: El alumno {alumno} no fue encontrado en la lista.❌")
                    regresar = (
                        input(
                            "¿Qué desea hacer?: (a) para agregarlo a la lista o (v) para volver al menú?."
                        )
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "a":
                        calificacion = float(
                            input(
                                f"Agrega la calificación que tiene el alumno {alumno}: "
                            )
                        )
                        calificaciones_finales[alumno] = calificacion
                        print(EXITO)
                        for alumno, calificacion in calificaciones_finales.items():
                            print(f"Alumno: {alumno} -  Calificación: {calificacion}")
                    elif regresar == "v":
                        print(REGRESAR)
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

    elif menu == "3":
        if not calificaciones_finales:
            print(SINVALOR)
        else:
            print("Ordenador Alfabético de nombres.")
            lista_calificaciones = list(calificaciones_finales)
            lista_calificaciones.sort()
            print("Esta es la lista de alumnos ordenados de manera alfabética: ")
            for nombre in lista_calificaciones:
                letra = nombre[0].upper()
                grupos[letra].append(nombre)
            for letra in sorted(grupos.keys()):
                print(f"Alumnos con la letra '{letra}':")
                for nombre in sorted(grupos[letra]):
                    print(f"  - {nombre}")
            regresar = (
                input(
                    "¿Qué desea hacer ahora?: regresar al menú(r) o salir de este programa(s): "
                )
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)
    elif menu == "4":
        if not calificaciones_finales:
            print(VACIO)
        else:
            eleccion = (
                input(
                    """
    -Escoge '1' para saber cuáles son los alumnos con los mejores promedios ➕🤩
    -Escoge '2' para saber cuáles son los alumnos con los peores promedios ➖😥
    -Escoge el número de tu elección: """
                )
                .strip()
                .replace(" ", "")
            )
            if eleccion == "1":
                mejor = max(calificaciones_finales)
                print(f"Éstos son los alumnos con los mejores promedios: {mejor}")
                regresar = (
                    input("¿Desea regresar ahora al menú(r) o salir del programa(s): ")
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eleccion == "2":
                peor = min(calificaciones_finales)
                print(f"Éstos son los alumnos con los peores promedios: {peor}")
                regresar = (
                    input("¿Desea regresar ahora al menú(r) o salir del programa(s): ")
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            else:
                print(ERROR)

    elif menu == "5":
        if not calificaciones_finales:
            print(SINVALOR)
        else:
            eliminar = (
                input(
                    "⚠️ La lista de alumnos con calificaciones está por ser eliminada, esta acción no puede ser revertida después, ¿Está seguro que desea proceder?: (s/n) ⚠️"
                )
                .lower()
                .strip()
                .replace(" ", "")
            )
            if eliminar == "s":
                print("Eliminando lista...⚠️")
                calificaciones_finales.clear()
                lista_calificaciones.clear()
                print(EXITO)
                regresar = (
                    input(
                        "¿Desea regresar al menú(r) o finalizar con el programa (f): (r/f) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "f":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            elif eliminar == "n":
                print(SALIDA)
            else:
                print(ERROR)
    elif menu == "6":
        if not calificaciones_finales:
            print(SINVALOR)
        else:
            print("Lista actual impresa: ")
            for alumno, calificacion in calificaciones_finales.items():
                print(f"Alumno: {alumno} - Calificación: {calificacion}")
            regresar = (
                input("¿Desea regresar al menú (r) o salir del software(s): (r/s) ")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "r":
                print(REGRESAR)
            elif regresar == "s":
                print(SALIDA)
                break
            else:
                print(ERROR)
    elif menu == "7":
        if not calificaciones_finales:
            print(SINVALOR)
        else:
            valores_dic = calificaciones_finales.values()
            suma_valores = sum(valores_dic)
            alumnos_dic = calificaciones_finales.keys()
            total_alumnos = len(alumnos_dic)
            promedio_general = suma_valores / total_alumnos
            print(
                f"El promedio general en relación a la suma - '{suma_valores}' y la cantidad de alumnos - '{total_alumnos}' es: {promedio_general}. "
            )
            if promedio_general >= 7:
                print(
                    f"El grupo ha aprobado la materia con un promedio de: {promedio_general}🤩"
                )
                regresar = input(
                    "¿Desea regresar el menú de inicio (r) o salir del programa(s): (r/s) "
                ).lower().strip().replace(" ", "")
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
            else:
                print(
                    f"El grupo ha reprobado con un promedio no satisfactorio de {promedio_general}😥❌"
                )
                regresar = input(
                    "¿Desea regresar el menú de inicio (r) o salir del programa(s): (r/s) "
                ).lower().strip().replace(" ", "")
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else:
                    print(ERROR)
    elif menu == "8":
        print(SALIDA)
        break
    else:
        print(ERROR)
