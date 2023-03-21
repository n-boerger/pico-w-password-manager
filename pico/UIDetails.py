from Color import Color

class UIDetails:
    def __init__(self, display):
        self.display = display
    
    def render(self, credentials, activeIndex):
        offset = 6
        index = 0
        
        self.display.text(credentials.title, 16, 12, Color.WHITE)
        self.display.hline(0, 26, 240, Color.WHITE)
        
        offset = 32
        
        if activeIndex == "username":
            self.display.fill_rect(0, offset, 240, 30, Color.WHITE)
            self.display.text("Autofill username", 16, offset + 6, Color.BLACK)
            self.display.text(credentials.username, 16, offset + 16, Color.BLACK)
        else:
            self.display.text("Autofill username", 16, offset + 6, Color.WHITE)
            self.display.text(credentials.username, 16, offset + 16, Color.WHITE)
        
        offset += 36
        
        if activeIndex == "password":
            self.display.fill_rect(0, offset, 240, 30, Color.WHITE)
            self.display.text("Autofill password", 16, offset + 6, Color.BLACK)
            self.display.text(credentials.password, 16, offset + 16, Color.BLACK)
        else:
            self.display.text("Autofill password", 16, offset + 6, Color.WHITE)
            self.display.text(credentials.password, 16, offset + 16, Color.WHITE)