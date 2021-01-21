import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You drop ", die1, "and ", die2, "and you've got total", total)

input("Press enter")