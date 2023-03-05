from PIL import Image
from PyQt6.QtGui import QImage
import numpy as np

# Исходные данные. Путь к картинке и значение слайдера
IMAGE_PATH = r"D:\Users\manof\Desktop\Игры\ \НАДО\картинки какие то\Лайки\два папуга.jpg"
SLIDER = 255  # от 0 до 255


# какое-то преобразование с картинкой
def main_low_poly_image(image_path: str, sldr: int):
    # There will be some complicate code

    image = Image.open(image_path)
    # Преобразование картинки в nampy array
    im_as_ar = np.array(image)
    transform_image=sldr - im_as_ar
    # Преобразование numpy array обратно в картинку QT, чтобы загрузить её в Label
    h, w, _ = transform_image.shape
    res_image = QImage(transform_image, w, h, 3 * w, QImage.Format.Format_RGB888)
    return res_image






