import pygame

from Robot.coordinate import Coordinate
from Display.tile import Tile


class Screen():

    def __init__(self, width, height, title):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            pygame.display.update()
            self.clock.tick(60)

    def draw(self, coordinates : Coordinate  ):
        pygame.draw.rect(self.screen, Tile.ROBOT.value, pygame.Rect(coordinates[0].X, coordinates[0].Y, 10, 10))