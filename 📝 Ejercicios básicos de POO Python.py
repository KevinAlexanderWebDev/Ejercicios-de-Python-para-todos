# 📝 Ejercicios básicos de POO (Calentamiento)
"""Ejercicio 1: Crear tu primera clase

Crea una clase llamads Persona.

La clase debe tener 2 atributos: nombre y edad.

Haz un método que imprima un saludo: "Hola, me llamo X y tengo Y años".

Crea dos objetos de la clase y llama al método en cada uno."""


class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años. Soy {self.profesion}")

    def despedida(self):
        print(f"Adios, se despide {self.nombre} acabamos de saludarnos pero ya me voy😅")


user1 = Persona("Kevin", 22, "Desarrollador de Software")
user2 = Persona("Guffy", 6, "El más grande amor de mi mejor amigo Kevin")

user1.saludar()
user2.saludar()

user1.despedida()
user2.despedida()

"""Ejercicio 2: Objeto con comportamiento

Crea una clase llamada Perro 🐶.

Debe tener los atributos: nombre, raza y edad.

Haz dos métodos:

ladrar() → imprime "Guau! Soy X"

cumplir_anios() → aumenta en 1 la edad y lo imprime.

Crea un perro y hazlo ladrar, luego haz que cumpla años."""


class perrito:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self):
        print(
            f"🐶Guau Guau, ¡hola! soy {self.nombre}, tu amigo más leal. Pertenezco a la raza {self.raza}."
        )

    def cumplir_anios(self):
        print(f"Actualmente tengo {self.edad} años")
        self.edad += 1
        print(f"Pero el siguiente año cumpliré {self.edad} años. 🐶🥳")


nombre = input("Escribe el nombre del perrito: ").strip()

edad = int(input(f"Escribe la edad de {nombre}: "))

raza = input(f"Escribe la raza de {nombre}: ")

amigo_fiel1 = perrito(nombre, raza, edad)

amigo_fiel1.ladrar()

amigo_fiel1.cumplir_anios()


def viejo_joven(edad):
    if edad <= 1:
        return f"Con mis {edad} años... Soy aún un peque, listo para brindarte mis mejores años por ti, eres lo más importante en mi vida, amigo fiel❤️."
    elif edad < 10:
        return f"Con mis {edad} años... Estoy joven aún, me quedan aún muchos años de amor hacia ti.❤️"
    else:
        return f"Con mis {edad} años... Ya estoy algo viejito pero mi amor por ti nunca envejecerá, cuídame mucho así como yo lo haría por ti🐶❤️."


print(viejo_joven(edad))

"""Ejercicio 3: Clase con atributos inicializados

Crea una clase llamada CuentaBancaria.

Debe tener: titular, saldo.

Métodos:

depositar(cantidad) → suma al saldo.

retirar(cantidad) → resta al saldo si hay suficiente dinero.

mostrar_saldo() → imprime el saldo actual.

Simula una cuenta bancaria con varias operaciones."""


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo  # Entra con el nombre 'simulacion_saldo'

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Agregando dinero a tu cuenta ➕💵")
        print(f"Se ha agregado: ${cantidad} a tu cuenta bancaria!")
        print(f"Saldo actualizado: ${self.saldo}")

    def retirar(self, cantidad):
        self.saldo
        if self.saldo < cantidad:
            print("No hay suficiente saldo para realizar la operación.")
        else:
            print("Eliminando dinero de tu cuenta ➖💸")
            self.saldo -= cantidad
            print(
                f"""
                  Se ha retirado: ${cantidad}
                  Saldo bancario actualizado: ${self.saldo}"""
            )

    def mostrar_saldo(self):
        saldo_actual = self.saldo
        print(f"Saldo actual: ${saldo_actual}")


cantidad = int(input("¿Cuánto dinero desea agregar o retirar a su cuenta?: $"))

