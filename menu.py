import Scheikunde
import Natuurkunde

answer = 0

def main_selection_menu():
    # For choosing the section
    global answer

    print("\033c")
    print("Please pick one of the following options \n 1. Scheikunde \n 2. Natuurkunde \n 3. Exit \n Current Answer: " + str(answer))
    selection = input(" Selection: ")
    if selection == "1":
        print("\033c")
        Scheikunde.selection_menu()
        main_selection_menu()
    elif selection == "2":
        print("\033c")
        Natuurkunde_selection_menu()
        main_selection_menu()
    elif selection == "3":
        exit()

def Natuurkunde_selection_menu():
    # Just for choosing the function
    global answer

    print("\033c")
    print("Please pick one of the following options \n 1. Calculate Snelheid Zonder Weerstand \n 2. Calculate Snelheid met Weerstand \n 3. Calculate Maximale Hoogte \n 4. Exit \n Current Answer: " + str(answer))
    selection = input(" Selection: ")
    if selection == "1":
        print("\033c")
        answer = Natuurkunde.calculate_snelheid_van_hoogte_zonder_luchtweerstand()
        Natuurkunde_selection_menu()
    elif selection == "2":
        print("\033c")
        answer = Natuurkunde.calculate_snelheid_van_hoogte_met_lucht_weerstand()
        Natuurkunde_selection_menu()
    elif selection == "3":
        print("\033c")
        answer = Natuurkunde.calculate_maximale_hoogte_met_kinetische_energy()
        Natuurkunde_selection_menu()
    elif selection == "4":
        return(answer)

main_selection_menu()