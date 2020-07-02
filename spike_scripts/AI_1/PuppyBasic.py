#!/usr/bin/env pybricks-micropython

"""
PuppyBasic
-----------

Prototype by Tufts Center for Engineering Education and Outreach
May 2020

Modified by Teo (Therese) Patrosio
June 2020
"""

from spike import PrimeHub
from spike import Motor
from spike.control import wait_for_seconds

class PuppyBasic:
    "PuppyBasic class with basic Puppy actions"
    
    def __init__(self, leftmotorport, rightmotorport, headmotorport=None):
        """Assumes a three motor puppy configuration
        with two legs and one head motor"""
        self.prime_hub = PrimeHub() 
        self.prime_hub.light_matrix.show_image('HAPPY')
        self.legR = Motor(rightmotorport)   # right leg
        self.legL = Motor(leftmotorport)    # left leg
            

        #self.legs = DriveBase(self.legL, self.legR, 30, 80)
        if headmotorport is not None:
        # If no headmotorport is given, it is not assigned.
            self.head = Motor(headmotorport)    # head motor
        else:
            self.head = None

    def sit(self):
        """ Puppy sit with leg motors"""
        # TODO: modify to use paired motors
        self.legR.start_at_power(75)
        self.legL.start_at_power(75)
        wait_for_seconds(.4)
        self.legR.start_at_power(0)
        self.legL.start_at_power(0)
        print("Sitting Down")

    def stand(self):
        """ Puppy stand with leg motors"""
        # TODO: modify to use paired motors
        self.legR.start_at_power(-75)
        self.legL.start_at_power(-75)
        wait_for_seconds(.4)
        self.legR.start_at_power(0)
        self.legL.start_at_power(0)
        print("Standing Up")

    def bark(self):
        """Play bark sound"""
        self.prime_hub.speaker.beep(69, 0.5)

    def snore(self):
        """Play snore sound"""
        self.prime_hub.speaker.beep(60, 0.5)

    def happy(self):
        """Happy behavior
        Assumes puppy is seated"""

        self.self.prime_hub.light_matrix.show_image('MEH')
        for value in range(1, 4):
            #self.legs.drive(-100, 0)
            self.bark()
            wait_for_seconds(.2)
            self.legs.stop()
            wait_for_seconds(.3)
            #self.legs.drive(10, 0)
            wait_for_seconds(.3)
            self.legs.stop()
        self.self.prime_hub.light_matrix.show_image('HAPPY')

    def sleepy(self):
        """Sleepy behavior
        Assumes puppy is seated"""
        self.prime_hub.light_matrix.show_image('ASLEEP')
        self.head.run_time(900, 3000)
        for value in range(1, 3):
            self.snore()
        self.head.run_time(-900, 3000)
        self.prime_hub.light_matrix.show_image('HAPPY')
