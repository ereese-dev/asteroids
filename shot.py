import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        self.width = 2
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt