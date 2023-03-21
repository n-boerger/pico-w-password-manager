from Color import Color

class DetailsUI:
    def __init__(self, credentials, activeIndex):
        self.credentials = credentials
        self.activeIndex = activeIndex
    
    def render(self, display):
        offset = 6
        
        display.text(self.credentials.title, 16, 12, Color.WHITE)
        display.hline(0, 26, 240, Color.WHITE)
        
        offset = 32
        
        if self.activeIndex == "username":
            display.fill_rect(0, offset, 240, 30, Color.WHITE)
            display.text("Autofill username", 16, offset + 6, Color.BLACK)
            display.text(self.credentials.username, 16, offset + 16, Color.BLACK)
        else:
            display.text("Autofill username", 16, offset + 6, Color.WHITE)
            display.text(self.credentials.username, 16, offset + 16, Color.WHITE)
        
        offset += 36
        
        if self.activeIndex == "password":
            display.fill_rect(0, offset, 240, 30, Color.WHITE)
            display.text("Autofill password", 16, offset + 6, Color.BLACK)
            display.text("********", 16, offset + 16, Color.BLACK)
        else:
            display.text("Autofill password", 16, offset + 6, Color.WHITE)
            display.text("********", 16, offset + 16, Color.WHITE)
