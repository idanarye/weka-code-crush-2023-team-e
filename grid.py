from enum import Enum

import pygame

from globals import CELL_SIZE

class CellContent(Enum):
    Empty = 0
    Wall = 1
    Dot = 2
    Powerup = 3

    def draw(self, screen, x, y):
        if self == CellContent.Dot:
            pygame.draw.circle(screen, 'white', (x, y), 5)
        elif self == CellContent.Powerup:
            pygame.draw.circle(screen, 'white', (x, y), 10)
        elif self == CellContent.Wall:
            pygame.draw.rect(screen, 'blue', (x - CELL_SIZE // 2, y - CELL_SIZE // 2, CELL_SIZE, CELL_SIZE))


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # it's all dots for now. We'll change it later
        self.cells = [[CellContent.Dot for _ in range(height)] for _ in range(width)]
        self.cells[2][2] = CellContent.Powerup
        self.cells[2][3] = CellContent.Wall
        self.cells[3][3] = CellContent.Wall
        self.cells[2][4] = CellContent.Empty
        self.cells[2][5] = CellContent.Empty
        self.cells[2][6] = CellContent.Empty

    def draw(self, screen):
        for col, col_cells in enumerate(self.cells):
            x = CELL_SIZE // 2 + col * CELL_SIZE
            for row, cell in enumerate(col_cells):
                y = CELL_SIZE // 2 + row * CELL_SIZE
                cell.draw(screen, x, y)

    
    def get_cell(self, c, r):
        return self.cells[c][r]

    def set_cell(self, c, r,new_content):
        self.cells[c][r] = new_content

