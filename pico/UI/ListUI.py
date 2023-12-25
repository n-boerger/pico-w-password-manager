from Color import Color
from math import ceil

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

        if self.state.length > 5:
            self.renderScrollbar(display)
        
    def renderScrollbar(self, display):
        display.fill_rect(220, 0, 20, 135, Color.BLACK)
        display.fill_rect(232, 6, 2, 123, Color.WHITE)

        height = ceil(123 / self.state.length)
        offset = 6 + ceil(self.state.index * (123 / self.state.length))

        display.fill_rect(226, offset, 14, height, Color.WHITE)
