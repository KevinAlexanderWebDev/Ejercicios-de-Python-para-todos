"""Vamos a entrarle con todo a los 4 pilares de la Programación Orientada a Objetos (POO). 
A continuación unos ejemplos de: Herencia, Encapsulación, Polimorfismo y Abstracción.
Su repaso es fundamental para tener los 'cimientos de una casa': sin ellos, la construcción no se sostiene."""

#Ejemplo de Herencia
# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido.")


# clase Hija
class Perro(Animal):
    def hacer_sonido(self):
        print(f"El perro {self.nombre} está ladrando.")


guffy = Perro("Tobbie")

guffy.hacer_sonido()

#Ejemplo de Encapsulación(_'variable') + Herencia
# Parent class
class BankAccount:
    def __init__(self, balance, username, password):
        self._balance = balance  # Balance es saldo en inglés
        self.bank_name = "BanRegio"
        self.username = username
        self._password = password

    def deposit(self, amount):
        self._balance += amount  # amount es cantidad o monto en inglés

    def show_balance(self):
        print("This is your data-bank information: ")
        print(f"The current balance of the account is: ${self._balance} dllrs.")


# Daughter class
class BankUser(BankAccount):
    def show_userdata(self):
        print(f"Welcome back to {self.bank_name} {self.username} !")


user_name = input("Enter your username: ").strip()

user_password = input("Add your user-password: ").strip()

account = BankAccount(10000, user_name, user_password)

user_account = BankUser(10000, user_name, user_password)

user_account.show_userdata()

amount = int(
    input(
        "How many amount you want deposit en the BankAccount in americans dollars?: $"
    )
)

account.deposit(amount)

account.show_balance()

# Polimorfismo


class Cat:
    def __init__(self):
        self.cat_dic = {}
        self.cat_sound = "Miau🐱"

    def make_sound(self):
        self.cat_dic["Cat"] = self.cat_sound
        return self.cat_dic


class Chicken:
    def __init__(self):
        self.chicken_dic = {}
        self.chicken_sound = "Ki ki ri ki Ki 🐔🎶"

    def make_sound(self):
        self.chicken_dic["Chicken"] = self.chicken_sound
        return self.chicken_dic

    # Es el mismo método en ambas clases, pero una diferente acción, eso la hace flexible.


animals = [Cat(), Chicken()]

for i, animal in enumerate(animals, start=1):
    print(f"{i} - Animal: Sound {animal.make_sound()}")

#EJemplo de Abstracción
from abc import ABC, abstractclassmethod

class Figure(ABC):
    @abstractclassmethod
    def area(self):
        pass
class Circle(Figure):
    def __init__(self, radio):
        self.radio= radio
    def area(self):
        circle_formule= 3.1416 * (self.radio ** 2)
        circle_formule_round= round(circle_formule, 2)
        return circle_formule_round

figure1= Circle(5)
print(f"El área del círculo es: {figure1.area()}")

"""🟦 6. Herencia

Crea una clase Animal que tenga un método hacer_sonido(). Luego crea dos clases hijas (Perro y Gato) que hereden de Animal y hagan su propio sonido.

👉 Objetivo: Practicar cómo una clase hija puede heredar atributos/métodos de una clase padre.
"""


class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def make_sound(self):
        print(f"The buddie {self.animal_name} makes a sound🎵.")


class Dog(Animal):
    def make_sound(self):
        print(f"The puppy '{self.animal_name}' does Guau Guau🐶.")


class Cat(Animal):
    def make_sound(self):
        print(f"The kitten '{self.animal_name}' does Miau 🐱.")


animal_name = input("Insert the buddy name: ").strip()

animal1 = Animal(animal_name)

animal1.make_sound()

buddie1 = Dog(animal_name)

buddie1.make_sound()

buddie2 = Cat("Michi")

buddie2.make_sound()

"""🟦 2. Encapsulación

Crea una clase CuentaBancaria que tenga un atributo privado __saldo. Haz métodos públicos para depositar(cantidad) y retirar(cantidad) y un método mostrar_saldo().

👉 Objetivo: Practicar cómo ocultar atributos internos y exponer solo lo necesario mediante métodos.
"""


class BankAccount:
    def __init__(self, balance, username, user_password):
        self.__balance = balance
        self.username = username
        self._user_password = user_password
        self.bank_name = "BBVA Bancomer"

    def greeting(self):
        print(f"Welcome back to {self.bank_name} {self.username}!")

    def deposit_amount(self, amount):
        print(f"Depositing ${amount}dllrs in the account")
        self._balance += amount
        print("Amount successfully deposited💰👍!.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: You do not have sufficient balance.")
            print(f"You have: ${self.__balance} dllrs of balance.")
        else:
            print(f"Ok, withdrawing: ${amount} dllrs from account.")
            self.__balance -= amount
            print("Amount successfully withdraw ➖💸")

    def donate(self, amount_todonate):
        if amount_todonate > self.__balance:
            print("Error: You do not have sufficient balance.")
            print(f"You have: ${self.__balance}dllrs of balance.")
        else:
            print(f"Ok, donating: ${amount_todonate} dllrs from account.")
            self.__balance -= amount_todonate
            print("Amount successfully donate 🥹💸")

    def show_balance(self):
        print(f"Your account balance is: ${self.__balance} dllrs. ")


username = input("Enter your username: ").strip()

