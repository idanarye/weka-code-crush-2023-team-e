import pygame

from grid import Grid
from pacman import Pacman

class GameLoop:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        self.grid = Grid(20, 10)
        self.pacman = Pacman(1, 1, 1)

    def run_loop(self):
        while self.running:
            self.run_frame()

    def run_frame(self):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        for key, direction in [
                (pygame.K_UP, (0, -1)),
                (pygame.K_DOWN, (0, 1)),
                (pygame.K_LEFT, (-1, 0)),
                (pygame.K_RIGHT, (1, 0)),
        ]:
            if keys[key]:
                self.pacman.direction = direction

        for entity in self.iter_entities():
            entity.move(self.grid, self.clock.get_time())

        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("purple")

        self.grid.draw(self.screen)
        self.draw_entities()
        # flip() the display to put your work on screen
        pygame.display.flip()

        self.clock.tick(60)  # limits FPS to 60

    def draw_entities(self):
        self.pacman.draw(self.screen)

    def iter_entities(self):
        yield self.pacman