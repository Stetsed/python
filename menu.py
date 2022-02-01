import Scheikunde
import Natuurkunde

answer = 0

def main_selection_menu():
    # For choosing the section
    print("\033c")
    print("Please pick one of the following options \n 1. Scheikunde \n 2. Natuurkunde \n 3. Exit \n Current Answer: " + str(answer))
    selection = input(" Selection: ")
    if selection == "1":
        print("\033c")
        Scheikunde.selection_menu()
    elif selection == "2":
        print("\033c")
        Natuurkunde.selection_menu()
    elif selection == "3":
        exit()

main_selection_menu()