simulacion_saldo = int(
    input(
        "Proporciona la cantidad en pesos que tendrá la persona al iniciar(solo es simulación): $"
    )
)

titular = input("Ingresa el nombre del titular de la tarjeta: ").strip()

cuenta1 = CuentaBancaria(titular, simulacion_saldo)

cuenta1.depositar(cantidad)

cuenta1.retirar(cantidad)

cuenta1.mostrar_saldo()

"""Ejercicio 4: Uso de listas en objetos

Crea una clase llamada Biblioteca.

Debe tener un atributo libros (una lista vacía al inicio).

Métodos:

agregar_libro(titulo) → añade a la lista.

mostrar_libros() → imprime todos los títulos.

Crea una biblioteca y agrega al menos 3 libros."""


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        lista_libros = self.libros
        informacion_libro = input(
            "Ingresa el nombre del título del libro y del autor con el siguiente formato --> (libro, autor): "
        )
        print("Agregando libro a la lista ➕📖")
        titulo, autor = informacion_libro.strip().split(",")
        lista_libros.append((titulo, autor))
        with open("biblioteca_libros.txt", "a") as file:
            for titulo, autor in lista_libros:
                file.write(f"Libro --> Título: {titulo} - Autor: {autor}\n")

    def mostrar_libros(self):
        try:
            if not self.libros:
                print("La biblioteca no tiene libros. ⚠️")
            else:
                print("Imprimiendo los libros de la biblioteca: ")
                with open("biblioteca_libros.txt", "r") as file:
                    lectura = file.read()
                    print(lectura)
        except FileNotFoundError:
            print("No está creado el archivo solicitado, creándolo...")
            lista_libros = self.libros
            informacion_libro = input(
                "Ingresa el nombre del título del libro y del autor con el siguiente formato --> (libro, autor): "
            )
            print("Agregando libro a la lista ➕📖")
            titulo, autor = informacion_libro.strip().split(",")
            lista_libros.append((titulo, autor))
            with open("biblioteca_libros.txt", "a") as file:
                for titulo, autor in lista_libros:
                    file.write(f"Libro --> Título: {titulo} - Autor: {autor}\n")


biblioteca = Biblioteca()

while True:
    biblioteca.agregar_libro()
    continuar = input("¿Desea seguir agregando libros? --> (s/n): ")
    if continuar == "s":
        print("Continua agregando 🫡")
    elif continuar == "n":
        print("Saliendo...")
        break
    else:
        print("Solo puedes escoger entre (s/n)⚠️")

biblioteca.mostrar_libros()

"""Ejercicio 5: Objetos interactuando

Crea una clase Alumno con atributos nombre y calificacion.

Crea otra clase Curso con:

Atributo alumnos (lista vacía).

Método agregar_alumno(alumno) que recibe un objeto de tipo Alumno.

Método mostrar_aprobados() → muestra alumnos con calificación >= 6.

Simula un curso con 3 alumnos."""


class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion


class Curso:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def muestra_lista(self):
        print("Lista de alumnos completa: ")
        for alumno in self.alumnos:
            print(f"Alumno: {alumno.nombre} - Calificacion: {alumno.calificacion}")
        print("\n")

    def mostrar_aprobados_reprobados(self):
        print("Lista de alumnos aprobados🥳: ")
        for alumno in self.alumnos:
            if alumno.calificacion >= 6:
                print(f"Alumno: {alumno.nombre} - Calificacion: {alumno.calificacion}")
        print("\nLista de alumnos reprobados❌: ")
        for alumno in self.alumnos:
            if alumno.calificacion < 6:
                print(f"Alumno: {alumno.nombre} - Calificacion: {alumno.calificacion}")
        print("\n")


alumno1 = Alumno("Kevin", 9)
alumno2 = Alumno("Guffy", 10)
alumno3 = Alumno("Tobbies", 9)
alumno4 = Alumno("Isis", 5)
alumno5 = Alumno("Nai", 7)


curso = Curso()

