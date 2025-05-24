import time
from smiley import Smiley


class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws an angry mouth (e.g., a straight or downturned line)
        """
        mouth = [48, 49, 50, 51, 52, 53, 54, 55, 56]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws angry eyes (e.g., slanted or intense)
        """
        brows = [9, 10, 13, 14]
        eyes = [17, 22]
        for pixel in brows:
            self.pixels[pixel] = self.complexion()  # Red for brows
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()