import math


def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r (float): Радиус круга.
        
        Возвращает:
            area (float): Площадь круга.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r (float): Радиус круга.

        Возвращает:
            perimeter (float): Периметр круга.
    '''
    return 2 * math.pi * r

