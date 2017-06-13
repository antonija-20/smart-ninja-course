#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():

    pokusaji = 0

    print "Dobrodosli u igru - Pogodi tajni broj"

    number = random.randint(1, 10)
    print "Broj je izmedu 1 i 10"


    while pokusaji < 5:
        secret = raw_input("Unesi broj: ")
        secret = int(secret)

        pokusaji = pokusaji + 1

        if secret < number:
            print "Broj je veci"

        if secret > number:
            print "Broj je manji"

        if secret == number:
            break

    if secret == number:
        pokusaji = str(pokusaji)
        print "Bravo pogodio si broj u " + pokusaji + " pokusaja"

    if secret != number:
        number = str(number)
        print "zao mi je nisi pogodio broj."

if __name__ == "__main__":
    main()



