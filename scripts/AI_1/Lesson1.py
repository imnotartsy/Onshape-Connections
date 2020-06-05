#!/usr/bin/env pybricks-micropython
'''
Example for Using PuppyTraining Module
Prototype by Tufts Center for Engineering Education and Outreach
April 2020

PuppyTraining is an AI module and class for an EV3 running micropython.

We use a supervised 1-dimenional minimum-distance-to-mean algorithm
for training a robot to detect two gyroscope states corresponding to
"command A" and "command B" for a puppy learning a trick.

Modified by Teo (Therese) Patrosio
June 2020
'''

from spike import PrimeHub
from spike.control import wait_for_seconds
import PuppyTraining
import PuppyBasic

prime_hub = PrimeHub()
prime_hub.speaker.beep(72,0.5)

# Initial puppy using motors for Left Leg, Right Leg, and optionally Head
puppy = PuppyBasic.PuppyBasic('D', 'C', 'F')

state = "standing"  # Puppy begins standing,
# so that it can only sit (see sit and stand commands)

# Initialized puppy training using a Gyro
training = PuppyTraining.PuppyTraining(gyroport='A')

# Start a training session with the puppy
# Push the "up" button to record an example of command A
# Push the "down" button to record an example of command B
# Push the "center" button to stop the training session
# In this example, command A is for sitting,and command B is for standing
training.watch()

# Uses the recorded examples to train a decision model for puppy
training.train()
wait_for_seconds(.01)

# Print out the final results of the training make sure the puppy has it right!
training.report()
while not hub.button.center.is_pressed():
    wait_for_seconds(.01)
while hub.button.center.is_pressed():
    wait_for_seconds(.01)

# Use the trained model to have the puppy to do the commands you create!
while not hub.button.center.is_pressed():
    command = training.prediction()
    if command == 'A' and state == "standing":
        # Puppy should sit
        state = "sitting"
        puppy.sit()
        wait_for_seconds(.01)

    elif command == 'B' and state == "sitting":
        # Puppy should stand
        state = "standing"
        puppy.stand()
        wait_for_seconds(.01)

    else:
        wait_for_seconds(.02)

# If you want to clear out your puppy's training in order to teach
# something new, tell the puppy to forget
training.forget()
