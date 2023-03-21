from machine import Pin

class Input:
    def __init__(self):
        self.keyA = Pin(15, Pin.IN, Pin.PULL_UP)
        self.keyB = Pin(17, Pin.IN, Pin.PULL_UP)
        self.keyUp = Pin(2, Pin.IN, Pin.PULL_UP)
        self.keyCenter = Pin(3, Pin.IN, Pin.PULL_UP)
        self.keyDown = Pin(18, Pin.IN, Pin.PULL_UP)
        
        self.lastPress = ""
        
        self.callback = None
    
    def setCallback(self, callback):
        self.callback = callback
    
    def removeCallback(self):
        self.callback = None

    def tick(self):
        if self.keyA.value() == 0:
            self.lastPress = "keyA"
        elif self.lastPress == "keyA":
            self.handle("keyA")
            self.lastPress = ""

        if self.keyB.value() == 0:
            self.lastPress = "keyB"
        elif self.lastPress == "keyB":
            self.handle("keyB")
            self.lastPress = ""
            
        if self.keyUp.value() == 0:
            self.lastPress = "keyUp"
        elif self.lastPress == "keyUp":
            self.handle("keyUp")
            self.lastPress = ""
            
        if self.keyCenter.value() == 0:
            self.lastPress = "keyCenter"
        elif self.lastPress == "keyCenter":
            self.handle("keyCenter")
            self.lastPress = ""
            
        if self.keyDown.value() == 0:
            self.lastPress = "keyDown"
        elif self.lastPress == "keyDown":
            self.handle("keyDown")
            self.lastPress = ""
    
    def handle(self, action):
        if self.callback == None:
            return
        
        self.callback(action)