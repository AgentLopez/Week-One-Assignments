print("Let's Check to see if your word is a palindrome\n")
word = input("What is the word I'm checking? > ")

wordsplit = list(word)
wordbackwards = ""
currentletter = []

i=0

while i < len(word):
    i = i + 1
    currentletter = wordsplit.pop()
    wordbackwards = wordbackwards + currentletter
    
if (word == wordbackwards):
    print("Congradulations, You've got a Palindrome!\n\tDon't Drop It!!")
else:
    print("Sorry, it's not a palindrome, try again!")