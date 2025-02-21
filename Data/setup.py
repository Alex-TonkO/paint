import os
from PIL import Image, ImageTk

PATH = os.path.dirname(os.path.dirname(__file__))


def load_image(name):
    locetion = os.path.join(PATH, 'resources', 'icons', name)
    img = Image.open(locetion).resize((20,20), Image.BICUBIC)
    return ImageTk.PhotoImage(img)