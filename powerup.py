import pygame

class PowerUp:
    def __init__(self, x, y, power):
        self.x = x
        self.y = y
        self.power = power
        self.size = 20

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size)

    def move(self):
        self.x -= 5

    def collision(self, player):
        player_rect = pygame.Rect(player.x - player.size // 2, player.y - player.size // 2, player.size, player.size)
        powerup_rect = pygame.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size)
        if player_rect.colliderect(powerup_rect):
            return True
        return False
