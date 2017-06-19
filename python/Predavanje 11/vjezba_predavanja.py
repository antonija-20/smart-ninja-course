class user(object):
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    def puno_ime(self):
        return self.ime + " " + self.prezime

class nas_korisnik(user):
    def __init__(self, ime, prezime, broj_telefona):
        user.__init__(self, ime, prezime)
        self.broj_telefona = broj_telefona
    def telefon(self):
        return "Broje telefona je: " + self.broj_telefona()

novi_korisnik = nas_korisnik("Marin", "Drzic", "099 555 444")
print novi_korisnik.puno_ime()
print novi_korisnik.telefon()

korisnik = user("Ivan", "Gundulic")
marko = user("Marko", "Marulic")
petar = user("Petar", "Zoranic")

korisnici = {
    korisnik,
    marko,
    petar
}

for user in korisnici:
    print "nas korisnik se zove: " + user.puno_ime()