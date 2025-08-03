nombre = input("Escribe tu nombre usando el teclado ")
edad = input("Escribe tu edad ")
altura = float(input("Proporciona tu estatura en metros: "))
peso = float(input("Proporciona tu peso en kg: "))
IMC = peso / (altura**2)
estudiante = True


print(
    f"""Hola, gracias por proporcionar tus datos {nombre}. Tienes: {edad} años, tu índice de masa corporal es de: {IMC}, ¿actualmente te encuentras estudiando?: {estudiante}"""
)
if IMC < 18.5:
    print("Estas en bajo peso💀")
elif IMC < 25:
    print("Estas en rango normal de peso🤗")
elif IMC < 30:
    print("Estas en sobrepeso 😥")
else:
    print("Estas en obesidad⚰️")
