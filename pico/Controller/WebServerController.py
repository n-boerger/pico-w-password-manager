from UI.WebServerUI import WebServerUI
from WebServer import WebServer
from ApSettings import ApSettings

class WebServerController:
    def __init__(self, ui):
        self.apSettings = ApSettings()

        self.render(ui)
        
        WebServer(self.apSettings)
    
    def render(self, ui):
        ui.render(WebServerUI(self.apSettings))
