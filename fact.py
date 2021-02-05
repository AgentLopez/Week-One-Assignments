# gold = int(input("I NEED A Number, like now > "))

# total = 1
# i = 0

def factorial(gold):
    total = 1
    i=0
    while i < gold:
        i = i + 1
        total = total * i
    return total

#print(f"The Factorial of {gold} is {total}!")