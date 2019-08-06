import random
import datetime
import prettytable                                  # пакет для таблицы
import matplotlib.pyplot as plt                     # библиотека для графика


def ShakerSort(A):                                  # шейкерная сортировка
    for i in range(len(A) // 2):
        for j in range(i, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
        for j in range(len(A) - 2 - i, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


def InsertSort(A):                                  # сортировка вставками
    for i in range(1, len(A)):
        t = A[i]
        j = i - 1
        while j >= 0:
            if A[j] > t:
                A[j + 1] = A[j]
            else:
                break
            j -= 1
        A[j + 1] = t


def SelectSort(A):                                  # сортировка выбором
    for i in range(len(A)):
        m = i
        for j in range(i + 1, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]

table = prettytable.PrettyTable(["Размер списка", "Время шейкерной", "Время вставками", "Время выбором"])
x=[]
y1=[]
y2=[]
y3=[]

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    t1 = datetime.datetime.now()
    ShakerSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    # print("Шейкерная сортировка " + str(N) + " заняла " + str((t2-t1).total_seconds()) + " cек ")

    t3 = datetime.datetime.now()
    InsertSort(A)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    # print("Сортировка вставками " + str(N) + " заняла " + str((t4 - t3).total_seconds()) + " cек ")

    t5 = datetime.datetime.now()
    SelectSort(A)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    # print("Сортировка выбором " + str(N) + " заняла " + str((t6 - t5).total_seconds()) + " cек ")

    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y2, "C2")
plt.show()
