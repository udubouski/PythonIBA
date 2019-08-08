"""
Задание 1. Определить пользовательский класс в соответствии с вариантом задания (смотри варианты ниже).
определить в классе следующие конструкторы: с параметрами и без параметров
компоненты-функции для просмотра и установки полей данных: setТип(), getТип() (помним про инкапсуляцию проверку корректности задания параметров);
написать демонстрационную программу, в которой создаются и разрушаются объекты (от 3 до 5 шт.) и указатели на объекты пользовательского класса и каждый вызов конструктора сопровождается выдачей соответствующего сообщения.
использовать метод __setattr__()
не забывайте выполнять задание, выделенное курсивом в варианте.

Вариант 1
"Создать класс – Треугольник, заданного тремя точками. Функции-члены изменяют точки, обеспечивают вывод на экран координат, рассчитывают длины сторон и периметр треугольника.
Создать список объектов.
подсчитать количество треугольников разного типа (равносторонний,	равнобедренный,	прямоугольный, произвольный).
определить для каждой группы наибольший и наименьший по периметру объект."
"""
from math import sqrt


class Point:                                                # класс Точка
    __x = 0
    __y = 0

    def __init__(self, x_init, y_init):
        self.__x = x_init
        self.__y = y_init

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


class Triangle:                                             # класс Треугольник
    __count = 0
    __pointA = 0
    __pointB = 0
    __pointC = 0

    def __init__(self, x1, y1, x2, y2, x3, y3):
        Triangle.__count += 1
        print("Конструктор c параметрами " + str(Triangle.__count) + "\n")
        self.__pointA = Point(x1, y1)
        self.__pointB = Point(x2, y2)
        self.__pointC = Point(x3, y3)

    def __del__(self):
        Triangle.__count -= 1
        print("Деструктор " + str(Triangle.__count) + "\n")

    def __str__(self):
        print("A_x:" + str(self.__pointA.getX()))
        print("A_y:" + str(self.__pointA.getY()))
        print("B_x:" + str(self.__pointB.getX()))
        print("B_y:" + str(self.__pointB.getY()))
        print("C_x:" + str(self.__pointA.getX()))
        print("C_y:" + str(self.__pointA.getY()))

    """
        def __init__(self):
            print("Конструктор без параметров\n")
            self.__pointA = Point(0, 0)
            self.__pointB = Point(0, 0)
            self.__pointC = Point(0, 0)
    """

    def set_coordinates(self, x1, y1, x2, y2, x3, y3):
        self.__pointA = Point(x1, y1)
        self.__pointB = Point(x2, y2)
        self.__pointC = Point(x3, y3)

    def get_coordinates(self):
        list_coords = [
            self.__pointA.getX(),
            self.__pointA.getY(),
            self.__pointB.getX(),
            self.__pointB.getY(),
            self.__pointC.getX(),
            self.__pointC.getY()]
        return list_coords

    def distance(self):
        sideAB = sqrt((self.__pointB.getX() - self.__pointA.getX()) ** 2 + (self.__pointB.getY() - self.__pointA.getY()) ** 2)
        sideBC = sqrt((self.__pointC.getX() - self.__pointB.getX()) ** 2 + (self.__pointC.getY() - self.__pointB.getY()) ** 2)
        sideCA = sqrt((self.__pointA.getX() - self.__pointC.getX()) ** 2 + (self.__pointA.getY() - self.__pointC.getY()) ** 2)
        list_sides = [sideAB, sideBC, sideCA]
        return list_sides

    def perimetr(self):
        list_sides = self.distance()
        sum = 0
        for i in list_sides:
            sum += i
        return sum

"""
    def __setattr__(self, key, value):
        if key == 'x1' or key == 'x2' or key == 'x3' or key == 'y1' or key == 'y2' or key == 'y3':
            self.__dict__[key] = value
        else:
            raise AttributeError
"""


tr1 = Triangle(1, 2, 3, 5, 4, 6)
tr2 = Triangle(1, 1, 2, 2, 3, 3)
tr3 = Triangle(1, 10, 20, 2, 3, 30)
tr4 = Triangle(5, 5, 7, 2, 3, 30)
tr5 = Triangle(11, 10, 25, 2, 32, 30)

print("------------------------------\n")
print("Координаты для tr1 : ")
print(str(tr1.get_coordinates()))

tr1.set_coordinates(0, 0, 2, 2, 3 , 3)

print("Координаты для tr1 : ")
print(str(tr1.get_coordinates()))

print("Длина сторон для tr2 :")
print(str(tr2.distance()))

print("Периметр для tr2 : ")
print(str(tr2.perimetr()))

list_trs = [tr1, tr2, tr3, tr4, tr5]

ravnostoronniy = 0
ravnobedrenniy = 0
priamougolniy = 0
proizvolniy = 0

list_perimetr_ravnostoronniy = []
list_perimetr_ravnobedrenniy = []
list_perimetr_priamougolniy = []
list_perimetr_proizvolniy = []

for tr in list_trs:
    if tr.distance()[0] == tr.distance()[1] and tr.distance()[1] == tr.distance()[2] and tr.distance()[2] == tr.distance()[0]:
        ravnostoronniy += 1
        list_perimetr_ravnostoronniy.append(tr.perimetr())
    elif tr.distance()[0] == tr.distance()[1] != tr.distance()[2] or tr.distance()[1] == tr.distance()[2] != tr.distance()[0] or tr.distance()[2] == tr.distance()[0] != tr.distance()[1]:
        ravnobedrenniy += 1
        list_perimetr_ravnobedrenniy.append(tr.perimetr())
    elif tr.distance()[0]**2 == tr.distance()[1]**2 + tr.distance()[2]**2 or tr.distance()[1]**2 == tr.distance()[2]**2 + tr.distance()[0]**2 or tr.distance()[2]**2 == tr.distance()[0]**2 + tr.distance()[1]**2:
        priamougolniy += 1
        list_perimetr_priamougolniy.append(tr.perimetr())
    else:
        proizvolniy += 1
        list_perimetr_proizvolniy.append(tr.perimetr())

print("Равносторонних треугольников = " + str(ravnostoronniy))
if ravnostoronniy !=0:
    print("Наибольший периметр = " + str(max(list_perimetr_ravnostoronniy)))
    print("Наименьший периметр = " + str(min(list_perimetr_ravnostoronniy)))

print("Равнобедренных треугольников = " + str(ravnobedrenniy))
if ravnobedrenniy !=0:
    print("Наибольший периметр = " + str(max(list_perimetr_ravnobedrenniy)))
    print("Наименьший периметр = " + str(min(list_perimetr_ravnobedrenniy)))

print("Прямоугольных треугольников = " + str(priamougolniy))
if priamougolniy !=0:
    print("Наибольший периметр = " + str(max(list_perimetr_priamougolniy)))
    print("Наименьший периметр = " + str(min(list_perimetr_priamougolniy)))

print("Произвольных треугольников = " + str(proizvolniy))
if proizvolniy !=0:
    print("Наибольший периметр = " + str(max(list_perimetr_proizvolniy)))
    print("Наименьший периметр = " + str(min(list_perimetr_proizvolniy)))

print("------------------------------\n")




