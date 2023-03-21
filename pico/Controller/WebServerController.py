from UI.WebServerUI import WebServerUI
from WebServer import WebServer

class WebServerController:
    def __init__(self, ui):
        self.render(ui)
        
        WebServer()
    
    def render(self, ui):
        ui.render(WebServerUI())
