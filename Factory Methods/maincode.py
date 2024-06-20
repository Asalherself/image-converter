from Classes.FORMATS import FORMATS
#--------------------------------------------------------
def convert_image(image, format, *args):
    factory = FORMATS()
    format_conventer = factory.create_format(format, *args)
    return image.convert()
image1 = convert_image("image", "GIF")
image2 = convert_image("image", "PNG")
image3 = convert_image("image", "JPEG")
