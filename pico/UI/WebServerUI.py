from Color import Color

class WebServerUI:
    def __init__(self, apSettings):
        self.apSettings = apSettings

    def render(self, display):
        display.text("Running webserver", 52, 64, Color.WHITE)
        
        display.text(f"> Connect to '{self.apSettings.ssid}'", 12, 99, Color.WHITE)
        display.text(f"> With password '{self.apSettings.password}'", 16, 111, Color.WHITE)
        display.text("> Navigate to 'ppm.local'", 20, 123, Color.WHITE)
