import random
listA = []

n = int(input("Input size of list: "))
for i in range(n):
    elem = random.random()
    listA.append(elem)

print("ListA: ", listA)

x = int(input("Input index of element: "))
listA.pop(x)

print("ListA: ", listA)