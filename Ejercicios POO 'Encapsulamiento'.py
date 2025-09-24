"""🔐 Ejercicios de Encapsulación
1. Banco (seguimos con tu mini sistema)

Crea un atributo privado __pin para la cuenta.

Al iniciar la cuenta, pide que el usuario establezca un PIN.

Para retirar dinero, el usuario debe ingresar su PIN correctamente.

Si el PIN es incorrecto, no se realiza la operación.

👉 Pregunta: ¿cómo protegerías este atributo para que no pueda ser modificado directamente desde fuera?
"""


class BankAccount:
    def __init__(self, name, balance, pin):
        self.username = name
        self.__balance = balance
        self.__pin = pin
        self.__attempts = 3

    @property  # Ayuda a hacer un getter de forma más elegante y propia de python
    def balance(self):
        return self.__balance

    @balance.setter  # Ayuda a hacer un setter de forma más elegante y propia de python
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid Balance❌")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"It has been deposited successfully ${amount} dollars.")
            print(f"New Balance: {self.__balance}")
        else:
            print("Invalid Amount❌")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("You do not have sufficient balance❌")
        else:
            while True:
                max_lengh = 4
                pin_password = (
                    input("Insert the pin-password to proceed: ")
                    .strip()
                    .replace(" ", "")
                )
                if len(pin_password) > max_lengh:
                    print("The pin is too long❌")
                elif len(pin_password) == max_lengh:
                    password_int = int(pin_password)
                    if password_int == self.__pin and self.__attempts > 1:
                        self.__balance -= amount
                        print(f"It has been withdraw successfully ${amount} dollars.")
                        print(f"New Balance: {self.__balance}")
                        break
                    elif password_int != self.__pin and self.__attempts > 1:
                        print("Incorrect Password❌")
                        self.__attempts -= 1
                        print(f"You have: {self.__attempts} attempts.")
                    else:
                        print("Incorrect Password: You have no more attemps❌")
                        print("Failed procedure👎")
                        break
                else:
                    print("The pin is too short❌")

    def show_data(self):
        print("User Data 👨‍🦰 👩‍🦰: ")
        print(f"User👤: {self.username}")
        print(f"This is your User-Balance💰: ${self.__balance} dollars.")


print("Welcome to Mini Bank System!")

name = input("Insert the username: ").strip()

while True:
    max_lengh = 4
    password = (
        input("Insert the pin-password (The value can only four caracters): ")
        .strip()
        .replace(" ", "")
    )
    if len(password) > max_lengh:
        print("The pin is too long❌")
    elif len(password) == max_lengh:
        print("Pin entered successfully👍")
        password_int = int(password)
        break
    else:
        print("The pin is too short❌")

init_balance = int(input("Insert the init_balance in americans dollars: $"))

account = BankAccount(name, init_balance, password_int)

while True:
    print("\n Chooce from the menu options: ")
    print("1: Show Balance")
    print("2: Deposit Amount")
    print("3: Whithdraaw Amount")
    print("4: Fix the balance")
    print("5: Show User-Data")
    print("6: Exit to System")

    choice = input("You choose: ").strip().replace(" ", "")

    if choice == "1":
        print(f"Init_Balance: {account.balance}")

    elif choice == "2":
        amount = int(input("Amount to Deposit: $"))
        account.deposit(amount)

    elif choice == "3":
        amount = int(input("Amount to Withdraw: $"))
        account.withdraw(amount)

    elif choice == "4":
        amount = int(input("Insert the new balance: $"))
        account.balance = amount

    elif choice == "5":
        account.show_data()

    elif choice == "6":
        print("Leaving from System, see you next time!🫡...")
        break

    else:
        print("⚠️ Error, you can only choice between: 1 ...4...6 ⚠️")

"""2. Videojuego – Personaje

Crea una clase Character con:

Atributos privados __health y __energy.

Métodos take_damage(amount) y recover(amount) para modificar salud y energía de forma controlada.

Si el daño supera la vida, esta nunca baja de 0.

Si se recupera, la salud no puede superar 100.

👉 ¿Por qué crees que es importante proteger la salud de un personaje?"""


