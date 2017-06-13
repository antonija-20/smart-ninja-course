# -*- coding: utf-8 -*-

print "Restorant menu"

main_menu = {}

var1 = "da"

while True:
    dan = raw_input("Unesi dan menija: ")
    meni = raw_input("Unesi meni za " + dan)
    cijena = raw_input("unesi cijenu menija: ")
    meni_ok = raw_input("Meni je spreman da / ne: ")

    main_menu[meni] = meni_ok.lower() == var1

    jos = raw_input("Zelite li dodati novi dan da / ne: ")

    if jos.lower() != var1:
        break

restoran_meni = open("restoran.txt", "w+")

print "Jelovnik \n"
restoran_meni.write("Meni za: \n" + dan + "\n" + "Glavno jelo " + meni + "\n" + "Cijena menija: " + cijena + " kn")

for meni in main_menu:
    if main_menu[meni]:
        print str(main_menu) + str(dan)

restoran_meni.close()


