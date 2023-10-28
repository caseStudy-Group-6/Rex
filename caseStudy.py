choice = 0
innerChoice = 0
over1, over2, over3, over4, over5 = [0] * 5
b1, b2, b3, b4, b5, pb1, pb2, pb3, pb4, pb5 = [0] * 10
s1, s2, s3, s4, s5, ps1, ps2, ps3, ps4, ps5 = [0] * 10
sf1, sf2, sf3, sf4, s5, psf1, psf2, psf3, psf4, psf5 = [0] * 10
br1, br2, br3, br4, br5, pbr1, pbr2, pbr3, pbr4, pbr5 = [0] * 10
bd1, bd2, bd3, bd4, bd5, pbd1, pbd2, pbd3, pbd4, pbd5 = [0] * 10
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
    global bd1, bd2, bd3, bd4, bd5
    match innerChoice:
        case 1:
            bd1 = bd1 + 1
        case 2:
            bd2 = bd2 + 1
        case 3:
            bd3 = bd3 + 1
        case 4:
            bd4 = bd4 + 1
        case 5:
            bd5 = bd5 + 1
        case -1:
            bd1 = bd1 - 1
        case -2:
            bd2 = bd2 - 1
        case -3:
            bd3 = bd3 - 1
        case -4:
            bd4 = bd4 - 1
        case -5:
            bd5 = bd5 - 1
    return bd1, bd2, bd3, bd4, bd5

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
            over5 = over5 + bd1 + bd2 + bd3 + bd4 + bd5
    return over1, over2, over3, over4, over5

def checkout(payment):
    global pb1, pb2, pb3, pb4, pb5, total, ps1, ps2, ps3, ps4, ps5, psf1, psf2, psf3, psf4, psf5, pbr1, pbr2, pbr3, pbr4, pbr5, pbd1, pbd2, pbd3, pbd4, pbd5
    pb1 = 310 * b1
    pb2 = 25 * b2
    pb3 = 180 * b3
    pb4 = 180 * b4
    pb5 = 165 * b5
    ps1 = 200 * s1
    ps2 = 636 * s2
    ps3 = 250 * s3
    ps4 = 196 * s4
    ps5 = 200 * s5
    psf1 = 249 * sf1
    psf2 = 389 * sf2
    psf3 = 349 * sf3
    psf4 = 480 * sf4
    psf5 = 320 * sf5
    pbr1 = 40 * br1
    pbr2 = 40 * br2
    pbr3 = 60 * br3
    pbr4 = 50 * br4
    pbr5 = 40 * br5
    pbd1 = 200 * bd1
    pbd2 = 250 * bd2
    pbd3 = 150 * bd3
    pbd4 = 150 * bd4
    pbd5 = 990 * bd5
    total = payment - pb1 - pb2 - pb3 - pb4 - pb5 - ps1 - ps2 - ps3 - ps4 - ps5 - psf1 - psf2 - psf3 - psf4 - psf5 - pbr1 - pbr2 - pbr3 - pbr4 - pbr5 - pbd1 - pbd2 - pbd3 - pbd4 - pbd5
    return total, pb1, pb2, pb3, pb4, pb5, total, ps1, ps2, ps3, ps4, ps5, psf1, psf2, psf3, psf4, psf5, pbr1, pbr2, pbr3, pbr4, pbr5, pbd1, pbd2, pbd3, pbd4, pbd5

while choice <= 5:
    result = Overalls(choice)
    print(f"[1] Barbeque = Ordered: {over1}")
    print(f"[2] Sizzling Plate = Ordered: {over2}")
    print(f"[3] Seafood = Ordered: {over3}")
    print(f"[4] Beverages = Ordered: {over4}")
    print(f"[5] Bundle = Ordered: {over5}")
    print(f"[6] Checkout = ")
    choice = int(input(""))
    innerChoice = 0
    if choice == 1:
        while innerChoice != 6:
            result = Barbque(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Barbeque = 310 : {b1}")
            print(f"[2] chicken intestines = 25 : {b2}")
            print(f"[3] Pork Barbeque = 180 : {b3}")
            print(f"[4] Chicken Barbeque Stick = 180 : {b4}")
            print(f"[5] Chicken Breast = 165 : {b5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 2:
        while innerChoice != 6:
            result = Sizzling(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Pork Sisig = 200 : {s1}")
            print(f"[2] Crispy Pata = 636 : {s2}")
            print(f"[3] Special sizzling chicken with gravy = 250  : {s3}")
            print(f"[4] Sizzling liempo = 196 : {s4}")
            print(f"[5] Sizzling Pusit = 200 : {s5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 3:
        while innerChoice != 6:
            result = Seafood(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Fish And Chips = 249 : {sf1}")
            print(f"[2] Crab Cakes = 389 : {sf2}")
            print(f"[3] Grilled Octopus = 349 : {sf3}")
            print(f"[4] Grilled Salmon = 480 : {sf4}")
            print(f"[5] Butter Shrimp = 320 : {sf5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 4:
        while innerChoice != 6:
            result = Beverages(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Ice Tea = 40  : {br1}")
            print(f"[2] Tanduay Ice = 40: {br2}")
            print(f"[3] Red Horse = 60 : {br3}")
            print(f"[4] San Miguel = 50 : {br4}")
            print(f"[5] Gold Eagle = 40 : {br5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 5:
        while innerChoice != 6:
            result = Bundle(innerChoice)
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] San Miguel Bucket = 200  : {bd1}")
            print(f"[2] Red Horse Bucket = 250 : {bd2}")
            print(f"[3] Gold Eagle Bucket = 150  : {bd3}")
            print(f"[4] Tanduay Ice Bucket = 150 : {bd4}")
            print(f"[5] Barbeque party trey = 990 : {bd5}")
            print(f"[6] Return to the Main Menu")
            innerChoice = int(input("order: "))
    elif choice == 6:
        print(f"CHECK OUT")
        print(f"\nBarbeque:")
        print(f"\tBarbeque = {pb1}")
        print(f"\t Chicken Intestines = {pb2}")
        print(f"\tPork Barbeque = {pb3}")
        print(f"\tChicken Barbeque Stick = {pb4}")
        print(f"\tChicken Breast = {pb5}")
        print(f"\tPork Sisig = {ps1}")
        print(f"\tCrispy Pata = : {ps2}")
        print(f"\tSpecial sizzling chicken with gravy = {ps3}")
        print(f"\tSizzling liempo = {ps4}")
        print(f"\tSizzling Pusit = {ps5}")
        print(f"\tFish And Chips = {psf1}")
        print(f"\tCrab Cakes = {psf2}")
        print(f"\tGrilled Octopus = {psf3}")
        print(f"\tGrilled Salmon = {psf4}")
        print(f"\tButter Shrimp = {psf5}")
        print(f"\tFish And Chips = {psf1}")
        print(f"\tCrab Cakes = {psf2}")
        print(f"\tGrilled Octopus = {psf3}")
        print(f"\tGrilled Salmon = {psf4}")
        print(f"\tButter Shrimp = {psf5}")
        print(f"\tSan Miguel Bucket = {pbd1}")
        print(f"\tRed Horse Bucket =  {pbd2}")
        print(f"\tGold Eagle Bucket = {pbd3}")
        print(f"\tTanduay Ice Bucket = {pbd4}")
        print(f"\tBarbeque party trey = {pbd5}")
        print(f"Change: {total}")
