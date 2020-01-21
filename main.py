from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QLabel, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D # used for ploting 3d graphs

import sys
import numpy as np
import noise
import random

MAP_SIZE = (512, 512)
SCALE = 256
EXPO_HEIGHT = 2


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    # noise function
    def update_point(self, coords, seed):
        return noise.snoise2(coords[0] / SCALE,
                             coords[1] / SCALE,
                             octaves=5,  # low octave is smooth
                             persistence=0.5,
                             lacunarity=2,
                             repeatx=MAP_SIZE[0],
                             repeaty=MAP_SIZE[1],
                             base=seed
                             )

    # returns a randomly generated height map
    def generate_height_map(self):
        seed = int(random.random() * 1000)
        minimum = 0
        maximum = 0
        height_map = np.zeros(MAP_SIZE)

        for x in range(MAP_SIZE[0]):
            for y in range(MAP_SIZE[1]):
                new_value = self.update_point((x, y), seed)
                height_map[x][y] = new_value
                if new_value < minimum:
                    minimum = new_value
                if new_value > maximum:
                    maximum = new_value
        print("Height map generated with seed:", seed)
        return self.normalize(height_map, minimum, maximum, EXPO_HEIGHT)

    def normalize(self, input_map, minimum, maximum, expo):
        scale = maximum - minimum
        output_map = np.zeros(MAP_SIZE)
        for x in range(MAP_SIZE[0]):
            for y in range(MAP_SIZE[1]):
                output_map[x][y] = ((input_map[x][y] - minimum) / scale) ** expo
        return output_map

    def plot_3d(self):
        z = self.generate_height_map()
        x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))
        ax = self.figure.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z)
        ax.set_title("Z As 3D Height Map")
        self.draw()

    def plot_2d(self):
        ax = self.figure.add_subplot(111)
        ax.set_title("Z As 2D Heat Map")
        z = self.generate_height_map()
        p = ax.imshow(z)
        self.figure.colorbar(p)
        self.draw()

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setGeometry(150, 150, 450, 300)
        self.setWindowTitle('Prototype!!')

        self.initUI()

    def initUI(self):
        menu = self.menuBar()
        fileMenu = menu.addMenu('File')
        plotMenu = menu.addMenu('Plot Options')

        openFile = QAction('Open File', self)
        openFile.triggered.connect(self.open_image)
        openFile.setShortcut("Ctrl+O")
        fileMenu.addAction(openFile)

        closeFile = QAction('Close File', self)
        closeFile.triggered.connect(self.close)
        closeFile.setShortcut("Ctrl+W")
        fileMenu.addAction(closeFile)

        plot2d = QAction('Show 2d plot', self)
        plot2d.triggered.connect(self.show_2d_plot)
        plot2d.setShortcut("Ctrl+2")
        plotMenu.addAction(plot2d)

        plot3d = QAction('Show 3d plot', self)
        plot3d.triggered.connect(self.show_3d_plot)
        plot3d.setShortcut("Ctrl+3")
        plotMenu.addAction(plot3d)

        self.img = QLabel()

        self.m = PlotCanvas(self, width=10, height=8)
        self.m.move(0, 0)
        self.setCentralWidget(self.m)

        self.show()

    def open_image(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.img.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()

    def show_2d_plot(self):
        self.m.figure.clear()
        self.m.plot_2d()
        self.show()

    def show_3d_plot(self):
        self.m.figure.clear()
        self.m.plot_3d()
        self.show()

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
