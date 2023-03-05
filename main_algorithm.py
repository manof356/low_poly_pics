from PIL import Image
import numpy as np

IMAGE = Image.open(r"D:\Users\manof\Desktop\Игры\ \НАДО\картинки какие то\Лайки\два папуга.jpg")
SLIDER = 50

im_as_ar = np.array(IMAGE)
grayscale_image = SLIDER - im_as_ar

# не нравится мне такое решение. Скорее всего вылезет боком в будущем. Нужно numpy array как то преобразовывать в
# Qt.Image
res_image = Image.fromarray(grayscale_image)
res_image.save("res_image.jpg")
