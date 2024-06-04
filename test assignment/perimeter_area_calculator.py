import math


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        self.perimeter = 4 * self.side
        return self.perimeter

    def calculate_area(self):
        self.area = self.side**2
        return self.area


class Rectangle:
    def __init__(self, top_right_x, top_right_y, bottom_left_x, bottom_left_y):
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y
        self.length = self.top_right_x - self.bottom_left_x
        self.width = self.top_right_y - self.bottom_left_y

    def calculate_perimeter(self):
        self.perimeter = (self.length + self.width) * 2
        return self.perimeter

    def calculate_area(self):
        self.area = self.length * self.width
        return self.area


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter

    def calculate_area(self):
        self.area = math.pi * (self.radius**2)
        return self.area


class ShapeResult:
    def __init__(self, geometric_figure, perimeter, area):
        self.geometric_figure = geometric_figure
        self.perimeter = perimeter
        self.area = area

    def format_result(self):
        return f"{self.geometric_figure} Perimeter {round(self.perimeter, 2)} Area {round(self.area, 2)}"


def main():
    geometric_figure = input("Type geometric figure: ")

    match geometric_figure:
        case "Square":
            side = float(input("Enter side of square: "))
            square = Square(side)
            result = ShapeResult(
                geometric_figure, square.calculate_perimeter(), square.calculate_area()
            )
            print(result.format_result())

        case "Rectangle":
            top_right_x = float(input("Enter top right x coordinate: "))
            top_right_y = float(input("Enter top right y coordinate: "))
            bottom_left_x = float(input("Enter bottom left x coordinate: "))
            bottom_left_y = float(input("Enter bottom left y coordinate: "))
            rectangle = Rectangle(
                top_right_x, top_right_y, bottom_left_x, bottom_left_y
            )
            result = ShapeResult(
                geometric_figure,
                rectangle.calculate_perimeter(),
                rectangle.calculate_area(),
            )
            print(result.format_result())

        case "Circle":
            radius = float(input("Enter radius of circle: "))
            circle = Circle(radius)
            result = ShapeResult(
                geometric_figure, circle.calculate_perimeter(), circle.calculate_area()
            )
            print(result.format_result())


if __name__ == "__main__":
    main()
