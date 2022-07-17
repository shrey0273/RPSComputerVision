import cv2
from run_model import  activate_model,cap
from manual_rps import get_comp_choice,get_winner,options

def new_prediction():
    distribution = list((activate_model())[0])
    max_val = max(distribution)
    print(max_val)
    return distribution.index(max_val)

def play():
    games = 0
    wins = 0
    losses = 0
    while wins!=3 and losses!=3:
        games+=1
        input("You ready?")
        print("Okay let's go! Round "+str(games))
        comp_choice = get_comp_choice();
        user_choice = new_prediction();
        print("The Computer Chose "+options[comp_choice]+" while you chose "+options[user_choice])
        result = get_winner(comp_choice,user_choice);
        if result=="Win!!":
            wins+=1
        elif result=="Lose...":
            losses+=1
        print("You "+result)
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

play()