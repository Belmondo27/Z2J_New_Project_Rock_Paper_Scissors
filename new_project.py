
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
    elif menu_choose != "1" and menu_choose !="2":
        print('\x1b[48;2;0;0;255m\x1b[38;2;255;255;0m' + 'WRONG NUMBER, TRY AGAIN!' + '\x1b[0m')
    elif menu_choose == "1":
        while True:
            print("Single Player Mode")
            print("What you choose?")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Enter " "\"Back\"" " to go back to the menu")
            sinlge_choose = input("Select your weapon (enter Rock, Paper, Scissors): ")
            if sinlge_choose == "Back":
                break
            elif sinlge_choose != "Rock" and sinlge_choose !="Paper" and sinlge_choose != "Scissors":
                print('\x1b[48;2;0;0;255m\x1b[38;2;255;255;0m' + 'WRONG WEAPON, TRY AGAIN!' + '\x1b[0m')
            elif sinlge_choose == "Rock":
                print("Your choose: ", sinlge_choose)
                computer1 = random.choice(computer)
                print("Computer choose: ", computer1 )
                if sinlge_choose == computer1:
                    print('\x1b[48;2;255;255;0m\x1b[38;2;255;255;0m' + "DRAW! SO CLOSE!" + '\x1b[0m')  
                elif sinlge_choose == "Rock" and computer1 == "Scissors":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "YOU WIN!" + '\x1b[0m')  
                elif sinlge_choose == "Rock" and computer1 == "Paper":
                    print('\x1b[48;2;255;0;0m\x1b[38;2;255;255;0m' + "YOU LOSE!" + '\x1b[0m')  
            elif sinlge_choose == "Paper":
                print("Your choose: ", sinlge_choose)
                computer1 = random.choice(computer)
                print("Computer choose: ", computer1 )
                if sinlge_choose == computer1:
                    print('\x1b[48;2;255;255;0m\x1b[38;2;255;255;0m' + "DRAW! SO CLOSE!" + '\x1b[0m')  
                elif sinlge_choose == "Paper" and computer1 == "Rock":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "YOU WIN!" + '\x1b[0m')
                elif sinlge_choose == "Paper" and computer1 == "Scissors":
                    print('\x1b[48;2;255;0;0m\x1b[38;2;255;255;0m' + "YOU LOSE!" + '\x1b[0m')  
            elif sinlge_choose == "Scissors":
                print("Your choose: ", sinlge_choose)
                computer1 = random.choice(computer)
                print("Computer choose: ", computer1 )
                if sinlge_choose == computer1:
                    print('\x1b[48;2;255;255;0m\x1b[38;2;255;255;0m' + "DRAW! SO CLOSE!" + '\x1b[0m')  
                elif sinlge_choose == "Scissors" and computer1 == "Paper":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "YOU WIN!" + '\x1b[0m')  
                elif sinlge_choose == "Scissors" and computer1 == "Rock":
                    print('\x1b[48;2;255;0;0m\x1b[38;2;255;255;0m' + "YOU LOSE!" + '\x1b[0m')  
    elif menu_choose == "2":
        while True:
            print("Multi Player Mode")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Enter " "\"Back\"" " to go back to the menu")
            multi_choose = input("Player 1 select your weapon (enter Rock, Paper or Scissors): ")
            print("Player 1 choose: ", multi_choose)
            if multi_choose == "Back":
                break   
            elif multi_choose != "Rock" and multi_choose !="Paper" and multi_choose != "Scissors":
                print('\x1b[48;2;0;0;255m\x1b[38;2;255;255;0m' + 'WRONG WEAPON, TRY AGAIN!' + '\x1b[0m') 
                break
            multi_choose2 = input("Player 2 select your weapon (enter Rock, Paper or Scissors): ") 
            print("Player 2 choose: ", multi_choose2)
            if multi_choose2 == "Back":
                break   
            elif multi_choose2 != "Rock" and multi_choose2 !="Paper" and multi_choose2 != "Scissors":
                print('\x1b[48;2;0;0;255m\x1b[38;2;255;255;0m' + 'WRONG WEAPON, TRY AGAIN!' + '\x1b[0m')    
                break                 
            if multi_choose == "Rock":
                if multi_choose == multi_choose2:
                    print('\x1b[48;2;255;255;0m\x1b[38;2;255;255;0m' + "DRAW! SO CLOSE!" + '\x1b[0m')  
                elif multi_choose == "Rock" and multi_choose2 == "Scissors":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "PLAYER 1 WIN!" + '\x1b[0m')  
                elif multi_choose == "Rock" and multi_choose2 == "Paper":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "PLAYER 2 WIN!" + '\x1b[0m')  
            elif multi_choose == "Paper":
                if multi_choose == multi_choose2:
                    print('\x1b[48;2;255;255;0m\x1b[38;2;255;255;0m' + "DRAW! SO CLOSE!" + '\x1b[0m')  
                elif multi_choose == "Paper" and multi_choose2 == "Rock":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "PLAYER 1 WIN!" + '\x1b[0m')  
                elif multi_choose == "Paper" and multi_choose2 == "Scissors":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "PLAYER 2 WIN!" + '\x1b[0m')  
            elif multi_choose == "Scissors":
                if multi_choose == multi_choose2:
                    print('\x1b[48;2;255;255;0m\x1b[38;2;255;255;0m' + "DRAW! SO CLOSE!" + '\x1b[0m')  
                elif multi_choose == "Scissors" and multi_choose2 == "Paper":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "PLAYER 1 WIN!" + '\x1b[0m')  
                elif multi_choose == "Scissors" and multi_choose2 == "Rock":
                    print('\x1b[48;2;0;255;0m\x1b[38;2;255;255;0m' + "PLAYER 2 WIN!" + '\x1b[0m')  
    print( "*" * 68)
