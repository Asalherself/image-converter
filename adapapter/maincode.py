from Classes.image                import Image
from Classes.gif                  import GIF
from Classes.png                  import PNG
from Classes.jpeg                 import JPEG
from Classes.FormatConverter import FormatConventer
#----------------------------------------------------
print(FormatConventer("image", "GIF").calculate())
print(FormatConventer("image", "PNG").calculate())
print(FormatConventer("image", "JPEG").calculate())
