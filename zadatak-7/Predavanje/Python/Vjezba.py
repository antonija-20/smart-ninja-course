#pretvaranje kilometara u milje
#milja je 0.621371 kilometara

#pozdravna poruka
    #korisnik unosi broj kilometara
    #ispituje koliko je to milja
    #pita korisnika zeli li jos
    #akoda ponovi postupak
    #ako bilo koji drugiunos prekini i zavrsi
#obavjestava korisnika da je program zavrsio


milja = 0.621371

print "Bok"

while True:
    kilometri = input("Unesite kilometre koje zelite preracunati u milje: ")
    print ("ovo je " + str(milja * kilometri) + " kilometri")
    jos = raw_input("Zelis jos? ")
    if jos != 'da':
        break

print "Kraj"



