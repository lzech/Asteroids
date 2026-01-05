import pygame
import random
from circleshape import CircleShape
from logger import log_event

from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rnd = random.uniform(20,50)
        vect_1 = self.velocity.rotate(rnd)
        vect_2 = self.velocity.rotate(-rnd)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position[0], self.position[1], new_radius)
        ast_2 = Asteroid(self.position[0], self.position[1], new_radius)
        ast_1.velocity = vect_1*1.2
        ast_2.velocity = vect_2*1.2