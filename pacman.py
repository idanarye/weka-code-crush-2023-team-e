import pygame

from entity import Entity

from globals import CELL_SIZE

class Pacman(Entity):
    def draw(self, screen):
        pygame.draw.circle(screen, 'yellow', self.get_current_xy(), 35)
