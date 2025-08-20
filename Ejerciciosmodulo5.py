# Modulo 5, ejercicio 1: Crear una lista de frutas
# Objetivo: Aprender a declarar listas.

frutas = ["Manzana", "Pera", "Platano", "Uva", "Fresa"]

print(
    f"""Lista de compras: 
    frutas --- {frutas}"""
)

# Modulo 5, ejercicio 2: Acceder a elementos por Índice
# Objetivo: Acceder correctamente a posiciones de la lista.

print(
    f"""Este es el primer elemento de la lista: 
    {frutas[0]}
    Este es el último elemento de la lista: 
    {frutas[-1]}"""
)

# Modulo 5, ejercicio 3: Cambiar un valor de la lista.
# Objetivo: Modificar elementos existentes.

frutas[1] = "Kiwi"

print(
    f"""Lista de compras: 
    frutas --- {frutas}"""
)

# Modulo 5, ejercicio 4: Agregar Elementos
# Objetivo: Aprender append() y insert().

while True:

    agregar = input(
        """Oprime 'a' para agregar una fruta al final de la lista:
           Oprime 'p' para agregar al principio: """
    ).lower()

    if agregar == "a":
        print(
            f""" Agregando elemento...{frutas.append("Sandia")}.
              Elemento agregado con éxito: {frutas}"""
        )
    elif agregar == "p":
        print(
            f"""Agregando elemento al principio...{frutas.insert(0, "Melon")}
              Elemento agregado con éxito: {frutas}"""
        )
    else:
        print("Escoge una opción válida: a / p.")

    volver = input("¿Desea agregar más frutas?: (s/n). ").lower()
    if volver == "s":
        print("Volviendo...")
    elif volver == "n":
        print("Proceso terminado, que tenga un buen día ☺️.")
        break
    else:
        print("Error: Favor de escoger (s/n).")

# Modulo 5, ejercicio 5: Eliminar elementos
# Objetivo: Eliminar usando .remove() y .pop().


proceder = input("¿Desea eliminar alguna fruta de la lista?: (s/n). ").lower()

while proceder == "s":
    eliminar = input(f"¿Qué fruta deseas eliminar?: {frutas}. ")

    if eliminar == "Manzana":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Manzana")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    elif eliminar == "Kiwi":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Kiwi")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    elif eliminar == "Melon":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Melon")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    elif eliminar == "Plátano":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Platano")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    elif eliminar == "Uva":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Uva")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    elif eliminar == "Fresa":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Fresa")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    elif eliminar == "Sandia":
        print(f"Eliminando a {eliminar} de la lista...")
        frutas.remove("Sandia")
        print(f"Fruta eliminada satisfactoriamente de la lista🥳: {frutas}")
    else:
        print(f"No hay alguna fruta que coincida con la mencionada: '{eliminar}'.")

    elim_mas = input("¿Desea continuar eliminando más frutas?: (s/n). ")
    if elim_mas == "s":
        print(
            """Volviendo...
            Volviendo...
            Volviendo...
            Volviendo..."""
        )
    elif elim_mas == "n":
        print("Excelente, que tenga un buen día.☺️")
        break
    else:
        print("Escoge un valor correcto: s/n. ")

print("Proceso finalizado, tenga un buen día🤗.")

# Modulo 5, ejercicio 6: Ordenar y revertir la lista.
# Objetivo: Usar .sort() y .reverse().

seguir = input("¿Deseas proceder a ordenar o invertir la lista?: (s/n)").lower()

frutas_cop = ["Manzana", "Pera", "Platano", "Uva", "Fresa"]

while seguir == "s":

    manipular = input(
        "¿Desea ordenar la Lista Alfabéticamente (o) o desea revertirlo (r)?: (o/r)"
    ).lower()

    if manipular == "o":
        frutas.sort()
        print(f"Lista Actualizada correctamente: {frutas}.🥳")
        invertir = input("¿Desea invertir la lista actual?: (s/n). ")
        if invertir == "s":
            frutas.sort(reverse=True)
            print(f"Lista Actualizada nuevamente: {frutas}. 🥳")
        elif invertir == "n":
            print("Entendido, finalizando el proceso...")
        else:
            print("Por favor, agrega un valor válido: s/n.")

    elif manipular == "r":
        frutas.reverse()
        print(f"¡Lista invertida exitosamente!🥳: {frutas}")
    else:
        print("Por favor, escoge un valor válido: o/r")

    regresar = input("¿Desea revertir los cambios?: (s/n). ").lower()

    if regresar == "s":
        print(f"Lista restaurada con éxito: {frutas_cop}")
        break
    elif regresar == "n":
        print("Ok 🏋️")
        break
    else:
        print("Por favor, escoge un valor entre: s/n. ")
print("Finalizando proceso...😴")

frutas = ["Manzana", "Pera", "Platano", "Uva", "Fresa"]
# Modulo 5, ejercicio 7: Contar elementos.
# Objetivo: Usar .count() y len().

print("Contador de Frutas")

contar = input("¿Desea proceder a contar las frutas existentes hasta ahora?: (s/n). ")

if contar == "s":
    print(f"Cantidad de frutas totales: {len(frutas)}")
elif contar == "n":
    print("Entendido...")
else:
    print("Escoge un valor válido: s/n. ")

while True:

    aparece = input("¿Desea saber cuántas veces aparece una fruta de la lista?: s/n. ")

    if aparece == "s":
        fruta_veces = input(
            f"Escoge un elemento de la lista que desees saber cuántas veces está: {frutas}"
        )
        if fruta_veces == "Manzana":
            print(f"La fruta '{fruta_veces}' aparece {frutas.count("Manzana")} veces.")
        elif fruta_veces == "Pera":
            print(f"La fruta '{fruta_veces}' aparece {frutas.count("Pera")} veces.")
        elif fruta_veces == "Platano":
            print(f"La fruta '{fruta_veces}' aparece {frutas.count("Platano")} veces.")
        elif fruta_veces == "Uva":
            print(f"La fruta '{fruta_veces}' aparece {frutas.count("Uva")} veces.")
        elif fruta_veces == "Fresa":
            print(f"La fruta '{fruta_veces}' aparece {frutas.count("Fresa")} veces.")
        else:
            print("La fruta no se encuentra agregada a la lista.😥")
            agregar = input("¿Desea agregar la fruta a la lista?: s/n")
            if agregar == "s":
                print(f"Agregando fruta: {fruta_veces}")
                frutas.append(fruta_veces)
                print(f"Fruta agregada con éxito: {frutas}")
            elif agregar == "n":
                print("Entendido...")
            else:
                print("Por favor, agrega un elemento válido: s/n")

        retornar = input("¿Desea continuar (c) o desea salir (s)?: (c/s). ")
        if retornar == "c":
            print("Regresando...")
        elif retornar == "s":
            print("Entendido, terminando proceso...")
            break
        else:
            print("Escoge un valor válido: s/n. ")

    else:
        print("Entendido, deteniendo procesos... Espere...")
        break

# Modulo 5, Ejercicio 9: Crear una lista y llenarla:
# Objetivo: Llenar una lista desde el teclado.

print(
    """
    Crea una lista vacía llamada favoritos.

    -Pide al usuario 3 comidas favoritas y agrégalas con .append()."""
)

favoritos = []

bebidas_fav = []

while True:

    print("Agregando al menú tus comidas favoritas: ")

    print(
        """Couch - Para que tu plan sea lo más agradable de hacer y no afecte a tus ánimos, 
           podemos agregar comidas que sean de tu agrado."""
    )

    eleccion = input("Couch - ¿Deseas agregar alguna bebida (b) o comida (c)?: (b/c)")

    limite_agregado = 3

    while eleccion == "c":

        print(f"Couch - Tienes: {limite_agregado} comidas disponibles. ")

        if limite_agregado > 0:
            comidas = input("""Couch - ¿Qué comidas deseas agregar a tu menú?: """)
            favoritos.append(comidas)
            print(f"Comida agregada al menú: {comidas}")
            print(f"Menú actualizado: {favoritos}")
            limite_agregado -= 1
            print(f"Te restan: {limite_agregado} comidas por agregar. ")

            mas_comidas = input("Desea agregar más comidas?: (s/n) - ").lower()

            if mas_comidas == "s":
                comidas = input("Agregar comida número 2: ")
                favoritos.append(comidas)
                print(f"Comida agregada al menú: {comidas}")
                print(f"Menú actualizado: {favoritos}")
                limite_agregado -= 1
                print(f"Limite de comidas disponibles: {limite_agregado}")

                mas_comidas = input("¿Desea seguir agregando más comidas?: (s/n) - ")

                if mas_comidas == "s":
                    comidas = input("Agregar comida número 3: ")
                    favoritos.append(comidas)
                    print(f"Comida agregada al menú: {comidas}")
                    print(f"Menú actualizado: {favoritos}")
                    limite_agregado -= 1
                    print(f"Limite de comidas disponibles: {limite_agregado}")

                elif mas_comidas == "n":
                    print("Entendido...Abortando proceso...")

                else:
                    print("Por favor, elige un valor correcto: (s/n) - ")
        else:
            print("No tienes más comidas disponibles para agregar. 😥☹️")
            break

    while eleccion == "b":
        print(f"Couch - Tienes: {limite_agregado} bebidas disponibles. ")

        if limite_agregado > 0:
            bebidas = input("""Couch - ¿Qué bebida deseas agregar a tu menú?: """)
            bebidas_fav.append(bebidas)
            print(f"Bebida agregada al menú: {bebidas}")
            print(f"Menú actualizado: {bebidas_fav}")
            limite_agregado -= 1
            print(f"Te restan: {limite_agregado} bebidas por agregar. ")

            mas_comidas = input("Desea agregar más bebidas?: (s/n) - ").lower()

            if mas_comidas == "s":
                bebidas = input("Agregar bebida número 2: ")
                bebidas_fav.append(bebidas)
                print(f"Bebida agregada al menú: {bebidas}")
                print(f"Menú actualizado: {bebidas_fav}")
                limite_agregado -= 1
                print(f"Limite de bebidas disponibles: {limite_agregado}")

                mas_comidas = input("¿Desea seguir agregando más bebidas?: (s/n) - ")

                if mas_comidas == "s":
                    bebidas = input("Agregar bebida número 3: ")
                    bebidas_fav.append(bebidas)
                    print(f"Comida agregada al menú: {bebidas}")
                    print(f"Menú actualizado: {bebidas_fav}")
                    limite_agregado -= 1
                    print(f"Limite de bebidas disponibles: {limite_agregado}")

                elif mas_comidas == "n":
                    print("Entendido...Abortando proceso...")

                else:
                    print("Por favor, elige un valor correcto: (s/n) - ")
        else:
            print("No tienes más bebidas disponibles para agregar. 😥☹️")

    if limite_agregado == 0:
        print("Saliendo...Tenga un buen día...")
        break

