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

    def draw(self, coordinates : Coordinate ):
        for i in range(len(coordinates)):
            if pygame.draw.rect(self.screen, Tile.ROBOT.value, pygame.Rect(coordinates[i].X, coordinates[i].Y, 10, 10)):
                pygame.draw.rect(self.screen, Tile.LASTCOORDINATE.value, pygame.Rect(coordinates[i-1].X, coordinates[i-1].Y, 10, 10))
            if i >= 1:
                pygame.draw.line(self.screen, Tile.TRACK.value, (coordinates[i].X+5, coordinates[i].Y+10), (coordinates[i-1].X+5, coordinates[i-1].Y), 3)
