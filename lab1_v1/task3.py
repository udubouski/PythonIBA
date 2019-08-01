number = input("Input 6-digit number: ")
number = str(number)

sum = 0
for i in range(len(number)):
    sum+=int(number[i])

if sum%7 == 0:
    print("You are lucky")
else:
    print("You are lose")
