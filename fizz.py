num = int(input("Number Time >"))

if ((num % 5 == 0) & (num % 3 == 0)):
    print("Fizz Buzz")

elif (num % 5 == 0):
    print("Buzz")

elif (num % 3 == 0):
    print("Fizz")

else:
    print(num)