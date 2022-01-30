import math

answer = 0

def calculate_snelheid_van_hoogte_zonder_luchtweerstand():
    # Ez = Ek
    # m * g * h = 0.5 * m * v^2
    hoogte = float(input("Wat is de hoogte?: "))
    massa = float(input("Wat is het gewicht in KG?: "))
    gravitatie = float(9.81)

    Zwaartekracht = float(massa * gravitatie * hoogte)
    EzDivide = float(0.5 * massa)
    VKwadraat = float(Zwaartekracht / EzDivide)
    v = math.sqrt(VKwadraat)
    print(vars())

    global answer
    answer = v

    selection_menu()

def calculate_snelheid_van_hoogte_met_lucht_weerstand():
    # Ez = Ek + Q
    # m * g * h = 0.5 * m * v^2 + Fw * h
    hoogte = float(input("Wat is de hoogte in M?: "))
    massa = float(input("Wat is het gewicht in KG?: "))
    weerstandkracht = float(input("Wat is the weerstand in N?:"))
    gravitatie = float(9.81)

    ZwaartekrachtStart = float(massa * gravitatie * hoogte)
    Weerstand = float(weerstandkracht * hoogte)
    EzMin = float(ZwaartekrachtStart - Weerstand)
    EzDivide = float(0.5 * massa)
    VKwadraat = float(EzMin / EzDivide)
    v = math.sqrt(VKwadraat)
    print(vars())

    global answer
    answer = v

    selection_menu()

def calculate_maximale_hoogte_met_kinetische_energy():
    # EzV + Ek = EzN
    # m * g * h + 0.5 * m * v^2 = m * g * h
    # m kan weg worden gestreept
    # g * h + 0.5 * v^2 = g * h
    hoogte = float(input("Wat is de hoogte in M?: "))
    velocity = float(input("Wat is de snelheid?: "))
    gravitatie = float(9.81)

    Ek = float(0.5 * (velocity * velocity))
    EzVoor = float(hoogte * gravitatie)
    Evoor = float(Ek + EzVoor)
    HNa = float(Evoor / gravitatie)
    print(vars())

    global answer
    answer = HNa

    selection_menu()

def selection_menu():
    # Just for choosing the function
    print("\033c")
    print("Please pick one of the following options \n 1. Calculate Snelheid Zonder Weerstand \n 2. Calculate Snelheid met Weerstand \n 3. Calculate Maximale Hoogte \n 4. Exit \n Current Answer: " + str(answer))
    selection = input(" Selection: ")
    if selection == "1":
        print("\033c")
        calculate_snelheid_van_hoogte_zonder_luchtweerstand()
    elif selection == "2":
        print("\033c")
        calculate_snelheid_van_hoogte_met_lucht_weerstand()
    elif selection == "3":
        print("\033c")
        calculate_maximale_hoogte_met_kinetische_energy()
    elif selection == "4":
        exit()

selection_menu()