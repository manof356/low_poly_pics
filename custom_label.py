from PyQt6 import QtCore, QtWidgets


class ScaledLabel(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        QtWidgets.QLabel.__init__(self)
        self._pixmap = self.pixmap()
        self._resised = False

    def resizeEvent(self, event):
        self.setPixmap(self._pixmap)

    def setPixmap(self, pixmap):  # overiding setPixmap
        if not pixmap: return
        self._pixmap = pixmap
        return QtWidgets.QLabel.setPixmap(self, self._pixmap.scaled(
            self.frameSize(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))
