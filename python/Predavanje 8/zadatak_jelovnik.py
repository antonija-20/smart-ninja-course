while True:
    jelovnik = {}

    while True:
        naziv = raw_input("Naziv jela: ")
        cijena = int(raw_input("Unesi cijenu jela: %s: " % naziv))

        jelovnik[naziv] = cijena
        break

        if raw_input("Jos (da / ne): ") <> da:
            break

dokument = open("jelovnik.txt", "w+")
for naziv in jelovnik:
    dokument.write(naziv + " " + jelovnik[naziv] + "\n")

print jelovnik

dokument.close()