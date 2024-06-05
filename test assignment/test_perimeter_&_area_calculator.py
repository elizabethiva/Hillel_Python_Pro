from perimeter_area_calculator import Circle, Rectangle, Square
import unittest


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(2)

    def test_perimeter(self):
        perimeter = self.square.calculate_perimeter()
        assert perimeter == 8.0
        print("Square perimeter test passed")

    def test_area(self):
        area = self.square.calculate_area()
        assert area == 4.0
        print("Square area test passed")


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(2, 2, 1, 1)

    def test_perimeter(self):
        perimeter = self.rectangle.calculate_perimeter()
        assert perimeter == 4.0
        print("Rectangle perimeter test passed")

    def test_area(self):
        area = self.rectangle.calculate_area()
        assert area == 1.0
        print("Rectangle area test passed")


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(2)

    def test_perimeter(self):
        perimeter = self.circle.calculate_perimeter()
        assert round(perimeter, 2) == 12.57
        print("Circle perimeter test passed")

    def test_area(self):
        area = self.circle.calculate_area()
        assert round(area, 2) == 12.57
        print("Circle area test passed")


def main():
    square_tester = TestSquare()
    square_tester.test_perimeter()
    square_tester.test_area()

    rectangle_tester = TestRectangle()
    rectangle_tester.test_perimeter()
    rectangle_tester.test_area()

    circle_tester = TestCircle()
    circle_tester.test_perimeter()
    circle_tester.test_area()


if __name__ == "__main__":
    main()
