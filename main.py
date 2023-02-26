from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import sys
from PIL import Image
from custom_label import ScaledLabel
import numpy as np


class MainWindow(QMainWindow):
    """
    Main window class
    """

    def __init__(self):
        """
        Constructor of main window
        """
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi('low_poly.ui', baseinstance=self)

        self.Button_Import = self.findChild(QtWidgets.QPushButton, 'Button_Import')
        self.Button_Import.clicked.connect(self.browse_image)

        self.Button_Export = self.findChild(QtWidgets.QPushButton, 'Button_Export')
        self.Button_Export.clicked.connect(self.export_image)
        # пришлось сделать в Qt Designer promote labels, скопировать код со StackOverflow
        # https://stackoverflow.com/questions/72188903/pyside6-how-do-i-resize-a-qlabel-without-loosing-the-size-aspect-ratio
        # И создать файл, как описано в ссылке.
        # TODO: правда теперь пропали надписи
        self.Label_before = self.findChild(ScaledLabel, 'Label_before')
        self.Label_after = self.findChild(ScaledLabel, 'Label_after')

    def browse_image(self):
        browse_frame = QFileDialog.getOpenFileName(self, "Выбрать изображение", r"D:\Users\manof\Desktop",
                                                   "Image Files (*.png;*.jpg;*.jpeg)")
        self.image_path = browse_frame[0]
        # get downloaded image's dimensions:
        # self.image_dims = Image.open(self.image_path).size

        image_profile = QtGui.QImage(self.image_path)

        # image_profile = image_profile.scaled(self.image_dims[0] // 2, self.image_dims[1] // 2,
        #                                      Qt.AspectRatioMode.KeepAspectRatio,
        #                                      Qt.TransformationMode.SmoothTransformation)

        # set Label dimensions as dimensions of image:
        # self.Label_before.setPixmap(QtGui.QPixmap(self.image_path).scaled(self.image_dims[0] // 2, self.image_dims[1] // 2,
        #                                           Qt.AspectRatioMode.KeepAspectRatio,
        #                                           Qt.TransformationMode.SmoothTransformation))

        self.Label_before.setPixmap(QtGui.QPixmap.fromImage(image_profile))

    def export_image(self):
        print(self.image_dims)


# some code


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
