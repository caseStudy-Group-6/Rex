choices = 0
innerChoice = 0
payment = 0
over1, over2, over3, over4, over5, b1, b2, b3, b4, b5, pb1, pb2, pb3, pb4, pb5, s1, s2, s3, s4, s5, ps1, ps2, ps3, ps4, ps5, sf1, sf2, sf3, sf4, sf5, psf1, psf2, psf3, psf4, psf5, br1, br2, br3, br4, br5, pbr1, pbr2, pbr3, pbr4, pbr5, bd1, bd2, bd3, bd4, bd5, pbd1, pbd2, pbd3, pbd4, pbd5 = [0] * 55
totalPrice, totalPriceB, bundle, totalPriceS, totalPriceSf, totalPriceBr = [0] * 6

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

def Bundle(innerChoice):
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

def checkout():
    global pb1, pb2, pb3, pb4, pb5, ps1, ps2, ps3, ps4, ps5, psf1, psf2, psf3, psf4, psf5, pbr1, pbr2, pbr3, pbr4, pbr5, pbd1, pbd2, pbd3, pbd4, pbd5, totalPrice, totalPriceB, totalPriceS, totalPriceSf, totalPriceBr, totalPriceBd
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
    totalPriceB = pb1 + pb2 + pb3 + pb4 + pb5
    totalPriceS = ps1 + ps2 + ps3 + ps4 + ps5
    totalPriceSf = psf1 + psf2 + psf3 + psf4 + psf5
    totalPriceBr = pbr1 + pbr2 + pbr3 + pbr4 + pbr4
    totalPriceBd = pbd1 + pbd2 + pbd3 + pbd4 + pbd5
    totalPrice = totalPriceB + totalPriceBr + totalPriceS + totalPriceSf + totalPriceBd
    return pb1, pb2, pb3, pb4, pb5, ps1, ps2, ps3, ps4, ps5, psf1, psf2, psf3, psf4, psf5, pbr1, pbr2, pbr3, pbr4, pbr5, pbd1, pbd2, pbd3, pbd4, pbd5, totalPriceB, totalPriceBd, totalPriceBr, totalPriceS, totalPriceSf

def are_you_sure():
    while True:
        try:
            response = input("Are you sure (y/n): ")
            if response in ["y", "Y"]:
                return True
            elif response in ["n", "N"]:
                return False
            else:
                print("Invalid input. Please enter y or n.")
        except KeyboardInterrupt:
            print("\nExiting...")
            exit()

def choice():
    while True:
        try:
            choices = int(input("Enter an Order: "))
            if 1 <= choices <= 6 and choices != 7:
                return choices
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an again.")

