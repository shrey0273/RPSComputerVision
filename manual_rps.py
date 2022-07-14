import random

#uses labels.txt to discover the options of the game, + dict. assigns indices
options_file = open("labels.txt","r")
options = (options_file.read()).split("\n")
options = [option[2:] for option in options]
indexofoption = {options[i]:i for i in range(len(options))}
print(indexofoption)

options_file.close()

def get_comp_choice():
    comp = random.randint(0,len(options)-2)
    return comp

def get_user_choice():
    user = input("What do you play? ")
    user = str.title(user) #must put input into correct form
    return indexofoption[user]

def get_winner(comp_choice,user_choice):
    decisions = {0:"Draw!",1:"Win!!",2:"Lose..."}
    return decisions[(user_choice-comp_choice)%3]

def play():
    comp_choice = get_comp_choice();
    print(comp_choice)
    user_choice = get_user_choice();
    print("You "+get_winner(comp_choice,user_choice))

play()