class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)  # E501 line too long (40 > 79 characters)

    def circumference(self):
        return 2 * 3.14159 * self.radius  # E501 line too long (37 > 79 characters)

# Пример использования класса
circle = Circle(10)
print("Circle area:", circle.area())  # W291 trailing whitespace
print("Circle circumference:", circle.circumference())  # E501 line too long (46 > 79 characters)

# Ошибка в блоке except
try:
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
except ValueError as TypeError:  # E999 SyntaxError: multiple exception types must be parenthesized
    print("Invalid input")
