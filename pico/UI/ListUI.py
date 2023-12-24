from Color import Color

class ListUI:
    def __init__(self, items, state):
        self.items = items
        self.state = state
    
    def render(self, display):
        offset = 6
        index = 0
        
        for item in self.items:
            fgColor = Color.WHITE
            
            if index == self.state.listIndex:
                fgColor = Color.BLACK
                
                display.fill_rect(0, offset, 240, 20, Color.WHITE)
            
            display.text(item.title, 16, offset + 6, fgColor)
            
            offset += 26
            index += 1
