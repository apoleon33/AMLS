class Api():
    __url: str

    def __init__(self, url: str):
        self.__url = url

    @property
    def Url(self) -> str:
        return self.__url

    @Url.setter
    def Url(self, url: str):
        self.__url = url

    def send(self, subdomain: str, data):
        pass

    def receive(self, subdomain: str) -> str:
        pass

    def __str__(self) -> str:
        return self.__url
