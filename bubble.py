

numbers = [2000, 88, 2, 45, 105, 67, 89, 4, 5, 7, 9, 1]
i = 0
fact = len(numbers) * len(numbers)

while i < fact:
    for index in range(0, len(numbers) -1):
        if numbers[index] > numbers[index + 1]:
            first = numbers[index]
            second = numbers[index + 1]
            numbers[index] = second
            numbers[index + 1] = first
        i = i + 1
    
    print(numbers)
print(numbers[::-1])

