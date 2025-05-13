import math
import sys
from decimal import Decimal


def square(coord, point):
    formula = math.sqrt((point[0] - coord[0]) ** 2 + (point[1] - coord[1]) ** 2)
    return round(formula, 2)


def check(formula, r):
    if r > formula:
        return 1
    elif r < formula:
        return 2
    else:
        return 0


def main():
    """
    Компанда для запуска:
    python3 task2.py circle.txt points.txt

    """
    with open(sys.argv[1], 'r') as f:
        line1 = f.readline().strip().split()
        circle_x = Decimal(line1[0])
        circle_y = Decimal(line1[1])
        r = Decimal(f.readline().strip())
        coord = (circle_x, circle_y)
    with open(sys.argv[2], 'r') as f:
        points = []
        for line in f:
            x, y = line.strip().split()
            x = Decimal(x)
            y = Decimal(y)
            points.append((x, y))

    for x, y in points:
        point = (x, y)

        print(check(square(coord, point), r))


main()
