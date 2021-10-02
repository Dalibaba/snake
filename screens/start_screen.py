import pygame


import constants

# Snake image
from screens import fonts

snake_image = pygame.image.load("assets/images/snake_frontal.png")
snake_image = pygame.transform.scale(snake_image, (300, 300))


def show(screen, clock):

    # Score font
    font = fonts.text()
    # Game over font
    game_over_font = fonts.game_over()

    # fill background with black
    screen.fill((0, 0, 0))

    # display snake image
    rect = snake_image.get_rect()
    rect = rect.move((constants.Window.SCREEN_WIDTH / 4, 50))
    screen.blit(snake_image, rect)


    game_over_text = font.render("ENTER NAME", True, (
        constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = game_over_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 1.5))
    screen.blit(game_over_text, text_rect)

    type_your_name_text = font.render("PRESS ENTER", True, (
        constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = type_your_name_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 1.15))
    screen.blit(type_your_name_text, text_rect)

    type_your_name_text = font.render("HIGHSCORE", True, (
        constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = type_your_name_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 1.05))
    screen.blit(type_your_name_text, text_rect)


    # text input
    user_input = ""
    # create rectangle
    input_rect = pygame.Rect(0,0,10,10)
    input_rect.center = ((constants.Window.SCREEN_WIDTH / 4, constants.Window.SCREEN_HEIGHT / 1.4))
    pygame.display.flip()
    waiting = True


    while waiting:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_input = user_input[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_input += event.unicode
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        waiting = False
            # draw rectangle and argument passed which should
            # be on screen
            pygame.draw.rect(screen, (0,0,0), input_rect)
            text_surface = game_over_font.render(user_input, True, constants.Color.PRIMARY)
            # render at position stated in arguments
            screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            # set width of textfield so that text cannot get
            # outside of user's text input
            input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()
