from Robot.coordinate import Coordinate


class Robot():
    __coordinates: Coordinate

    def __init__(self, x: int, y: int):
        self.__coordinates = Coordinate(x, y)

    def getCoordinate(self) -> Coordinate:
        return self.__coordinates
