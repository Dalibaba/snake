import pygame

import constants

# Snake image
from screens import fonts
from services.database_service import database


def show(screen, clock):
    # Initialize database
    db = database()

    # fetch highscore
    highscore = db.get_highscore()
    print(highscore)
    print(type(highscore))
    # Text font
    font = fonts.text()
    # Game over font
    game_over_font = fonts.game_over()
    # highscore text font
    font_highscore = fonts.text_highscore()

    # fill background with black
    screen.fill((0, 0, 0))

    game_over_text = game_over_font.render("GAME OVER", True, (
        constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = game_over_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 10))
    screen.blit(game_over_text, text_rect)

    type_your_name_text = font.render("HIGHSCORE", True, (
        constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = type_your_name_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 5))
    screen.blit(type_your_name_text, text_rect)

    # display highscore
    add = 10
    for element in highscore:

        name_length = len(element["name"])
        player_name = element["name"]
        player_score = str(element["score"])
        score_length = len(player_score)
        for i in range(0, (6 - name_length)):
            player_name = player_name + " "
        for i in range(0, (6 - score_length)):
            player_score = "0" + player_score

        string_name = player_name
        highscore_element = font_highscore.render(string_name, True, (
            constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
        text_rect = highscore_element.get_rect(
            center=(constants.Window.SCREEN_WIDTH / 3, (constants.Window.SCREEN_HEIGHT / 4) + add), )
        screen.blit(highscore_element, text_rect)

        string_score = player_score
        highscore_element = font_highscore.render(string_score, True, (
            constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
        text_rect = highscore_element.get_rect(
            center=(constants.Window.SCREEN_WIDTH / 1.5, (constants.Window.SCREEN_HEIGHT / 4) + add), )
        screen.blit(highscore_element, text_rect)
        add += 40

    type_your_name_text = font.render("PRESS ENTER TO PLAY AGAIN", True, (
        constants.Window.COLOR_RED, constants.Window.COLOR_GREEN, constants.Window.COLOR_BLUE))
    text_rect = type_your_name_text.get_rect(
        center=(constants.Window.SCREEN_WIDTH / 2, constants.Window.SCREEN_HEIGHT / 1.05))
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
