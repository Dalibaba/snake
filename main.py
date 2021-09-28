import pygame
import constants
from snake import snake
from food import food
from player import player

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
game_snake = snake.Snake(constants.Window.SCREEN_WIDTH, constants.Window.SCREEN_HEIGHT)
# create food
game_food = food.Food(constants.Window.SCREEN_WIDTH, constants.Window.SCREEN_HEIGHT)
# create player
game_player = player.Player("test")



# Game Loop
running = True
while running:
    # loop trough all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard pressing events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_snake.turn(constants.Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                game_snake.turn(constants.Direction.RIGHT)
            if event.key == pygame.K_DOWN:
                game_snake.turn(constants.Direction.DOWN)
            if event.key == pygame.K_UP:
                game_snake.turn(constants.Direction.UP)
    # background color screen
    screen.fill((constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))

    # display game area
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 50, constants.Window.SCREEN_WIDTH -100, constants.Window.SCREEN_HEIGHT -100),  2)

    # display snake
    for pos in game_snake.block_positions:

        pygame.draw.rect(screen, game_snake.color, (pos[0], pos[1],
                                                      game_snake.size_x, game_snake.size_y))

    # display food
    pygame.draw.rect(screen, game_food.color, (game_food.x, game_food.y,
                                               game_food.size_x, game_food.size_y))

    # if snake eats food, delete food instance
    if game_snake.x == game_food.x and game_snake.y == game_food.y:
        game_food.change_position()
        game_snake.eat()
        game_player.increase_score()

    clock.tick(10)
    game_snake.move()
    pygame.display.update()
