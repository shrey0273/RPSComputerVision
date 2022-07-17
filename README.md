# RPSComputerVision
> Compete against computer in rock paper scissors using actual hand gestures to play your moves.

## Milestone 1: The trained model
Used 'Teachable-Machine' to train a model to recognise whether my right hand is in the form of a 'rock', 'paper' or pair of 'scissors' or whether my hand is not present (i.e. 'nothing'). This will be used to enable the user to play their move in Milestone 4.

The model is under 'keras_model.h5' and the labels are listed under 'labels.txt'

## Milestone 2: Uses the keras model to figure out the user's input
**NEW** Now also uses the 'time' module to only take the 'prediction' after 15 seconds, in each round

"""run_model.py
import cv2,time
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def activate_model():
    


    end = time.time()+15
    while time.time()<end: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return prediction
"""

## Milestone 3: The main body of the game
Uses 'random' module to enable computer to generate random choice of rock/paper/scissors. Then compares with user's input to decide the winner; note that the user must lose if they play nothing. 

"""manual_rps.py
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
    return decisions[(user_choice-comp_choice)%3] if user_choice!=3 else "Lose..."

def play():
    comp_choice = get_comp_choice();
    print(comp_choice)
    user_choice = get_user_choice();
    print("You "+get_winner(comp_choice,user_choice))
"""

## Milestone 4: Incorporating computer vision into the game
Uses 'manual_rps' and 'run_model' from previous milestones to make the rps game incorporate computer vision for player input. Also made modifications to makw it user friendly, by including rounds and clearly stating who played what and who won.
"""camera_rps.py
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
"""
