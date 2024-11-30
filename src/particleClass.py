# Import libraries
import pygame
import random

class Particle:

    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.size = 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size)

def createParticles