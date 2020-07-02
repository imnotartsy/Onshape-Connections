#!/usr/bin/env pybricks-micropython
"""
Example Code 1 K-Nearest Neighbor using PetTrainingSupervised
Prototype by Tufts Center for Engineering Education and Outreach
May 2020

PetTrainingSupervised is an AI module which provides
PetTrainingKNN, a class for an EV3 running micropython.

PetTrainingKNN uses a 1-dimenional K-Nearest Neighbor algorithm
for training a robot to detect two different lenghts of button presses
corresponding to a "pat" and "stroke" for a puppy reacting to different
pet lengths.
"""
# from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import (Port, Stop, Direction, Button, Color,
#                                  SoundFile, ImageFile, Align)
# from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase
import PetTrainingSupervised
import PuppyBasic

# Initialize ev3
prime_hub = PrimeHub()
prime_hub.speaker.beep(72,0.5)

# Define the number of training strokes and pats
train_num = 5

# Initialize training model
training = PetTrainingSupervised.PetTrainingKNN('B', train_num)

# Collect train_num examples pats
training.record_examples(train_num, 'pat')

# Collect train_num examples strokes
training.record_examples(train_num, 'stroke')
training.report()

# Define the number of training examples used to predict the pet type
K = 3

# Initialize puppy model
puppy = PuppyBasic.PuppyBasic('D', 'A', 'C')

# Classify pets until center button is pressed
print("Stroke or Pet")
while not hub.button.center.is_pressed()::
    time = training.button_timer()
    if hub.button.center.is_pressed() or time == "END":
        # Exit when the center button is pressed
        break
    else:
        guess = training.k_nearest_neighbor_prediction(time, K)
        print('%d is classified as  %s' % (time, guess))
        # Puppy is happy when patted, sleepy when stroked
        if guess == "pat":
            puppy.happy()
        elif guess == "stroke":
            puppy.sleepy()
