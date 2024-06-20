from abc import ABC, converter
#--------------------------------------------------------
class IMAGE(ABC):
    def __init__(self, width, height, format, pixels):
        self.width  = width
        self.height = height
        self.format = format
        self.pixels = pixels
    @converter
    def convert(self):
        pass