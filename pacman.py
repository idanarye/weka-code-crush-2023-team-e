import pygame

from entity import Entity

from globals import CELL_SIZE

from grid import CellContent

class Pacman(Entity):
    score = 0

    def draw(self, screen):
        pygame.draw.circle(screen, 'yellow', self.get_current_xy(), 35)

    def on_movement(self, grid):
        # IN case pacman ate a dot - clrean cell
        if grid.get_cell(*self.current) == CellContent.Dot:
            grid.set_cell(*self.current, CellContent.Empty)
            self.score += 1
