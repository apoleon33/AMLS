from Robot.api import Api
from Robot.coordinate import Coordinate


class Robot():
    __coordinates: Coordinate
    __api: Api

    def __init__(self, x: int, y: int, api: Api):
        self.__coordinates = Coordinate(x, y)
        self.__api = api

    def getCoordinate(self) -> Coordinate:
        return self.__coordinates

    def updateCoordinate(self):
        pass
