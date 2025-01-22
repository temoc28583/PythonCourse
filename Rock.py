import random
def get_choice():
    player_choice= input("Enter a choice:rock,paper or scissor")
    option=["rock","paper","scissor"]
    computer_choice= random.choice(option)
    choices={"player":player_choice, "computer":computer_choice}
    return choices
def greeting():
    return "hi"

response=greeting() #use underscores for function in python
print(response)
choices=get_choice()

def check_win(player,computer):
    print(f"You chose {player}. Computer chose {computer}") # concat string by printing what the computer and player chose
    if player==computer:#allows program to function based on a condition based on the indentration
        return "It's a tie"#this value is within the if statement because of the indent which
    elif player=="rock":
        if computer=="scissors":
            return "rock smashed scissors,you win!"
        else:
            return "paper covers rock, you lose"
    elif player=="scissors":
        if computer=="paper":
            return "scissor cuts paper,you win!"
        else:
            return "rock smashes scissors you lose"
    return [player,computer]


#fstring, can make string with variable
a=3
b=5
if a<b:
    print("yes")
age=26
print(f"Mary is {age} years old")
check_win("rock", "paper")
#elifs will allow for only one output and wont check for any more if statements
if age>=18:
    print("You are an adult")
elif age>12:
    print("You are a teenager")
elif age>1:
    print("You are a child")
else:
    print("You are a baby")

choices=get_choice()
#to get the choice of a player
pChoice=choices["player"] #way to access value based one player key