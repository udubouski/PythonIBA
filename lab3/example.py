# класс "стол"
class Table:
    # масса стола
    # инкапсулирована - не должна меняться после создания
    __mass = 0

    # конструктор с присвоением заданного значения
    # инкапсулированной массе
    def __init__(self, mass0):
        self.__mass = mass0

    # чтение инкапсулированной массы
    # (записи кроме как в конструкторе не будет)
    def get_mass(self):
        return self.__mass


# класс "обеденный стол"
class DinnerTable(Table):
    # число мест
    __places = 0

    # дополнение родительского конструктора
    # для присвоения значения числу мест
    def __init__(self, mass1):
        Table.__init__(self, mass1)
        self.__places = mass1//5

    # чтение инкапсулированного числа мест
    def get_places(self):
        return self.__places


# класс "грузовик"
class Truck:
    # грузоподъемность
    __maxMass = 0

    def __init__(self, max_mass):
        self.__maxMass = max_mass
        # загруженные в грузовик столы
        # композиция - в классе "грузовик" будет хранится список объектов класса "стол"
        self.__tables = []

    # расчет массы всех погруженных столов
    def __current_mass(self):
        s = 0
        for i in self.__tables:
            s += i.get_mass()
        return s

    # расчет оставшейся доступной массы для погрузки столов
    def reserved_mass(self):
        return self.__maxMass - self.__current_mass()

    # погрузка одного стола в грузовик
    def add_table(self, new_table):
        if new_table.get_mass() <= self.reserved_mass():
            self.__tables.append(new_table)
            print("Стол массой " +
                  str(new_table.get_mass()) +
                  " загружен!")
        else:
            print("Стол массой " +
                  str(new_table.get_mass()) +
                  " не влазит!\nОсталось только " +
                  str(self.reserved_mass()) + " кг!")

    # подсчет числа погруженных столов
    # с заданной массой needle
    # selector - параметр-функция для извлечения из каждого стола его массы
    def count_by_mass(self, needle, selector):
        s = 0
        for i in self.__tables:
            # если не выпендриваться с параметром-функцией -
            # можно написать if i.get_mass() == needle:
            if selector(i) == needle:
                s += 1
        return s

    # выгрузка всех столов
    def remove_tables(self):
        self.__tables.clear()

    # чтение инкапсулированной грузоподъемности
    def get_max_mass(self):
        return self.__maxMass


# вывод слова "столы" в нужном падеже
# в зависимости от числа столов num
def tables_to_string(num):
    # перевод числа столов в строку
    s = str(num)
    # получаем последний символ в строке,
    # именно его нужно проверять для определения падежа
    last_s = s[-1:]
    # 10 столов, 11 столов, 12 столов ... 20 столов
    if 10 <= num <= 20:
        return 'столов'
    # 1 стол, 21 стол
    elif last_s == '1':
        return 'стол'
    # 2 стола, 3 стола, 4 стола, 22 стола, 33 стола, 44 стола
    elif last_s == '2' or last_s == '3' or last_s == '4':
        return 'стола'
    # 5 столов, 9 столов, 55 столов
    else:
        return 'столов'


# ГЛАВНАЯ ПРОГРАММА
# 2 типа столов с разной массой -
# объекты класса "обеденный стол"
table = [
    DinnerTable(11),
    DinnerTable(22)
]
# 2 грузовика - объекты класса "грузовик"
truck = [
    Truck(50),
    Truck(60)
]
# потребность в столах двух видов
need = [
    3,
    3
]
# почти бесконечный цикл - пока не выполним задание - не выйдем
while True:
    # номер выбранного пункта меню
    select = 0
    # подсчет числа загруженных столов по типам
    sums = list([])
    # подсчет числа загруженных столов первого типа, по 11 кг
    sums.append(
        # в первом грузовике
        truck[0].count_by_mass(
            table[0].get_mass(),
            Table.get_mass
        ) +
        # во втором грузовике
        truck[1].count_by_mass(
            table[0].get_mass(),
            Table.get_mass
        )
    )
    # подсчет числа загруженных столов второго типа, по 22 кг
    sums.append(
        # в первом грузовике
        truck[0].count_by_mass(
            table[1].get_mass(),
            Table.get_mass
        ) +
        # во втором грузовике
        truck[1].count_by_mass(
            table[1].get_mass(),
            Table.get_mass
        )
    )
    # проверка, загружео ли нужное кол-во каждого типа столов
    if sums[0] == need[0] and sums[1] == need[1]:
        print("Поздравляю, грузовики укомплектованы, выдвигаемся!")
        break
    # почти бесконечный цикл вывода меню - пока пользователь
    # не выберет один из предлагаемых вариантов
    while True:
        # вывод характеристик грузовиков
        print("Есть 2 грузовика грузоподъемностью " +
              str(truck[0].get_max_mass()) + " кг первый и " +
              str(truck[1].get_max_mass()) + " кг второй.")
        # вывод требуемого количества столов
        print("Нужно завести " + str(need[0]) + " " +
              tables_to_string(need[0]) + " по " +
              str(table[0].get_mass()) + " кг и " +
              str(need[1]) + " "+tables_to_string(need[1])+" по " +
              str(table[1].get_mass()) + " кг.")
        # вывод кол-ва уже погруженных в оба грузовика столов
        print("Уже погружено " + str(sums[0]) + " " +
              tables_to_string(sums[0]) + " по " +
              str(table[0].get_mass()) + " кг и " +
              str(sums[1]) + " " +
              tables_to_string(sums[1]) + " по " +
              str(table[1].get_mass()) + " кг.")
        # вывод меню с возможными действиями пользователей
        print("Что делаем?\n" +
              "1 - грузим стол массой " + str(table[0].get_mass()) +
              " кг в грузовик 1;\n" +
              "2 - грузим стол массой " + str(table[1].get_mass()) +
              " кг в грузовик 1;\n" +
              "3 - грузим стол массой " + str(table[0].get_mass()) +
              " кг в грузовик 2;\n" +
              "4 - грузим стол массой " + str(table[1].get_mass()) +
              " кг в грузовик 2.\n" +
              "5 - что-то не получается, выгружаем все.")
        # ввод действия пользователем
        select = int(input())
        # если выбрано допустимое действие -
        # выход из цикла вывода меню
        if 1 <= select <= 5:
            break
    # действия, одно из которых выбрал пользователь
    if select == 1:
        truck[0].add_table(table[0])
    elif select == 2:
        truck[0].add_table(table[1])
    elif select == 3:
        truck[1].add_table(table[0])
    elif select == 4:
        truck[1].add_table(table[1])
    elif select == 5:
        truck[0].remove_tables()
        truck[1].remove_tables()

input("Нажмите Enter для выхода...")


