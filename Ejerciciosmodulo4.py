# Modulo 4, ejercicio 1: Contador del 1 al 10
print("Contador del 1 al 10")

contador = 1

while contador <= 10:
    print(
        contador, end=""  # End sirve para escribir una lista en una sola fila o línea
    )
    contador += 1

# Modulo 4, ejercicio 2: Suma acumulativa
print("Suma acumulativa")

suma_numeros = 0

for num in range(1, 100):
    suma_numeros += num
print(f"La suma de todos estos números es: {suma_numeros}")

# Modulo 4, ejercicio 3: Tabla de multiplicar
print("Tabla de Multiplicar.")

tabla_num = int(
    input(
        "Bienvenido a este creador de tablas de multiplicar, por favor escoge el número que desees: "
    )
)

print(f"Tabla de multiplicar para: {tabla_num}")

for tabla in range(1, 11):
    tabla_res = tabla_num * tabla
    print(
        f"{tabla_num} x {tabla}: {tabla_res}"  # Muestra en formato tabla convencional de multiplicar 1x10=10
    )

# Modulo 4, ejercicio 4: Bucle infinito controlado
print("Bucle Infinito Controlado")
while True:
    name = input(
        "Escribe tu nombre si deseas continuar: , escribe Kevin si deseas un logueo distinto. "
    )
    if name.lower() == "kevin":
        print(f"Hola {name}, se bienvenido")
        break
    else:
        print(f"Bienvenido {name}")

# Modulo 4, ejercicio 5: Número Secreto
import random  # Importamos el modulo random para importar variables aleatorias

print("Número Secreto🤫")

ran_num = random.randint(1, 10)

while True:
    eleccion = int(
        input(
            "Juguemos un juego💀. Instrucciones: Elige un número del 1 al 10, si lo adivinas Ganarás el juego, sino estarás eliminado⚰️."
        )
    )
    if eleccion < 1 or eleccion > 10:
        print(
            f"Escogiste: {eleccion}, se encuentra en un rango fuera de lo establecido"
        )
    elif eleccion == ran_num:
        print(f"Ganaste de manera arrolladora, adivinaste el número: {ran_num}🏋️.")
        break
    else:
        print(f"Sigue intentándolo. Tu número descartado fue: {eleccion}")

# Modulo 4, ejercicio 6: Contador regresivo con pasos personalizados
# Objetivo: Solicita al usuario un número inicial y un valor de decremento, luego muestra una cuenta regresiva.

print("Contador regresivo con pasos personalizados")

primer_val = int(input("Ingresa con el teclado un número cual sea: "))

decremento = int(
    input("Ingresa el número de pasos regresivos que tendrá el número base: ")
)

while primer_val > 0:
    print(primer_val)
    primer_val -= decremento

# Modulo 4, ejercicio 7: Suma solo de números pares
# Objetivo: Suma todos los números pares entre 1 y 100.

print("Suma solo de números pares del 1 al 100")

suma_par = 0

for num in range(1, 101):
    if num % 2 == 0:
        suma_par += num
        print(f"Suma de números pares: {num}")

# Modulo 4, ejercicio 8: Juego del número divisible
# Objetivo: El usuario escribe un número, y el programa muestra todos los números del 1 al 50 que sean divisibles por ese número.
print("Juego del número divisible")

num_divisible = int(input("Escoge un número: "))

divisor = int(
    input(
        "Escoge el divisor de dicho número, a continuación el programa te mostrará los números del 1 al 50 que sean divisibles entre él: "
    )
)

for divisible in range(1, 51):
    if divisible % divisor == 0:
        print(f"Estos son los números divisibles entre {divisible}")

# Modulo 4, ejercicio 9: Bucle controlado con continue
# Objetivo: Del 1 al 20, muestra todos los números excepto los múltiplos de 3.

multiplo = 0

for num_mul in range(1, 21):
    if num_mul % 3 == 0:  # Primero filtra los números múltiplos
        continue
    else:
        multiplo += num_mul
        print(f"Estos son los números a excepción de los múltiplos de 3: {num_mul}")

# Modulo 4, ejercicio 10: Intentos limitados para adivinar una palabra
# Objetivo: El usuario debe adivinar una palabra secreta en máximo 5 intentos.

print(
    "Juego de adivina la palabra. Instrucciones: Tendrás 5 intentos para adivinar una palabra, si no lo consigues en esos intentos, perderás. "
)

secret_key = "Gato"

