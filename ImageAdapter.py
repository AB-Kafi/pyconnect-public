from PIL import Image,ImageTk

class ImageAdapter:
    
    def __init__(self, size = None ):
        self.size = size
    
    def convert(self, location, size = (300,300)):
        if self.size == None:
            self.size = size
        image = Image.open(location)
        new = ImageTk.PhotoImage(image.resize(self.size))
        return new