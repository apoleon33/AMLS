class Coordinate():
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def X(self) -> int:
        return self._x

    @X.setter
    def X(self, value: int):
        self._x = value

    @property
    def Y(self) -> int:
        return self._y

    @Y.setter
    def Y(self, value: int):
        self._y = value

    def __str__(self) -> str:
        return f'({self._x}, {self._y})'
