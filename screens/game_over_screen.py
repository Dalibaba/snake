import pygame

import constants

# Snake image
from screens import fonts

snake_image = pygame.image.load("assets/images/snake_frontal.png")
snake_image = pygame.transform.scale(snake_image, (300, 300))


def show(screen, clock):

    # Text font
    font = fonts.text()
    # Game over font
    game_over_font = fonts.game_over()


    # fill background with black
    screen.fill((0, 0, 0))

    # display snake image
    rect = snake_image.get_rect()
    rect = rect.move((constants.Window.SCREEN_WIDTH / 4, 50))
    screen.blit(snake_image, rect)

    game_over_text = game_over_font.render("GAME OVER", True, (
    constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = game_over_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 1.5))
    screen.blit(game_over_text, text_rect)

    type_your_name_text = font.render("PRESS ENTER TO PLAY AGAIN", True, (
    constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = type_your_name_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 1.2))
    screen.blit(type_your_name_text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(constants.Game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    waiting = False


