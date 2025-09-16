"""🟦 Ejercicios de Diferenciación: Herencia vs Composición
1. Mascotas y Dueños

Crea una clase Mascota con nombre y edad.

Crea una clase Dueño con nombre y telefono.

Haz que un Dueño tenga una o varias mascotas (composición).

Pregunta: ¿por qué no tendría sentido que Dueño herede de Mascota?"""

class Pet: 
    def __init__(self, pet_name, age):
        self.pet_name= pet_name
        self.age= age

        
class Owner:
    def __init__(self, owner_name, owner_phone, pet_list):
        self.owner_name= owner_name
        self.owner_phone= owner_phone
        self.pet_list= pet_list
        self.pet_dic= {}
        
    def owner_data(self):
        print("This is the owner's data: ")
        print(f"Owner_Name: {self.owner_name} - Owner_Phone: {self.owner_phone}")
        
    def pet_data(self):
        self.pet_dic[self.pet_list.pet_name]= self.pet_list.age
        print("This is the pet's-data: ")
        for pet_name, pet_age in self.pet_dic.items():
            print(f"Pet_Name: {pet_name} - Pet_Age: {pet_age}")
        
pet_data= Pet("Guffy", 6)

owner_data= Owner("Kevin", 8332875807, pet_data)

owner_data.owner_data()

owner_data.pet_data()

"""2. Rectángulo y Cuadrado

Crea una clase Rectangulo con atributos base y altura, y un método area().

Crea una clase Cuadrado que herede de Rectangulo.

Inicializa el Cuadrado con un solo lado, pero aprovecha el constructor del padre para asignar base y altura.

Pregunta: ¿Aquí por qué sí conviene usar herencia en lugar de composición?"""

class Rectangle: 
    def __init__(self, base, height):
        self.base= base
        self.height= height
    def area(self):
        area= self.base * self.height
        return area

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 
 
side= int(input("Insert the square side in square's cm: "))

base= int(input("Insert the rectangle base in square's cm: ")) 

height= int(input("Insert the rectangle height in square's cm: "))
        
figure_square= Square(side)
square_area= figure_square.area()
figure_rectangle= Rectangle(base, height)
rectangle_area= figure_rectangle.area()
print(f"The square area is: {square_area} squares cm.")
print(f"The rectangle area is: {rectangle_area} squares cm.")
    
"""3. Vehículo y Motor

Crea una clase Motor con un método encender().

Crea una clase Vehiculo que tenga una instancia de Motor dentro (composición).

Haz que Vehiculo use el método encender() del motor.

Pregunta: ¿Por qué no sería buena idea que Vehiculo herede de Motor?"""


class Engine:
    def __init__(self, motor_model):
        self.motor_model = motor_model

    def turn_on(self):
        print("The vehicle is turn on🔑")


class Vehicle:
    def __init__(self, brand, model, engine_model):
        self.brand = brand
        self.moderl = model
        self.engine_model = engine_model
        self.engine = Engine(
            engine_model
        )  # No se está heredando, se está haciendo una composición.

    def show_vehicle_data(self):
        print(f"Vehicle data --> Brand: {self.brand} - Model: {self.moderl}.")
        print(f"Vehicle Engine Brand: {self.engine_model.motor_model}")

    def turn_on(self):
        self.engine.turn_on()


vehicle_brand = input("Insert the vehicle brand: ").strip()

vehicle_model = input("Insert the vehicle model: ").strip()

vehicle_engine = input("Insert the vehicle engine: ").strip()

engine_obj = Engine(vehicle_engine)

vehicle_obj = Vehicle(vehicle_brand, vehicle_model, engine_obj)

vehicle_obj.show_vehicle_data()

vehicle_obj.turn_on()

"""4. Persona y Dirección

Crea una clase Direccion con atributos calle, ciudad, pais.

Crea una clase Persona que tenga dentro un objeto Direccion.

Haz un método en Persona que muestre su dirección.

Pregunta: ¿Qué pasaría si en lugar de composición usaras herencia?"""


class Adress:
    def __init__(self, street, city, country):
        self.street = street
        self.country = country
        self.city = city


class Person:
    def __init__(self, person_name, person_age, adress_data):
        self.person_name = person_name
        self.persona_age = person_age
        self.adress_data = adress_data

    def show_adress(self):
        print(f"This is the person adress for {self.person_name}: ")
        print(f"Street: {self.adress_data.street}")
        print(f"City: {self.adress_data.city}")
        print(f"Country: {self.adress_data.country}")


person_name = input("Insert the person name: ").strip()

person_age = int(input("Insert the person age: "))

person_street = input("Insert the person street: ").strip()

person_city = input("Insert the person city: ").strip()

person_country = input("Insert the person country: ").strip()

adress_one = Adress(person_street, person_city, person_country)

person_one = Person(person_name, person_age, adress_one)

person_one.show_adress()

"""5. Juego de Personajes

Crea una clase Personaje con atributos nombre y vida.

Crea clases hijas Guerrero y Mago (herencia), con métodos diferentes (atacar y lanzar_hechizo).

Ahora crea una clase Inventario que guarde objetos que tiene un personaje (composición).

Pregunta: ¿Cómo combina este ejemplo herencia + composición y qué ventajas da?"""


class Character:
    def __init__(self, character_name, character_life):
        self.name = character_name
        self.life = character_life
        self.inventory = Inventory(self)


class Warrior(Character):
    def __init__(self, character_name, character_life):
        super().__init__(character_name, character_life)

    def attack(self, enemy):
        print(f"The warrior: {self.name} is attack.🛡️⚔️🤺 to {enemy.name}")
        enemy.life -= 10


class Wizard(Character):
    def __init__(self, character_name, character_life):
        super().__init__(character_name, character_life)

    def cast_a_spell(self, enemy):
        print(f"The wizard: {self.name} is cast a spell🧙🧿 to {enemy.name}")
        enemy.life -= 20


class Inventory:
    def __init__(self, character):
        self.obj = []
        self.character = character

    def add_object(self):
        print("Add the items the character will use, press '+' to stop adding.")
        while True:
            object_character = input(
                f"Add the '{self.character.name}' objects: "
            ).strip()
            if object_character == "+" or not object_character:
                break
            print(f"Object '{object_character}' add to list!")
            self.obj.append(object_character)

    def show_lifes(self):
        print(f"These are the lifes of {self.character.name}: {self.character.life}")

    def show_object(self):
        print(f"This is the inventory to {self.character.name}")
        for i, object in enumerate(self.obj, start=1):
            print(f"{i} - Object: {object}")


wizard_name = input("Insert the name of the character 'Wizard': ").strip()

wizard_lives = int(input("Insert the wizard lives♥️: "))

wizard1 = Wizard(wizard_name, wizard_lives)

warrior_name = input("Insert the name of the character 'Warrior': ").strip()

warrior_lives = int(input("Insert the warrior lives♥️: "))

warrior = Warrior(warrior_name, warrior_lives)

wizard1.inventory.add_object()

warrior.inventory.add_object()

wizard1.inventory.show_object()

warrior.inventory.show_object()

wizard1.cast_a_spell(warrior)
print(f"Remaining lives: {wizard1.life}")

warrior.attack(wizard1)
print(f"Remaining lives: {warrior.life}")

wizard1.inventory.show_lifes()

warrior.inventory.show_lifes()
