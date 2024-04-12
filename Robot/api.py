import requests
from requests.exceptions import ConnectTimeout


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

        fullUrl = self.__url + subdomain
        print(f"Essai de connexion à {fullUrl}...")

        try:
            response = requests.get(fullUrl, timeout=5)
        except ConnectTimeout:
            print(f"La connexion à {fullUrl} a échouée")
            return {"success": False}
        print(f"connecté à {fullUrl} avec succès!")

        response = response.json()
        response["success"] = True
        return response

    def __str__(self) -> str:
        return self.__url
