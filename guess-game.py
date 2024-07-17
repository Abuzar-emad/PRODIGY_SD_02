#("guessing Game")
import random

ran_num = random.randint(0,10)
def guss_game():
    print("Wellcome to Guessing Game, Your guess should be between 0,10 ")
    counter = 0
    guss= None
    while guss != ran_num: 
        guss= int(input("Pleace Enter Your Guess "))
        counter += 1
        if guss > ran_num:
          print("too larg") 
        elif guss < ran_num:
           print("too low") 
        else:
           guss == ran_num
           print(" Congratulations! your guss right and your number of attempts is",counter)

           
guss_game()