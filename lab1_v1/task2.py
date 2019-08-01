import math
import numpy

c = 2.1
r = 4 * (10 ** (-4))
m = 7
j = [4.2, 0.3, 1.7]

print("Cycle For")
for i in range(len(j)):
    h = (10 * r - j[i])/(c**2 + math.exp(-m))
    y = (h * m - j[i]**2) + (0.1 * c)**2
    print("Value h = ", h, "for j = ", j[i])
    print("Value y = ", y, "for j = ", j[i])

print("Cycle While")
j = []
for i in numpy.arange(0.0, 1.7, 0.1):
    j.append(i)

x = 0
while x < len(j):
    h = (10 * r - j[x]) / (c ** 2 + math.exp(-m))
    y = (h * m - j[x] ** 2) + (0.1 * c) ** 2
    print("Value h = ", h, "for j = ", j[x])
    print("Value y = ", y, "for j = ", j[x])
    x+=1

print("Double Cycle")
j = [9, 1.8, 15, -3]
f = []
for t in numpy.arange(1.0, 2, 0.5):
    f.append(t)

for i in range(len(f)):
    for p in range(len(j)):
        h = (10 * r - j[p]) / (c ** 2 + math.exp(-f[i]))
        y = (h * f[i] - j[p] ** 2) + (0.1 * c) ** 2
        print("Value h = ", h, "for j = ", j[p], "and f = ", f[i])
        print("Value y = ", y, "for j = ", j[p], "and f = ", f[i])

