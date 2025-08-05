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
