import numpy as np
import pygame


class Wheel(pygame.Surface):
    def __init__(self, pos, angle):
        # init the parent and set a set wheel size 20x60
        super().__init__([20, 60], pygame.SRCALPHA)
        
        self.pos = pos
        self.angle = angle

        # render a rect on the wheels surface for rendering
        pygame.draw.rect(self, (150, 150, 150), (0, 0, 20, 60))


class Rover():
    def __init__(self, pos, wheels, max_turn_angle):
        '''
        Initialize the rover's parameters
        pos => rover's position
        wheels => list of wheels (1st 3 on the left, the other 3 on the right side of the rover)
        '''
        
        self.pos = pos
        self.wheels = wheels

        self.max_turn_angle = max_turn_angle
        self.angle = 0

        # get the length and the width of the rover
        self.L = abs(self.wheels[0].pos[1] - self.wheels[2].pos[1])
        self.W = abs(self.wheels[3].pos[0] - self.wheels[0].pos[0])

    
    def turn(self, a):
        '''
        turn the rover by `a` degrees conter clockwise
        '''

        self.angle += a
        if abs(self.angle) > self.max_turn_angle:
            self.angle = (self.angle / abs(self.angle)) * self.max_turn_angle

        # check which way the rover is turning
        if  self.angle > 0:
            # if turning to the left
            self.wheels[0].angle = self.angle
            r1 = self.L / np.tan(np.deg2rad(self.wheels[0].angle))  # Inner radius
    
            # Calculate the outer radius (for outer front wheel)
            r2 = self.L / np.tan(np.deg2rad(self.wheels[0].angle)) + self.W / 2  # Outer radius
            
            # Calculate the outer wheel angle (for outer front wheel)
            self.wheels[3].angle = np.rad2deg(np.arctan(self.L / r2))  # Outer right wheel angle
            
            # Rear wheels (steering in opposite direction for sharper turn)
            self.wheels[2].angle = -self.wheels[0].angle  # Rear left wheel
            self.wheels[5].angle = -self.wheels[3].angle  # Rear right wheel
        elif self.angle < 0:
            # if turning to the right
            self.wheels[3].angle = self.angle
            r1 = self.L / np.tan(np.deg2rad(self.wheels[3].angle))  # Inner radius
    
            # Calculate the outer radius (for outer front wheel)
            r2 = self.L / np.tan(np.deg2rad(self.wheels[3].angle)) - self.W / 2  # Outer radius
            
            # Calculate the outer wheel angle (for outer front wheel)
            self.wheels[0].angle = np.rad2deg(np.arctan(self.L / r2))  # Outer right wheel angle
            
            # Rear wheels (steering in opposite direction for sharper turn)
            self.wheels[2].angle = -self.wheels[0].angle  # Rear left wheel
            self.wheels[5].angle = -self.wheels[3].angle  # Rear right wheel
            

