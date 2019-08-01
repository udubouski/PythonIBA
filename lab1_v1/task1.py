m = int(input("Input number m: "))
n = int(input("Input number n: "))
p = int(input("Input number p: "))
i = 0

if m<0:
    i+=1
if n<0:
    i+=1
if p<0:
    i+=1

print("Count of negative numbers: ", i)
