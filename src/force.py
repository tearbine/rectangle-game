class Force:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction
        
    def __repr__(self):
        return 'Force: ' + str(self.magnitude) + ' magnitude, ' +  str(self.direction) + ' direction'