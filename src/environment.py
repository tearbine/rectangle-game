from force import Force
from math import sin, cos, pi
from gravity import Gravity

class Environment:
    def __init__(self):
        self.things = set()
        self.positions = {}
        self.old_positions = {}
        self.forces = {}
        
    def add(self, thing, position, force=Force(magnitude=0, direction=0)):
        if thing in self.things:
            raise ValueError("This thing is already in the environment")
        
        self.things.add(thing)
        self.positions[thing] = position
        self.forces[thing] = [force]
        
    def remove(self, thing):
        if thing not in self.things:
            raise ValueError("This thing was never in the environment")
        
        self.things.remove(thing)
        del self.positions[thing]
        del self.forces[thing]
        
    def advance(self):
        for thing in self.things:
            forces = self.forces[thing] # get all the forces on a thing
                
            if thing.gravity:
                thing_gravity = Gravity()
                thing_gravity_force = thing_gravity.get_gravity()
                apply_gravity = self.get_controller(thing)
                apply_gravity(thing_gravity_force)
                
            for force in forces:
                x, y = self.positions[thing] # set the position of a thing to x and y (also backup for collision)
                dx = cos(force.direction)*force.magnitude/thing.mass # find the change in x
                dy = sin(force.direction)*force.magnitude/thing.mass # find the change in y
                
                force.magnitude -= .01 # make the magnitude weaker over time
                
                if force.magnitude > thing.speedlimit: # if the force is above thing's speed limit, cap it
                    force.magnitude = thing.speedlimit
                    
                    
                if force.magnitude <= 0: # if the force is 0, remove it
                    forces.remove(force)
                
                
                #----------COLLISION DETECTION AND MOVING-------------------------------------------------------------------------------    
                for thing2 in self.things: # check all objects to see if anything collides
                    if thing.rect != thing2.rect: # if they're the same object
                            
                        self.positions[thing] = x + dx, self.positions[thing][1] # move a coord
                        thing.rect.x = self.positions[thing][0]
                        if thing.rect.colliderect(thing2.rect): # if anything collides after moving x
                            if thing.mass < thing2.mass:
                                self.forces[thing] = []
                                self.positions[thing] = x, self.positions[thing][1]
                                thing.rect.x = self.positions[thing][0]
                                if thing.rect.right < thing2.rect.left:
                                    thing.rect.right = thing2.rect.left
                                if thing.rect.left > thing2.rect.right:
                                    thing.rect.left = thing2.rect.right
                                self.positions[thing] = thing.rect.x, thing.rect.y
                            
                        self.positions[thing] = self.positions[thing][0], y + dy # move a coord
                        thing.rect.y = self.positions[thing][1]
                        if thing.rect.colliderect(thing2.rect): # if anything collides after moving x
                            if hasattr(thing, 'jump_power'):
                                if thing.rect.y < thing2.rect.y:
                                    thing.jump_power = 15
                            if thing.mass < thing2.mass:
                                for force in self.forces[thing]:
                                    if force.direction == pi/2 or force.direction == -pi/2:
                                        force.magnitude = 0
                                self.positions[thing] = self.positions[thing][0], y
                                thing.rect.y = self.positions[thing][1]
                                if thing.rect.bottom < thing2.rect.top:
                                    thing.rect.bottom = thing2.rect.top
                                if thing.rect.top > thing2.rect.bottom:
                                    thing.rect.top = thing2.rect.bottom
                                self.positions[thing] = thing.rect.x, thing.rect.y
                #END COLLISION DETECTION AND MOVING-----------------------------------------------------------------
                                                        
                thing.rect.x, thing.rect.y = self.positions[thing]
                
                
    def get_controller(self, thing):
        if thing not in self.things:
            raise ValueError("Cannot make controller because thing is not in environment")
        def control(new_force):
            if thing not in self.things:
                raise ValueError("Cannot control thing because no longer in environment")
            self.forces[thing].append(new_force)
        return control
            
            