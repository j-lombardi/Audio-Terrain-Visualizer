from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QLabel
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(150, 150, 450, 300)
        self.setWindowTitle('Prototype!!')

        self.initUI()

    def initUI(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('File')

        openFile = QAction('Open File', self)
        openFile.triggered.connect(self.open_image)
        openFile.setShortcut("Ctrl+O")
        fileMenu.addAction(openFile)

        closeFile = QAction('Close File', self)
        closeFile.triggered.connect(self.close)
        closeFile.setShortcut("Ctrl+W")
        fileMenu.addAction(closeFile)

        self.img = QLabel()
        self.setCentralWidget(self.img)

    def open_image(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.img.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()

    def update(self):
        self.label.adjustSize()


def window():
    # Initializing app and window
    app = QApplication(sys.argv)
    window = MyWindow()
    # Displaying window and giving it a clean exit function using sys.exec_()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(window())
