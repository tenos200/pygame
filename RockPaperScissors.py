import sys    


def play():
    
    
    while True:
        usr_1 = input("Welcome to rock, paper, scissor\nIf you would like to quit press q\nElse enter your choice\nPlayer1>")
        usr_2 = input("Player2>")

        if usr_1 == "rock":
            if usr_2 == "paper":
                print(f"Player 2 wins")
            elif usr_2 =="rock":
                print("Draw")
            elif usr_2 == "scissor":
                print("Player 1 wins")

        elif usr_1 == "paper":
            if usr_2 == "rock":
                print("Player 1 wins")
            elif usr_2 == "paper":
                print("Draw")
            elif usr_2 == "scissor":
                print("Player 2 wins")

        elif usr_1 == "scissor":
            if usr_2 == "rock":
                print("Player 2 wins")
            elif usr_2 == "paper":
                print("Player 1 wins")
            elif usr_2 == "scissor":
                print("Draw")
        elif usr_1 or usr_2 == "q":
            break
        else:
            print("I don't understand that")
            play()

play()