class Character:
    def __init__(self, health, energy):
        self.__health = health
        self.__energy = energy

    def attack(self, energy_consumed):
        if energy_consumed <= self.__energy:
            self.__energy = max(self.__energy - energy_consumed, 0)
        else:
            print("You don't have enough energy to attack")

    def take_damage(
        self, amount
    ):  # Aquí debo de corregir porque aunque ya no haya energía como quiera se recibe el daño XD
        self.__health = max(self.__health - amount, 0)

    def recover(self, amount):
        if self.__health == 100 or self.__health == 150:  # We Manage two health ranges
            print("You can't recover, your life is at its maximum")
        else:
            self.__health = min(self.__health + amount, 100)
            self.__energy = min(self.__energy + amount, 100)

    # Show health
    @property
    def health(self):
        return self.__health

    # Show energy
    @property
    def energy(self):
        return self.__energy


print("Avangers Assamble: Battle Game ⚔️")
print(
    "Instructions: Challenge a friend. Choose the character you like best, each with different abilities. Each participant has 3 lives. Each turn allows you to perform an action (Attack or Recover). At the end of the turn, the player with the most health wins."
)
print("Choose a character: ")
print("Hulk🟢: ")
print("Maximum Damage of Attack ⚔️: 40")
print("Health ♥️: 150")
print("Recover 💚: 30")
print("Iron Man🔴🟡: ")
print("Maximum Damage of Attack ⚔️: 20")
print("Health ♥️: 100")
print("Recover 💛: 50")
hulk = Character(health=150, energy=100)
iron_man = Character(health=100, energy=150)

iron_man_attempts = 3
hulk_attempts = 3

while True:
    print("Is turn of Hulk🟢")
    print(
        f"Current Energy: {hulk.energy}"
    )  # Ctrl + right clic for variable declaration
    print(f"Current Health: {hulk.health}")
    hulk_attempts -= 1
    print("List of skills: ")
    print("1. Ultra Smash - Range of Damage: 30, - Energy consumed: 30")
    print("2. Mega Applause - Range of Damage: 20, - Energy consumed: 15")
    print("3. Hulk is upset - Range of Damage: 40, - Energy consumed: 35")
    print("4. Recover (Can only be used if you take damage)")
    choose = input("You choose: ")
    if choose == "1":
        print("🟢Hulk smashes!!, Hulk Smash ⚔️")
        hulk.attack(30)
        iron_man.take_damage(30)
    elif choose == "2":
        print("🟢Hulk claps!!⚔️")
        hulk.attack(15)
        iron_man.take_damage(20)
    elif choose == "3":
        print("🟢Hulk is angry!!, Hulk is upset!!⚡")
        hulk.attack(35)
        iron_man.take_damage(40)
    elif choose == "4":
        hulk.recover(30)
    else:
        print("You can only choise between - 1, 2, 3, 4")

    print("Is turn of Iron Man 🔴🟡")
    print(f"Current Energy: {iron_man.energy}")
    print(f"Current Health: {iron_man.health}")
    iron_man_attempts -= 1
    print("List of skills: ")
    print("1. Lightning Bolt - Range of Damage: 20, - Energy consumed: 10")
    print("2. Stark Reactor - Range of Damage: 10, - Energy consumed: 5")
    print("3. Laser Destroyer - Range of Damage: 15, - Energy consumed: 7")
    print("4. Recover (Can only be used if you take damage)")

    choose = input("You choose: ")
    if choose == "1":
        print("🔴🟡Jarvis, activate the lighting bolt!")
        print("Of course Sir⚡ ⚔️")
        iron_man.attack(10)
        hulk.take_damage(20)
    elif choose == "2":
        print("🔴🟡Jarvis, activate the stark reactor!")
        print("Right away sir!⚡⚔️")
        iron_man.attack(5)
        hulk.take_damage(10)
    elif choose == "3":
        print("🔴🟡Jarvis, activate the laser destroyer!")
        print("As you command, sir!⚡⚔️")
        iron_man.attack(7)
        hulk.take_damage(15)
    elif choose == "4":
        iron_man.recover(50)
    else:
        print("You can only choise between - 1, 2, 3, 4")

    if hulk.health <= 0:
        print("Iron Man wins the battle🥳.")
        break
    elif iron_man.health <= 0:
        print("Hulk wins the battle🥳.")
        break

