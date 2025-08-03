# Modulo 1
nombre = input("Escribe tu nombre: ")
fraseMotivacional = input(
    "Escribe una frase que te motive a seguir y no abandonar tus sueños: "
)
print(
    f"Hola {nombre}, recuerda que estas aqui para dar lo mejor de ti; tu frase: {fraseMotivacional}"
)

# Modulo 2: Calculadora de edad futura
edad = int(input("Por favor, proporciona tu edad: "))

print(
    f"Tu edad actual es: {edad}, tu edad futura es: {edad + 5} (en 5 años), {edad + 10} (en 10 años) y {edad + 20} (en 20 años)"
)

# Modulo 2, Ejercicio 2: Conversor de temperatura
print("Conversor de Grados Centígrados a Farenheit")
gradosC = int(
    input(
        "Escribe la temperatura de tu ciudad en grados Centígrados para hacer la conversión: "
    )
)
F = gradosC * 1.8 + 32

print(f"La temperatura de tu ciudad es: {gradosC} C° y {F} F°")

# Modulo 2, ejercicio 3: Perfil del usuario
print(
    "Ya tenemos tu nombre y edad gracias a que lo proporcionaste anteriormente, ahora necesitamos nos proporciones los siguientes datos: "
)

ciudad = input("Proporciona a continuación tu ciudad de prosendencia: ")
profesión = input("Ahora proporciona tu ocupasión o a que te dedicas: ")

print(
    f"""Gracias por proporcionar tus datos, por favor dales un vistazo: {nombre, edad, ciudad, profesión}"""
)

# Modulo 2, ejercicio 4: Área de un triángulo
print("Calculadora del área de un triángulo")

b = float(input("Introduce la base del triángulo en cm: "))
h = float(input("Introduce la altura del triángulo en cm: "))
areaTriangulo = (b * h) / 2
print(f"El área del triángulo es: {round(areaTriangulo)}cm al cuadrado")

# Modulo 3, ejercicio 1: Verificador de derecho al voto
print("¿El usuario puede votar?")

if edad >= 18:
    print("Sí, el usuario tiene derecho al voto")
else:
    print("No, el usuario aún no puede votar")

# Modulo 3, ejercicio 2: Clasificador de número
print("Clasificador de números (solo números enteros)")

numeroX = int(input("Escribe un número entero cual sea: "))
if numeroX == 0:
    print("Tu número es de valor nulo o cero")
elif numeroX < 0:
    print("Tu número es negativo")
else:
    print("Tu número es entero positivo")
# Modulo 3, ejercicio 3: Números pares
print("Clasificadora de números pares o impares")

numeroY = int(
    input(
        "Selecciona usando el teclado un número de tipo, cual sea, verificaremos si es par o no: "
    )
)

if numeroY % 2 == 0:
    print("El número escogido es par.")
else:
    print("El número que escogiste es impar.")
# Modulo 3, ejercicio 4: Mayor de tres números
print("Mayor de tres números")

numOne = int(input("Escoge el primer número"))

numTwo = int(input("Escoge el segundo número"))

numThree = int(input("Escoge el tercer número"))

if numOne >= numTwo and numOne >= numThree:
    print(f"Este número es el mayor de los tres: {numOne}")
elif numTwo >= numOne and numTwo >= numThree:
    print(f"El número más grande es: {numTwo}")
elif numThree >= numOne and numThree >= numTwo:
    print(f"El número más grande es: {numThree}")
else:
    print("Todos los números son iguales🤗")
# Modulo 3, ejercicio 5: Calculadora de calificaciones
print("Calculadora de calificaciones.")

print(
    "Escribe las calificaciones correspondientes a las materias de Programación Orientada a Objetos, Programación Web, Análisis de datos y Ciberseguridad"
)

calificacionOne = float(input("POO= "))

calificacionTwo = float(input("Programación Web= "))

calificacionThree = float(input("Análisis de datos= "))