curso.agregar_alumno(alumno1)
curso.agregar_alumno(alumno2)
curso.agregar_alumno(alumno3)
curso.agregar_alumno(alumno4)
curso.agregar_alumno(alumno5)
curso.muestra_lista()
curso.mostrar_aprobados_reprobados()


"""6. Vehículo 🚗

Enunciado:
Crea una clase Vehiculo con atributos marca, modelo, año.

Método arrancar() → imprime "El coche [marca] [modelo] está arrancando".

Método detener() → imprime "El coche [marca] [modelo] se ha detenido".

Pistas:

¿Qué debe ir dentro de __init__?

¿Qué palabra necesitas para referirte a los atributos dentro de los métodos?

Crea al menos 2 objetos y prueba sus métodos."""


class Vehicle:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0

    def arrancar(self):
        print(
            f"El coche: {self.marca} - {self.modelo} se encuentra en una velocidad= {self.velocidad}km/h."
        )
        print("---Arrancando coche---")
        self.velocidad += 40
        print(
            f"El coche lleva recorrido 50 mts de distancia - Velocidad actuaL: {self.velocidad}km/h."
        )

    def detener(self):
        print("---Deteniendo el coche---")
        self.velocidad -= 40
        print(
            f"Coche detenido en su totalidad - Velocidad actual: {self.velocidad}km/h."
        )


marca_coche = input("Escribe la marca del coche: ").strip()

modelo_coche = input(f"Escribe el modelo del coche {marca_coche}: ").strip()

año_coche = int(
    input(f"Ingresa el año del coche {marca_coche} - modelo {modelo_coche}: ")
)

coche1 = Vehicle(marca_coche, modelo_coche, año_coche)

coche2 = Vehicle("Chevrolet", "Camaro", 2017)

coche1.arrancar()

coche1.detener()

coche2.arrancar()

coche2.detener()

"""7. Estudiante 🎓

Enunciado:
Crea una clase Estudiante con atributos nombre, matricula, carrera.

Método mostrar_info() → imprime todos los datos formateados.

Pistas:

Piensa: ¿qué tipo de dato usarías para la matrícula (string o número)?

¿Puedes usar un f-string para mostrar los datos bonitos?

Crea 3 estudiantes y llama al método en cada uno."""


class Student:
    def __init__(self, name, tuition, career):
        # tuition significa matrícula en inglés (Trataremos de ir empleando lo más que se pueda los enunciados en inglés)
        self.name = name
        self.tuition = tuition
        self.career = career

    def show_info(self):
        print("\nStudent data in English: ")
        print(
            f"""
Student data --> 
- 🎒Name: {self.name} 
- 📖Tuition: {self.tuition} 
- 🧑‍🎓Career: {self.career}\n"""
        )
        print("\nInformación del estudiante en español: ")
        print(
            f"""Información del estudiante --> 
- 🎒Nombre: {self.name} 
- 📖Matrícula: {self.tuition} 
- 🧑‍🎓Carrera: {self.career}\n"""
        )


name = input("Ingresa el nombre del estudiante: ").strip()

tuition = input(
    f"Ingresa la combinación de matrícula del estudiante - {name}: "
).strip()

career = input(f"Ingresa el nombre de la carrera del estudiante - {name}: ").strip()

estudiante1 = Student(name, tuition, career)

estudiante1.show_info()

"""8. Tienda 🛒

Enunciado:
Crea una clase Producto con atributos nombre, precio, stock.

Método vender(cantidad) → descuenta el stock si es suficiente, si no muestra un mensaje de error.

Método mostrar_info() → imprime nombre, precio y stock.

Pistas:

Dentro de vender(), ¿qué tipo de estructura de control (if/else) necesitas?

No olvides restar al atributo del objeto (self.stock).

Simula un producto con stock inicial y al menos 2 ventas."""


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show_info(self):
        print(
            f"""
Product Info: 
-Product Name: {self.name}
-Product Price: ${self.price}
-Product Stock: {self.stock} units in stock\n"""
        )

    def sell_quanti(self, quanti):
        self.stock -= quanti
        if self.stock >= 2:
            print(f"Stock in existence: There are {self.stock} units in stock.")
        elif self.stock < 2 and self.stock > 0:
            print(f"Stock in existence: There is {self.stock} unit in stock.")
        else:
            print(f"The product {self.name} haven´t existence in stock.")


