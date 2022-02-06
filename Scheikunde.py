import math
from molmass import Formula

answer = 0

def calculate_moleculaire_massa():
    stoff = input("Welke stof?: ")

    f = Formula(stoff)

    moleculaire_massa = f.mass

    global answer
    answer = (str(moleculaire_massa) + 'g/mol')

    selection_menu()

def calculate_hoeveelheid_mol():
    stoff = input("Welke Stof?: ")
    gewicht = input("Hoeveel stof in g?: ")

    f = Formula(stoff)
    moleculaire_massa = f.mass

    hoeveelheid_mol = ( float(gewicht) / float(moleculaire_massa) )

    global answer
    answer = (str(hoeveelheid_mol) + ' mol')

    selection_menu()

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

    selection_menu()

def selection_menu():
    # Just for choosing the function
    print("\033c")
    print("Please pick one of the following options \n 1. Calculate Moleculaire Massa. \n 2. Calculate hoeveelheid mol.\n 3. Calculate hoeveelheid ml \n 4. Exit \n Current Answer: " + str(answer))
    selection = input(" Selection: ")
    if selection == "1":
        print("\033c")
        calculate_moleculaire_massa()
    elif selection == "2":
        print("\033c")
        calculate_hoeveelheid_mol()
    elif selection == "3":
        print("\033c")
        calculate_hoeveelheid_ml()
    elif selection == "4":
        exit()