user_password = input("Enter your password: ").strip().replace(" ", "")

user1 = BankAccount(10000, username, user_password)

user1.greeting()  # Se saluda al usuario

while True:
    choice = (
        input(
            "Do you want to deposit(d) or withdraw(w) money from your account? (d/w): "
        )
        .strip()
        .replace(" ", "")
    )

    if choice == "d":
        user1.show_balance()
        balance = float(
            input(
                "How much money do you want to deposit into your account (in amercicans dollars): $"
            )
        )
        user1.deposit_amount(balance)
        user1.show_balance()
        choice = (
            input(
                "Do you want to continue(c) depositing or exit(e) the account? (c/d): "
            )
            .strip()
            .replace(" ", "")
        )
        if choice == "c":
            print("Ok, back to the beggining")
        elif choice == "e":
            donate = (
                input("Do you want to donate to ugly children? - (y/n): ")
                .strip()
                .replace(" ", "")
            )
            if donate == "y":
                print("You are a beatiful person🥹")
                donation = float(
                    input(
                        "How much money do you want to donate (in americans dollars): $"
                    )
                )
                user1.donate(donation)
                user1.show_balance()
                break
            elif donate == "n":
                print("You are a horrible person and you will die alone.💀⚰️")
                print("Ok, logging out")
                break
            else:
                print("Error: you can only choice between - (c/e)")
        else:
            print("Error: you can only choice between (c/e)")

    if choice == "w":
        user1.show_balance()
        balance = float(
            input(
                "How much money do you want to withdraw from your account (in amercicans dollars): $"
            )
        )
        user1.withdraw(balance)
        user1.show_balance()
        choice = (
            input(
                "Do you want to continue(c) withdrawing or exit(e) the account? (c/d): "
            )
            .strip()
            .replace(" ", "")
        )
        if choice == "c":
            print("Ok, back to the beggining")
        elif choice == "e":
            donate = (
                input("Do you want to donate to ugly children? - (y/n): ")
                .strip()
                .replace(" ", "")
            )
            if donate == "y":
                print("You are a beatiful person🥹")
                donation = float(
                    input(
                        "How much money do you want to donate (in americans dollars): $"
                    )
                )
                user1.donate(donation)
                user1.show_balance()
                break
            elif donate == "n":
                print("You are a horrible person and you will die alone.💀⚰️")
                print("Ok, logging out")
                break
            else:
                print("Error: you can only choice between - (c/e)")
        else:
            print("Error: you can only choice between (c/e)")

"""🟦 3. Polimorfismo

Crea una función presentar_animal(animal) que reciba cualquier objeto de tipo Animal y llame a su método hacer_sonido().

👉 Objetivo: Practicar cómo un mismo método puede funcionar de distintas formas según el objeto.
"""


class Chicken:
    def show_animal(self):
        chicken_sound = "ki ki ri ki ki 🐔🎶"
        animal_name = "Chicken"
        return animal_name, chicken_sound


class Cow:
    def show_animal(self):
        cow_sound = "Mouuuw Mouuuw 🐮🎶"
        animal_name = "Cow"
        return animal_name, cow_sound


def present_animal(animal):
    animal_name, animal_sound = animal.show_animal()
    print(f"The animal {animal_name} makes a sound: {animal_sound}🎶")


animals = [Cow(), Chicken()]

for animal in animals:
    present_animal(animal)

"""🟦 4. Abstracción

Usa from abc import ABC, abstractmethod.
Crea una clase abstracta Figura con un método abstracto area(). Luego crea dos clases (Cuadrado y Circulo) que implementen el método area().

👉 Objetivo: Practicar cómo obligar a las clases hijas a implementar métodos."""

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Circule(Figure):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area_circule = 3.1416 * (self.radio**2)
        area_circuleround = round(area_circule, 2)
        return area_circuleround


class Square(Figure):
    def __init__(self, side):
        self.side = side  # Side is 'lado' in english

    def area(self):
        area_square = self.side * self.side
        area_squareround = round(area_square, 2)
        return area_squareround


while True:

    choice = (
        input(
            "Which figure do you want to calculate the area of? - 's' for square or 'c' for circle: "
        )
        .strip()
        .replace(" ", "")
    )

    if choice == "s":
        print("Area of the square ⏹️")
        figure = float(
            input("Insert the measurement of the sides of the square in cm: ")
        )
        figure_area = Square(figure)
        print(f"The area of the squeare is: {figure_area.area()}cm squares.")
        choice = (
            input(
                "Do you want to continue(c) adding or log out(lo) of the system? (c/lo): "
            )
            .strip()
            .replace(" ", "")
        )
        if choice == "c":
            print("Ok, back to the beggining")
        elif choice == "lo":
            print("Ok, logging out")
            break
        else:
            print("Error: you can only choice between (c/lo)")

    elif choice == "c":
        print("Area of the circle⭕")
        figure = float(input("Insert radio measuraments in cm: "))
        figure_area = Circule(figure)
        print(f"The area of the circle is: {figure_area.area()}cm squares.")
        choice = (
            input(
                "Do you want to continue(c) adding or log out(lo) of the system? (c/lo): "
            )
            .strip()
            .replace(" ", "")
        )
        if choice == "c":
            print("Ok, back to the beggining")
        elif choice == "lo":
            print("Ok, logging out")
            break
        else:
            print("Error: you can only choice between (c/lo)")
