from PIL import Image
from PyQt6.QtGui import QImage
import numpy as np
from methods_of_match_pixels.method_1 import find_diff_colors


# какое-то преобразование с картинкой
def main_low_poly_image(image_path: str, sldr: int):
    image = Image.open(image_path)
    # Преобразование картинки в nampy array
    im_as_ar = np.array(image, dtype="int16")

    # main algorithm here ----vvv----
    transform_image = find_diff_colors(im_as_ar, sldr, 1)
    # main algorithm here ----^^^----

    # Преобразование numpy array обратно в картинку QT, чтобы загрузить её в Label
    h, w, _ = transform_image.shape
    res_image = QImage(transform_image, w, h, 3 * w, QImage.Format.Format_RGB888)
    return res_image
