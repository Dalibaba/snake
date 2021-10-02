import pygame
from pygame import mixer

import constants
from services.database_service import database
from snake import snake
from food import food
from player import player

from screens import start_screen
from screens import game_over_screen
# Initialize pygame
pygame.init()

# Initialize database
db = database()

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

# define game area
game_area_width = constants.Window.SCREEN_WIDTH - 100
game_area_height = constants.Window.SCREEN_WIDTH - 100
game_area_width_offset = 50
game_area_height_offset = 50

# coordinates range for creating snake and food
min_x = game_area_width_offset
max_x = game_area_width_offset + game_area_width
min_y = game_area_width_offset
max_y = game_area_width_offset + game_area_height

# create snake
game_snake = snake.Snake(min_x, max_x, min_y, max_y)
# create food
game_food = food.Food(min_x, max_x, min_y, max_y)
# create player
game_player = player.Player()

# Score font
font = pygame.font.Font('freesansbold.ttf', 22)
score_x = (constants.Window.SCREEN_WIDTH / 2) - 50
score_y = min_y - 25

# Game over font
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# Sound
losing_sound = mixer.Sound("assets/sounds/losing.wav")
eating_sound = mixer.Sound("assets/sounds/eating.wav")

# Snake image
snake_image = pygame.image.load("assets/images/snake_frontal.png")
snake_image = pygame.transform.scale(snake_image, (300, 300))



# Game Loop
running = True
game_over = False
game_start = True
while running:
    if game_start:
        player_name = start_screen.show(screen, clock)
        game_player.name = player_name
        game_start = False

    if game_over:
        game_over_screen.show(screen, clock)
        game_snake.reset(min_x, max_x, min_y, max_y)
        game_player.reset()
        game_over = False
        game_start = True

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
    pygame.draw.rect(screen, (0, 0, 0),
                     pygame.Rect(game_area_width_offset, game_area_height_offset, game_area_width, game_area_height), 2)

    # display snake
    for pos in game_snake.block_positions:
        pygame.draw.rect(screen, game_snake.color, (pos[0], pos[1],
                                                    game_snake.size_x, game_snake.size_y))

    # display food
    pygame.draw.rect(screen, game_food.color, (game_food.x, game_food.y,
                                               game_food.size_x, game_food.size_y))

    # if snake eats food, delete food instance
    if game_snake.x == game_food.x and game_snake.y == game_food.y:
        eating_sound.play()
        game_food.change_position()
        game_snake.eat()
        game_player.increase_score()

    # if snake touches borders or itself, it's game over
    if game_snake.x == min_x or game_snake.y == min_y - 10 or game_snake.x == max_x or game_snake.y == max_y:
        losing_sound.play()
        # insert score to database
        db.insert(game_player.name, game_player.score)
        game_over = True

    for i, pos in enumerate(game_snake.block_positions):
        if game_snake.x == pos[0] and game_snake.y == pos[1] and i > 1:
            losing_sound.play()
            game_over = True

    score = font.render("Score :" + str(game_player.score), True, (0, 0, 0,))
    screen.blit(score, (score_x, score_y))
    clock.tick(constants.Game.FPS)
    game_snake.move()
    pygame.display.update()
