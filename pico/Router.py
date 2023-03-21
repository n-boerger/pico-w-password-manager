from Controller.ListController import ListController
from Controller.DetailsController import DetailsController
from Controller.SplashScreenController import SplashScreenController

class Router:
    def push(self, route, state):
        if route == "list":
            return ListController(state)
        elif route == "details":
            return DetailsController(state)
        elif route == "splashScreen":
            return SplashScreenController(state)
