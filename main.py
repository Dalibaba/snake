import pygame
import constants

# Initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((
    constants.Window.SCREEN_HEIGHT,
    constants.Window.SCREEN_WIDTH,
))

# Title and Icon
pygame.display.set_caption(constants.Window.TITLE)
icon = pygame.image.load("assets/images/snake.png")
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    # loop trough all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((constants.Window.COLOR_RED,constants.Window.COLOR_GREEN,constants.Window.COLOR_BLUE))
    pygame.display.update()
