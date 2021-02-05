total = input("What is the total bill amount?")
tipper = input("What percentage would you like to tip?")
tiptoper = int(tipper) * .01
tipamount = float(total) * tiptoper
tipamountdone = round(tipamount, 2)
tipamountdone = str(tipamountdone)

print(f"Your tip amount is {tipamountdone}")