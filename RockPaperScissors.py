import os
import sys
def play():

    i = 5 

    play = True
    while play:
        rock = "rocks"
        scissors = "sicssors"
        paper = "paper"

        rock > scissors, paper > rock, scissors > paper 
        
        print("Welcome to rock, paper, scissor")
        while (i > 0):
            playerOne = int(input("Enter 1 for rock:\nEnter 2 for paper:\nEnter 3 for scissors:\nEnter 4 to quit:\nPlayer1>"))
            if playerOne == 1:
                playerOnechoice = rock 
                break
            elif playerOne == 2:
                playerOnechoice = paper 
                break
            elif playerOne == 2:
                playerOnechoice = scissors 
                break
            elif playerOne == 4:
                sys.exit()
            else:
                print("I don't understand that enter it again")

        while (i > 0): 
            playerTwo= int(input("\nEnter 1 for rock:\nEnter 2 for paper:\nEnter 3 for scissors:\nEnter 4 to quit:\nPlayer2>"))
            if playerTwo == 1:
               playerTwochoice = rock 
               break
            elif playerTwo == 2:
               playerTwochoice = paper 
               break
            elif playerTwo == 3:
               playerTwochoice = scissors 
               break
            elif playerTwo == 4:
                sys.exit()
            else:
                print("I don't understand that enter it again")



        if playerOnechoice > playerTwochoice:
           print(f"Player one wins with{playerOnechoice}") 
        elif playerTwochoice > playerOnechoice:
           print(f"Player two wins with {playerTwochoice}") 
        elif playerOnechoice == playerTwochoice:
            print(f"Draw both players draw {playerOnechoice}")

        
        
            

    
     
    
play()
