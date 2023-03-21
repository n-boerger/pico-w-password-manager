import usb_device
import time
from KeyCodesDE import KeyCodes

class Autofill:
    def __init__(self):
        self.hid = usb_device.HID()
        self.keyCodes = KeyCodes()
    
    def sendString(self, string):
        self.keyCodes.decode(string, self.sendBuffer)
    
    def sendBuffer(self, buffer):
        self.hid.report(0, 0, buffer)
        
        time.sleep_ms(50)
