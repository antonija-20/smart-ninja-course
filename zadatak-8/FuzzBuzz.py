
while True:

    unos_broja = int(raw_input("Unesite broj izmedu 1 i 100"))
    if unos_broja > 0 and unos_broja < 100:
        break
    else:
        print("Unseseni broj nije izmedu 1 i 100")

print unos_broja

for broj in range(1, (unos_broja + 1)):
    if broj % 3 == 0 and broj % 5 == 0:
        print "fizzbuzz"
    if broj % 3 == 0:
        print "fizz"
    elif broj % 5 == 0:
        print "buzz"
    else:
        print broj
