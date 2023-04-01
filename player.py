import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 50
        self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), self.size)

    def move(self):
        self.y += self.velocity
        self.velocity += 0.5

    def jump(self):
        self.velocity = -10
