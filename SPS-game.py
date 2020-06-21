# A game of Stone|Paper|Scissor with the User and the Computer

# import random module
import random

# menu function which displays options to choose from
def print_menu():
    print("Enter a choice\n 1.Stone\n 2.Paper\n 3.Scissor\n")
print("Welcome to Stone|Paper|Scissor\n")

# Printing a multiline instruction to perform string concatenation of string 
print("Winning rules of the Stone|Paper|Scissor game are as follows: \n "
                                +"Stone vs Paper -> Paper wins \n "
                                +"Stone vs Scissor -> Stone wins \n "
                                +"Paper vs Scissor -> Scissor wins \n ")
# To start the game
play = input("Enter 1 to play: ")
while(play!='1'):
    play = input("\nEnter 1 to play: ")    

# Initialising Scores to 0
User = 0
Computer = 0

# Taking maximum points input from user
n = int(input("Enter number of points you want to play: "))
while(play=='1'):
    print_menu()
    
    # Taking input from user
    choice = int(input("User Turn: "))
    
    # Looping until the user enters a valid input
    while choice<1 or choice>3:
        choice = int(input("\nPlease enter a valid input \nUser Turn: "))
        
    # Initializing the value of choice_name variable corresponding to the choice value
    if choice==1:
        choice_name = 'Stone'
    elif choice==2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    print("User choice is: "+choice_name)
    print("\nNow its my turn....\n")
    
    # Computer chooses randomly any number among 1 , 2 and 3 using randint method of random module 
    comp_choice = random.randint(1,3)
    
    # Looping until comp_choice value not equal to the choice value
    # It means looping until computer value not equal to user value
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
        
    # Initializing the value of comp_choice_name variable corresponding to the choice value
    if comp_choice==1:
        comp_choice_name = 'Stone'
    elif comp_choice==2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
    print("My choice is: "+comp_choice_name)
    print("\n" +choice_name+ " vs " +comp_choice_name+ " => ",end = "")
    
    # Condition for winning 
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("Paper wins") 
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Stone wins") 
        result = "Stone"
    else: 
        print("Scissor wins") 
        result = "Scissor"
      
    # Printing winner in each round and computing scores
    if result == choice_name: 
        print("Uggh!! I lost this round")
        User += 1
    else: 
        print("Yes!!! I win this round")
        Computer += 1
        
    # Printing the scores after each round
    print("\n----Scores---- \nUser: ",User,"\nComputer: ",Computer,"\n--------------\n")
    
    # Checking for game over condition
    if User == n:
        print("\nYou won the match!!! I'll see you next time.")
        break
    elif Computer == n:
        print("\nYou lose the match!!! I'll see you next time.")
        break
    else:
        continue
