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
