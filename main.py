import pygame
import time

from Robot.api import Api
from Robot.robot import Robot
from Display.screen import Screen
from Display.tile import Tile

screen1 = Screen(800, 600, "Robot Cartographer")
robotTest = Robot(Api("http://192.168.4.1"))


#robotTest.updateCoordinate()a

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    time.sleep(0.5)
    robotTest.updateCoordinate()
    time.sleep(0.5)


    screen1.screen.fill(Tile.EMPTY.value)  # Remplir l'écran avec la couleur de la tuile VIDE
    screen1.draw(robotTest.getCoordinate())  # Dessiner le robot à ses coordonnées actuelles
    pygame.display.update()  # Mettre à jour l'affichage
    screen1.clock.tick(60)  # Limiter à 60 images par seconde

