import random

baza = {
    "hrvatska": "zagreb",
    "slovenija": "ljubljana",
    "austrija": "bec"
}

def glavni_grad(drzava, grad):
    return baza[drzava] == grad

def main():
    while True:
        rand = random.randint(0, 2)
        drzava = sorted(baza.keys())[rand]
        grad = raw_input("koji je glavni grad za drzavu %s: " % drzava)
        if glavni_grad(drzava, grad):
            break

    print "bravo odgovor je tocan"

if __name__ == "__main__":
    main()
