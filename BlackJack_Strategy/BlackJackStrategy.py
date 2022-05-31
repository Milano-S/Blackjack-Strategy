x = 0
while x < 4:
    ut = int(input("Your Total; "))
    cardType = input("Is total hard, soft or pair; ")
    dealerUpcard = int(input("Dealers Upcard; "))


    def hard_totals():
        if ut < 9:
            print("Hit")
        elif ut == 9 and dealerUpcard in range(3, 7):
            print("Double")
        elif ut == 10 and dealerUpcard in range(2, 10):
            print("Double")
        elif ut == 11:
            print("Double")
        elif ut == 12:
            if dealerUpcard in range(4, 7):
                print("Stand")
            else:
                print("Hit")
        elif ut in range(13, 17):
            if dealerUpcard < 7:
                print("Stand")
            else:
                print("Hit")
        else:
            print("Hit")


    def soft_totals():
        if ut in range(13, 15):
            if dealerUpcard in range(5, 7):
                print("Double")
            else:
                print("Hit")
        elif ut in range(15, 17):
            if dealerUpcard in range(5, 7):
                print("Double")
            else:
                print("Hit")
        elif ut == 17:
            if dealerUpcard in range(3, 7):
                print("Double")
            else:
                print("Hit")
        elif ut == 18:
            if dealerUpcard in range(2, 7):
                print("Double if allowed otherwise Stand")
            elif dealerUpcard in range(7, 9):
                print("Stand")
            else:
                print("Hit")
        elif ut == 19:
            if dealerUpcard == 6:
                print("Double or stand if allowed")
            else:
                print("Stand")
        elif ut > 19:
            print("Stand")
        else:
            print("Hit")


    def pair_totals():
        if ut == 4 or ut == 6:
            if dealerUpcard in range(2, 4):
                print("Split only if Double After Stand is allowed")
            elif dealerUpcard in range(4, 8):
                print("Split")
            else:
                print("Do not Split instead; ")
                hard_totals()
        elif ut == 8:
            if dealerUpcard in range(5, 7):
                print("Split only if Double After Stand is allowed")
            else:
                print("Do not Split instead; ")
                hard_totals()
        elif ut == 10:
            print("Never Split")
            hard_totals()
        elif ut == 12:
            if dealerUpcard == 2:
                print("Split only if Double After Stand is allowed")
            elif dealerUpcard in range(3, 7):
                print("Split")
                hard_totals()
            else:
                print("Do not Split instead; ")
                hard_totals()
        elif ut == 14:
            if dealerUpcard < 7:
                print("Split")
                hard_totals()
            else:
                print("Do not Split instead; ")
                hard_totals()
        elif ut == 16:
            print("Split")
            hard_totals()
        elif ut == 18:
            if dealerUpcard < 7:
                print("Split")
                hard_totals()
            elif dealerUpcard in range(8, 10):
                print("Split")
                hard_totals()
            else:
                print("Do not Split instead; ")
                hard_totals()
        elif ut == 20:
            print("Never Split")
            hard_totals()
        elif ut == 22:
            print("Always Split and Double if allowed")


    if cardType == "hard":
        hard_totals()
    if cardType == "soft":
        soft_totals()
    if cardType == "pair":
        pair_totals()
    x += 1
