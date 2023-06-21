import pygame

from entity import Entity
from globals import CELL_SIZE

GHOST_WIDTH = int(CELL_SIZE * 0.5)
GHOST_HEIGHT = int(CELL_SIZE * 0.75)

class Ghost(Entity):
    def __init__(self, c, r, speed, color):
        super().__init__(c, r, speed)
        self.color = color

    def draw(self, screen):
        (x, y) = self.get_current_xy()
        pygame.draw.ellipse(screen, self.color, (
            x - GHOST_WIDTH // 2,
            y - GHOST_HEIGHT // 2,
            GHOST_WIDTH,
            GHOST_HEIGHT,
        ))
    
    def on_movement(self, grid):
        # TODO: properly decide the direction
        self.direction = (-1, 0)
