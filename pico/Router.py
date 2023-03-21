from ListController import ListController
from DetailsController import DetailsController
from SplashScreenController import SplashScreenController

class Router:
    def push(self, route, state):
        if route == "list":
            return ListController(state)
        elif route == "details":
            return DetailsController(state)
        elif route == "splashScreen":
            return SplashScreenController(state)
