import math

# Ezv + Ek = Ezn

# Ez = m * g * h
# Ek = 0.5*m*v^2
# m * g * h + 0.5 * m * v^2 = m * g * h

def calculate_snelheid_van_hoogte_zonder_luchtweerstand():
    # Ez = Ek
    # m * g * h = 0.5 * m * v^2
    h = float(input("Wat is de hoogte?: "))
    m = float(input("Wat is het gewicht in KG?: "))
    g = float(9.81)

    Ez = float(m * g * h)
    EzDivide = float(0.5 * m)
    EkWortel = float(Ez / EzDivide)
    v = math.sqrt(EkWortel)
    print(vars())

def calculate_snelheid_van_hoogte_met_lucht_weerstand():
    # Ez = Ek + Q
    # m * g * h = 0.5 * m * v^2 + Fw * h
    h = float(input("Wat is de hoogte?: "))
    m = float(input("Wat is het gewicht in KG?: "))
    w = float(input("Wat is the weerstand?:"))
    g = float(9.81)

    EzS = float(m * g * h)
    Q = float(w * h)
    EzM = float(EzS - Q)
    EzDivide = float(0.5 * m)
    EkWortel = float(EzM / EzDivide)
    v = math.sqrt(EkWortel)
    print(vars())

calculate_snelheid_van_hoogte_met_lucht_weerstand()