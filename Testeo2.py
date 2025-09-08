NOMBRE_ARCHIVO = "numeros.txt"
with open(NOMBRE_ARCHIVO, "w") as f:
    for num in range(1, 21):
        f.write(str(num) + "\n")

with open(NOMBRE_ARCHIVO, "r") as f:
    total= 0
    for line in f:
        total += int(line.strip())
    print("La lista de números es: ")
    for i, numero in enumerate(f, start=1):
        print(f"{i} - Número: {numero}")
    
print(f"La suma de los números en el archivo es: {total}")