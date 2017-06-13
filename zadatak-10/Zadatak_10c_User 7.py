import random

brojevi = set()

max = 10
min = 0

while min < max:
    r = random.randint(0,100)
    if r not in brojevi:
        min += 1
        brojevi.add(r)

print brojevi