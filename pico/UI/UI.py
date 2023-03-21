from Display import Display
from Color import Color

class UI:
    def __init__(self):
        self.display = Display()
    
    def render(self, ui):
        self.display.fill(Color.BLACK)
        
        ui.render(self.display)
        
        self.display.show()