from spike import PrimeHub, DistanceSensor
import hub
class PuppyTraining:
    def __init__(self, dsPort):
        self.prime_hub = PrimeHub()
        self.hub.speaker.beep(72,0.5)
        self.hand_distance = DistanceSensor(dsPort)
        self.boundary = None  # Initial Decision boundary
        self.ATraining = []  # Initial A examples
        self.BTraining = []  # Initial B example
        self.averageA = None  # Initial average for the A training
        self.averageB = None  # Initial average for the B training
        
    def observation(self):
        print('Press up or down button to tell the puppy which command you are demonstrating Press the center to stop training')
        print("Press up or down button to give example.")
        print("Press center to exit")
        while True: 
            if hub.button.left.is_pressed():
                hand_distance = self.distanceSensor.get_distance_cm()
                dog_command = 'A'
                print('Puppy learns that this means command A')
                self.hub.speaker.beep(72,0.5)
                self.ATraining.append(force)
                wait(100)
                return force, dog_command
            elif hub.button.right.is_pressed():
                force = self.forceSensor.get_force_newton()
                dog_command = 'B'
                print('Puppy learns that this means command B')
                self.hub.speaker.beep(72,0.5)
                self.BTraining.append(force)
                wait(100)
                return force, dog_command
            elif hub.button.center.is_pressed():
                force = 0
                dog_command = 'Exit'
                self.hub.speaker.beep(72,0.5)
                print('Puppy is done training for now.')
                return angle, dog_command
            
            def watch(self):
        '''Adds multiple training observations to the training data
        Puppy watches for commands until the center button is pressed'''
        command = ""
        print('Puppy is ready to start learning!')
        while (hub.button.center.is_pressed() not True) and command != "Exit":
            # Repeat observations until the center button is pressed
            distance, command = self.observation()
        print('Training Over.')
        
    def train(self):
        '''Calculate the means and decision boundary
        between two labelled clusters'''
        sumA = 0
        sumB = 0
        # Calculate totals
        for observation in self.ATraining:
            sumA += observation  # Totals all A Training examples
        for observation in self.BTraining:
            sumB += observation  # Totals all B Training examples
        # Calculate averages
        self.averageA = sumA/len(self.ATraining)  # Finds mean of A commands
        self.averageB = sumB/len(self.BTraining)  # Finds mean of B commands
        # +++ If you are creating additional commands, be sure to calculate
        #       the new totals and averages too!
        # The decision boundary is halfway between the A and B means.
        self.boundary = (self.averageA + self.averageB)/2
        return self.boundary
        
    def difference(self, distance, command):
        '''Calculates the one dimensional distance between
        the current eangl and given command average'''
        if command == 'A':
            return abs(distance - self.averageA)
        elif command == 'B':
            return abs(distance - self.averageB)
        else:
            # +++ You can add distance calculations for more commands here.
            return 1000
            
    def prediction(self, showresult=True):
        '''Calculate the current prediction of the current Gyro angle based on
        the training and classifies based on the minimum-distance-to-mean'''
        distance = self.distanceSensor.get_distance_cm()
        if self.difference(distance, 'B') >= self.difference(distance, 'A'):
            # If the current angle is closer to A, predict it is A.
            prediction = 'A'
        elif self.difference(distance, 'B') < self.difference(distance, 'A'):
            # If the current angle is closer to B, predict it is B.
            prediction = 'B'
        else:
            pass  # +++ You can add additional commands here.
        if showresult:  # Optionally print the prediction result.
            print('The puppy thinks that is a ' + prediction + ' command!')
        return prediction
        
    def report(self):
        '''Prints out the current state of the model'''
        tablewidth = 20  # Adjust this constant to change table width
        print("The Puppy Training Report")
        print("*"*tablewidth)
        print("These are the examples of command A: \n", self.ATraining)
        print("The average is %.2f" % self.averageA)
        print("*"*tablewidth)
        print("These are the examples of command B: \n", self.BTraining)
        print("The average is %.2f" % self.averageB)
        print("*"*tablewidth)
        print('The decision boundary is: ', self.boundary)
        print("*"*tablewidth)
        
    def forget(self):
        '''Reset the training data and the model'''
        self.boundary = None  # Reset Decision boundary
        self.angledata = []  # Reset observation measurements
        self.commanddata = []  # Reset observation labels
        self.averageA = None  # Reset average for the A training
        self.averageB = None  # Reset average for the B training
        # +++ If you added an extra command, be sure to reset it here too!
        print('The puppy has forgotten the training!')mand == 'B':
    #         return abs(angle - self.averageB)
    #     else:
    #         # +++ You can add distance calculations for more commands here.
    #         return 1000

    # def prediction(self, showresult=True):
    #     """Calculate the current prediction of the current Gyro angle based on
    #     the training and classifies based on the minimum-distance-to-mean"""
    #     angle = self.gyro.angle()
    #     if self.distance(angle, 'B') >= self.distance(angle, 'A'):
    #         # If the current angle is closer to A, predict it is A.
    #         prediction = 'A'
    #     elif self.distance(angle, 'B') < self.distance(angle, 'A'):
    #         # If the current angle is closer to B, predict it is B.
    #         prediction = 'B'
    #     else:
    #         pass  # +++ You can add additional commands here.

    #     if showresult:  # Optionally print the prediction result.
    #         print('The puppy thinks that is a ' + prediction + ' command!')
    #     return prediction

    # def report(self):
    #     """Prints out the current state of the model"""
    #     tablewidth = 20  # Adjust this constant to change table width
    #     print("The Puppy Training Report")
    #     print("*"*tablewidth)
    #     print("These are the examples of command A: \n", self.ATraining)
    #     print("The average is %.2f" % self.averageA)
    #     print("*"*tablewidth)
    #     print("These are the examples of command B: \n", self.BTraining)
    #     print("The average is %.2f" % self.averageB)
    #     print("*"*tablewidth)
    #     print('The decision boundary is: ', self.boundary)
    #     print("*"*tablewidth)

    # def forget(self):
    #     """Reset the training data and the model"""
    #     self.boundary = None  # Reset Decision boundary
    #     self.angledata = []  # Reset observation measurements
    #     self.commanddata = []  # Reset observation labels
    #     self.averageA = None  # Reset average for the A training
    #     self.averageB = None  # Reset average for the B training
    #     # +++ If you added an extra command, be sure to reset it here too!
    #     print('The puppy has forgotten the training!')
