from UI.SplashScreenUI import SplashScreenUI
import time

class SplashScreenController:
    def __init__(self, state):
        self.action = None
        self.initTime = time.ticks_ms()
    
    def mount(self, userInput, ui):
        userInput.setCallback(self.onAction)
        
        self.render(ui)
    
    def onAction(self, action):
        self.action = action
    
    def tick(self, ui):
        if self.action == "keyCenter":
            return "webServer"
        elif time.ticks_diff(time.ticks_ms(), self.initTime) > 750:
            return "list"
        
        return None
    
    def render(self, ui):
        ui.render(SplashScreenUI())
