#definirati broj koji treba pogoditi

broj_pokusaja = 5
secret = 75
guess = 0
i = 0

while i < broj_pokusaja:
    i = i + 1
    guess = input("Unesi tajni broj: ")

    if guess == secret:
        print "Bravo, pogodio si broj!"
        break
    elif guess > secret:
        print "Krivi odgovor vas unos je veci od tajnog broja"
    elif guess < secret:
        print "Krivi odgovor vas unos je manji od tajnog broja"

    print "Imate jos " + str(broj_pokusaja - i) + " pokusaja"

print "Kraj"


