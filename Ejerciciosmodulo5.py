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
                print("Por favor, escoge un valor válido: (s/n). ")

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
                print("Por favor, escoge un valor válido: (s/n). ")

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

#Modulo 5, ejercicio 12: Elimina por posición
#Objetivo: Eliminar un elemento de la lista basado en una posición ingresada por el usuario.

while True:

    print("Eliminador de objetos por posición")

    input("¿Desea eliminar un objeto?: (s/n). ")
    
    validar= input("¿Desea eliminar por posición (1) o por nombre (2)?")

    if validar == "2": 
        print("Por favor, escoge un elemento de la lista: ")
        for i, pendiente in enumerate(pendientes, start=1):
            print(f"{i} - {pendiente}")
        eliminar= input("Elemento a eliminar❌: ")
        
        if eliminar in pendientes: 
            print("""Entendido, eliminando elemento...
                    Espere un momento...""")
            pendientes.remove(eliminar)
            print(f"Se ha eliminado '{eliminar}' de la lista.🥳")
            print("Elemento Eliminado Satisfactoriamente👍")
            validar= input("¿Desea eliminar otro elemento de la lista?: (s/n). ").lower()
            
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
                            print("Error: Escoge un valor entre (s/n). ")
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


 
