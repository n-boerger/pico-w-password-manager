class Modifiers:
    LCTRL = 0x01
    LSHIFT = 0x02
    LALT = 0x04
    LMETA = 0x08
    RCTRL = 0x10
    RSHIFT = 0x20
    RALT = 0x40
    RMETA = 0x80

class Keys:
    KEY_NONE = 0x00
    KEY_A = 0x04
    KEY_B = 0x05
    KEY_C = 0x06
    KEY_D = 0x07
    KEY_E = 0x08
    KEY_F = 0x09
    KEY_G = 0x0a
    KEY_H = 0x0b
    KEY_I = 0x0c
    KEY_J = 0x0d
    KEY_K = 0x0e
    KEY_L = 0x0f
    KEY_M = 0x10
    KEY_N = 0x11
    KEY_O = 0x12
    KEY_P = 0x13
    KEY_Q = 0x14
    KEY_R = 0x15
    KEY_S = 0x16
    KEY_T = 0x17
    KEY_U = 0x18
    KEY_V = 0x19
    KEY_W = 0x1a
    KEY_X = 0x1b
    KEY_Y = 0x1d
    KEY_Z = 0x1c
    KEY_SZ = 0x2d
    KEY_AE = 0x34
    KEY_OE = 0x33
    KEY_UE = 0x2f
    KEY_1 = 0x1e
    KEY_2 = 0x1f
    KEY_3 = 0x20
    KEY_4 = 0x21
    KEY_5 = 0x22
    KEY_6 = 0x23
    KEY_7 = 0x24
    KEY_8 = 0x25
    KEY_9 = 0x26
    KEY_0 = 0x27
    KEY_PLUS = 0x30
    KEY_HASH = 0x32
    KEY_LT = 0x64
    KEY_COMMA = 0x36
    KEY_DOT = 0x37
    KEY_MINUS = 0x38
    KEY_SPACE = 0x2c

