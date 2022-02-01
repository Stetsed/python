import math
from molmass import Formula

answer = 0

def calculate_moleculaire_massa():
    stoff = input("Welke stof?: ")

    f = Formula(stoff)

    moleculaire_massa = f.mass

    global answer
    answer = (str(moleculaire_massa) + 'g/mol')


