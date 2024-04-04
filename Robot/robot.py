from Robot.api import Api
from Robot.coordinate import Coordinate


class Robot:
    __coordinates: [Coordinate]
    __api: Api

    def __init__(self, x: int, y: int, api: Api):
        self.__coordinates = []
        self.__coordinates.append(Coordinate(x, y))
        self.__api = api

    def getCoordinate(self) -> Coordinate:
        print(self.__coordinates)
        return self.__coordinates

    def updateCoordinate(self):
        newCoordinate = self.__api.receive("")

        if newCoordinate["success"]:  # on a bien reçu des coordonnées
            self.addCoordinate(newCoordinate["x"], newCoordinate["y"])

    def addCoordinate(self, x: int, y: int):
        self.__coordinates.append(Coordinate(x, y))
        coordinates = self.__api.receive("")
        self.addCoordinate(coordinates['x'], coordinates['y'])

    def addCoordinate(self, x: int, y: int):
        self.__coordinates.append(Coordinate(x, y))
