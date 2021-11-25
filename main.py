# The Simp Game

# Buildings
# ---------------------- #
# Beach (BCH) , Factory (FAC) , House (HSE) , Shop (SHP) , Highway (HWY)

# Board
# ---------------------- #
# [['A1','B1','C1','D1'],
#  ['A2','B2','C2','D2'],
#  ['A3','B3','C3','D3'],
#  ['A4','B4','C4','D4']]

# Game Options
# -----------------------#
# 6 Options
# 1. Place Random Building
# 2. Place Random Building
# 3. See remaining buildings
# 4. See current score

# 5. Save game
# 0. Exit to main menu

# Imports

# for mapping locations to buildings
plots = {"A1": "\t", "A2": "\t", "A3": "\t", "A4": "\t", "B1": "\t",
         "B2": "\t", "B3": "\t", "B4": "\t", "C1": "\t", "C2": "\t",
         "C3": "\t", "C4": "\t", "D1": "\t", "D2": "\t", "D3": "\t",
         "D4": "\t", "Turn": "0", "lastPlace": ""}
buildings = {0: "BCH", 1: "FAC", 2: "HSE", 3: "SHP", 4: "HWY"}

bchCount = 8
facCount = 8
hseCount = 8
shpCount = 8
hwyCount = 8
lastPlace = ""  # stores last plot built upon


# module displays game/city grid
def CityMapFunc():
    print("\t     A \t     B \t     C \t     D")
    for i in range(4):
        print("\t   --------------------------------")
        if i == 0:
            print("\t", i + 1, "| ", plots["A1"], " | ", plots["B1"],
                  " | ", plots["C1"], " |", plots["D1"], "  | ")
        if i == 1:
            print("\t", i + 1, "| ", plots["A2"], " | ", plots["B2"],
                  " | ", plots["C2"], " |", plots["D2"], "  | ")
        if i == 2:
            print("\t", i + 1, "| ", plots["A3"], " | ", plots["B3"],
                  " | ", plots["C3"], " |", plots["D3"], "  | ")
        if i == 3:
            print("\t", i + 1, "| ", plots["A4"], " | ", plots["B4"],
                  " | ", plots["C4"], " |", plots["D4"], "  | ")

    print("\t   --------------------------------")


# function for main menu
def MenuSelection(option):
    if option == 1:
        StartGameFunc()
    elif option == 2:
        LoadGameFunc()
    elif option == 0:
        exit(0)
    else:
        print("invalid option, try again")
        FirstMenu()


# module returns a list of adjacent locations to the function parameter 
def CheckAdjacency(loc):
    A1 = ["A2", "B1"]
    A2 = ["A1", "A3", "B2"]
    A3 = ["A2", "A4", "B3"]
    A4 = ["A3", "B4"]
    B1 = ["A1", "B2", "C1"]
    B2 = ["A2", "B1", "B3", "C2"]
    B3 = ["A3", "B2", "B4", "C3"]
    B4 = ["A4", "B3", "C4"]
    C1 = ["B1", "C2", "D1"]
    C2 = ["B2", "C1", "C3", "D2"]
    C3 = ["B3", "C2", "C4", "D3"]
    C4 = ["B4", "C3", "D4"]
    D1 = ["C1", "D2"]
    D2 = ["C2", "D1", "D3"]
    D3 = ["D2", "D4", "C3"]
    D4 = ["D3", "C4"]
    if loc == "A1":
        return A1
    if loc == "A2":
        return A2
    if loc == "A3":
        return A3
    if loc == "A4":
        return A4
    if loc == "B1":
        return B1
    if loc == "B2":
        return B2
    if loc == "B3":
        return B3
    if loc == "B4":
        return B4
    if loc == "C1":
        return C1
    if loc == "C2":
        return C2
    if loc == "C3":
        return C3
    if loc == "C4":
        return C4
    if loc == "D1":
        return D1
    if loc == "D2":
        return D2
    if loc == "D3":
        return D3
    if loc == "D4":
        return D4


def FirstMenu():
    print("Welcome, mayor of Simp City!")
    print("------------------------------")
    print("1- Start new game")
    print("2- Load saved game")
    print("0- Exit")
    option = (int)(input("Your choice? "))
    MenuSelection(option)


def StartGameFunc():
    print("start")


def LoadGameFunc():
    print("load")
