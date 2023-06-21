import pygame

from grid import Grid
from pacman import Pacman
from ghost import Ghost
from globals import NUM_COLS, NUM_ROWS, CELL_SIZE

class GameLoop:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

        self.grid = Grid(NUM_COLS, NUM_ROWS)
        self.pacman = Pacman(1, 1, 1)
        self.ghosts = [
            Ghost(5, 1, 1, 'green'),
        ]

    def run_loop(self):
        while self.running:
            self.run_frame()

    def run_frame(self):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Move Packman in case of arrow press
        keys = pygame.key.get_pressed()
        for key, direction in [
                (pygame.K_UP, (0, -1)),
                (pygame.K_DOWN, (0, 1)),
                (pygame.K_LEFT, (-1, 0)),
                (pygame.K_RIGHT, (1, 0)),
        ]:
            if keys[key]:
                self.pacman.direction = direction

        # Exit in case of ESCAPE press
        if keys[pygame.K_ESCAPE]:
            self.running = False

        if self.game_over:
            pygame.display.set_caption(f"Game Over. Score: {self.pacman.score}")
        else:
            for entity in self.iter_entities():
                entity.move(self.grid, self.clock.get_time())

            pygame.display.set_caption(f"Score: {self.pacman.score}")

        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("purple")

        self.grid.draw(self.screen)
        for entity in self.iter_entities():
            entity.draw(self.screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        if self.is_game_over():
            self.game_over = True

        self.clock.tick(60)  # limits FPS to 60

    def iter_entities(self):
        yield self.pacman
        yield from self.ghosts

    def is_game_over(self):
        pacman_xy = self.pacman.get_current_xy()
        for ghost in self.ghosts:
            if all(
                    abs(pacman_coord - ghost_coord) <= CELL_SIZE // 2
                    for pacman_coord, ghost_coord in zip(pacman_xy, ghost.get_current_xy())
            ):
                return True
        return False
