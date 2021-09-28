import pygame
import constants
from snake import snake


# Initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((
    constants.Window.SCREEN_WIDTH,
    constants.Window.SCREEN_HEIGHT,
))

# Title and Icon
pygame.display.set_caption(constants.Window.TITLE)
icon = pygame.image.load("assets/images/snake.png")
pygame.display.set_icon(icon)

# clock
clock = pygame.time.Clock()

# create snake
player_snake = snake.Snake(constants.Window.SCREEN_WIDTH, constants.Window.SCREEN_HEIGHT)

# Game Loop
running = True
while running:
    # loop trough all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background color screen
    screen.fill((constants.Window.COLOR_RED,constants.Window.COLOR_GREEN,constants.Window.COLOR_BLUE))


    # display snake
    pygame.draw.rect(screen, player_snake.color, (player_snake.x, player_snake.y,
                                                  player_snake.size_x, player_snake.size_y))


    clock.tick(1)
    player_snake.move()
    print(player_snake.x)
    pygame.display.update()
