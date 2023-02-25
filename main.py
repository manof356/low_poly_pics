from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import sys
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

        self.Image_before = self.findChild(QtWidgets.QLabel, 'Image_before')
        self.Image_after = self.findChild(QtWidgets.QLabel, 'Image_after')

    def browse_image(self):
        browse_frame = QFileDialog.getOpenFileName(self, "Open image", r"D:\Users\manof\Desktop")
        self.image_path = browse_frame[0]
        self.Image_before.setPixmap(QtGui.QPixmap(browse_frame[0]))

    def export_image(self):
        print(self.image_path)


# some code


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
