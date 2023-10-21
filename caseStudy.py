choice = 0 
innerChoice = 0
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
sf1 = 0
sf2 = 0
sf3 = 0
sf4 = 0
sf5 = 0
br1 = 0
br2 = 0
br3 = 0
br4 = 0
br5 = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0

def Barbque(innerChoice):
    match innerChoice:
        case 1:
            global b1
            b1 = b1 + 1 
            return b1
        case 2:
            global b2
            b2 = b2 + 1 
            return b2
        case 3:
            global b3 
            b3 = b3 + 1 
            return b3
        case 4:
            global b4 
            b4 = b4 + 1 
            return b4
        case 5:
            global b5
            b5 = b5 + 1 
            return b5
        case -1:
            b1 = b1 - 1 
            return b1
        case -2:
            b2 = b2 - 1 
            return b2
        case -3: 
            b3 = b3 - 1 
            return b3
        case -4:
            b4 = b4 - 1 
            return b4
        case -5:
            b5 = b5 - 1 
            return b5

def Sizzling(innerChoice):
    match innerChoice:
        case 1:
            global s1
            s1 = s1 + 1 
            return s1
        case 2:
            global s2
            s2 = s2 + 1 
            return s2
        case 3:
            global s3 
            s3 = s3 + 1 
            return s3
        case 4:
            global s4 
            s4 = s4 + 1 
            return s4
        case 5:
            global s5
            s5 = s5 + 1 
            return s5
        case -1:
            s1 = s1 - 1 
            return s1
        case -2:
            s2 = s2 - 1 
            return s2
        case -3: 
            s2 = s3 - 1 
            return s3
        case -4:
            s4 = s4 - 1 
            return s4
        case -5:
            s5 = s5 - 1 
            return s5

def Seafood(innerChoice):
    match innerChoice:
        case 1:
            global sf1
            sf1 = sf1 + 1 
            return sf1
        case 2:
            global sf2
            sf2 = sf2 + 1 
            return sf2
        case 3:
            global sf3 
            sf3 = sf3 + 1 
            return sf3
        case 4:
            global sf4 
            sf4 = sf4 + 1 
            return sf4
        case 5:
            global sf5
            sf5 = sf5 + 1 
            return sf5
        case -1:
            sf1 = sf1 - 1 
            return sf1
        case -2:
            sf2 = sf2 - 1 
            return sf2
        case -3: 
            sf2 = sf3 - 1 
            return sf3
        case -4:
            sf4 = sf4 - 1 
            return sf4
        case -5:
            sf5 = sf5 - 1 
            return sf5

def Beverages(innerChoice):
    match innerChoice:
        case 1:
            global br1
            br1 = br1 + 1 
            return br1
        case 2:
            global br2
            br2 = br2 + 1 
            return br2
        case 3:
            global br3 
            br3 = br3 + 1 
            return br3
        case 4:
            global br4 
            br4 = br4 + 1 
            return br4
        case 5:
            global br5
            br5 = br5 + 1 
            return br5
        case -1:
            br1 = br1 - 1 
            return br1
        case -2:
            br2 = br2 - 1 
            return br2
        case -3: 
            br2 = br3 - 1 
            return br3
        case -4:
            br4 = br4 - 1 
            return br4
        case -5:
            br5 = br5 - 1 
            return br5

def Dessert(innerChoice):
    match innerChoice:
        case 1:
            global d1
            d1 = d1 + 1 
            return d1
        case 2:
            global d2
            d2 = d2 + 1 
            return d2
        case 3:
            global d3 
            d3 = d3 + 1 
            return d3
        case 4:
            global d4 
            d4 = d4 + 1 
            return d4
        case 5:
            global d5
            d5 = d5 + 1 
            return d5
        case -1:
            d1 = d1 - 1 
            return d1
        case -2:
            d2 = d2 - 1 
            return d2
        case -3: 
            d2 = d3 - 1 
            return d3
        case -4:
            d4 = d4 - 1 
            return d4
        case -5:
            d5 = d5 - 1 
            return d5

while choice <= 5:
    print(f"[1] Barbeque ")
    print(f"[2] Sizzling Plate ")
    print(f"[3] Seafood ")
    print(f"[4] Beverages ")
    print(f"[5] Dessert ")
    print(f"[6] Checkout ")
    choice = int(input(""))
    innerChoice = 0
    if choice == 1:
        while innerChoice != 6:
            result = Barbque(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Barbeque = 310 : {b1}")
            print(f"[2] Barbeque Party Trey = 1,565 : {b2}")
            print(f"[3] Pork Barbeque = 60 : {b3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {b4}")
            print(f"[5] Chicken Breast = 85 : {b5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 2:
        while innerChoice != 6:
            result = Sizzling(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Pork Sisig = 310 : {s1}")
            print(f"[2] Crispy Pata = 1,565 : {s2}")
            print(f"[3] Special sizzling chicken with gravy = 250  : {s3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {s4}")
            print(f"[5] Chicken Breast = 85 : {s5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 3:
        while innerChoice != 6:
            result = Seafood(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Barbeque = 310 : {sf1}")
            print(f"[2] Barbeque Party Trey = 1,565 : {sf2}")
            print(f"[3] Pork Barbeque = 60 : {sf3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {sf4}")
            print(f"[5] Chicken Breast = 85 : {sf5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 4:
        while innerChoice != 6:
            result = Beverages(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Barbeque = 310 : {br1}")
            print(f"[2] Barbeque Party Trey = 1,565 : {br2}")
            print(f"[3] Pork Barbeque = 60 : {br3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {br4}")
            print(f"[5] Chicken Breast = 85 : {br5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    if choice == 5:
        while innerChoice != 6:
            result = Dessert(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] mark = 310 : {d1}")
            print(f"[2] Barbeque Party Trey = 1,565 : {d2}")
            print(f"[3] Pork Barbeque = 60 : {d3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {d4}")
            print(f"[5] Chicken Breast = 85 : {d5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    if choice == 6:
        break