name = input("-Enter the product name: ").strip()

price = float(input("-Enter the product price (In Americans dollars): $"))

stock = int(input("-Enter the product stock: "))

product = Product(name, price, stock)

product.show_info()

while True:
    sell_product = input(
        "Do you want to buy the product or continue shopping for more? (y/n): "
    ).strip()
    if sell_product == "y":
        quanti = int(input("How much product do you want to sell?: "))
        print(f"Selling product: {name}")
        product.sell_quanti(quanti)
    elif sell_product == "n":
        print("Ok, not problem - leaving to system")
        break
    else:
        print("Error: You can only choose between y/n ⚠️ ")

"""9. Playlist 🎶

Enunciado:
Crea una clase Playlist con atributo canciones (list vacía).

Método agregar_cancion(titulo) → añade la canción a la list.

Método mostrar_canciones() → imprime todas las canciones.

Pistas:

Recuerda que una list empieza vacía ([]).

¿Qué método de listas te sirve para añadir un nuevo elemento? (append)

Usa un bucle for para imprimir las canciones.

Agrega al menos 3 canciones y muéstralas."""


class Playlist:
    def __init__(self):
        self.list = []

    def add_song(self):
        song = input("Add a song to the playlist: ").strip()
        artist = input("Add a artist to the list: ").strip()
        self.list.append((song, artist))

    def show_songs(self):
        print("🎵📝Curren Playlist: ")
        for song, artist in self.list:
            print(f"Song: {song} - Artist: {artist}")


song1 = Playlist()

while True:
    song1.add_song()
    contn = input("Do you want to continue adding songs? --> (y/n): ")
    if contn == "y":
        print("Keep adding 🫡")
    elif contn == "n":
        print("Leaving...")
        break
    else:
        print("You can only choose between (y/n)⚠️")

song1.show_songs()


"""10. Restaurante 🍽️

Enunciado:
Crea una clase Restaurante con atributos nombre y menu (diccionario con platillo → precio).

Método mostrar_menu() → imprime el menú con todos los platillos y precios.

Método ordenar(platillo) → si existe, imprime el precio; si no, un mensaje de error.

Pistas:

¿Qué estructura de Python te permite asociar clave → valor? (diccionario)

Dentro de ordenar(), ¿cómo verificas si un platillo está en el diccionario? (in)

Simula al menos 2 pedidos: uno correcto y otro con un platillo que no exista."""


class Restaurant:
    def __init__(self, name_restaurant, menu_name):
        self.menu_resturant = name_restaurant
        self.menu_name = menu_name
        self.menu = {}

    def add_dish(self, name_dish, price_menu):
        self.menu[name_dish] = price_menu

    def show_menu(self):
        print(f"Welcome to {self.menu_resturant}, show the menu {self.menu_name}: 🍽️")
        for name_dish, price_menu in self.menu.items():
            print(f"Dish: {name_dish} - Price: ${price_menu}dllrs")

    def order_dish(self, name_dish):
        if name_dish in self.menu:
            print(f"The dish: {name_dish} have a price: ${self.menu[name_dish]}dllrs")
        else:
            print(f"Error, the dish is not found in {self.menu_name}")


dishes = Restaurant("The Premium Kitchen", "💪Fitness Menu")

name_dish = input("Add the dish to the menu: ").strip()

price_menu = float(input(f"Add the price of {name_dish} dllrs: "))

dishes.add_dish(name_dish, price_menu)

dishes.show_menu()

dishes.order_dish(name_dish)
