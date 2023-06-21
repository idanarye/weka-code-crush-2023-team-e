from enum import Enum

import pygame

from globals import *

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

        holes_up = (3,16)
        holes_side = (3,6)
        def draw_walls():
            for cell in range(NUM_ROWS):
                if cell not in (holes_side):
                    self.cells[0][cell] = CellContent.Wall
                    self.cells[NUM_COLS-1][cell] = CellContent.Wall

            for cell in range(NUM_COLS):
                if cell not in (holes_up):
                    self.cells[cell][0] = CellContent.Wall
                    self.cells[cell][NUM_ROWS-1] = CellContent.Wall


            self.cells[2][3] = CellContent.Wall
            self.cells[2][4] = CellContent.Wall
            self.cells[2][5] = CellContent.Wall

            self.cells[3][5] = CellContent.Wall

            self.cells[4][3] = CellContent.Wall
            self.cells[4][4] = CellContent.Wall
            self.cells[4][5] = CellContent.Wall

            self.cells[5][5] = CellContent.Wall

            self.cells[6][3] = CellContent.Wall
            self.cells[6][4] = CellContent.Wall
            self.cells[6][5] = CellContent.Wall

            # self.cells[7][2] = CellContent.Wall
            # self.cells[8][2] = CellContent.Wall
            # self.cells[9][2] = CellContent.Wall

        draw_walls()
        self.cells[2][2] = CellContent.Powerup
        self.cells[7][2] = CellContent.Powerup
        self.cells[6][6] = CellContent.Powerup

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

