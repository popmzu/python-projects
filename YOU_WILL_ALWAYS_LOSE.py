credit = 100


decision = "Y"
while(decision == "Y"):
    sign_string = ("="*36)
    print(sign_string)
    print("WELCOME TO YOU WILL ALWAYS LOSE")
    print(sign_string)
    print("WIN BIG OR GO HOME WITH NOTHING.....")
    print(sign_string)
    print("GET 3 OF THE SAME NUMBER TO WIN DUBBLE WHAT YOU PLAYED")
    print(sign_string)
    print("YOU CURRENTLY HAVE " + str(credit) + " CREDITS, HOW MUCH WOULD YOU LIKE TO PLAY")

    bet = int(input(""))

    if bet > credit:
        print("YOU SEEM TO BE BROKE TO DO THAT, GOOD BYE\n"
                "YOU HAVE CASHED OUT 100 CREDITS\n"
                "COME LOSE AGAIN SOON!!!!!!!!! HAHAHAHA")


    else:    
        from random import randint
        
        credit = credit-bet
        rand1 = randint(0,10)
        rand2 = randint(0,10)
        rand3 = randint(0,10)

        print("YOUR NUMBERS ARE.........")
        print(sign_string)
        print(rand1,rand2,rand3)
        
        
        if rand1 == rand2 == rand3:
            won=bet*2
           
            print("YOU HAVE WON" + str(won) + "CREDITS")
            credit = credit + won
            
        else:
            
            print("YOU LOST THAT ONE !!!!!!!!!!!! HAHAHAHAHAHA")
            print(sign_string)
                
       
    print("YOU CURRENTLY HAVE " + str(credit) + " CREDITS.")
    print("WOULD LIKE TO PLAY AGAIN??? Y/N")
    print(sign_string)
    decision = input("")
print("YOU HAVE CASHED OUT " + str(credit) + " CREDITS")

     