# Modulo 5, ejercicio 10: Verificar si algo esta en una lista
# Objetivo: Usar el operador in.

acceso = input("Acceder al Buscardor de productos: (s/n). ")

while acceso == "s":

    producto = input("(__🔍Nombre del producto...__)")

    if producto in frutas:
        print("Producto encontrado🥳.")
        regresar = input("¿Desea seguir buscando más productos?: (s/n). ").lower()

        if regresar == "s":
            print("Entendido, regresando al buscador 🏋️")
        elif regresar == "n":
            print("Entendido, finalizando proceso...Espere...")
            break
        else:
            print("Escoge un valor válido: (s/n). ")

    else:
        print("El producto no se encuentra")
        agregar = input("¿Desea agregar este producto?: (s/n)").lower()

        if agregar == "s":
            frutas.append(producto)
            print(f"Fruta agregada con éxito: {frutas}")
            regresar = input("¿Desea regresar al buscador?: (s/n). ")

            if regresar == "s":
                print("Regresando...Espere...")
            elif regresar == "n":
                print(
                    """Entendido, terminando proceso...
                            Proceso terminado, tenga un buen día. 🤗"""
                )
                break
            else:
                print("Por favor, escoge un valor válido: - (s/n). ")

        elif agregar == "n":
            print("Entendido...☺️")
            regresar = input("¿Desea regresar al buscador?: (s/n). ")

            if regresar == "s":
                print("Regresando...Espere...")
            elif regresar == "n":
                print(
                    """Entendido, terminando proceso...
                         Proceso terminado, tenga un buen día. 🤗"""
                )
                break
            else:
                print("Por favor, escoge un valor válido: -- (s/n). ")

print("Abortando... saliendo del software😴")

# Modulo 5, ejercicio 11: Contador de elementos duplicados
# Objetivo: Identificar cuántas veces se repite un elemento en una lista.

pendientes = ["Módulo-5", "Curso-Inglés", "Módulo-5", "EnglishDevs"]

print("Lista de pendientes del día: ")

for i, pendiente in enumerate(pendientes, start=1):
    print(f"{i} - {pendiente}")

while True:

    elemento = input("Verificar elemento de la lista: ")

    if elemento in pendientes:
        validar = input(
            "Elemento encontrado, ¿Desea saber cuántas veces aparece en su lista?: (s/n). "
        ).lower()
        if validar == "s":
            print(
                f"Entendido, elementos totales en la lista: {pendientes.count(elemento)}"
            )  # Metodo lista.count(argumento)
            volver = input("¿Desea verificar más elementos?: (s/n). ")
            if volver == "s":
                print("Excelente, volviendo...")
            elif volver == "n":
                print("Entendido, abortando proceso...")
                break
            else:
                print("Error: Favor de escoger un valor válido - s/n. ")
        elif validar == "n":
            print("Entendido, terminando proceso... Espere...")
            break
        else:
            print("Error: El valor debe ser: s/n. ")

    else:
        validar = input(
            "Elemento no encontrado en la lista, ¿Desea agregarlo a la lista?: (s/n). "
        )

        if validar == "s":
            pendientes.append(elemento)
            print("Elemento agregado con éxito a la lista: ")
            for i, pendiente in enumerate(pendientes, start=1):
                print(f"{i} - {pendiente}")
            volver = input("¿Desea regresar al verificador?: (s/n). ")
            if volver == "s":
                print("Entendido, volviendo...")
            elif volver == "n":
                print("Entendido, finalizando proceso...")
                break
            else:
                print("Error: Favor de escoger un valor válido: s/n. ")
        elif validar == "n":
            print("Entendido, deteniendo proceso...")
            volver = input("¿Desea regresar al verificador?: (s/n). ")
            if volver == "s":
                print("Entendido, volviendo...")
            elif volver == "n":
                print("Entendido, finalizando proceso...")
                break
            else:
                print("Error: Favor de escoger un valor válido: s/n. ")
        else:
            print("Error: Por favor, escoge un valor válido: s/n. ")

# Modulo 5, ejercicio 12: Elimina por posición
# Objetivo: Eliminar un elemento de la lista basado en una posición ingresada por el usuario.

while True:

    print("Eliminador de objetos por posición")

    input("¿Desea eliminar un objeto?: (s/n). ")

    validar = input("¿Desea eliminar por posición (1) o por nombre (2)?")

    if validar == "2":
        print("Por favor, escoge un elemento de la lista: ")
        for i, pendiente in enumerate(pendientes, start=1):
            print(f"{i} - {pendiente}")
        eliminar = input("Elemento a eliminar❌: ")

        if eliminar in pendientes:
            print(
                """Entendido, eliminando elemento...
                    Espere un momento..."""
            )
            pendientes.remove(eliminar)
            print(f"Se ha eliminado '{eliminar}' de la lista.🥳")
            print("Elemento Eliminado Satisfactoriamente👍")
            validar = input(
                "¿Desea eliminar otro elemento de la lista?: (s/n). "
            ).lower()

            if validar == "s":
                print("Regresando...⬆️⬆️⬆️")
            elif validar == "n":
                print("Entendido, deteniendo el proceso✋")
                break
            else:
                print("Error, debe ser (s/n). ")
        else:
            print("Elemento no encontrado en la lista, escribe un nombre válido: ")
            for i, pendiente in enumerate(pendientes, start=1):
                print(f"{i} - {pendiente}")

    elif validar == "1":
        print("Entendido, Eliminando por posición...⬇️")
        break

    else:
        print("Error: El valor debe ser (s/n). ")

print("Lista de Pendientes:")
for i, pendiente in enumerate(pendientes, start=1):
    print(f"{i}. {pendiente}")

