import usb_device
from Input import Input
from Router import Router
from State import State
from UI import UI

class USBApplication:
    def __init__(self):
        descriptor = bytearray([
            0x05, 0x01,
            0x09, 0x06,
            0xA1, 0x01,
            0x05, 0x07,
            0x19, 0xe0,
            0x29, 0xe7,
            0x15, 0x00,
            0x25, 0x01,
            0x75, 0x01,
            0x95, 0x08,
            0x81, 0x02,

            0x95, 0x01,
            0x75, 0x08,
            0x81, 0x01,

            0x95, 0x05,
            0x75, 0x01,
            0x05, 0x08,
            0x19, 0x01,
            0x29, 0x05,
            0x91, 0x02,
            0x95, 0x01,
            0x75, 0x03,
            0x91, 0x01,

            0x95, 0x06,
            0x75, 0x08,
            0x15, 0x00,
            0x25, 0x65,
            0x05, 0x07,
            0x19, 0x00,
            0x29, 0x65,
            0x81, 0x00,

            0x09, 0x05,
            0x15, 0x00,
            0x26, 0xFF, 0x00,
            0x75, 0x08,
            0x95, 0x02,
            0xB1, 0x02,

            0xC0
        ])

        hid = usb_device.HID()
        hid.add_descriptor("Pico Keyboard", 1, len(descriptor), 32, descriptor)

        desc = usb_device.Descriptor()
        desc.device(idVendor=0xF055, idProduct=0xF055)
        desc.strings(Manufacturer="Nicolas Boerger", Product="Pico Password Manager", CDC="CDC PPM")
        
        userInput = Input()
        state = State()
        router = Router()
        ui = UI()

        controller = router.push("splashScreen", state)
        controller.mount(userInput, ui)

        while True:
            userInput.tick()
            
            nextRoute = controller.tick(ui)
            
            if nextRoute != None:
                userInput.removeCallback()
                
                controller = router.push(nextRoute, state)
                
                controller.mount(userInput, ui)
