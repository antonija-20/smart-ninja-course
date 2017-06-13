def lottery():
    import random
    brojevi = []
    for number in range(0 , 6):
        brojevi.append(random.randint(0, 60))
    return brojevi


print "Brojevi su " + format(lottery())