from force import Force
from math import pi

class Gravity(Force):
    def __init__(self):
        self.gravity_strength = 3.0
        self.gravity_direction = -pi/2
    
    def get_gravity(self):
        return Force(self.gravity_strength, self.gravity_direction)