intentos_rest = 5

while intentos_rest > 0:
    intentos = input(f"Intenta adivinar la palabra secreta, tienes: {intentos_rest}")
    if intentos == "Gato":
        print(
            f"Lo Lograste, obtuviste la palabra en el intento número: {intentos_rest} intentos. -      - "
        )
        break
    else:
        print(f"Intentalo nuevamente, te quedan: {intentos}")
        intentos_rest -= 1

# Modulo 4, ejercicio 11: Buscar el míltiplo de 7 en una lista
# Objetivo: Dada una lista de números, encuentra y muestra el primer número divisible entre 7.

print("Busca el primer múltiplo de 7 en una lista")

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 32, 45, 55, 88, 101, 102, 203, 204]

for div in lista_numeros:
    if div % 7 == 0:
        print(f"El primer número divisible entre 7 es: {div}")
        break
else:
    print("No se encontro ningún número que sea divisible entre 7.")

# Modulo 4, ejercicio 12: Verificar si una palabra es un palíndromo
# Objetivo: Pide una palabra al usuario y determina si se lee igual al revés.

print("Juego Verificador de palabras Palíndromo")

vidas = 3

inten = 0

while vidas > 0 and inten < 3:
    palabra = input(
        f"Ingresa una palabra al verificador para saber si se trata de un palíndromo o no, cuentas con {vidas} vidas solamente: "
    )

    palabra_min = palabra.lower()

    palíndromo = palabra_min[::-1]

    inten += 1

    vidas -= 1

    if palabra_min == palíndromo:
        print(
            f"Lo conseguiste, la palabra que anotaste es un palíndromo: {palabra_min}🤩. "
        )
        print(f"Número de intentos: {inten}. ")

        break
    else:
        print(f"Error, la palabra no es un palíndromo😥, vidas restantes: {vidas}")
        print(f"Número de intentos: {inten}")

if inten == 0:
    print(f"Perdiste, te quedaste sin intentos. Vidas restantes: {vidas}")

# Modulo 4, ejercicio 13: Serie de fimonacci hasta un límite
# Objetivo: Muestra los números de la serie de Fibonacci que no superen un número límite dado por el usuario.

print("Serie de fimonacci con límite")

num_a, num_b = 0, 1

limite = int(input("Escribe el número límite que mostrará la serie: "))

print(f"Escogiste un límite de: {limite}")

while num_b <= limite:
    print(num_b, end=" ")
    num_a, num_b = num_b, num_a + num_b

# Modulo 4, ejercicio 14: Tabla de multiplicar personalizada
# Objetivo: El usuario introduce un número, y el programa imprime su tabla de multiplicar del 1 al 10.

print("Tabla de multiplicar personalizada")

while True:

    a = int(input("Selecciona el número que deseas: "))

    print(f"Tabla de multiplicar del: {a}")

    for b in range(1, 11):
        print(f"{a} x {b} = {a * b}")

    seguir = int(
        input("Oprime 1 si desea retornar o cualquier otro si desea finalizar: ")
    )

    if seguir != 1:
        print("Gracias por utilizar la herramienta, tenga un buen día.🤗")
        break

# Modulo 4, ejercicio 15: Contador de vocales en una frase
# Objetivo: Cuenta cuántas vocales hay en una frase ingresada por el usuario.

print("Contador de vocales🤗.")

while True:
    frase = input("Ingresa la frase o palabra que quieras: ")

    frase_min = frase.lower()

    vocales = "aeiou"

    continuar = input(f"Ingresaste la frase: {frase}, ¿Desea continuar?: (s/n) ")

    if continuar.lower() != "s":
        continue

    contador_vocales = 0
    for letra in frase_min:
        if letra in vocales:
            contador_vocales += 1

    print(f"Su palabra u oración '{frase}' tiene: {contador_vocales} vocales.")

    volver = input("¿Desea volver?: (s/n) ")

    if volver.lower() == "n":
        break
    elif volver.lower() != "s":
        print("Entrada inválida. Por favor, ingresa 's' o 'n'.")

# Modulo 4, ejercicio 16: Cajero Automático Simulado
# Objetivo: Simular un cajero donde el usuario tiene un saldo inicial y puede retirar dinero hasta que decida salir o el saldo se agote.

print(
    """Cajero Automático Personalizado: 
      -Insertar tarjeta aquí: --   --"""
)

password = input(
    """Introduce la contraseña: 
    **** """
)

