class Dots():
    """
    this class describes dots (pixels) on the image which were chosen during comparison pixels
    dots have coordinates X and Y by row and col in image
    dots also have a color
    .
    Methods for determining which dot will be used to make a triangle

    """

    def __init__(self, row, col):
        self.row = row
        self.col = col
