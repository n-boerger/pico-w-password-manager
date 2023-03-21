from machine import Pin

keyCenter = Pin(3, Pin.IN, Pin.PULL_UP)

if keyCenter.value() == 0:
    from WebServerApplication import WebServerApplication
    
    WebServerApplication()
else:
    from USBApplication import USBApplication
    
    USBApplication()