PASSWORD_TRUE = "1234"

saldo_inicial = 120000

if password == PASSWORD_TRUE:

    print(f"Bienvenido a Isis VA, usted cuenta actualmente con: ${saldo_inicial}.")

    while True:

        retiro = int(input("¿Cuánto dinero desea retirar?: "))

        if retiro > saldo_inicial:

            print(f"Error: No cuentas con dinero suficiente: {saldo_inicial}")
            continue

        seguir = input(
            f"Vas a retirar: ${retiro}. ¿Desea confirmar la transacción?: (s/n). "
        )

        if seguir != "s":
            continue
        saldo_inicial -= retiro
        print(f"Dinero disponible: ${saldo_inicial}")

        finalizar = input(
            "Desea continuar retirando?: ('f' para finalizar | 'c' para continuar)"
        )

        if finalizar == "t":
            print(
                f"""Comprobante: 
                Usted ha retirado: ${retiro}
                Le restan: ${saldo_inicial}"""
            )
            print("Operación finalizada. Que tenga buen día.")
            break
        elif finalizar != "c":
            print("Entrada inválida. Por favor, ingresa 'c' o 'f'.")
else:
    print("Contraseña Incorrecta. Prueba Otra Vez.")

# Modulo 4, ejercicio 17: Adivina el número (Modo Hardcore)
# Objetivo: El sistema elige un número entre 1 y 100. El jugador tiene 7 intentos para adivinarlo.
import random

print("Juego de Adivinar el número (HARDCORE mode)")

while True: 

    num_random= random.randint(1, 100)

    contador_vidas= 7 
        
    contador_intentos= 0
    
    print ("Instrucciones: Intenta adivinar el número que la máquina está generando aleatoriamente del 1 al 100, tienes 7 intentos. ")

    while contador_vidas >0 and contador_intentos <=7: 
        num_eleccion= int(
        input(
                f"""Adivina el número 
                - intento: {contador_intentos}
                - vidas restantes: {contador_vidas}.
                - ¿Cuál crees que es el número?: """
            )
        )
        
        contador_vidas -= 1
        
        contador_intentos += 1
        
        if num_eleccion <1 or num_eleccion >100:
            print(
                "☹️ Error: Por favor, escoge un número válido (entre 1-100)."
            )
        
        elif num_eleccion == num_random and contador_intentos <= 7 and contador_vidas >0: 
            print(
                f"¡Lo lograste!: Encontraste el número secreto en el intento número: {contador_intentos}.🥳"
            )
            break
        else: 
            print(f"Error: Esa no es la palabra secreta, te restan: {contador_vidas} vidas.")
            
    regresar= input(
        "¿Desea regresar?: Oprime 'r' si desea regresar o 't' para terminar. "
    ).lower()
                
    if regresar == "t": 
        print(
            "Gracias por Jugar, vuelve pronto ☺️."
        )
        break
    elif regresar == "r": 
        print(
            "Vamos a ello, vidas reestablecidas: +7, contador de intentos: -7"
        )
    else: 
        print(
            "Entrada inválida, por favor proporciona r/t para proceder."
        )
    
#Modulo 4, ejercicio 18: Registro de asistencia con validaciones
#Objetivo: Crear un pequeño programa donde el usuario puede registrar nombres hasta escribir "fin".

print(
    """Lista de asistencia: Instituto Tecnológico de Naranjos
    -----Tecnologías de la Información y comunicaciones--
    -----Materia: Teoria del análisis de datos-----------"""
) 

asistencia= []

while True: 
    nombre_alumno= input(
        "Escribe el nombre del alumno: "
    ).strip().title()
    
    if not nombre_alumno: 
        print("Nombre no puede estar vacío")
        continue  
    if nombre_alumno in asistencia:
        print(f"Error: El nombre '{nombre_alumno}' ya está registrado.")
        continue
    else: 
        print("El nombre no esta agregado en la litsa, puede continuar.")
    
    asistencia.append(nombre_alumno)
    print(f"Se ha registrado correctamente el nombre: {nombre_alumno}")
    
    agregar_mas= input("¿Desea continuar agregando más nombres?: (con/fin). ")
    if agregar_mas != "con": 
        print(f"""Proceso finalizado.
        Recuento:
        Se agregó a la lista - {nombre_alumno}""")
        break
print("\nLista de Asistencia:")
for i, nombre_alumno in enumerate(asistencia, 1): 
    print(f"{i} - {nombre_alumno}")
 