import pygame
import constants


def text():
    font = pygame.font.Font('freesansbold.ttf', constants.Fonts.TEXT)
    return font


def game_over():
    font = pygame.font.Font('freesansbold.ttf', constants.Fonts.GAME_OVER)
    return font
