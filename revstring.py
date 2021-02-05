word = input("Please enter something for me to magically turn >")

backwards = ""


for index in range(len(word) - 1, -1, -1):
    backwards = backwards + word[index]

print(backwards)
