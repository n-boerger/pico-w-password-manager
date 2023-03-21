from Color import Color

class SplashScreenUI:
    def render(self, display):
        display.text("Pico Password Manager", 36, 64, Color.WHITE)
        
        display.text("Press joystick to boot", 32, 111, Color.WHITE)
        display.text("into the webserver", 48, 123, Color.WHITE)

