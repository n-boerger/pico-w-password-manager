from machine import unique_id
from urandom import choice, seed

class ApSettings:
    def __init__(self):
        id = unique_id()
        hexId = "{:02x}{:02x}{:02x}{:02x}".format(id[0], id[1], id[2], id[3])

        self.ssid = f"PPM-{hexId}"

        seed(int(hexId, 16))
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

        self.password = ''.join((choice(chars) for _ in range(8)))