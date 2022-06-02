#
R = "Rock"
P = "Paper"
S = "Scissors"
Mylist = ["R", "P","S"]
import module
print("Rules:\n" + "R vs P -> P wins \n" + "R vs S -> R wins \n" + "P vs S -> S wins \n")
while True:
    print("enter player_choice from mylist \n")
    # take users input
   choice = int(input("Users turn:"))
    while player_choice != Mylist:
        player_choice = int(input("input is invalid, please enter a valid input:"))
        if player_choice == 'R':
            player_choice_name = "Rock"
            elif player_choice == 'P':
            Player_choice_name = "Paper"
        else:
            player_choice_name = "Scissors"
            print("user choice is:" + player_choice_name)
            #computer's choice
            computer_choice = random.Mylist
            #looping
            while computer_choice == choice:
                computer_choice = random.Mylist
                if computer_choice == 'R':
                    computer_choice_name = "Rock"
                elif computer_choice == 'P':
                    computer_choice_name = "Paper"
                else:
                    computer_choice_name = "Scissors"
                    print("computer_choice is:" + computer_choice_name)
                    print( player_choice_name "vs" computer_choice_name)
                    if((player_choice == 'R' and computer_choice == 'P') or ( player_choice == 'P' and computer_choice == 'R')):
                        print("computer won")
                        result = "Paper"
                    elif((player_choice == 'R' andcomputer_choice == 'S' ) or (player_choice == 'S' and computer_choice == 'R')):
                        print(" Hurray! You are the winner")
                        result = "Rock"
                    else:
                        print("computer won")
                        result = "Scissors"
                        if(player_choice == computer_choice)
                        print("there is a tie")
                    
            
            



   