class KeyCodes:
    def decode(self, string, callback):
        for char in string:
            callback(self.decodeChar(char))
            callback(self.decodeChar(""))
    
    def decodeChar(self, char):
        # lowercase letters
        if char == "a": return self.buildBuffer(0x00, Keys.KEY_A)
        if char == "b": return self.buildBuffer(0x00, Keys.KEY_B)
        if char == "c": return self.buildBuffer(0x00, Keys.KEY_C)
        if char == "d": return self.buildBuffer(0x00, Keys.KEY_D)
        if char == "e": return self.buildBuffer(0x00, Keys.KEY_E)
        if char == "f": return self.buildBuffer(0x00, Keys.KEY_F)
        if char == "g": return self.buildBuffer(0x00, Keys.KEY_G)
        if char == "h": return self.buildBuffer(0x00, Keys.KEY_H)
        if char == "i": return self.buildBuffer(0x00, Keys.KEY_I)
        if char == "j": return self.buildBuffer(0x00, Keys.KEY_J)
        if char == "k": return self.buildBuffer(0x00, Keys.KEY_K)
        if char == "l": return self.buildBuffer(0x00, Keys.KEY_L)
        if char == "m": return self.buildBuffer(0x00, Keys.KEY_M)
        if char == "n": return self.buildBuffer(0x00, Keys.KEY_N)
        if char == "o": return self.buildBuffer(0x00, Keys.KEY_O)
        if char == "p": return self.buildBuffer(0x00, Keys.KEY_P)
        if char == "q": return self.buildBuffer(0x00, Keys.KEY_Q)
        if char == "r": return self.buildBuffer(0x00, Keys.KEY_R)
        if char == "s": return self.buildBuffer(0x00, Keys.KEY_S)
        if char == "t": return self.buildBuffer(0x00, Keys.KEY_T)
        if char == "u": return self.buildBuffer(0x00, Keys.KEY_U)
        if char == "v": return self.buildBuffer(0x00, Keys.KEY_V)
        if char == "w": return self.buildBuffer(0x00, Keys.KEY_W)
        if char == "x": return self.buildBuffer(0x00, Keys.KEY_X)
        if char == "y": return self.buildBuffer(0x00, Keys.KEY_Y)
        if char == "z": return self.buildBuffer(0x00, Keys.KEY_Z)
        
        # uppercase letters
        if char == "A": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_A)
        if char == "B": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_B)
        if char == "C": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_C)
        if char == "D": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_D)
        if char == "E": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_E)
        if char == "F": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_F)
        if char == "G": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_G)
        if char == "H": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_H)
        if char == "I": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_I)
        if char == "J": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_J)
        if char == "K": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_K)
        if char == "L": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_L)
        if char == "M": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_M)
        if char == "N": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_N)
        if char == "O": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_O)
        if char == "P": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_P)
        if char == "Q": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_Q)
        if char == "R": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_R)
        if char == "S": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_S)
        if char == "T": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_T)
        if char == "U": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_U)
        if char == "V": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_V)
        if char == "W": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_W)
        if char == "X": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_X)
        if char == "Y": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_Y)
        if char == "Z": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_Z)
        
        # lowercase special letters
        if char == "ä": return self.buildBuffer(0x00, Keys.KEY_AE)
        if char == "ö": return self.buildBuffer(0x00, Keys.KEY_OE)
        if char == "ü": return self.buildBuffer(0x00, Keys.KEY_UE)
        if char == "ß": return self.buildBuffer(0x00, Keys.KEY_SZ)
        
        # uppercase special letters
        if char == "Ä": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_AE)
        if char == "Ö": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_OE)
        if char == "Ü": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_UE)

        # numbers
        if char == "1": return self.buildBuffer(0x00, Keys.KEY_1)
        if char == "2": return self.buildBuffer(0x00, Keys.KEY_2)
        if char == "3": return self.buildBuffer(0x00, Keys.KEY_3)
        if char == "4": return self.buildBuffer(0x00, Keys.KEY_4)
        if char == "5": return self.buildBuffer(0x00, Keys.KEY_5)
        if char == "6": return self.buildBuffer(0x00, Keys.KEY_6)
        if char == "7": return self.buildBuffer(0x00, Keys.KEY_7)
        if char == "8": return self.buildBuffer(0x00, Keys.KEY_8)
        if char == "9": return self.buildBuffer(0x00, Keys.KEY_9)
        if char == "0": return self.buildBuffer(0x00, Keys.KEY_0)

        # special chars
        if char == "+": return self.buildBuffer(0x00, Keys.KEY_PLUS)
        if char == "#": return self.buildBuffer(0x00, Keys.KEY_HASH)
        if char == "<": return self.buildBuffer(0x00, Keys.KEY_LT)
        if char == ",": return self.buildBuffer(0x00, Keys.KEY_COMMA)
        if char == ".": return self.buildBuffer(0x00, Keys.KEY_DOT)
        if char == "-": return self.buildBuffer(0x00, Keys.KEY_MINUS)
        if char == " ": return self.buildBuffer(0x00, Keys.KEY_SPACE)
        
        if char == "*": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_PLUS)
        if char == "'": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_HASH)
        if char == ">": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_LT)
        if char == ";": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_COMMA)
        if char == ":": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_DOT)
        if char == "_": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_MINUS)
        
        if char == "~": return self.buildBuffer(Modifiers.RALT, Keys.KEY_PLUS)
        if char == "@": return self.buildBuffer(Modifiers.RALT, Keys.KEY_Q)
        if char == "€": return self.buildBuffer(Modifiers.RALT, Keys.KEY_E)
        if char == "|": return self.buildBuffer(Modifiers.RALT, Keys.KEY_LT)

        if char == "!": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_1)
        if char == "\"": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_2)
        if char == "§": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_3)
        if char == "$": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_4)
        if char == "%": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_5)
        if char == "&": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_6)
        if char == "/": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_7)
        if char == "(": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_8)
        if char == ")": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_9)
        if char == "=": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_0)
        if char == "?": return self.buildBuffer(Modifiers.LSHIFT, Keys.KEY_SZ)

        if char == "{": return self.buildBuffer(Modifiers.RALT, Keys.KEY_7)
        if char == "[": return self.buildBuffer(Modifiers.RALT, Keys.KEY_8)
        if char == "]": return self.buildBuffer(Modifiers.RALT, Keys.KEY_9)
        if char == "}": return self.buildBuffer(Modifiers.RALT, Keys.KEY_0)
        if char == "\\": return self.buildBuffer(Modifiers.RALT, Keys.KEY_SZ)

        return self.buildBuffer(0x00, 0x00)
    
    def buildBuffer(self, modifier, key):
        return bytearray([ modifier, 0x00, key, 0x00, 0x00, 0x00, 0x00, 0x00 ])
