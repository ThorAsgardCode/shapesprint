import pygame

class Pipe:
    def __init__(self, x, y, gap_size):
        self.x = x
        self.y = y
        self.width = 70
        self.height = screen_height - y - gap_size

    def draw(self, screen):
        top_rect = pygame.Rect(self.x, 0, self.width, self.y)
        bottom_rect = pygame.Rect(self.x, self.y + gap_size, self.width, self.height)
        pygame.draw.rect(screen, (0, 255, 0), top_rect)
        pygame.draw.rect(screen, (0, 255, 0), bottom_rect)

    def move(self):
        self.x -= 5

    def collision(self, player):
        player_rect = pygame.Rect(player.x - player.size // 2, player.y - player.size // 2, player.size, player.size)
        top_rect = pygame.Rect(self.x, 0, self.width, self.y)
        bottom_rect = pygame.Rect(self.x, self.y + gap_size, self.width, self.height)
        if player_rect.colliderect(top_rect) or player_rect.colliderect(bottom_rect):
            return True
        return False
