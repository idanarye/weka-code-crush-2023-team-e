#!/usr/bin/python3

# Example file showing a basic pygame "game loop"
import pygame

from globals import SCREEN_WIDTH, SCREEN_HEIGHT
from gameloop import GameLoop

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_loop = GameLoop(screen)

game_loop.run_loop()

pygame.quit()
