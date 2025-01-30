import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (40, 40))

# Game variables
bird_x = 50
bird_y = 300
bird_y_change = 0

gravity = 0.5
flap_strength = -10

pipe_width = 70
pipe_gap = 150
pipe_x = SCREEN_WIDTH
pipe_height = random.randint(100, 400)
pipe_speed = 3

score = 0
font = pygame.font.Font(None, 36)

# Function to check for collisions
def is_collision(bird_y, pipe_x, pipe_height):
    if bird_y > SCREEN_HEIGHT or bird_y < 0:
        return True
    if pipe_x < bird_x + 40 < pipe_x + pipe_width:
        if bird_y < pipe_height or bird_y > pipe_height + pipe_gap:
            return True
    return False

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = flap_strength

    bird_y_change += gravity
    bird_y += bird_y_change

    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = SCREEN_WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    screen.fill(WHITE)
    screen.blit(bird_img, (bird_x, bird_y))

    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT))

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    if is_collision(bird_y, pipe_x, pipe_height):
        running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()