from force import Force
from math import sin, cos, pi
from gravity import Gravity
from constants import *

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
                
            dx = 0
            dy = 0    
            for force in forces:
                x, y = self.positions[thing] # set the position of a thing to x and y (also backup for collision)
                mod_x = cos(force.direction)*force.magnitude # find the change in x
                mod_y = sin(force.direction)*force.magnitude # find the change in y
                dx += mod_x
                dy += mod_y
                
            for force in forces:
                for direction in thing.speed_decay:
                    if force.direction == direction:
                        force.magnitude -= thing.speed_decay[direction]
                        if force.magnitude >= thing.speedlimit[direction]:
                            force.magnitude = thing.speedlimit[direction]
                            thing.speed_decay[direction] = .1         
                if abs(dx) > thing.speedlimit[LEFT]:
                    if dx < 0:
                        dx = -thing.speedlimit[LEFT]
                        thing.speed_decay[LEFT] = 1
                    else:
                        dx = thing.speedlimit[RIGHT]
                        thing.speed_decay[RIGHT] = 1
                        
                if abs(dy) > thing.speedlimit[UP]:
                    if dy < 0:
                        dy = -thing.speedlimit[UP]
                        thing.speed_decay[UP] = 100
                    else:
                        dy = thing.speedlimit[DOWN]
                        thing.speed_decay[DOWN] = .01
                
                
                    
                if force.magnitude <= 0: # if the force is 0, remove it
                    forces.remove(force)
                
                #----------COLLISION DETECTION AND MOVING-------------------------------------------------------------------------------       
                

                thing.colliding = False
                
                self.positions[thing] = x + dx, self.positions[thing][1] # move x
                thing.rect.x = self.positions[thing][0]
                for thing2 in self.things:
                    if thing.rect.colliderect(thing2.rect): # if anything collides after moving x
                        if thing != thing2:
                            thing.colliding = True                          
                            if hasattr(thing, 'walljump_power_right'):
                                if thing.rect.x > thing2.rect.x:
                                    thing.walljump_power_right = 15
                                    thing.walljump_power_left = 0
                                if thing.rect.x < thing2.rect.x:
                                    thing.walljump_power_left = 15
                                    thing.walljump_power_right = 0
                                thing.jump_power2 = 15
                                
                            self.forces[thing] = []
                            self.positions[thing] = x, self.positions[thing][1]
                            thing.rect.x = self.positions[thing][0]
                            if thing.rect.right < thing2.rect.left:
                                thing.rect.right = thing2.rect.left
                            if thing.rect.left > thing2.rect.right:
                                thing.rect.left = thing2.rect.right
                
                self.positions[thing] = self.positions[thing][0], y + dy # move y
                thing.rect.y = self.positions[thing][1]
                for thing2 in self.things:
                    if thing.rect.colliderect(thing2.rect): # if anything collides after moving y
                        if thing != thing2:
                            thing.colliding = True
                            if hasattr(thing, 'jump_power'):
                                if thing.rect.y < thing2.rect.y:
                                    thing.jump_power = 20
                                    thing.jump_power2 = 20

                            
                            for force in self.forces[thing]:
                                if force.direction == pi/2 or force.direction == -pi/2:
                                    force.magnitude = 0
                            self.positions[thing] = self.positions[thing][0], y
                            thing.rect.y = self.positions[thing][1]
                            if thing.rect.bottom < thing2.rect.top:
                                thing.rect.bottom = thing2.rect.top
                            if thing.rect.top > thing2.rect.bottom:
                                thing.rect.top = thing2.rect.bottom
                            
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
            
            