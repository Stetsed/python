import math
from molmass import Formula

answer = 0

def calculate_moleculaire_massa():
    stoff = input("Welke stof?: ")

    f = Formula(stoff)

    moleculaire_massa = f.mass

    global answer
    answer = (str(moleculaire_massa) + 'g/mol')

def calculate_hoeveelheid_mol():
    stoff = input("Welke Stof?: ")
    gewicht = input("Hoeveel stof in g?: ")

    f = Formula(stoff)
    moleculaire_massa = f.mass

    hoeveelheid_mol = ( float(gewicht) / float(moleculaire_massa) )

    print (hoeveelheid_mol)

    global answer
    answer = (str(hoeveelheid_mol) + 'mol')




