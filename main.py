from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog
import sys
from custom_label import ScaledLabel
from main_algorithm import res_image


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
        self.Image_before = self.findChild(ScaledLabel, 'Image_before')
        self.Image_after = self.findChild(ScaledLabel, 'Image_after')


    def browse_image(self):
        # browse_frame = QFileDialog.getOpenFileName(self, "Выбрать изображение", r"D:\Users\manof\Desktop",
        #                                            "Image Files (*.png;*.jpg;*.jpeg)")
        # image_path = browse_frame[0]
        # -------------------------------------------------------------------------------------------
        image_path = r"D:\Users\manof\Desktop\Игры\ \НАДО\картинки какие то\Лайки\два папуга.jpg"
        # -------------------------------------------------------------------------------------------
        image_profile_before = QtGui.QImage(image_path)
        self.Image_before.setPixmap(QtGui.QPixmap.fromImage(image_profile_before))
        image_profile_after = QtGui.QImage("res_image.jpg")
        self.Image_after.setPixmap(QtGui.QPixmap.fromImage(image_profile_after))



    def export_image(self):
        print("click")


# some code

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
