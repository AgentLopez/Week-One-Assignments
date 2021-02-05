prime = int(input("Let's Check a number to see if it's prime >"))

primeswitch = True

for i in range(2, prime - 1):
    if (prime % i == 0):
        primeswitch = False
        

if primeswitch == True:
    print(f"Congradulations, {prime} is a prime number!")

else:
    print(f"Sorry, {prime} is not a prime number.")