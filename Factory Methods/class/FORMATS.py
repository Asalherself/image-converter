from .jpeg import JPEG
from .png  import PNG
from .gif  import GIF
#----------------------------------------------------
class FORMATS:
    def create_format(self, format, *args):
        self.image_class = {
            "JPEG": JPEG,
            "PNG" : PNG,
            "GIF" : GIF,}
        image_class = self.image_class.get(format)
        return image_class(format, *args)