calificacionFour = float(input("Ciberseguridad= "))

promedio = (
    calificacionOne + calificacionTwo + calificacionThree + calificacionFour
) / 4

if promedio >= 90:
    print(f"Tienes un promedio de: {promedio}, Excelente 🤩.")
elif promedio >= 80:
    print(f"Tu promedio es: {promedio}, Muy bien eres Sobresaliente🤗.")
elif promedio >= 70:
    print(f"Tu promedio es: {promedio}, Bien hecho🫡.")
elif promedio >= 60:
    print(
        f"Tu promedio es: {promedio}, ¡Vamos, no te desanimes, puedes hacerlo mejor!☺️."
    )
else:
    print("Tu promedio fue de: {promedio}, Calificación no aprobatoria⚰️.")

# Modulo 3, ejercicio 6: Conversor de monedas
print("Conversor de monedas: Pesos mexicanos a Dólares, Euros o Yenes.")

mxn = float(input("Proporciona la cantidad en pesos: "))
if mxn < 0:
    print("Favor de escribir una cantidad válida.")
else:
    dllr = (mxn * 1) / 17.5
    euro = (mxn * 1) / 19.1
    yen = (mxn * 1) / 0.1212
    print(
        f"Tu cantidad de ${mxn} mexicanos, son: ${dllr} americanos, {euro}$ europeos y {yen} yenes."
    )

# Modulo 3, ejercicio 7: Calculadora de edad con validación
print("Calculadora de edad con validación")

añoNacimiento = int(input("Por favor, proporciona tu año de nacimiento: "))

if añoNacimiento >= 1900 and añoNacimiento < 2025:
    edadFinal = 2025 - añoNacimiento
    print(f"Gracias por proporcionar los datos, tu edad es: {edadFinal}")
else:
    print("Por favor, proporciona una fecha válida")

# Modulo 3, ejercicio 8: Calculadora de operaciones básicas
print("Calculadora de operaciones básicas")

num1 = float(input("Escoge el primer número: "))

num2 = float(input("Escoge el segundo número: "))

operacion = input(
    "¿Qué operación desea realizar con ese número?: suma, resta, multiplicación o división "
)

operacion_lower = operacion.lower()

if operacion_lower == "division" and num2 == 0:
    print("Fixt Error: No es posible una división entre cero")
elif operacion_lower == "suma":
    resultado = num1 + num2
    print(f"El resultado es: {resultado}")
elif operacion_lower == "resta":
    resultado = num1 - num2
    print(f"El resultado es: {resultado}")
elif operacion_lower == "multiplicación":
    resultado = num1 * num2
    print(f"El resultado es: {resultado}")
elif operacion_lower == "división":
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")

else:
    print("Escoge una operación válida")

# Modulo 3, ejercicio 9: Clasificador de letras
print("Clasificador de letras")

letra = input("Ingresa una sola letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Debes ingresar una única letra válida.")
elif letra in "aeiou":
    print("Escogiste una letra vocal 🫡")
else:
    print("Escogiste una letra consonante 💀")

# Modulo 3, ejercicio 10: Aprobación múltiple
print(
    "Aprobación múltiple: Por favor, proporciona tus promedios para las materias solicitadas."
)

desWeb = float(input("Proporciona la calificación correspondiente a Desarrollo Web: "))

desMovil = float(
    input("Proporciona la calificación correspondiente a Desarrollo Móvil: ")
)

hackingEtico = float(
    input("Proporciona la calificación correspondiente a Hacking Etico: ")
)

if desWeb >= 70 and desMovil >= 70 and hackingEtico >= 70:
    print("Felicitaciones, aprobaste todas las materias🤩🤩🤩")
else:
    print("Reprobaste alguna materia.")
    print("Materias Reprobadas: ")
    if desWeb < 70:
        print("Desarrollo Web")
    if desMovil < 70:
        print("Desarrollo Movil")
    if hackingEtico < 70:
        print("Hacking Etico")
