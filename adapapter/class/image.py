from abc import ABC, abstractmethod
#-----------------------------------------------------
class Image(ABC):
    def __init__(self, width, height, format, pixels):
        self.width  = width
        self.height = height
        self.format = format
        self.pixels = pixels
    @abstractmethod
    def convert(self):
        pass