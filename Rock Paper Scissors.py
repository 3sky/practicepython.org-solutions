a = ['rock', 'scissors', 'paper']
name1 = "player1"
name2 = "player2"
def change_name():
    global name1
    global name2
    which_player = input("\nWhich players name you want to change?\n      "
                         "* First players name - press 1\n      "
                         "* Second players name - press 2\n      "
                         "* Both of players's names - pres 3\n      "
                         "* I'm lost take me back(pres q)\n"
                         "What you want to do? ")
    if which_player == "1":
        name1 = input('[{}] - Give your new name: '.format(name1))
        if not name2 or name2 != "Player 2":
            name2 = name2
        else :
            name2 = "Player 2"
        menu()
    elif which_player == "2":
        name2 = input('[{}] - Give your new name: '.format(name2))
        if not name1 or name1 != "Player 1":
            name1 = name1
        else :
            name2 = "Player 2"
        menu()
    elif which_player == "3":
        name1 = input('[{}] - Give your new name: '.format(name1))
        name2 = input('[{}] - Give your new name: '.format(name2))
        menu()
    elif which_player == "q":
        menu()
    else:
        change_name

def menu():
    main_choose = input("\nWhat you want to do?\n      "
                        "* If you want play game - press 1\n      "
                        "* If you want change player name - pres 2\n      "
                        "* If you want to quit game - press 3\n"
                        "Your choose(1,2,3): ")
    if main_choose == "1":
        lets_play()
    elif main_choose == "2":
        change_name()
    elif main_choose == "3":
        print ("\nThanks for playing")
        exit()
    else :
        menu()

def lets_play():
    player1 = input('[{}] - Give me your type:'.format(name1))
    player1 = player1.lower()
    while player1 not in a:
        print ( player1 + " is invalid word")
        player1 = input("Input it again: " )
        player1 = player1.lower()
    player2 = input('[{}] - Give me your type:'.format(name2))
    player2 = player2.lower()
    while player2 not in a:
        print ( player2 + " is invalid word")
        player2 = input("Input it again: " )
        player2 = player2.lower()
    if player1 == player2:
        print ("IT'S TIE !!!")
    elif player1 == "rock" and player2 == "scissors":
        print (name1 + " - WIN!!!")
    elif player1 == "rock" and player2 == "paper":
        print (name2 + " - WIN!!!")
    elif player1 == "scissors" and player2 == "rock":
        print (name2 + " - WIN!!!")
    elif player1 == "scissors" and player2 == "peper":
        print (name1 + " - WIN!!!")
    elif player1 == "paper" and player2 == "rock":
        print (name1 + " - WIN!!!")
    elif player1 == "paper" and player2 == "scissors":
        print (name2 + " - WIN!!!")
    menu()


print ("\nWelcome my dear friend in game")
menu()
