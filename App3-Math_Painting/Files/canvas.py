import numpy as np
from PIL import Image


class Canvas:
    """An object which creates a background for all the shapes to be drawn"""
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3d numpy array
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imgPath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imgPath)