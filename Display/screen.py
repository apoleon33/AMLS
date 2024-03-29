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
        touches = pygame.key.get_pressed()
        if touches[pygame.K_d]:
            coordinates.X += 1
        elif touches[pygame.K_a]:
            coordinates.X -= 1
        if touches[pygame.K_w]:
            coordinates.Y -= 1
        elif touches[pygame.K_s]:
            coordinates.Y += 1
        pygame.draw.rect(self.screen, Tile.ROBOT.value, pygame.Rect(coordinates.X, coordinates.Y, 10, 10))