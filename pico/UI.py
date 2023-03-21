from Display import Display
from Color import Color

class UI:
    def __init__(self):
        self.display = Display()
    
    def render(self, ui):
        self.display.fill(Color.BLACK)
        
        ui.render(self.display)
        
        self.display.show()
        
        
    def renderSplashScreen(self):
        self.display.fill(Color.BLACK)
        
        self.display.text("Pico Password Manager", 36, 64, Color.WHITE)
        
        self.display.text("Press joystick to boot", 32, 111, Color.WHITE)
        self.display.text("into the webserver", 48, 123, Color.WHITE)
        
        self.display.show()