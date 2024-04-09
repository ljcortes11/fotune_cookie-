
#IMPORT RANDOM MODULE 
import random
#DEF FUNCTION TO HAVE A LIST OF FORTUNES
player_name = input("Would you like to know your fortune? Please enter your name: ")
def fortune():
    fortune_list = ["You will have a great day today",
                    "You will find a new friend","you will find love",
                    "You will win the lottery","You will have a a great job",
                    "you will make more money"]
    
    return random.choice(fortune_list)
#DEF FUNCTION TO HAVE A LIST OF LOTTO NUMBERS

def lotto():
    lotto_list = []
    for i in range(6):
        lotto_list.append(random.randint(1,54))
    return lotto_list

#MAIN FUNCTION
def main():
    print("Welcome to the Fortune Cookie Program")
    print("Your fortune is: ",fortune())
    print("Your lotto numbers are: ",lotto())


#functin calls
fortune()
lotto()
main()

