import math


def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r (int|float): Радиус круга.
        
        Возвращает:
            area (int|float): Площадь круга.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (int|float): Радиус круга.

        Возвращает:
            perimeter (int|float): Периметр круга.
    '''
    return 2 * math.pi * r

