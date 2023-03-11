from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import sys
from UI.custom_label import ScaledLabel
from main_algorithm import main_low_poly_image


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
        self.Button_Import.clicked.connect(self.import_image_button)

        self.Button_Export = self.findChild(QtWidgets.QPushButton, 'Button_Export')
        self.Button_Export.clicked.connect(self.export_image_button)

        self.Button_Triangulate = self.findChild(QtWidgets.QPushButton, 'Button_Triangulate')
        self.Button_Triangulate.clicked.connect(self.triangulate_image_button)

        self.Slider = self.findChild(QtWidgets.QSlider, 'Slider')
        self.Slider.valueChanged.connect(self.slide_it)

        # пришлось сделать в Qt Designer promote labels, скопировать код со StackOverflow
        # https://stackoverflow.com/questions/72188903/pyside6-how-do-i-resize-a-qlabel-without-loosing-the-size-aspect-ratio
        # И создать файл, как описано в ссылке.
        self.Label_Image_before = self.findChild(ScaledLabel, 'Label_Image_before')
        self.Label_Image_after = self.findChild(ScaledLabel, 'Label_Image_after')
        self.Label_slider = self.findChild(QtWidgets.QLabel, 'Label_slider')

        # vars ----------------------------------------------------------------------------------
        self.image_before_path = ""
        self.slider_val = 0

    def error_mes_box_text(self):
        err = QMessageBox()
        err.setWindowTitle("Ошибка")
        err.setIcon(QMessageBox.Icon.Warning)
        err.setStandardButtons(QMessageBox.StandardButton.Ok)
        err.setText("Сначала выберете изображение!")
        err.exec()

    def import_image_button(self):
        # browse_frame1 = QFileDialog.getOpenFileName(self, "Выбрать изображение", r"D:\Users\manof\Desktop",
        #                                             "Image Files (*.png;*.jpg;*.jpeg)")
        # self.image_before_path = browse_frame1[0]
        self.image_before_path= "два папуга.jpg"

        image_before_profile = QtGui.QImage(self.image_before_path)
        self.Label_Image_before.setPixmap(QtGui.QPixmap.fromImage(image_before_profile))

    def export_image_button(self):
        if self.image_before_path == "":
            self.error_mes_box_text()
        else:
            browse_frame2 = QFileDialog.getSaveFileName(self, "Сохранить как", r"D:\Users\manof\Desktop",
                                                        "PNG files (*.png)")
            image_after_path = browse_frame2[0]
            self.image_after.save(image_after_path)

    def triangulate_image_button(self):
        if self.image_before_path == "":
            self.error_mes_box_text()
        else:
            self.image_after = main_low_poly_image(self.image_before_path, self.slider_val)
            self.Label_Image_after.setPixmap(QtGui.QPixmap.fromImage(self.image_after))

    def slide_it(self, value):
        self.slider_val = value
        self.Label_slider.setText(str(value))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
