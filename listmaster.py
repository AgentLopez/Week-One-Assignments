numbers = [5, 2, 3, 4, 5, 99, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# highest = numbers[0]
# lowest = numbers[0]

def highest_num():
    highest = numbers[0]
    for index in range(1, len(numbers)):
        if (numbers[index] > highest):
            highest = numbers[index]
    print(highest)

# highest = numbers[0]

# for index in range(1, len(numbers)):
#     if numbers[index] > highest:
#         highest = numbers[index]
# print(highest)



def lowest_num():   
    lowest = numbers[0]
    for index in range(1, len(numbers)):
        if (numbers[index] < lowest):
            lowest = numbers[index]
    print(lowest)

def even_nums():
    even_digits = []
    for index in range(0, len(numbers)):
        if (numbers[index] % 2 == 0):
            even_digits.append(numbers[index])
    print(even_digits)


print("Lowest Number:")
lowest_num()
print("Highest Number:")
highest_num()
print("Even Digits:")
even_nums()