import math

def calculate_square(side):
    perimeter = 4 * side
    area = side ** 2
    return 'Square', perimeter, area

def calculate_rectangle(top_right_x, top_right_y, bottom_left_x, bottom_left_y):
    length = top_right_x - bottom_left_x
    width = top_right_y - bottom_left_y
    perimeter = 2 * (length + width)
    area = length * width
    return 'Rectangle', perimeter, area

def calculate_circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return 'Circle', perimeter, area

def display(geometric_figure, perimeter, area):
    print(f'{geometric_figure} Perimeter {round(perimeter, 2)} Area {round(area, 2)}')

def main():
    geometric_figure = input('Type geometric figure: ')
    match geometric_figure:
        case 'Square':
            shape = float(input('Type side of the square: '))
            figure, perimeter, area = calculate_square(shape)
            display(figure, perimeter, area)
        case 'Rectangle':
            top_right_x = float(input('Type top right x coordinate: '))
            top_right_y = float(input('Type top right y coordinate: '))
            bottom_left_x = float(input('Type bottom left x coordinate: '))
            bottom_left_y = float(input('Type bottom left y coordinate: '))
            figure, perimeter, area = calculate_rectangle(*[top_right_x, top_right_y, bottom_left_x, bottom_left_y])
            display(figure, perimeter, area)
        case 'Circle':
            shape = float(input('Type radius of the circle: '))
            figure, perimeter, area = calculate_circle(shape)
            display(figure, perimeter, area)
            
if __name__ == '__main__':
    main()
