class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14159 * self.radius

# Пример использования класса
circle = Circle(10)
print("Circle area:", circle.area())
print("Circle circumference:", circle.circumference())

# Обработка ошибок при вводе
try:
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
except ValueError:  # Удалили TypeError и исправили на ValueError
    print("Invalid input")
