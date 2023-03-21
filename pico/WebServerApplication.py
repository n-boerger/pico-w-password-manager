from UI.UI import UI
from Controller.WebServerController import WebServerController

class WebServerApplication:
    def __init__(self):
        WebServerController(UI())
