from abc import ABCMeta, abstractmethod

import pygame

from grid import CellContent
from globals import CELL_SIZE, NUM_COLS, NUM_ROWS

class Entity(metaclass=ABCMeta):
    """
    Represents both pacman and the ghosts - something that can move
    """
    def __init__(self, c, r, speed):
        self.current = (c, r)
        self.next = (c, r)
        self.speed = speed * 0.001
        self.direction = (0, 0)
        self.ongoing_direction = (0, 0)  # this should not be changed mid-step
        self.movement_progress = 0.0

    def move(self, grid, frame_duration):
        self.movement_progress += frame_duration * self.speed
        if 1.0 <= self.movement_progress:
            self.movement_progress = 0.0
            self.ongoing_direction = self.direction

            self.current = self.next

            def calc_with_wrap(coord, direction, size):
                next_coord = coord + direction
                if next_coord < 0:
                    return size - 1
                elif size <= next_coord:
                    return 0
                else:
                    return next_coord

            self.next = tuple(calc_with_wrap(*args) for args in zip(self.current, self.ongoing_direction, [NUM_COLS, NUM_ROWS]))
            if grid.get_cell(*self.next) == CellContent.Wall:
                self.ongoing_direction = (0, 0)
                self.next = self.current

            self.on_movement(grid)


    def get_current_xy(self):
        return tuple(
            int(CELL_SIZE / 2 + (coord + direction * self.movement_progress) * CELL_SIZE)
            for coord, direction in zip(self.current, self.ongoing_direction)
        )

    @abstractmethod
    def draw(self, screen):
        pass
    
    @abstractmethod
    def on_movement():
        pass
