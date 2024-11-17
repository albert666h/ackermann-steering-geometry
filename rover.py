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
    def __init__(self, pos, wheels):
        '''
        Initialize the rover's parameters
        pos => rover's position
        wheels => list of wheels
        '''
        
        self.pos = pos
        self.wheels = wheels

