from Color import Color

class WebServerUI:
    def render(self, display):
        display.text("Running webserver", 52, 64, Color.WHITE)
        
        display.text("> Connect to wifi 'PPM'", 23, 111, Color.WHITE)
        display.text("> Navigate to 'ppm.local'", 20, 123, Color.WHITE)
