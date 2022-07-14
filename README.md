# RPSComputerVision
> Compete against computer in rock paper scissors using actual hand gestures to play your moves.

## Milestone 1: The trained model
Used 'Teachable-Machine' to train a model to recognise whether my right hand is in the form of a 'rock', 'paper' or pair of 'scissors' or whether my hand is not present (i.e. 'nothing'). This will be used to enable the user to play their move in Milestone 4.

The model is under 'keras_model.h5' and the labels are listed under 'labels.txt'

## Milestone 2: Uses the keras model to figure out the user's input
"""run_model.py
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
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

cap.release()
cv2.destroyAllWindows()
"""

## Milestone 3: The main body of the game
Uses 'random' module to enable computer to generate random choice of rock/paper/scissors. Then compares with user's input to decide the winner. 

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
    return decisions[(user_choice-comp_choice)%3]

def play():
    comp_choice = get_comp_choice();
    print(comp_choice)
    user_choice = get_user_choice();
    print("You "+get_winner(comp_choice,user_choice))

play()
"""