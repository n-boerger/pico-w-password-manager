from UI import UI
from WebServerController import WebServerController

class WebServerApplication:
    def __init__(self):
        WebServerController(UI())
