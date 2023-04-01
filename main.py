import pygame
import random

pygame.init()
screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
player_size = 50
player_pos = [screen_width // 2, screen_height // 2]

def draw_player():
    pygame.draw.circle(screen, (255, 255, 0), player_pos, player_size)

pipe_width = 70
pipe_gap = 150
pipe_list = []


class Pipe:
    def __init__(self, gap_position):
        self.x = screen_width
        self.gap_size = 200  # set the size of the gap between the top and bottom pipes
        self.top_height = gap_position
        self.bottom_height = screen_height - gap_position - self.gap_size
        self.top_rect = pygame.Rect(self.x, 0, pipe_width, self.top_height)
        self.bottom_rect = pygame.Rect(self.x, self.top_height + self.gap_size, pipe_width, self.bottom_height)

    def move(self):
        self.x -= 5
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.top_rect)
        pygame.draw.rect(screen, (0, 255, 0), self.bottom_rect)

    def collision(self, player_pos):
        if self.top_rect.collidepoint(player_pos) or self.bottom_rect.collidepoint(player_pos):
            # check if the player is inside the gap between the pipes
            if player_pos[1] >= self.top_height and player_pos[1] <= self.top_height + self.gap_size:
                return False
            return True
        return False



def create_pipe():
    last_pipe = pipe_list[-1] if len(pipe_list) > 0 else None
    if last_pipe is None or last_pipe.x < screen_width - pipe_gap:
        gap_position = random.randint(100, screen_height - 100 - pipe_gap)
        pipe_list.append(Pipe(gap_position))


def draw_pipes():
    for pipe in pipe_list:
        pipe.draw()

def move_pipes():
    for pipe in pipe_list:
        pipe.move()
        if pipe.x < -pipe_width:
            pipe_list.remove(pipe)

score = 0
score_font = pygame.font.Font(None, 50)

def display_score():
    score_surface = score_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_surface, (screen_width // 2 - score_surface.get_width() // 2, 50))

def update_score():
    global score
    for pipe in pipe_list:
        if pipe.x + pipe_width < player_pos[0] < pipe.x + pipe_width + 5:
            score += 1


game_over_font = pygame.font.Font(None, 70)

def game_over():
    game_over_surface = game_over_font.render("GAME OVER", True, (255, 255, 255))
    score_surface = score_font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(game_over_surface, (screen_width // 2 - game_over_surface.get_width() // 2, screen_height // 2 - game_over_surface.get_height() // 2))
    screen.blit(score_surface, (screen_width // 2 - score_surface.get_width() // 2, screen_height // 2 + game_over_surface.get_height() // 2 + 50))
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_pos[1] -= player_size
            if event.key == pygame.K_DOWN:
                player_pos[1] += player_size

    screen.fill((0, 0, 0))

    create_pipe()
    move_pipes()
    draw_pipes()

    draw_player()

    display_score()
    update_score()

    if any(pipe.collision(player_pos) for pipe in pipe_list):
        game_over()
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    pygame.display.update()
    pygame.time.Clock().tick(30)
