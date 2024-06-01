from perimeter_area_calculator import (calculate_circle, calculate_rectangle,
                                       calculate_square)


def test_calculate_square():
    figure, perimeter, area = calculate_square(2)
    assert figure == "Square"
    assert perimeter == 8.0
    assert area == 4.0
    print("Square test passed")


def test_calculate_rectangle():
    figure, perimeter, area = calculate_rectangle(2, 2, 1, 1)
    assert figure == "Rectangle"
    assert perimeter == 4.0
    assert area == 1.0
    print("Rectangle test passed")


def test_calculate_circle():
    figure, perimeter, area = calculate_circle(2)
    assert figure == "Circle"
    assert round(perimeter, 2) == 12.57
    assert round(area, 2) == 12.57
    print("Circle test passed")


test_calculate_square()
test_calculate_rectangle()
test_calculate_circle()
