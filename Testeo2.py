"""🟦 4. Abstracción

Usa from abc import ABC, abstractmethod.
Crea una clase abstracta Figura con un método abstracto area(). Luego crea dos clases (Cuadrado y Circulo) que implementen el método area().

👉 Objetivo: Practicar cómo obligar a las clases hijas a implementar métodos."""

from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Figure):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        area_circule = 3.1416 * (self.radio**2)
        area_circuleround = round(area_circule, 2)
        return area_circuleround

class Triangle(Figure):
    def __init__(self, base, height):
        self.base= base
        self.height= height
    
    def area(self):
        area_triangle= (self.base * self.height) / 2
        area_triangleround= round(area_triangle, 2)
        return area_triangleround
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
            "Which figure do you want to calculate the area of? - 's' for square, 'c' for circle or 't' for triangle: "
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
        figure_area = Circle(figure)
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
            
    elif choice == "t":
        print("Area of the triangle📐")
        base = float(input("Insert base measuraments in cm: "))
        height= float(input("Insert height measuraments in cm: "))
        figure_area = Triangle(base, height)
        print(f"The area of the triangle is: {figure_area.area()}cm squares.")
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
