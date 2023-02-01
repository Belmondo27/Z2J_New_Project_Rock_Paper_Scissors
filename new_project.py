
import sys
import random

computer = ["Rock", "Paper", "Scissors"]

while True:
    print( "*" * 20 , " Rock Paper Scissors GAME ", "*" * 20 )
    print("1. Single Player")
    print("2. Multi Player")
    print("3. Exit")
    menu_choose = input("Select game mode (enter 1 or 2) or 3 to close program: ")
    if menu_choose == "3":
        print("GAME OVER")
        break
    elif menu_choose != "1" and "2":
        print('\x1b[38;2;255;0;0m\x1b[48;2;255;255;0m' + 'WRONG NUMBER, TRY AGAIN!' + '\x1b[0m')
    elif menu_choose == "1":
        print("Single Player Mode")
        print("What you choose?")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        sinlge_choose = input("Select your weapon (enter Rock, Paper or Scissors): ")
        if sinlge_choose == "Rock":
            print("Your choose: ", sinlge_choose)
            computer1 = random.choice(computer)
            print("Computer choose: ", computer1 )
            if sinlge_choose == computer1:
                print("DRAW! So Close! :O")
            elif sinlge_choose == "Rock" and computer1 == "Scissors":
                print("YOU WIN! Congrats! :)")
            elif sinlge_choose == "Rock" and computer1 == "Paper":
                print("YOU LOSE! So sad :(")
        elif sinlge_choose == "Paper":
            print("Your choose: ", sinlge_choose)
            computer1 = random.choice(computer)
            print("Computer choose: ", computer1 )
            if sinlge_choose == computer1:
                print("DRAW! So Close! :O")
            elif sinlge_choose == "Paper" and computer1 == "Rock":
                print("YOU WIN! Congrats! :)")
            elif sinlge_choose == "Paper" and computer1 == "Scissors":
                print("YOU LOSE! So sad :(")
        elif sinlge_choose == "Scissors":
            print("Your choose: ", sinlge_choose)
            computer1 = random.choice(computer)
            print("Computer choose: ", computer1 )
            if sinlge_choose == computer1:
                print("DRAW! So Close! :O")
            elif sinlge_choose == "Scissors" and computer1 == "Paper":
                print("YOU WIN! Congrats! :)")
            elif sinlge_choose == "Scissors" and computer1 == "Rock":
                print("YOU LOSE! So sad :(")
    elif menu_choose == "2":
            print("Multi Player Mode")
            print("Player 1 what you choose?")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            multi_choose = input("Player 1 select your weapon (enter Rock, Paper or Scissors): ")
            multi_choose2 = input("Player 2 select your weapon (enter Rock, Paper or Scissors): ")
            print("Player 1 choose: ", multi_choose)
            print("Player 2 choose: ", multi_choose2)
            if multi_choose == "Rock":
                if multi_choose == multi_choose2:
                    print("DRAW! So Close! :O")
                elif multi_choose == "Rock" and multi_choose2 == "Scissors":
                    print("Player 1 WIN! Congrats! :)")
                elif multi_choose == "Rock" and multi_choose2 == "Paper":
                    print("Player 2 WIN! Congrats! :)")
            elif multi_choose == "Paper":
                if multi_choose == multi_choose2:
                    print("DRAW! So Close! :O")
                elif multi_choose == "Paper" and multi_choose2 == "Rock":
                    print("Player 1 WIN! Congrats! :)")
                elif multi_choose == "Paper" and multi_choose2 == "Scissors":
                    print("Player 2 WIN! Congrats! :)")
            elif multi_choose == "Scissors":
                if multi_choose == multi_choose2:
                    print("DRAW! So Close! :O")
                elif multi_choose == "Scissors" and multi_choose2 == "Paper":
                    print("Player 1 WIN! Congrats! :)")
                elif multi_choose == "Scissors" and multi_choose2 == "Rock":
                    print("Player 2 WIN! Congrats! :)")
    print( "*" * 68)
