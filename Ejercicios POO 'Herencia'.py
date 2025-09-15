"""🟦 Ejercicios de Herencia
1. Herencia básica – atributos y métodos

Crea una clase Vehiculo con atributos brand y model.
Luego crea una clase hija Coche que además tenga puertas.
Instancia un Coche y muestra sus datos.

👉 Objetivo: Familiarizarte con herencia directa."""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_auto(self):
        print("These are the car data: ")
        print(f"Brand: {self.brand} - Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
        print(f"The car has {self.doors} doors")


car_brand = input("Insert the car brand: ").strip().replace(" ", "")

car_model = input("Insert the car model: ").strip().replace(" ", "")

car_doors = int(
    input(f"Enter the number of doors the car '{car_brand} - {car_model}' will have: ")
)

car_one = Car(car_brand, car_model, car_doors)

car_one.show_auto()

"""2. Extender métodos usando super()

Crea una clase Empleado con un método mostrar_datos().
Luego crea una clase Gerente que herede de Empleado y agregue su propio campo departamento.
Haz que mostrar_datos() en Gerente llame al método del padre con super(), y luego muestre el departamento.

👉 Objetivo: Practicar cómo no perder la lógica del padre."""


class Employee:  # Employee es empleado del inglés
    def __init__(self, employee_name, employee_id, employee_age):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.employee_age = employee_age

    def show_data(self):
        print(f"Employee Name: {self.employee_name}")
        print(f"Employee id: {self.employee_id}")
        print(f"Employee age: {self.employee_age} years old")


class Manager(Employee):
    def __init__(
        self,
        employee_name,
        employee_id,
        employee_age,
        employee_position,
        employee_departament,
    ):
        super().__init__(employee_name, employee_id, employee_age)
        self.employee_position = employee_position
        self.employee_departament = employee_departament
        print("These are the employee data: ")
        print(f"The employee is: Is a {self.employee_position}")
        print(f"Work in: Works in department number {self.employee_departament}. ")


print("Insert data of employee...")
employee_name = input("Insert the employee name: ").strip()

employee_id = input("Insert the employee ID: ").strip().replace(" ", "")

employee_age = int(input("Insert the employee age: "))

employee_position = input("Insert the employee position: ").strip()

employee_departament = int(input("Insert the employee departament: "))

employee_one = Manager(
    employee_name, employee_id, employee_age, employee_position, employee_departament
)

employee_one.show_data()

"""3. Polimorfismo en herencia

Crea una clase Instrumento con un método tocar().
Luego crea Guitarra y Bateria que hereden y sobrescriban el método.
Haz una lista con distintos instrumentos y recórrela llamando tocar().

👉 Objetivo: Ver cómo distintas clases hijas usan el mismo método pero con resultados diferentes.
"""


class Instrument:
    def __init__(self):
        self.instruments = []

    def play(self):
        print(
            "Next, insert the instruments you want to add to the list, press '+' or 'enter' to stop adding."
        )
        while True:
            instrument = input("Insert the instruments to list: ").strip()
            if not instrument or instrument == "+":
                break
            self.instruments.append(instrument)
        print("\n")
        print("List of Instruments to play🎶")
        for i, instrument in enumerate(self.instruments, start=1):
            print(f"{i} - Instrument: {instrument}🎶")
        print("\n")


class Guitar(Instrument):
    def play(self):
        return "Playing Guitar🎸🎶"


class Piano(Instrument):
    def play(self):
        return "Playing Piano 🎹"


instruments_list = Instrument()

instruments_list.play()

instrument = [Guitar(), Piano()]
print("Playing this instruments: ")
for i, inst in enumerate(instrument, start=1):
    print(f"{i} - Instrument: {inst.play()}")
print("\n")

"""4. Herencia múltiple + MRO

Crea una clase Terrestre con un método moverse().
Crea otra clase Acuatico con un método moverse().
Crea una clase Anfibio que herede de ambas.
Prueba obj.moverse() y revisa qué método se ejecuta.
Después usa super() para combinar ambos comportamientos.

👉 Objetivo: Practicar cómo Python resuelve el MRO (Method Resolution Order)."""


class Land:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def move(self):
        print(f"The land vehicle {self.vehicle} is moving")


class Water:
    def move(self):
        print(f"The water vehicle {self.vehicle} is moving")


class Amphibian(Land, Water):
    def move(self):
        super().move()
        print("I move on land or water")


vehicle = Amphibian("Truck")

vehicle.move()

"""5. Caso avanzado: Herencia vs Composición

Crea una clase Usuario con nombre y email.
Crea una clase CuentaBancaria que tenga un saldo y un objeto Usuario dentro.
Muestra cómo acceder a los datos del usuario desde la cuenta.

👉 Pregunta de reflexión: ¿por qué aquí no conviene que CuentaBancaria herede de Usuario?
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class BankAccount:
    def __init__(self, balance, user):
        self.__balance = balance
        self.user = user

    def show_user(self):
        print("This is the user's data: ")
        print(
            f"Username: {self.user.name} - User_Email: {self.user.email} - User_Balance: ${self.__balance} dllrs."
        )


user_name = input("Insert your user name: ").strip().replace(" ", "")

user_email = input("Insert your user email: ").strip().replace(" ", "")

name = User(user_name, user_email)

user_account = BankAccount(4000, name)

user_account.show_user()
