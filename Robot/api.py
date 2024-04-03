import requests


class Api:
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

    def receive(self, subdomain: str) -> dict:
        """
        A method that sends a GET request to the API and returns the response

        Parameters
        ----------
            subdomain : str
                the subdomain to send the request to

        Returns
        -------
            response : dict
                the response from the API, empty if no connection was established
                """
        print(f"essai de connexion à {self.__url + subdomain}...")
        try:
            response = requests.get(self.__url + subdomain, timeout=5)
        except:
            print("Erreur de connexion")
            return {"success": False}

        response = response.json()
        response["success"] = True
        return response

    def __str__(self) -> str:
        return self.__url
