from abc import ABCMeta, abstractmethod

import pygame

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
        self.movement_progress = 0.0

    def move(self, grid, frame_duration):
        self.movement_progress += frame_duration * self.speed
        if 1.0 <= self.movement_progress:
            self.movement_progress = 0.0

            def calc_with_wrap(coord, size):
                if coord < 0:
                    return size - 1
                elif size <= coord:
                    return 0
                else:
                    return coord

            self.current = (
                calc_with_wrap(self.next[0], NUM_COLS),
                calc_with_wrap(self.next[1], NUM_ROWS),
            )

            self.next = tuple(c + d for c, d in zip(self.current, self.direction))
            self.on_movement(grid)


    def get_current_xy(self):
        def calc(cur, nex):
            return int(CELL_SIZE / 2 + (cur + (nex - cur) * self.movement_progress) * CELL_SIZE)
        x = calc(self.current[0], self.next[0])
        y = calc(self.current[1], self.next[1])
        return (x, y)

    @abstractmethod
    def draw(self, screen):
        pass
    
    @abstractmethod
    def on_movement():
        pass
