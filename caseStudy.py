choice = 0 
innerChoice = 0
over1, over2, over3, over4, over5 = [0] * 5
b1, b2, b3, b4, b5, pb1, pb2, pb3, pb4, pb5 = [0] * 10
s1, s2, s3, s4, s5, ps1, ps2, ps3, ps4, ps5 = [0] * 10
sf1, sf2, sf3, sf4, s5, psf1, psf2, psf3, psf4, psf5 = [0] * 10
br1, br2, br3, br4, br5, pbr1, pbr2, pbr3, pbr4, pbr5 = [0] * 10
d1, d2, d3, d4, d5, pd1, pd2, pd3, pd4, pd5 = [0] * 10
total = 0

def Barbque(innerChoice):
    global b1, b2, b3, b4, b5
    match innerChoice:
        case 1:
            b1 = b1 + 1 
        case 2:
            b2 = b2 + 1 
        case 3: 
            b3 = b3 + 1 
        case 4:
            b4 = b4 + 1 
        case 5:
            b5 = b5 + 1 
        case -1:
            b1 = b1 - 1 
        case -2:
            b2 = b2 - 1     
        case -3: 
            b3 = b3 - 1 
        case -4:
            b4 = b4 - 1 
        case -5:
            b5 = b5 - 1 
    return b1, b2, b3, b4, b5

def Sizzling(innerChoice):
    global s1, s2, s3, s4, s5
    match innerChoice:
        case 1:
            s1 = s1 + 1 
        case 2:
            s2 = s2 + 1 
        case 3:
            s3 = s3 + 1 
        case 4:
            s4 = s4 + 1 
        case 5:
            s5 = s5 + 1 
        case -1:
            s1 = s1 - 1 
        case -2:
            s2 = s2 - 1 
        case -3: 
            s2 = s3 - 1 
        case -4:
            s4 = s4 - 1 
        case -5:
            s5 = s5 - 1 
    return s1, s2, s3, s4, s5

def Seafood(innerChoice):
    global sf1, sf2, sf3, sf4, sf5
    match innerChoice:
        case 1:
            sf1 = sf1 + 1 
        case 2:
            sf2 = sf2 + 1 
        case 3:
            sf3 = sf3 + 1 
        case 4:
            sf4 = sf4 + 1 
        case 5:
            sf5 = sf5 + 1 
        case -1:
            sf1 = sf1 - 1 
        case -2:
            sf2 = sf2 - 1 
        case -3: 
            sf2 = sf3 - 1 
        case -4:
            sf4 = sf4 - 1 
        case -5:
            sf5 = sf5 - 1 
    return sf1, sf2, sf3, sf4, sf5

def Beverages(innerChoice):
    global br1, br2, br3, br4, br5
    match innerChoice:
        case 1:
            br1 = br1 + 1 
        case 2:
            br2 = br2 + 1 
        case 3:
            br3 = br3 + 1 
        case 4:
            br4 = br4 + 1 
        case 5:
            br5 = br5 + 1 
        case -1:
            br1 = br1 - 1 
        case -2:
            br2 = br2 - 1 
        case -3: 
            br2 = br3 - 1 
        case -4:
            br4 = br4 - 1 
        case -5:
            br5 = br5 - 1 
    return br1, br2, br3, br4, br5

def Dessert(innerChoice):
    global d1, d2, d3, d4, d5
    match innerChoice:
        case 1:
            d1 = d1 + 1 
        case 2:
            d2 = d2 + 1 
        case 3:
            d3 = d3 + 1 
        case 4:
            d4 = d4 + 1 
        case 5:
            d5 = d5 + 1 
        case -1:
            d1 = d1 - 1 
        case -2:
            d2 = d2 - 1 
        case -3: 
            d2 = d3 - 1 
        case -4:
            d4 = d4 - 1 
        case -5:
            d5 = d5 - 1 
    return d1, d2, d3, d4, d5

def Overalls(innerChoice):
    innerChoice = innerChoice
    global over1, over2, over3, over4, over5
    match innerChoice:
        case 1:
            over1 = over1 + b1 + b2 + b3 + b4 + b5
        case 2:
            over2 = over2 + s1 + s2 + s3 + s4 +s5
        case 3: 
            over3 = over3 + sf1 + sf2 + sf3 + sf4 + sf5 
        case 4:
            over4 = over4 + br1 + br2 + br3 + br4 + br5
        case 5:
            over5 = over5 + d1 + d2 + d3 + d4 + d5
    return over1, over2, over3, over4, over5

def checkout(payment):
    global pb1, pb2, pb3, pb4, pb5, total, ps1, ps2, ps3, ps4, ps5, psf1, psf2, psf3, psf4, psf5, pbr1, pbr2, pbr3, pbr4, pbr5, pd1, pd2, pd3, pd4, pd5
    pb1 = 310 * b1
    pb2 = 1,565 * b2
    pb3 = 60 * b3
    pb4 = 70 * b4
    pb5 = 85 * b5
    ps1 = 
    ps2 = 
    ps3 = 
    ps4 = 
    ps5 = 
    psf1 = 
    psf2 = 
    psf3 = 
    psf4 = 
    psf5 = 
    pbr1 = 
    pbr2 = 
    pbr3 = 
    pbr4 = 
    pbr5 = 
    pd1 = 
    pd2 = 
    pd3 = 
    pd4 = 
    pd5 = 
    total = payment - pb1 - pb2 - pb3 - pb4 - pb5 - ps1 - ps2 - ps3 - ps4 - ps5 - psf1 - psf2 - psf3 - psf4 - psf5 - pbr1 - pbr2 - pbr3 - pbr4 - pbr5 - pd1 - pd2 - pd3 - pd4 - pd5
    return total, pb1, pb2, pb3, pb4, pb5, total, ps1, ps2, ps3, ps4, ps5, psf1, psf2, psf3, psf4, psf5, pbr1, pbr2, pbr3, pbr4, pbr5, pd1, pd2, pd3, pd4, pd5

while choice <= 5:
    result = Overalls(choice)
    print(f"[1] Barbeque = Ordered: {over1}")
    print(f"[2] Sizzling Plate = Ordered: {over2}")
    print(f"[3] Seafood = Ordered: {over3}")
    print(f"[4] Beverages = Ordered: {over4}")
    print(f"[5] Dessert = Ordered: {over5}")
    print(f"[6] Checkout = ")
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
    elif choice == 5:
        while innerChoice != 6:
            result = Dessert(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Barbeque = 310 : {d1}")
            print(f"[2] Barbeque Party Trey = 1,565 : {d2}")
            print(f"[3] Pork Barbeque = 60 : {d3}")
            print(f"[4] Chicken Barbeque Stick = 70 : {d4}")
            print(f"[5] Chicken Breast = 85 : {d5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 6:
        payment = int(input(""))
        result = checkout(payment)
        print(f"CHECK OUT")
        print(f"\nBarbeque:")
        print(f"\tBarbeque = {pb1}")
        print(f"\tBarbeque Party Trey = {pb2}")
        print(f"\tPork Barbeque = {pb3}")
        print(f"\tChicken Barbeque Stick = {pb4}")
        print(f"\tChicken Breast = {pb5}")
        print(f"Change: {total}")
        break