"""3. Empresa – Empleado

Crea una clase Employee con:

Atributo privado __salary.

Método público get_salary() que devuelve el sueldo.

Método increase_salary(amount) que solo permita aumentos positivos.

Si intentas asignar el sueldo directamente desde fuera (employee.__salary = 1), debe fallar.

👉 ¿Qué problema habría si cualquiera pudiera modificar el sueldo libremente?"""


class Employee:
    def __init__(self, employee_name, employee_age, employee_antique, salary):
        self.__salary = salary
        self.employee_name = employee_name
        self.employee_age = employee_age
        self.employee_antique = employee_antique
        self.employee_data = {}

    def get_employee_data(self):
        self.employee_data[self.employee_name] = (
            self.employee_age,
            self.employee_antique,
        )
        print("This is the employee data: ")
        for name, values in self.employee_data.items():
            print(f"Employee Name: {name} - Employee Age and Antique: {values}")

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount > 0:
            percentage_increase = (amount * 100) / self.__salary
            print(
                f"Salary has increased by {percentage_increase}% - ${amount} dollars. "
            )
            self.__salary += amount
        else:
            print("Invalid Amount❌: Salary increase must be a positive value.")


print("Human Resources Departament🧑👧")

employee_name = input("Insert the employee name: ").strip()

employee_age = int(input("Insert the employee age: "))

employee_antique = int(input("Insert the employee antique: "))

employee_salary = float(input("Insert the employee salary in americans dollars: $"))

employee = Employee(employee_name, employee_age, employee_antique, employee_salary)

while True:

    print("Human Resources Menu: ")
    print("Choose from the options offered by the menu")
    print("1. Show employee's data.")
    print("2. Show employee's current salary.")
    print("3. Increase employee's current salary.")
    print("4. Log off.")
    choise = input("You choose: ").strip().replace(" ", "")

    if choise == "1":
        employee.get_employee_data()

    elif choise == "2":
        employee_salary = employee.get_salary()
        print(f"Current Employee Salary: ${employee_salary}.")

    elif choise == "3":
        increase_salary = float(
            input("Add the salary increase in americans dollars: $")
        )
        employee.increase_salary(increase_salary)

    elif choise == "4":
       print("--Ok, log out--")
       break
          
    else: 
        print("Value Error: You can only choose in the range 1 to 5!.")

"""4. Escuela – Calificaciones

Crea una clase Student con:

Atributo privado __grades (lista de calificaciones).

Método add_grade(grade) que valide que esté entre 0 y 10.

Método average() que devuelva el promedio.

👉 ¿Por qué es mejor validar las calificaciones con métodos en vez de dejar la lista abierta?
"""

import math


class Student:

    def __init__(self, name, age, career):
        self.student_name = name
        self.student_age = age
        self.student_career = career
        self.__grades = []
        self.__student_data = {}

    def show_student_data(self):
        self.__student_data[self.student_name] = (self.student_age, self.student_career)
        print("This is the student's data: ")
        for name, data in self.__student_data.items():
            print(f"Student Name: {name} - Student Age and Carreer: {data}")

    def add_grade(self):
        while True:
            grade = (
                input(
                    "Please insert the student grade (Press '+' or enter only to stop adding): "
                )
                .strip()
                .replace(" ", "")
            )
            if grade == "+" or not grade:
                break
            grade = float(grade)
            if grade > 0 and grade <= 10:
                self.__grades.append(grade)
            else:
                print("Error: You can only choose in the range 1 to 10!.")

    def show_grades(self):
        if not self.__grades:
            print("Error: The rating list is empty")
        else:
            print("These are the student's grades: ")
            for i, grade in enumerate(self.__grades, start=1):
                print(f"{i} - Grade: {grade}")

    def average(self):
        if not self.__grades:
            print("Error: The rating list is empty")
        else:
            list_len = len(self.__grades)
            list_addition = sum(self.__grades)
            student_average = list_addition / list_len
            student_round_average = math.floor(student_average)

            print(f"This is the student's average: {student_round_average}")
            if student_average >= 7:
                print(
                    f"The student {self.student_name} of the career {self.student_career} is approved!🥳"
                )
            else:
                print(
                    f"The student {self.student_name} of the career {self.student_career} isn't approved😓"
                )


