import numpy as np
import cv2
from PIL import Image


# def gaussian_blurring(dim):
#     image_path = r"D:\Users\manof\Desktop\два папуга.jpg"
#     # img = Image.open(image_path)
#     # image = np.array(img, dtype=np.uint8)
#     sens = dim * 2 - 1
#     image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
#     img_blur_1 = cv2.blur(image, (sens, sens))
#     img_blur_2 = cv2.GaussianBlur(image, (sens, sens), 0)  # 0 is better
#     img_blur_3 = cv2.medianBlur(image, sens)
#     img_blur_4 = cv2.bilateralFilter(image, sens, 75, 75)
#     img_blur_5 = cv2.boxFilter(image, 100, (sens, sens))
#     img_blur_5_display = cv2.convertScaleAbs(img_blur_5)
#     cv2.imshow('blur', img_blur_1)
#     cv2.imshow('GaussianBlur', img_blur_2)
#     cv2.imshow('medianBlur', img_blur_3)
#     cv2.imshow('bilateralFilter', img_blur_4)
#     cv2.imshow('boxFilter', img_blur_5_display)
#     cv2.waitKey(0)


def segmentation_image(arr: np.array):
    img = cv2.cvtColor(arr, cv2.COLOR_RGB2HSV)
    img = cv2.pyrMeanShiftFiltering(img, 30, 10, 2)
    img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    return img.astype(np.uint8)


# image_path = r"D:\Users\manof\Desktop\два папуга.jpg"
# image = Image.open(image_path)
# im_as_ar = np.array(image, dtype=np.uint8)
# segmentation_image(im_as_ar)


def find_edges(img: np.array, sensitivity: int):
    # img_segm = segmentation_image(img)

    img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    dim = sensitivity * 2 - 1

    # img_blur = cv2.blur(img_grey, (dim, dim))
    # img_blur = cv2.GaussianBlur(img_grey, (dim, dim), 0)
    img_blur = cv2.medianBlur(img_grey, dim)
    # FILTERS
    # img_blur = cv2.bilateralFilter(img_grey, dim, 75, 75) # dim, 75, 75
    # img_blur = cv2.boxFilter(img_grey, 100, (dim, dim))

    # img_Threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 2) #23, 2

    img_canny = cv2.Canny(img_blur, sensitivity, sensitivity * 2.5)

    return img_canny.astype(np.uint8)
