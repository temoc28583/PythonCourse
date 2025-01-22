
import random
def get_choice():
    # player_choice= input("Enter a choice:rock,paper or scissor")
     computer_choice= "paper"
     choices={"player":player_choice, "computer":computer_choice}
     return choices

  
def greeting():
    return "hi"

response=greeting() #use underscores for function in python
print(response)
player_choice, computer_choice = get_choice(), get_choice()




dict={"name":"beau", "color":"choice"}#key-value pair as a way to store data
#value can be a string, number, list, or another dictionary
#by removing quotes, choices becomes a variable in which we get paper from the get_choice function stored in the variable choices

