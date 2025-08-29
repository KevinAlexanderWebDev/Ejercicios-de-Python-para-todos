# Ejercicio Número 4 "Palíndromo".

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
    