student_name = input("Insert the student's name: ").strip()

student_age = int(input("Insert the student's age: "))

student_career = input("Insert the studen's career: ").strip()

student = Student(student_name, student_age, student_career)

print("Student's date information 🧑‍🎓 👩‍🎓")
while True:
    print("Student's date Menu: ")
    print("Choose from the options offered by the menu")
    print("1. Show student's data.")
    print("2. Add student's grade.")
    print("3. Show student's grade.")
    print("4. Show student's average")
    print("5. Log off.")
    choise = input("You choose: ").strip().replace(" ", "")

    if choise == "1":
        student.show_student_data()

    elif choise == "2":
        student.add_grade()

    elif choise == "3":
        student.show_grades()

    elif choise == "4":
        student.average()

    elif choise == "5":
        print("--Ok, log out--")
        break

    else:
        print("Value Error: You can only choose in the range 1 to 5!.")
        
"""Crea una clase ShoppingCart con:

Atributo privado __items (diccionario con producto: cantidad).

Método add_item(product, qty) para agregar productos.

Método remove_item(product) para quitarlos.

Método show_cart() que muestre el carrito de forma legible.

👉 ¿Qué pasaría si el usuario pudiera manipular directamente la lista/diccionario de productos sin restricciones?
"""


class ShoppingCart:
    def __init__(self, user_name):
        self.__items = {}
        self.user_name = user_name

    def add_item(self):
        while True:
            print(
                f"{self.user_name}, next insert the product's data (press '+' or enter only to stop adding)."
            )
            product = input("Insert the product's name: ").strip()
            if product == "+" or not product:
                break
            qty = input("Insert the product's quanty: ")
            if qty == "+" or not qty:
                break
            qty = int(qty)
            self.__items[product] = qty

    def remover_item(self):
        product_delete = input(
            "Enter the name of the product you want to delete: "
        ).strip()
        if product_delete in self.__items:
            choise = (
                input(
                    "Are you sure you want to delete the product from the database(This action cannot be undone): (y/s) "
                )
                .strip()
                .replace(" ", "")
                .lower()
            )
            if choise == "y":
                print(f"Removing {product_delete} from the database...")
                del self.__items[product_delete]
                print("Process completed successfully!👍")
            elif choise == "n":
                print("Ok, returning to lobby...👍")
            else:
                print("Error: You can only choose between 'y' or 'n'.")
        else:
            print(f"The product {product_delete} is not found in Data Base")
            choise = (
                input("Do you want to add it to shopping cart?: y/n ")
                .strip()
                .replace(" ", "")
                .lower()
            )
            if choise == "y":
                quanty = int(input("Insert the product queanty: "))
                print(f"Adding {product_delete} to shopping cart.")
                self.__items[product_delete] = quanty
                print(
                    f"{product_delete} was successfully added to the shopping cart🥳!"
                )
            elif choise == "n":
                print("Ok, returning to lobby...🫡")
            else:
                print("Type Error: You can only choose between yes or no.")

    def show_shopping_cart(self):
        print(f"{self.user_name}, this is your shopping cart list🛒: ")
        for product, quanty in self.__items.items():
            print(f"Product: {product} - Quanty: {quanty}")


print("Welcome to your 'Shopping Cart List🛒' creator")

user_name = input("Adding your user name: ").strip()

shopping_cart1 = ShoppingCart(user_name)

while True:
    print(f"Welcome Back {user_name}")
    print("Software Menu: ")
    print("Choose from the options offered by the menu")
    print("1. Add product to list.")
    print("2. Remove product.")
    print("3. Show user shooping list.")
    print("4. Log off.")
    choise = input("You choose: ").lower().replace(" ", "").strip()

    if choise == "1":
        shopping_cart1.add_item()

    elif choise == "2":
        shopping_cart1.remover_item()

    elif choise == "3":
        shopping_cart1.show_shopping_cart()

    elif choise == "4":
        break

    else:
        print("Value Error: You can only choose in the range 1 to 4...")

