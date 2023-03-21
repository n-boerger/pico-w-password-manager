from Color import Color

class UIList:
    def __init__(self, display):
        self.display = display
    
    def render(self, items, activeIndex):
        offset = 6
        index = 0
        
        for item in items:
            fgColor = Color.WHITE
            
            if index == activeIndex:
                fgColor = Color.BLACK
                
                self.display.fill_rect(0, offset, 240, 20, Color.WHITE)
            
            self.display.text(item.title, 16, offset + 6, fgColor)
            
            offset += 26
            index += 1