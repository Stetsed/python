import math
from molmass import Formula

answer = 0

def calculate_moleculaire_massa():
    stoff = input("Welke stof?: ")

    f = Formula(stoff)

    moleculaire_massa = f.mass

    global answer
    answer = (str(moleculaire_massa) + 'g/mol')

    return(answer)

def calculate_hoeveelheid_mol():
    stoff = input("Welke Stof?: ")
    gewicht = input("Hoeveel stof in g?: ")

    f = Formula(stoff)
    moleculaire_massa = f.mass

    hoeveelheid_mol = ( float(gewicht) / float(moleculaire_massa) )

    global answer
    answer = (str(hoeveelheid_mol) + ' mol')

    return(answer)

def calculate_hoeveelheid_ml():
    stoff = input("Welke Stof?: ")
    gewicht = input("Hoeveel stof in g?: ")
    concentratie = input("Hoeveel mol/L zijn de oplossingen?: ")

    f = Formula(stoff)
    moleculaire_massa = f.mass

    hoeveelheid_mol = ( float(gewicht) / float(moleculaire_massa) )

    hoeveelheid_ml = ( float(hoeveelheid_mol) / float(concentratie) * 1000)

    global answer
    answer = (str(hoeveelheid_ml) + ' ml')

    return(answer)