while True:
    try:
        indice_eliminar = int(input("Ingresa el número del elemento a eliminar: "))
        if 1 <= indice_eliminar <= len(pendientes):
            break
        else:
            print("Índice fuera de rango. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

elemento_eliminado = pendientes.pop(indice_eliminar - 1)
print(f"Se ha eliminado el pendiente '{elemento_eliminado}' de la lista.")

print("Nueva lista de pendientes:")
for i, pendiente in enumerate(pendientes, start=1):
    print(f"{i}. {pendiente}")

# Modulo 5, ejercicio 13: Fusiona listas sin duplicados
# Objetivo: Unir dos listas pero sin repetir elementos.

print("Dieta para los siguientes dos días: ")

dieta1 = {"Pollo", "Res", "Cerdo"}
print(f"Dieta día 1: {dieta1}")
dieta2 = {"Pollo", "Atún", "Pescado"}
print(f"Dieta día 2: {dieta2}")

dieta_unida = dieta1.union(dieta2)

for i, union in enumerate(dieta_unida, start=1):
    print(f"{i} - {union}")

print("Fin 👍")

# Modulo 5, ejercicio 14: Ordena y muestra extremos.
# Objetivo: Ordenar la lista y mostrar el menor y el mayor valor.

numeros = []

while True:

    agregados = int(input("Agregar numeros: "))

    numeros.append(agregados)

    print(f"Lista de números actualizada: {numeros}")

    numeros_totales = len(numeros)

    validar = input(
        """¿Desea ordenar los números en la lista o acceder al primero/último en lista (Debe tener al menos dos números)?
        Oprime (o) para ordenar | Oprime (a) para acceder al primer/último. """
    ).lower()

    if numeros_totales > 1 and validar == "o":

        print("Ordenador de Lista")

        validar = input("¿Desea ordenar el número en la lista?: (s/n). ")

        if validar == "s":
            print("Lista ordenada")
            numeros.sort()
            for numero in numeros:
                print(f"Numero - {numero}")

            validar = input(
                """¿Desea agregar más números a la lista o desea acceder al primero/último en lista?: 
            Oprime (a) para agregar más, oprime (acc) para acceder o cualquier otra tecla para terminar. """
            ).lower()
            if validar == "a":
                print("Entendido, vamos de nuevo ⬆️")

            elif validar == "acc":

                mostrar = input(
                    "Elige 1 para ver el primer elemento de la lista o 2 para ver el último. "
                )
                if mostrar == "1":
                    print(
                        f"""Cargando primer Elemento...
                        El primer elemento es: {numeros[0]}"""
                    )
                elif mostrar == "2":
                    print(
                        f"""Cargando segundo Elemento...
                        El último elemento es: {numeros[-1]}"""
                    )
                else:
                    print("Escoge un número válido (1/2)")
            else:
                print("Perfecto, tu decides, terminando...")
                break

        elif validar == "n":
            print("Ok, saliendo del proceso...😴")
            break

        else:
            print("Error: Escoge un valor válido: (s/n). ")

    elif numeros_totales > 1 and validar == "a":
        mostrar = input(
            "Elige 1 para ver el primer elemento de la lista o 2 para ver el último"
        )

        if mostrar == "1":
            print(
                f"""Cargando primer Elemento...
                  El primer elemento es: {numeros[0]}"""
            )
        elif mostrar == "2":
            print(
                f"""Cargando segundo Elemento...
                  El último elemento es: {numeros[-1]}"""
            )
        else:
            print("Escoge un número válido (1/2)")
print("Proceso Terminado✋ ☺️")

# Modulo 5, ejercicio 15: Juego de adivinanza de frutas
# Objetivo: Adivinar un elemento que se encuentra dentro de una lista.

print(
    """Lista de números secretos🫣. 
      Instrucciones: Juego de dos, reta a un amigo a adivinar las palabras que tu irás agregando a una lista. 
      Tu compañero solo dispondrá de 3 vidas ❤️ ❤️ ❤️ para adivinar las palabras que tú añadirás a la lista.
      Puedes ayudarle dándole 3 pistas solamente 🕵️ 🕵️ 🕵️."""
)

while True:

    vidas = 3

    intentos = 1

    lista_adivinanza = []

    pistas = []

    comenzar = input("¿Quieres comenzar el reto?: (s/n)🔥😈. ").lower()

    print("Turno del creador de palabras secretas🙊: ")

    if comenzar == "s":
        palabra_secreta = input("Escribe la primer palabra: ")
        lista_adivinanza.append(palabra_secreta)
        pista = input("Crea la primer pista: ")
        pistas.append(pista)

        palabra_secreta = input("Escribe la segunda palabra: ")
        lista_adivinanza.append(palabra_secreta)
        pista = input("Crea la segunda pista: ")
        pistas.append(pista)

        palabra_secreta = input("Escribe la tercer palabra: ")
        lista_adivinanza.append(palabra_secreta)
        pista = input("Crea la tercer pista: ")
        pistas.append(pista)

        print(f"Turno del Adivinador🔮. Tienes {vidas} vidas para adivinar.")

        if vidas > 0 and intentos <= 3:
            intento = input(
                f"""Primer intento: 
                  Pista: {pistas[0]}
                  *** """
            )

            if intento in lista_adivinanza:
                print(
                    f"Lo lograste. Felicidades, lo conseguiste en el intento número: {intentos}"
                )
                volver = input("¿Deseas volver a jugar?: (s/n). ").lower()
                if volver == "s":
                    print("Regresando...⬆️")
                elif volver == "n":
                    print("Entendido, saliendo del juego ➡️")
                else:
                    print("Error: Escoge un valor entre - (s/n). ")
            elif intento not in lista_adivinanza:
                intentos += 1
                vidas -= 1
                print(
                    f"Fallaste, {intento} no era la palabra secreta 😥, te restan: {vidas} ❤️❤️ vidas. "
                )
                intento = input(
                    f"""Segundo intento: 
                  Pista: {pistas[1]}
                  *** """
                )
                if intento in lista_adivinanza:
                    print(
                        f"Lo lograste. Felicidades, lo conseguiste en el intento número: {intentos}"
                    )
                    volver = input("¿Deseas volver a jugar?: (s/n). ").lower()
                    if volver == "s":
                        print("Regresando...⬆️⬆️")
                    elif volver == "n":
                        print("Entendido, saliendo del juego ➡️➡️")
                    else:
                        print("Error: Escoge un valor - (s/n). ")
                elif intento not in lista_adivinanza:
                    intentos += 1
                    vidas -= 1
                    print(
                        f"Fallaste, {intento} no era la palabra secreta 😥, te restan: {vidas} ❤️ vidas. "
                    )
                    intento = input(
                        f"""Último intento: 
                    Pista: {pistas[-1]}
                    *** """
                    )
                    if intento in lista_adivinanza:
                        print(
                            f"Lo lograste. Felicidades, lo conseguiste en el intento número: {intentos}"
                        )
                        volver = input("¿Deseas jugar de nuevo?: (s/n). ").lower()
                        if volver == "s":
                            print("Regresando...⬆️")
                        elif volver == "n":
                            print("Entendido, saliendo del juego ➡️")
                        else:
                            print("Error: Escoge un valor entre - (s/n). ")
                    elif intento not in lista_adivinanza:
                        intentos += 1
                        vidas -= 1
                        print("Perdiste, no te quedan más vidas.😥❌")
                        volver = input("¿Deseas jugar de nuevo?: (s/n). ").lower()
                        if volver == "s":
                            print("Regresando ...🔥 Vidas Reestablecidas: ❤️❤️❤️")
                        elif volver == "n":
                            print("Entendido, saliendo del juego 🤡")
                        else:
                            print("Error: Escoge un valor entre (s/n). ")
    elif comenzar == "n":
        print("Entendido, tu te lo pierdes... Cerrando Juego ☺️")
        break

    else:
        print("Debe ser un valor: (s/n)")

print("Saliste del Juego, Vuelve pronto ☺️.")

# Ejercicios del 16 - 20:

# Modulo 5, Ejercicio 16: Generador de tabla de multiplicar avanzada
# Objetivo: Dado un número del usuario, genera su tabla de multiplicar del 1 al 10, pero en formato de lista y con validación.
while True:

    ingresar = input("¿Desea ingresar al multiplicador de multiplicaciones?: (s/n). ")

    if ingresar == "s":

        numero = int(input("Por favor, elige un número del 1 al 100: "))

        if 1 < numero > 100:
            print("El número es incorrecto: Rango permitido es 1-100")
            intentar = input("¿Desea volver a intentarlo?: (s/n). ").lower()
            if intentar == "s":
                print("Entendido, regresando...⬆️")
            elif intentar == "n":
                print("Terminando programa...⬇️")
                break
            else:
                print("Por favor, escoge un valor válido: (s/n). ")
        else:
            tabla_numero = [numero * i for i in range(1, 11)]
            print(f"Tabla de Multiplicar del número: {numero}")
            for i in range(1, 11):
                print(f"{numero} x {i}= {tabla_numero[i-1]}")
            intentar = input(
                "¿Desea regresar a crear una tabla de multiplicar?: (s/n). "
            ).lower()
            if intentar == "s":
                print("Regresando...⬆️⬆️⬆️")
            elif intentar == "n":
                print("Finalizando proceso...Saliendo ⬇️")
                break
            else:
                print("Por favor, escoge un valor válido: (s/n). ")
    elif ingresar == "n":
        print("Entendido, abortando proceso...⬇️")
        break
    else:
        print("Error: Escoge un valor entre (s/n). ")

print("Programa Finalizado. Tenga un buen día ☺️")

# Modulo 5, ejercicio 17: Invertir lista de calificaciones.
# Objetivo: Crea una lista con 5 calificaciones ingresadas por el usuario y luego imprímelas al revés.
import math

cal_programacion = []

cal_bd = []

cal_redes = []


while True:

    print("{} Programación: ")
    programacion = int(input("Ingresa la calificación Módulo - 1: "))
    cal_programacion.append(programacion)

    programacion = int(input("Ingresa la calificación Módulo - 2: "))
    cal_programacion.append(programacion)

    programacion = int(input("Ingresa la calificación Módulo - 3: "))
    cal_programacion.append(programacion)
    print(f"Califaciones registradas: {cal_programacion}")

    print("📈 Base de Datos:")
    base_datos = int(input("Ingresa la calificación Módulo 1: "))
    cal_bd.append(base_datos)

    base_datos = int(input("Ingresa la calificación Módulo 2: "))
    cal_bd.append(base_datos)

    base_datos = int(input("Ingresa la calificación Módulo 3: "))
    cal_bd.append(base_datos)
    print(f"Califaciones registradas: {cal_bd}")

    print("🛜Redes: ")
    redes = int(input("Ingresa la calificación Módulo 1: "))
    cal_redes.append(redes)

    redes = int(input("Ingresa la calificación Módulo 2: "))
    cal_redes.append(redes)

    redes = int(input("Ingresa la calificación Módulo 3: "))
    cal_redes.append(redes)
    print(f"Califaciones registradas: {cal_redes}")

    print("Éstas son las calificaciones registradas: ")

    print("Programación: ")
    for i, calificacion in enumerate(cal_programacion, start=1):
        print(f"{i} - {calificacion}")
    sum_cal = sum(cal_programacion)
    total = len(cal_programacion)
    promedio_pro = sum_cal / total
    print(f"Promedio - Programación: {math.ceil(promedio_pro)}")
    if promedio_pro < 7:
        print("❌Programación Reprobada, acumulada al semestre que viene.❌")

    print("Bases de Datos: ")
    for i, calificacion in enumerate(cal_bd, start=1):
        print(f"{i} - {calificacion}")
    sum_cal = sum(cal_bd)
    total = len(cal_bd)
    promedio_bd = sum_cal / total
    print(f"Promedio - Base de Datos: {math.ceil(promedio_bd)}")
    if promedio_bd < 7:
        print("❌Bases de Datos Reprobada, acumulada al semestre que viene.❌")

    print("Redes: ")
    for i, calificacion in enumerate(cal_redes, start=1):
        print(f"{i} - {calificacion}")
    sum_cal = sum(cal_redes)
    total = len(cal_redes)
    promedio_red = sum_cal / total
    print(f"Promedio - Redes: {math.ceil(promedio_red)}")
    if promedio_red < 7:
        print("❌Redes, acumulada al semestre que viene.❌")

    promedio_general = (promedio_red + promedio_bd + promedio_pro) / 3
    print(
        f"El promedio general redondeado del Alumno es: {math.ceil(promedio_general)}"
    )

    if promedio_general < 7:
        print("El alumnos no acreditó el semestre, deberá repetirlo❌✋ ")
        proceder = input("¿Desea corregir la lista (0) o desea proceder(1)?: . ")
        if proceder == "0":
            print("Ok, volviendo arriba ⬆️")
        elif proceder == "1":
            print(
                """Entendido, Subiendo calificaciones... Espere...
                Subiendo...
                Subiendo...
                
                Excelente, Calificaciones subidas ⏫👍"""
            )
            break
        else:
            print("Favor de escoger entre 1 y 0. ")
    else:
        print(
            f"El alumno acreditó el semestre con un promedio general de: {promedio_general}"
        )
        proceder = input("¿Desea corregir la lista (0) o desea proceder(1)?: . ")
        if proceder == "0":
            print("Ok, volviendo arriba ⬆️")
        elif proceder == "1":
            print(
                """Entendido, Subiendo calificaciones... Espere...
                Subiendo...
                Subiendo...
                
                Excelente, Calificaciones subidas ⏫👍"""
            )
            break
        else:
            print("Favor de escoger entre 1 y 0. ")
print("Proceso Finalizado, tenga un buen día👍 ☺️")

# Modulo 5, ejercicio 18: Juego de encontrar la palabra clave
# Objetivo: El usuario tiene que adivinar una palabra secreta que se encuentra en una lista predefinida.

print("Adivina la palabra secreta: El juego de adivinanza, para dos jugadores")
print("\n")  # Salto de línea básico
print(
    """Instrucciones: El juego consta de dos jugadores, el adivinador y el que crea las adivinanzas.
Jugador 1: Tu rol será crear una lista de 5 palabras que serán de utilidad para adivinar la palabra secreta que proporcionarás después🤫. 
Jugador 2: Tu rol será adivinar las palabra secreta del jugador 1, tendrás 3 vidas para hacerlo ❤️ ❤️ ❤️."""
)
print("\n")


lista_palabras = []

vidas = 3

intentos = 1


while True:

    print("Turno del Jugador 1: Crea la lista y la palabra secreta. ")
    print("\n")
    palabras = input(
        "Palabra 1 (Recuerda que esta debe ayudar a descubir la palabra secreta): "
    )
    lista_palabras.append(palabras)

    palabras = input(
        "Palabra 2 (Recuerda que esta debe ayudar a descubir la palabra secreta): "
    )
    lista_palabras.append(palabras)

    palabras = input(
        "Palabra 3 (Recuerda que esta debe ayudar a descubir la palabra secreta): "
    )
    lista_palabras.append(palabras)

    palabras = input(
        "Palabra 4 (Recuerda que esta debe ayudar a descubir la palabra secreta): "
    )
    lista_palabras.append(palabras)

    palabras = input(
        "Palabra 5 (Recuerda que esta debe ayudar a descubir la palabra secreta): "
    )
    lista_palabras.append(palabras)

    print("Es momento de crear la palabra secreta🔒: ")
    SECRETA = input("Escribe la palabra secreta a adivinar🤫🤭: ")
    print("Palabra secreta guardada con éxito🤫👍...")
    print("\n")
    print(f"Turno del adivinador. Posees ahora mismo: {vidas} vidas.")

    print("Observa la lista que crearon para ti: ")

    for i, elemento in enumerate(lista_palabras, start=1):
        lista_palabras.sort()
        print(f"{i} - {elemento}")

    print("LLegó tu turno de adivinar la palabra secreta 🕵️: ")
    print(f"Si es {lista_palabras[0]} y {lista_palabras[1]}")
    intento = input(f"Intento {intentos}: ")
    if intento in SECRETA:
        print(
            f"Ganaste🥳, eres todo un adivinador🔥 encontraste la palabra secreta en el intento número: {intentos}"
        )
        volver = input("¿Desea volver a jugar?: (s/n) ")
        if volver == "s":
            print("Tú decides capitán, regresando... ⬆️")
        elif volver == "n":
            print("Entendido, abortando el proceso... Saliendo ⬇️")
            break
    else:
        intentos += 1
        vidas -= 1
        print(
            f"Fallataste, {intento} no era la palabra secreta, te restan: {vidas} vidas"
        )
        print("\n")

        print(f"Si es {lista_palabras[2]} y {lista_palabras[3]}")
        intento = input(f"Intento número {intentos}: ")
        if intento in lista_palabras:
            print(
                f"Ganaste🥳, 😏nada mal, lo lograste esta vez en el intento: {intentos}"
            )
            volver = input("¿Desea volver a jugar 🔥?: (s/n) ")
            if volver == "s":
                print("Vamos a ello, volviendo...♻️")
            elif volver == "n":
                print("Ok, Jugador 1 gana🥳, saliendo del juego...")
                break
            else:
                print("Escoge entre (s/n). ")
        else:
            intentos += 1
            vidas -= 1
            print(
                f"Fallataste de nuevo, {intento} no era la palabra secreta, ahora te restan: {vidas} vidas"
            )
            print("\n")

            print(f"Es tu último intento😥, piensa bien, si es... {lista_palabras[4]}")
            intento = input(f"Intento número {intentos}: ")
            if intento in lista_palabras:
                print(
                    f"Ganaste🥳, 😏nada mal, lo lograste esta vez en el intento: {intentos}"
                )
                volver = input(
                    "¿Desea volver a jugar el juego de la adivinanza?: (s/n) "
                ).lower()
                if volver == "s":
                    print("Volviendo al inicio...♻️")
                elif volver == "n":
                    print("Entendido, cerrando juego ⬇️...")
                    break
                else:
                    print("Escoge un valor entre s/n. ")
            else:
                intentos += 1
                vidas -= 1
                print(
                    f"Perdiste😭, {intento} no era la palabra secreta, tus vidas: {vidas} vidas"
                )
                print(f"La palabra secreta es: {SECRETA}")
                print("\n")

                volver = input(
                    "Jugador 1 Gana🥳, al adivinador ya no le quedan vidas - ¿Desea Volver a Jugar?: (s/n) "
                ).lower()
                if volver == "s":
                    vidas += 3
                    intentos -= 3
                    print("Tú no te rindes, eso me gusta, reseteando vidas ♻️...")
                elif volver == "n":
                    print("Te rindes ¿eh?, bien no te culpo...⬇️ Saliendo...")

print("Juego Finalizado, Tenga un Buen día ☺️❤️.")

# Modulo 5, ejercicio 19: Números Pares y suma total.
# Objetivo: Pide al usuario 10 números y determina cuáles son pares. Al final, imprime la suma de todos los números pares ingresados.

print("Detector de números pares")

lista_nums = []

lista_pares = []

suma_pares = 0

while True:

    print(
        "Ingresa 10 números, cuales sean, el detector arrojará de manera automática los números pares y su suma al final. "
    )

    for i in range(10):
        nums = int(input(f"Ingresa el número {i + 1}: "))#Evita repeticiones de código innecesarias.
        lista_nums.append(nums)

    print("Esta es la lista creada hasta el momento: ")
    for i, numero in enumerate(lista_nums, start=1):
        print(f"{i} - {numero}")
    ordenar = input("¿Desea ordenar los números de la lista?: (s/n) ")
    if ordenar == "s":
        lista_nums.sort()
        print("Ok, ordenando números... Espere...")
        print("Lista ordenada:")
        for i, numero in enumerate(lista_nums, start=1):
            print(f"{i} - {numero}")
    elif ordenar == "n":
        print("Entendido, continuando proceso...")
    else:
        print(f"Regresando, '{ordenar}' no es una respuesta válida.")
        continue
    print("Ahora estamos ingresando al detector de pares...")

    for numero in lista_nums:
        if numero % 2 == 0:
            lista_pares.append(numero)
            suma_pares += numero
    print("Esta es la lista de números pares: ")
    for i, numero in enumerate(lista_pares, start=1):
        print(f"{i} - {numero}")
    ordenar = input("¿Desea ordenar la lista de pares?: (s/n) ")
    if ordenar == "s":
        lista_pares.sort()
        print("Lista de pares ordenada:")
        for i, numero in enumerate(lista_pares, start=1):
            print(f"{i} - {numero}")
    elif ordenar == "n":
        print("Entendido, continuando proceso...")
    else:
        print("Error, {ordenar} no es un valor válido. Regresando ⬆️")
        continue

    print(f"La suma de los números pares es: {suma_pares}")
    volver = input("¿Desea volver a ingresar números?: (s/n) ")
    if volver == "s":
        print("Entendido, vamos al inicio ♻️")
        lista_nums.clear()
        lista_pares.clear()
    elif volver == "n":
        print("Ok, no pasa nada, Saliendo ⬇️")
        break
    else:
        print("Por favor, escoja un valor (s/n).")

print("Detector cerrado, tenga un buen día ☺️👍")

# Modulo 5, ejercicio 20:  Encuentra el carácter más repetido en un string
# Objetivo: El usuario ingresa una palabra y el sistema detecta qué carácter se repite más veces.
print("Encuentra el carácter más repetido en un string")

while True: 
    texto = input(
        "Por favor, escribe una palabra o frase (sin espacios o con espacios): "
    ).strip()
    if not texto:
        print("Entrada vacía. Intente de nuevo ⬆️")
    else:
        texto = texto.lower()
        texto = texto.replace(
            " ", ""
        )  # eliminar espacios (quita esta línea si quieres contar espacios)

        counts = {}
        for ch in texto:
            counts[ch] = counts.get(ch, 0) + 1

        max_count = max(counts.values())

        # Obtener todos los caracteres que tengan ese máximo (por si hay empate)
        mas_repetidos = [ch for ch, c in counts.items() if c == max_count]

        # Mostrar resultado
        if len(mas_repetidos) == 1:
            print(
                f"El caracter más repetido es '{mas_repetidos[0]}' con {max_count} apariciones."
            )
        else:
            chars = ", ".join(f"'{c}'" for c in mas_repetidos)
            print(
                f"Hay un empate. Los caracteres más repetidos son {chars}, cada uno con {max_count} apariciones."
            )
        volver = input("¿Desea volver a contar las letras?: (s/n) ").lower()
        if volver == "s":
            print("Entendido... volviendo arriba.")
            counts.clear()
        elif volver == "n":
            print("Entendido, terminando proceso...⬇️👍")
            break
        else:
            print("Por favor, escoge un valor correcto: s/n. ")

# Modulo 5, ejercicio número 21: COntador de letras en una Palabra.
# Objetivo: Crea un programa que cuente cuántas veces aparece cada letra en una palabra dada por el usuario usando un diccionario.

print("Contador de letras por Texto🔥")

título = input(
    "Antes de iniciar el contador de palabras, puedes escoger un título o tu amig(a) si estás en compañía para el contador (No palabras obscenas ⚠️)"
)

título_lower = título.title

print(
    """\n By 'Kevin Meza'. 
      -Instrucciones:
      1. Elige una palabra, texto u oración, cuál sea. 
      2. Ponte cómodo y deja que el contador lo haga de forma automática. 
      3. Disfruta"""
)

while True:
    palabra = input(
        f"Bienvenido a {título}, tu contador de palabras profesional, por favor ingresa la palabra, frase u oración: "
    ).strip()

    if not palabra:
        print("Error: El campo no debe quedar vacío😒.")
    else:

        palabra = palabra.lower()

        palabra = palabra.replace(" ", "")

        conteo = {}

        for letra in palabra:
            conteo[letra] = conteo.get(letra, 0) + 1

        print(
            f"""Para la palabra: {palabra} - Tenemos: 
            Letras{conteo.keys()} - Repeticiones: {conteo.values()}"""
        )
        volver = input("¿Desea volver a ingresar una Palabra? - (s/n): ").lower()
        if volver == "s":
            print("Entendido, vamos arriba... 👍⬆️")
        elif volver != "s":
            print("Entendido, terminado proceso, tenga un maravilloso día👋.")
            break
        else:
            print("Por favor, debe elegir un valor válido: sea s/n. ")

# Modulo 5, ejercicio número 22: Actualizar Inventario.
# Objetivo: Realiza un inventario donde:
"""
-Pide al usuario una fruta y la cantidad que quiere agregar.

-Si la fruta existe, súmale la cantidad.

-Si no existe, agrégala con esa cantidad.

-Tip: Usa .update() o asignación directa."""

print("Sistema Inventariado de frutas para la empresa Kevin Developers.")

usuarios = {
    "user1": {"nombre": "Kevin", "contraseña": "Guffy"},
    "user2": {"nombre": "Isis", "contraseña": "Harley"},
}

bd_Frutas = {}

intentos = 3

while True:

    ingresar = input("Ingresa tu nombre de usuario: ").strip().replace(" ", "")

    contraseña = input("Ingresa la contraseña: ").strip().replace(" ", "")

    if ingresar in usuarios and usuarios[ingresar]["contraseña"] == contraseña:
        print(f"Bienvenid(a) {usuarios[ingresar]["nombre"]}")
        fruta = (
            input("Ingresa la fruta que desees agregar: ")
            .strip()
            .lower()
            .replace(" ", "")
        )

        try:
            cantidad = int(input(f"Ingresa la cantidad de {fruta} que deseas: "))
        except ValueError:
            print("Error encontrado: Debes ingresar un número entero.")
            continue

        print("Valores agregados: ")

        print(f"{fruta.title()}: {cantidad}")

        proceder = (
            input(
                "¿Los datos son correctos ('s' para proceder 'n' para volver)?: (s/n) "
            )
            .lower()
            .strip()
        )

        if proceder == "s":

            fruta = fruta.lower().strip().replace(" ", "")

            if fruta in bd_Frutas:

                print(
                    f"La fruta '{fruta}' ya existe y tiene: {bd_Frutas[fruta]} frutas."
                )

                bd_Frutas[fruta] += cantidad

                print("¡Lista actualizada con éxito!👍.")

                for fruta, cantidad in bd_Frutas.items():
                    print(f"{fruta} ➡️ {bd_Frutas[fruta]}")

                volver = (
                    input(
                        "¿Desea volver a ingresar más frutas (v), salir (s) o desea acceder al eliminador de frutas (e)?: (v/s/e) "
                    )
                    .lower()
                    .strip()
                )

                if volver == "v":
                    print("Entendido, volviendo... Espere ⬆️")
                elif volver == "s":
                    print("Entendido, estamos finalizando proceso, feliz día ☺️.")
                    break
                elif volver == "e":

                    print("Eliminador de elementos")

                    print("Lista actual: ")

                    for fruta, cantidad in bd_Frutas.items():
                        print(f"{fruta} ➡️ {bd_Frutas[fruta]}")

                    eliminar = (
                        input(
                            "¿Desea eliminar toda la lista (t) o un elemento de la lista (l): "
                        )
                        .lower()
                        .strip()
                    )

                    if eliminar == "t":
                        proceder = (
                            input(
                                "⚠️ ¿Está seguro que desea proceder?, si procede se eliminarán todos los datos de la base ⚠️: (s/n) "
                            )
                            .lower()
                            .strip()
                            .replace(" ", "")
                        )
                        if proceder == "s":
                            print(
                                "Entendido, eliminando toda la información de la Base de datos..."
                            )
                            bd_Frutas.clear()
                            print("Base de datos eliminada con éxito👍")
                            volver = (
                                input(
                                    "¿Desea volver a ingresar frutas (v) o desea salir (s)?: "
                                )
                                .lower()
                                .strip()
                            )
                            if volver == "v":
                                print("Regresando....⬆️")
                            elif volver == "s":
                                print("Saliendo, tenga un buen día ☺️👋")
                                break
                            else:
                                print("Error: Se debe asignar un valor válido: v/s")
                    elif eliminar == "l":
                        eliminar_original = input("¿Qué elemento desea eliminar?: ")
                        if eliminar_original in bd_Frutas:
                            bd_Frutas.pop(eliminar_original)
                            print(
                                f"{eliminar_original} eliminado correctamente de la base de datos"
                            )
                            print("Base de datos actualizada: ")
                            for fruta, cantidad in bd_Frutas.items():
                                print(f"{fruta} ➡️ {bd_Frutas[fruta]}")
                                volver = input(
                                    "¿Desea seguir eliminando elementos?: (s/n)"
                                )
                                if volver == "s":
                                    print("Entendido, volviendo arriba ⬆️⬆️⬆️")
                                elif volver == "n":
                                    print("Entendido, terminando proceso...")
                                    break
                                else:
                                    print("Error, solo puedes escoger (s/n).")
                        else:
                            print("El elemento no se encuentra en la Base de datos...")
                            agregar = input(
                                "¿Desea agregar el elemento a la base de datos?: (s/n)"
                            )

                            if agregar == "s":
                                print(
                                    "Entendido, agregando elemento a la Base de datos"
                                )
                                try:
                                    cantidad = int(
                                        input("Agrega una cantidad al elemento: ")
                                    )
                                    bd_Frutas[eliminar_original] = cantidad
                                    print(
                                        f"{eliminar_original} agregado correctamente."
                                    )
                                except ValueError:
                                    print("Error: Debes ingresar un número entero.")
                                volver = input("¿Dese finalizar el proceso? (s/n) ")
                                if volver == "s":
                                    print("Entendido, finalizando proceso...⬇️")
                                elif volver == "n":
                                    print("Entendido, volviendo al inicio👍")
                                else:
                                    print("Error de escritura, debe ser: (s/n)")
                            elif agregar == "n":
                                print("Entendido👍")
                                volver = input("¿Desea volver a intentarlo?: (s/n)")
                                if volver == "s":
                                    print("Entendido, volviendo a intentar...")
                                elif volver == "n":
                                    print("Entendido, abortando proceso...⬇️")
                                else:
                                    print(
                                        "Error de escritura:valor no válido, debe ser (s/n). "
                                    )
                    else:
                        print("Valor no válido, debe ser: t/l. ")
                else:
                    print("Error: Debe escoger un valor válido: v - s- e")

            else:

                bd_Frutas[fruta] = cantidad

                print(f"¡{fruta.title()} agregada con éxito!")

                print("Esta es la fruta agregada: ")

                print(f"Fruta: {fruta.title()} ➡️ Cantidad: {cantidad}")

                imprimir = (
                    input("¿Desea imprimir los datos de la Base actual?: (s/n) ")
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if imprimir == "s":
                    print("Base de datos actual: ")
                    for fruta, cantidad in bd_Frutas.items():
                        print(f"Fruta: {fruta} - Cantidad: {cantidad}")

                    volver = (
                        input(
                            "¿Desea volver a ingresar más frutas (v), salir (s) o desea acceder al eliminador de frutas (e)?: (v/s/e) "
                        )
                        .lower()
                        .strip()
                    )

                    if volver == "v":
                        print("Entendido, volviedo... Espere ⬆️")
                    elif volver == "s":
                        print("Entendido, finalizando proceso, feliz día ☺️.")
                        break
                    elif volver == "e":

                        print("Eliminador de elementos")

                        print("Lista actual: ")

                        for fruta, cantidad in bd_Frutas.items():
                            print(f"{fruta} ➡️ {bd_Frutas[fruta]}")

                        eliminar = (
                            input(
                                "¿Desea eliminar toda la lista (t) o un elemento de la lista (l): "
                            )
                            .lower()
                            .strip()
                        )

                        if eliminar == "t":
                            proceder = input(
                                "⚠️ ¿Está seguro que desea proceder?, si procede se eliminarán todos los datos de la base ⚠️: (s/n) "
                            )
                            if proceder == "s":
                                print(
                                    "Entendido, eliminando toda la información de la Base de datos..."
                                )
                                bd_Frutas.clear()
                                print("Base de datos eliminada con éxito👍")
                                volver = (
                                    input(
                                        "¿Desea volver a ingresar frutas (v) o desea salir (s)?: "
                                    )
                                    .lower()
                                    .strip()
                                )
                                if volver == "v":
                                    print("Regresando....⬆️")
                                elif volver == "s":
                                    print("Saliendo, tenga un buen día ☺️👋")
                                    break
                                else:
                                    print("Error: Se debe asignar un valor válido: v/s")
                        elif eliminar == "l":
                            eliminar_original = input("¿Qué elemento desea eliminar?: ")
                            if eliminar_original in bd_Frutas:
                                bd_Frutas.pop(eliminar_original)
                                print(
                                    f"{eliminar_original} eliminado correctamente de la base de datos"
                                )
                                print("Base de datos actualizada: ")
                                for fruta, cantidad in bd_Frutas.items():
                                    print(f"{fruta} ➡️ {bd_Frutas[fruta]}")
                                    volver = input(
                                        "¿Desea seguir eliminando elementos?: (s/n)"
                                    )
                                    if volver == "s":
                                        print("Entendido, volviendo arriba ⬆️⬆️⬆️")
                                    elif volver == "n":
                                        print("Entendido, terminando proceso...")
                                        break
                                    else:
                                        print("Error, solo puedes escoger (s/n).")
                            else:
                                print(
                                    "El elemento no se encuentra en la Base de datos..."
                                )
                                agregar = input(
                                    "¿Desea agregar el elemento a la base de datos?: (s/n)"
                                )

                                if agregar == "s":
                                    print(
                                        "Entendido, agregando elemento a la Base de datos"
                                    )
                                    try:
                                        cantidad = int(
                                            input("Agrega una cantidad al elemento: ")
                                        )
                                        bd_Frutas[eliminar_original] = cantidad
                                        print(
                                            f"{eliminar_original} agregado correctamente."
                                        )
                                    except ValueError:
                                        print("Error: Debes ingresar un número entero.")
                                    volver = input("¿Dese finalizar el proceso? (s/n) ")
                                    if volver == "s":
                                        print("Entendido, finalizando proceso...⬇️")
                                    elif volver == "n":
                                        print("Entendido, volviendo al inicio👍")
                                    else:
                                        print("Error de escritura, debe ser: (s/n)")
                                elif agregar == "n":
                                    print("Entendido👍")
                                    volver = input("¿Desea volver a intentarlo?: (s/n)")
                                    if volver == "s":
                                        print("Entendido, volviendo a intentar...")
                                    elif volver == "n":
                                        print("Entendido, abortando proceso...⬇️")
                                    else:
                                        print(
                                            "Error de escritura:valor no válido, debe ser (s/n). "
                                        )
                        else:
                            print("Valor no válido, debe ser: t/l. ")
                    else:
                        print("Error: Debe escoger un valor válido: v - s- e")
                elif imprimir == "n":
                    print("Entendido 👍☺️")
                    volver = input("¿Desea volver a ingresar más frutas?: (s/n) ")

                    if volver == "s":
                        print("Entendido, volviedo... Espere ⬆️")
                    elif volver == "n":
                        print("Entendido, finalizando proceso, feliz día ☺️.")
                        break
                    else:
                        print("Error: Debe escoger un valor válido: s - n")
        elif proceder == "n":
            print("Repitiendo proceso...♻️")
        else:
            print("Error de escritura: Debe escoger un valor entre s - n")

    elif (
        ingresar not in usuarios or usuarios[ingresar]["contraseña"] != contraseña
    ) and intentos > 1:
        intentos -= 1
        print("Error, usuario o contraseña inválidos. Intenta nuevamente")
        print(f"⚠️ Te restan solo: {intentos} intentos, sino se bloqueará el acceso.")

    else:
        print("Te has quedado sin intentos, acceso a base de datos BLOQUEADO❌.")
        break

print("Base de datos frutas cerrada👋")

# Modulo 5, ejercicio número 23: Diccionario Invertido.
# Objetivo: Crea un nuevo diccionario con los valores como claves y las claves como valores.

print("Diccionario invertido: Países y sus capitales.🗺️")

dic_normal = {}

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

while True:

    print(
        "Instrucciones: Agrega 3 países con sus 3 respectivas capitales para agregarlas a la base de datos. "
    )

    for i in range(3):
        pais = input(
            f"Ingresa el nombre del país que desees {i + 1}: "
        ).strip()  # Evita repeticiones de código innecesarias.
        capital = input(f"Escribe el nombre de la capital de ese país {i + 1}:").strip()
        dic_normal[pais] = capital
    print("Esta es la base de datos creada: ")
    for pais, capital in dic_normal.items():
        print(f"País: {pais} - Capital: {capital}")

    invertir = input(
        "¿Desea ver la información en el panel de vista invertida(i), eliminar/actualizar algún dato de la base (e) o ninguna de las dos (n)?: (i/e/n) "
    )
    if invertir == "i":
        dic_invertido = {v: k for k, v in dic_normal.items()}
        print("Base de datos invertida con éxito💯")
        for capital, pais in dic_invertido.items():
            print(f"Capital: {capital} - País: {pais}")
        regresar = (
            input("¿Desea volver a ingresar valores a la base de datos?: (s/n) ")
            .lower()
            .strip()
            .replace(" ", "")
        )
        if regresar == "s":
            print(REGRESAR)
        elif regresar == "n":
            print(SALIDA)
            break
        else:
            print(ERROR)

    elif invertir == "e":
        eliminar = (
            input(
                "¿Desea eliminar o actualizar algún elemento de la base de datos: (e/a)?"
            )
            .lower()
            .strip()
            .replace(" ", "")
        )
        if eliminar == "e":
            eliminar = input("Ingrese el nombre del país que desee eliminar: ").strip()
            if eliminar in dic_normal:
                proceder = (
                    input(
                        f"El elemento que desea eliminar es: {eliminar}, ¿Es correcto?: (s/n) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if proceder == "s":
                    print(f"Ok... Eliminando {eliminar} de la base de datos👍")
                    del dic_normal[eliminar]
                    print("Base de datos actualizada👍: ")
                    for pais, capital in dic_normal.items():
                        print(f"País:{pais} - Capital: {capital}")
                    regresar = (
                        input("¿Desea regresar(r) al inicio o desea salir(s)?: (r/s) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "s":
                        print(REGRESAR)
                    elif regresar == "n":
                        print(SALIDA)
                    else:
                        print(ERROR)
                elif proceder == "n":
                    print("Ok volviendo a ingresar valores")
                else:
                    print(ERROR)
            else:
                ingresar = (
                    input(
                        f"El país {eliminar} no existe en la base de datos, ¿Desea agregarlo?: s/n "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if ingresar == "s":
                    capital = input(
                        f"Agrega la capital correspondiente a {eliminar}"
                    ).strip()
                    print("Agregando el elemento a la base de datos...")
                    dic_normal[eliminar] = capital
                    print(EXITO)
                    print("Base de datos actualizada ☺️: ")
                    for pais, capital in dic_normal.items():
                        print(f"País: {pais} - Capital: {capital}")
                        regresar = (
                            input(
                                "¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) "
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
                elif ingresar == "n":
                    regresar = input("¿Desea regresar(r) o salir del programa(s): r/s ")
                    if regresar == "r":
                        print(REGRESAR)
                    elif regresar == "s":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

        elif eliminar == "a":
            actualizar = input(
                "Ingrese el nombre del país que desee actualizar: "
            ).strip()
            if actualizar in dic_normal:
                proceder = (
                    input(
                        f"El elemento que desea actualizar es: {actualizar}, ¿Es correcto?: (s/n) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if proceder == "s":
                    nuevo_valor = input("Ingrese la capital actualizada: ").strip()
                    print(f"Ok... Actualizando {actualizar} de la base de datos👍")
                    dic_normal[actualizar] = nuevo_valor
                    print("Base de datos actualizada: ")
                    for pais, capital in dic_normal.items():
                        print(f"País:{pais} - Capital: {capital}")
                    regresar = (
                        input("¿Desea regresar(r) al inicio o desea salir(s)?: (r/s) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "s":
                        print(REGRESAR)
                    elif regresar == "n":
                        print(SALIDA)
                    else:
                        print(ERROR)
                elif proceder == "n":
                    print("Ok volviendo a ingresar valores")
                else:
                    print(ERROR)
            else:
                ingresar = (
                    input(
                        f"El país {actualizar} no existe en la base de datos, ¿Desea agregarlo?: s/n "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if ingresar == "s":
                    capital = input(
                        f"Agrega la capital correspondiente a {actualizar}"
                    ).strip()
                    print("Agregando el elemento a la base de datos...")
                    dic_normal[actualizar] = capital
                    print(EXITO)
                    print("Base de datos actualizada: ")
                    for pais, capital in dic_normal.items():
                        print(f"País: {pais} - Capital: {capital}")
                        regresar = (
                            input(
                                "¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) "
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
                elif ingresar == "n":
                    regresar = input("¿Desea regresar(r) o salir del programa(s): r/s ")
                    if regresar == "r":
                        print(REGRESAR)
                    elif regresar == "s":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

    elif invertir == "n":
        regresar = (
            input("Entendido, ¿Desea regresar al inicio(i) o salir(s)?: (i/s)")
            .lower()
            .strip()
            .replace(" ", "")
        )
        if regresar == "i":
            print(REGRESAR)
        elif regresar == "s":
            print(SALIDA)
            break
        else:
            print(ERROR)
    else:
        print(ERROR)

# Modulo 5, ejercicio número 24: Eliminar elementos. 
# Objetivo: Pide al usuario un color a eliminar y bórralo si existe.

print("Colores 'Print' Base de datos.🌈")

dic_colores = {}

dic_invertido= {}

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

VACIO = "Error encontrado, no puedes dejar vacío."

print(
    "Base de datos de la empresa 🖍️"
)

while True:
    
    print("Menú principal:")
    menu= input("""
    -Oprime 1 para agregar colores a la base (3 por elección)
    -Oprime 2 para eliminar colores de la base de datos
    -Oprime 3 para actualizar un elemento de la base de datos
    -Oprime 4 para eliminar la base de datos entera (No recomendado)
    -Oprime 5 para imprimir la base de datos actuales
    -Oprime 6 para salir del programa
    Tú escoges: """)
    
    if menu == "1":
        for i in range(3):
            color_name = input(
                f"Ingresa el nombre del color a agregar {i + 1}: "
            ).strip()  # Evita repeticiones de código innecesarias.
            color_hexa = input(f"Escribe el color en formato hexadecimal (#) {i + 1}: ").strip()
            dic_colores[color_name] = color_hexa
        print("Esta es la base de datos creada: ")
        for  color_name, color_hexa in dic_colores.items():
            print(f"Color: {color_name} - Formato: {color_hexa}")

        invertir = input(
            "¿Desea ver la información en el panel de vista invertida(i) o volver al menú(v)?: "
        )
        if invertir == "i":
            dic_invertido = {v: k for k, v in dic_colores.items()}
            print("Base de datos invertida con éxito💯")
            for capital, pais in dic_invertido.items():
                print(f"Capital: {capital} - País: {pais}")
            regresar = (
                input("¿Desea volver al menú (s) o seguir (n)?: (s/n) ")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "s":
                print(REGRESAR)
            elif regresar == "n":
                print(SALIDA)
                break
            else:
                print(ERROR)
        elif invertir == "v":
            print(REGRESAR)
        else: 
            print(ERROR)
    elif menu == "2":
        if not dic_colores:
            print("La base de datos está vacía, no hay nada que eliminar. Volviendo ⬆️")
        else:
            eliminar = input("Ingrese el nombre del color que desee eliminar: ").strip()
            if eliminar in dic_colores:
                proceder = (
                    input(
                        f"El color que desea eliminar es: {eliminar}, ¿Es correcto?: (s/n) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if proceder == "s":
                    print(f"Ok... Eliminando {eliminar} de la base de datos👍")
                    del dic_colores[eliminar]
                    print("Base de datos actualizada👍: ")
                    for pais, capital in dic_colores.items():
                        print(f"País:{pais} - Capital: {capital}")
                    regresar = (
                        input("¿Desea regresar(r) al inicio o desea salir(s)?: (r/s) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "s":
                        print(REGRESAR)
                    elif regresar == "n":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                elif proceder == "n":
                    print("Ok volviendo a ingresar valores")
                else:
                    print(ERROR)
            else:
                ingresar = (
                    input(
                        f"El color {eliminar} no existe en la base de datos, ¿Desea agregarlo?: s/n "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if ingresar == "s":
                    color_hexa = input(
                        f"Agrega la clave hexadecimal correspondiente a {eliminar}"
                    ).strip()
                    print("Agregando el elemento a la base de datos...")
                    dic_colores[eliminar] = color_hexa
                    print(EXITO)
                    print("Base de datos actualizada ☺️: ")
                    for pais, capital in dic_colores.items():
                        print(f"Color: {color_name} - Clave hexadecimal: {color_hexa}")
                        regresar = (
                            input(
                                "¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) "
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
                elif ingresar == "n":
                    regresar = input("¿Desea regresar al menú(r) o salir del programa(s): r/s ")
                    if regresar == "r":
                        print(REGRESAR)
                    elif regresar == "s":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                else:
                    print(ERROR)
        
    elif menu == "3":
        if not dic_colores:
            print("La base de datos está vacía, no hay ningún elemento que actualizar. Volviendo ⬆️")
        else: 
            actualizar = input(
                "Ingrese el nombre del color que desee actualizar: "
            ).strip()
            if actualizar in dic_colores:
                proceder = (
                    input(
                        f"El color que desea actualizar es: {actualizar}, ¿Es correcto?: (s/n) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if proceder == "s":
                    nuevo_valor = input("Ingrese la clave hexadecimal actualizada: ").strip()
                    print(f"Ok... Actualizando {actualizar} de la base de datos👍")
                    dic_colores[actualizar] = nuevo_valor
                    print("Base de datos actualizada: ")
                    for color_name, color_hexa in dic_colores.items():
                        print(f"Color:{color_name} - Clave hexadecimal: {color_hexa}")
                    regresar = (
                        input("¿Desea regresar(r) al menú o desea salir(s)?: (r/s) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "s":
                        print(REGRESAR)
                    elif regresar == "n":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                elif proceder == "n":
                    print("Ok volviendo a ingresar valores")
                else:
                    print(ERROR)
            else:
                ingresar = (
                    input(
                        f"El color {actualizar} no existe en la base de datos, ¿Desea agregarlo?: s/n "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if ingresar == "s":
                    color_hexa = input(
                        f"Agrega la capital correspondiente a {actualizar}"
                    ).strip()
                    print("Agregando el elemento a la base de datos...")
                    dic_colores[actualizar] = color_hexa
                    print(EXITO)
                    print("Base de datos actualizada: ")
                    for color_name, color_hexa in dic_colores.items():
                        print(f"Color: {color_name} - Clave Hexadecimal: {color_hexa}")
                        regresar = (
                            input(
                                "¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) "
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
                elif ingresar == "n":
                    regresar = input("¿Desea regresar(r) o salir del programa(s): r/s ").lower().strip().replace(" ", "")
                    if regresar == "r":
                        print(REGRESAR)
                    elif regresar == "s":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                else:
                    print(ERROR)

    elif menu == "4":
        if not dic_colores: 
            print("La base de datos está vacía, no hay algo que eliminar. Volviendo ⬆️")
        else:
            print("Está ingresando a eliminar la base entera...⬇️")
            eliminar_base = (
                input("⚠️ La base de datos está apunto de ser eliminada por completo, ¿está seguro que desea proceder?: (s/n) ⚠️").lower().strip().replace(" ", "")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "s":
                print("Entendido, eliminando la base de datos...Esto tomará unos segundos ♻️")
                dic_colores.clear()
                print("Base de datos eliminada con éxtito👍")
                print(REGRESAR)
                regresar= input("¿Desea regresar al menú (r) o salir del programa (s)?: (r/s)").lower().strip().replace(" ", "")
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else: 
                    print(ERROR)
                
    elif menu == "5": 
        if not dic_colores:
            print("La base de datos está vacía, no hay valores que imprimir. Volviendo ⬆️")
        else:
            print("Imprimiendo base de datos actual: ")
            for color_name, color_hexa in dic_colores.items():
                print(f"Color:{color_name} - Clave hexadecimal:{color_hexa}")
                regresar= input("¿Qué desea hacer ahora?: salir(s) | regresar al menú(r) ").lower().strip().replace(" ", "")
                if regresar == "s":
                    print(SALIDA)
                    break
                elif regresar == "r":
                    print(REGRESAR)
                else: 
                    print(ERROR)
    
    elif menu == "6":
        print(SALIDA)
        break
    elif not menu.strip():
        raise ValueError(VACIO)
    elif "123456" not in menu:
        raise ValueError(ERROR)
    
# Modulo 5, ejercicio número 24: Eliminar elementos. 
# Objetivo: Pide al usuario un color a eliminar y bórralo si existe.

print("Sumador de valores.➕")

dic_suma = {}

dic_invertido= {}

SALIDA = "Saliendo del programa. Tenga un maravilloso día 👋☺️"

REGRESAR = "Entendido, volviendo arriba ⬆️👍"

ERROR = "Error encontrado, por favor elige un valor válido ⚠️"

EXITO = "Proceso realizado exitosamente"

VACIO = "Error encontrado, no puedes dejar vacío."

print(
    "'Base de datos números'"
)

while True:
    
    print("Menú principal:")
    menu= input("""
    -Oprime 1 para agregar números a la base (3 por elección)
    -Oprime 2 para eliminar números de la base de datos
    -Oprime 3 para actualizar un número de la base de datos
    -Oprime 4 para sumar los valores de la base de datos. 
    -Oprime 5 para eliminar la base de datos entera (No recomendado)
    -Oprime 6 para imprimir la base de datos actuales
    -Oprime 7 para salir del programa
    Escoge un número en la lista: """)
    
    if menu == "1":
        for i in range(3):
            num_nombre = input(
                f"Ingresa el nombre de la variable para almacenar el número a agregar {i + 1}: "
            ).strip()  # Evita repeticiones de código innecesarias.
            numero = int(input(f"Escribe el número correspondiente {i + 1}: "))
            dic_suma[num_nombre] = numero
        print("Esta es la base de datos creada: ")
        for  num_nombre, numero in dic_suma.items():
            print(f"Variable: {num_nombre} - Número: {numero}")

        invertir = input(
            "¿Desea ver la información en el panel de vista invertida(i) o volver al menú(v)?: "
        )
        if invertir == "i":
            dic_invertido = {v: k for k, v in dic_suma.items()}
            print("Base de datos invertida con éxito💯")
            for num_nombre, numero in dic_invertido.items():
                print(f"Variable: {num_nombre} - Número: {numero}")
            regresar = (
                input("¿Desea volver al menú (s) o seguir (n)?: (s/n) ")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "s":
                print(REGRESAR)
            elif regresar == "n":
                print(SALIDA)
                break
            else:
                print(ERROR)
        elif invertir == "v":
            print(REGRESAR)
        else: 
            print(ERROR)
    elif menu == "2":
        if not dic_suma:
            print("La base de datos está vacía, no hay nada que eliminar. Volviendo ⬆️")
        else:
            eliminar = input("Ingrese el nombre de la variable que desee eliminar: ").strip()
            if eliminar in dic_suma:
                proceder = (
                    input(
                        f"El color que desea eliminar es: {eliminar}, ¿Es correcto?: (s/n) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if proceder == "s":
                    print(f"Ok... Eliminando {eliminar} de la base de datos👍")
                    del dic_suma[eliminar]
                    print("Base de datos actualizada👍: ")
                    for num_nombre, numero in dic_suma.items():
                        print(f"Variable:{num_nombre} - Número: {numero}")
                    regresar = (
                        input("¿Desea regresar(r) al inicio o desea salir(s)?: (r/s) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "s":
                        print(REGRESAR)
                    elif regresar == "n":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                elif proceder == "n":
                    print("Ok volviendo a ingresar valores")
                else:
                    print(ERROR)
            else:
                ingresar = (
                    input(
                        f"La variable {eliminar} no existe en la base de datos, ¿Desea agregarlo?: s/n "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if ingresar == "s":
                    numero = int(input(
                        f"Agrega el número correspondiente a la variable {eliminar}"
                    ))
                    print("Agregando el elemento a la base de datos...")
                    dic_suma[eliminar] = numero
                    print(EXITO)
                    print("Base de datos actualizada ☺️: ")
                    for num_nombre, numero in dic_suma.items():
                        print(f"Variable: {num_nombre} - Número: {numero}")
                        regresar = (
                            input(
                                "¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) "
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
                elif ingresar == "n":
                    regresar = input("¿Desea regresar al menú(r) o salir del programa(s): r/s ")
                    if regresar == "r":
                        print(REGRESAR)
                    elif regresar == "s":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                else:
                    print(ERROR)
        
    elif menu == "3":
        if not dic_suma:
            print("La base de datos está vacía, no hay ningún elemento que actualizar. Volviendo ⬆️")
        else: 
            actualizar = input(
                "Ingrese el nombre de la variable que desee actualizar: "
            ).strip()
            if actualizar in dic_suma:
                proceder = (
                    input(
                        f"La variable que desea actualizar es: {actualizar}, ¿Es correcto?: (s/n) "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if proceder == "s":
                    nuevo_valor = int(input("Ingrese el número que quedará almacenado allí: "))
                    print(f"Ok... Actualizando {actualizar} de la base de datos👍")
                    dic_suma[actualizar] = nuevo_valor
                    print("Base de datos actualizada: ")
                    for num_nombre, numero in dic_suma.items():
                        print(f"Variable:{num_nombre} - Número: {numero}")
                    regresar = (
                        input("¿Desea regresar(r) al menú o desea salir(s)?: (r/s) ")
                        .lower()
                        .strip()
                        .replace(" ", "")
                    )
                    if regresar == "s":
                        print(REGRESAR)
                    elif regresar == "n":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                elif proceder == "n":
                    print("Ok volviendo a ingresar valores")
                else:
                    print(ERROR)
            else:
                ingresar = (
                    input(
                        f"La variable {actualizar} no existe en la base de datos, ¿Desea agregarlo?: s/n "
                    )
                    .lower()
                    .strip()
                    .replace(" ", "")
                )
                if ingresar == "s":
                    numero = int(input(
                        f"Agrega el número correspondiente a la variable {actualizar}"
                    ))
                    print("Agregando el elemento a la base de datos...")
                    dic_suma[actualizar] = numero
                    print(EXITO)
                    print("Base de datos actualizada: ")
                    for num_nombre, numero in dic_suma.items():
                        print(f"Variable: {num_nombre} - Número: {numero}")
                        regresar = (
                            input(
                                "¿Desea regresar al inicio(r) o salir del programa(s)?: (r/s) "
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
                elif ingresar == "n":
                    regresar = input("¿Desea regresar(r) o salir del programa(s): r/s ").lower().strip().replace(" ", "")
                    if regresar == "r":
                        print(REGRESAR)
                    elif regresar == "s":
                        print(SALIDA)
                        break
                    else:
                        print(ERROR)
                else:
                    print(ERROR)
    elif menu == "4": 
        if not dic_suma: 
            print("No hay elementos registrados para sumar en la base de datos")
        else: 
            print("Sumatoria de los elementos del diccionario: ")
            sumar= input("¿Desea sumar todos los elementos de la lista?: (s/n) ")
            if sumar == "s": 
                print("Entendido, sumando todos los elementos de la base: ")
                sumar_num= sum(dic_suma.values())
                print(f"La suma de los valores dentro de la base es: {sumar_num}")
    elif menu == "5":
        if not dic_suma: 
            print("La base de datos está vacía, no hay algo que eliminar. Volviendo ⬆️")
        else:
            print("Está ingresando a eliminar la base entera...⬇️")
            eliminar_base = (
                input("⚠️ La base de datos está apunto de ser eliminada por completo, ¿está seguro que desea proceder?: (s/n) ⚠️").lower().strip().replace(" ", "")
                .lower()
                .strip()
                .replace(" ", "")
            )
            if regresar == "s":
                print("Entendido, eliminando la base de datos...Esto tomará unos segundos ♻️")
                dic_suma.clear()
                print("Base de datos eliminada con éxtito👍")
                print(REGRESAR)
                regresar= input("¿Desea regresar al menú (r) o salir del programa (s)?: (r/s)").lower().strip().replace(" ", "")
                if regresar == "r":
                    print(REGRESAR)
                elif regresar == "s":
                    print(SALIDA)
                    break
                else: 
                    print(ERROR)
                
    elif menu == "6": 
        if not dic_suma:
            print("La base de datos está vacía, no hay valores que imprimir. Volviendo ⬆️")
        else:
            print("Imprimiendo base de datos actual: ")
            for color_name, color_hexa in dic_suma.items():
                print(f"Variable:{num_nombre} - Número:{numero}")
                regresar= input("¿Qué desea hacer ahora?: salir(s) | regresar al menú(r) ").lower().strip().replace(" ", "")
                if regresar == "s":
                    print(SALIDA)
                    break
                elif regresar == "r":
                    print(REGRESAR)
                else: 
                    print(ERROR)
    
    elif menu == "7":
        print(SALIDA)
        break
    elif not menu.strip():
        raise ValueError(VACIO)
    elif "123456" not in menu:
        raise ValueError(ERROR)