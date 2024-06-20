from Classes.image import Image
from Classes.gif   import GIF
from Classes.png   import PNG
#---------------------------------------------
from Classes.jpeg  import JPEG
class FormatConventer:
    class GifAdapter:
        def __init__(self, gif):
            if not isinstance(gif, GIF):
                pass
            self.gif = gif
    class PngAdapter:
        def __init__(self, png):
            if not isinstance(png, PNG):
                pass
            self.jpeg = png    
    class JpngAdapter:
        def __init__(self, jpeg):
            if not isinstance(jpeg, JPEG):
                pass
            self.jpeg = jpeg
    def __init__(self, image):
       if not isinstance(image, Image): 
            print ("Error")
       self.image = image
    def convert(self):
        if isinstance(self, Image, GIF):
            pass
        elif isinstance(self, Image, PNG):
            pass
        elif isinstance(self, Image, JPEG):
            pass
        else: 
            print ("Erorr")
            