while choices <= 5:
    result = Overalls(choice)
    print(f"=====RESTO BAR MENU===============")
    print(f"[1] Barbeque = Ordered: {over1}")
    print(f"[2] Sizzling Plate = Ordered: {over2}")
    print(f"[3] Seafood = Ordered: {over3}")
    print(f"[4] Beverages = Ordered: {over4}")
    print(f"[5] Bundle = Ordered: {over5}")
    print(f"[6] Checkout ")
    print(f"==================================")
    choices = choice()
    innerChoice = 0
    if choices == 1:
        while innerChoice != 6:
            result = Barbque(innerChoice)
            print(f"========BARBERQUE=========================")
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Barbeque = 310 : {b1}")
            print(f"[2] chicken intestines = 25 : {b2}")
            print(f"[3] Pork Barbeque = 180 : {b3}")
            print(f"[4] Chicken Barbeque Stick = 180 : {b4}")
            print(f"[5] Chicken Breast = 165 : {b5}")
            print(f"[6] Return to the Main Menu")
            print(f"==========================================")
            innerChoice = int(input("Order: "))
    elif choices == 2:
        while innerChoice != 6:
            result = Sizzling(innerChoice)
            print(f"=========SIZZLING=========================")
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Pork Sisig = 200 : {s1}")
            print(f"[2] Crispy Pata = 636 : {s2}")
            print(f"[3] Special sizzling chicken with gravy = 250 : {s3}")
            print(f"[4] Sizzling liempo = 196 : {s4}")
            print(f"[5] Sizzling Pusit = 200 : {s5}")
            print(f"[6] Return to the Main Menu")
            print(f"==========================================")
            innerChoice = int(input("Order: "))
    elif choices == 3:
        while innerChoice != 6:
            result = Seafood(innerChoice)
            print(f"=========SEAFOOD==========================")
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Fish And Chips = 249 : {sf1}")
            print(f"[2] Crab Cakes = 389 : {sf2}")
            print(f"[3] Grilled Octopus = 349 : {sf3}")
            print(f"[4] Grilled Salmon = 480 : {sf4}")
            print(f"[5] Butter Shrimp = 320 : {sf5}")
            print(f"[6] Return to the Main Menu")
            print(f"==========================================")
            innerChoice = int(input("Order: "))
    elif choices == 4:
        while innerChoice != 6:
            result = Beverages(innerChoice)
            print(f"=========BEVERAGES========================")
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] Ice Tea = 40  : {br1}")
            print(f"[2] Tanduay Ice = 40: {br2}")
            print(f"[3] Red Horse = 60 : {br3}")
            print(f"[4] San Miguel = 50 : {br4}")
            print(f"[5] Gold Eagle = 40 : {br5}")
            print(f"[6] Return to the Main Menu")
            print(f"==========================================")
            innerChoice = int(input("Order: "))
    elif choices == 5:
        while innerChoice != 6:
            result = Bundle(innerChoice)
            print(f"===========BUNDLES========================")
            print(f"To remove the Order, Input a negative sign")
            print(f"[1] San Miguel Bucket = 200  : {bd1}")
            print(f"[2] Red Horse Bucket = 250 : {bd2}")
            print(f"[3] Gold Eagle Bucket = 150  : {bd3}")
            print(f"[4] Tanduay Ice Bucket = 150 : {bd4}")
            print(f"[5] Barbeque party trey = 990 : {bd5}")
            print(f"[6] Return to the Main Menu")
            print(f"==========================================")
            innerChoice = int(input("order: "))
    elif choices == 6:
        while innerChoice != 7:
            result = checkout()
            print("====================CHECK-OUT====================")
            print("Barbeque:")
            print(f"\tBarbeque = Ordered: {b1} \n\t\tPrice: {pb1}")
            print(f"\tBarbeque Party Trey = Ordered: {b2} \n\t\tPrice: {pb2}")
            print(f"\tPork Barbeque = Ordered: {b3} \n\t\tPrice: {pb3}")
            print(f"\tChicken Barbeque Stick = Ordered: {b4} \n\t\tPrice: {pb4}")
            print(f"\tChicken Breast = Ordered: {b5} \n\t\tPrice: {pb5}")
            print(f" Total: {totalPriceB}")
            print("Sizzling:")
            print(f"\tPork Sisig = Ordered: {s1} \n\t\tPrice: {ps1}")
            print(f"\tCrispy Pata = Ordered: {s2} \n\t\tPrice: {ps2}")
            print(f"\tSpecial sizzling chicken with gravy = Ordered: {s3} \n\t\tPrice: {ps3}")
            print(f"\tChicken Barbeque Stick = Ordered: {s4} \n\t\tPrice: {ps4}")
            print(f"\tChicken Breast = Ordered: {s5} \n\t\tPrice: {ps5}")
            print(f" Total: {totalPriceS}")
            print("Seafood:")
            print(f"\tFish And Chips =Ordered: {sf1} \n\t\tPrice: {psf1}")
            print(f"\tCrab Cakes = Ordered: {sf2} \n\t\tPrice: {psf2}")
            print(f"\tGrilled Octopus = Ordered: {sf3} \n\t\tPrice: {psf3}")
            print(f"\tGrilled Salmon = Ordered: {sf4} \n\t\tPrice: {psf4}")
            print(f"\tButter Shrimp = Ordered: {sf5} \n\t\tPrice: {psf5}")
            print(f" Total: {totalPriceSf}")
            print("Beverages:")
            print(f"\tIce Tea = Ordered: {br1} \n\t\tPrice: {pbr1}")
            print(f"\tTanduay Ice = Ordered: {br2} \n\t\tPrice: {pbr2}")
            print(f"\tRed Horse = Ordered: {br3} \n\t\tPrice: {pbr3}")
            print(f"\tSan Miguel = Ordered: {br4} \n\t\tPrice: {pbr4}")
            print(f"\tGold Eagle = Ordered: {br5} \n\t\tPrice: {pbr5}")
            print(f"\nTotal: {totalPriceBr}")
            print("Bundle:")
            print(f"\tSan Miguel Bucket = Ordered: {bd1} \n\t\tPrice: {pbd1}")
            print(f"\tRed Horse Bucket = Ordered: {bd2} \n\t\tPrice: {pbd2}")
            print(f"\tGold Eagle Bucket = Ordered: {bd3} \n\t\tPrice:  {pbd3}")
            print(f"\tTanduay Ice Bucket = Ordered: {bd4} \n\t\tPrice: {pbd4}")
            print(f"\tBarbeque party trey = Ordered: {bd5} \n\t\tPrice: {pbd5}")
            print(f"Total: {totalPriceBd}")
            print(f"\nTotal Price Ordered: {totalPrice}")
            break
        if are_you_sure():
            print("You confirmed")
            payment = int(input("Payment: "))
            while payment < totalPrice:
                AllinAll = payment - totalPrice
                print(f"You Are {AllinAll * -1} peso/s short, pls pay the total amount needed.")
                payment = (input("Payment: "))
            break
        else:
            print("You canceled.")
            print(f"Choose [0] to return to the Main Menu\if not press any key...")
            choice = int(input("Input your choice: "))
            continue
    elif choices > 6:
        print(f"Please input [1] to [5] to order and input [6] to checkout.")
        continue

change = payment - totalPrice
print(f"===========================")
print(f"\nTotal price: {totalPrice:,.2f}")
print(f"Payment: {payment:,.2f}")
print(f"Change: {change:,.2f}")
print(f"THANK YOU FOR ORDERING <3")
print(f"==========================")
