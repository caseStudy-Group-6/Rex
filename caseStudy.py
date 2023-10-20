choice = 0 
ordered = 0
barbque = 0
innerChoice = str(1)
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0

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

sizzling = 0
def Sizzling():
    global sizzling
    sizzling =  sizzling + 1
    return sizzling

seafood = 0
def Seafood():
    global seafood
    seafood =  seafood + 1
    return seafood

beverages = 0
def Beverages():
    global beverages
    beverages =  beverages + 1
    return beverages

dessert = 0
def Dessert():
    global dessert
    dessert =  dessert + 1
    return dessert

#result = Barbque(innerChoice)

while choice <= 5:
    print(f"[1] Barbeque")
    print(f"[2] Sizzling Plate ")
    print(f"[3] Seafood ")
    print(f"[4] Beverages ")
    print(f"[5] Dessert ")
    print(f"[6] Checkout ")
    choice = int(input(""))
    if choice == 1:
        while innerChoice != 6:
            result = Barbque(innerChoice)
            print(f"[1] Barbeque = 310 : {b1}")
            print(f"[2] Barbeque Party Trey = 1,565 : {b2}")
            print(f"[3] Pork Barbeque = 60 : {b3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {b4}")
            print(f"[5] Chicken Breast = 85 : {b5}")
            print(f"[6] Return Menu")
            innerChoice = int(input("order: "))
    if choice == 6:
        break
