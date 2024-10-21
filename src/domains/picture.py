import time

class Picture:
    def __init__(self, name_file: str, color_palette: list):
        self.name_file = name_file
        self.name = "picture_" + str(int(time.time())) + ".png"
        self.color_palette = color_palette