"""
    Attempt to build a music player desktop application using PyQt5
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPalette
from pydub.playback import play
import audiosegment
import threading


class AudioPlayer(QMainWindow):

    def __init__(self):

        super(AudioPlayer, self).__init__()
        self.setGeometry(150, 150, 600, 450)
        self.setWindowTitle('Prototype!!')

        self.isButtonClick = False
        self.current_time = 0
        self.media_obj = audiosegment.empty()
        self.play_process = threading.Thread(target=play, args=(self.media_obj,))

        self.initUI()

    def initUI(self):
        menu = self.menuBar()  # create menu bar
        file_menu = menu.addMenu('File')  # create file button
        options_menu = menu.addMenu('Options')  # create options button
        wid = QWidget()
        self.setCentralWidget(wid)

        # create 'Open FIle' actions, add to 'File' button
        open_file = QAction('Open File', self)
        open_file.triggered.connect(self.openFile)
        open_file.setShortcut("Ctrl+O")
        file_menu.addAction(open_file)

        # create 'Close File' action, add to 'File' button
        close_file = QAction('Close File', self)
        close_file.triggered.connect(self.exit)
        close_file.setShortcut("Ctrl+W")
        file_menu.addAction(close_file)

        # create 'Exit' action, add to 'File' button
        exit_file = QAction('Close File', self)
        exit_file.triggered.connect(self.exit)
        exit_file.setShortcut("Ctrl+W")
        file_menu.addAction(exit_file)

        # create 'Color' action, add to 'Options' button
        color_option = QAction('Color', self)
        color_option.triggered.connect(self.show_color_dialog)
        color_option.setShortcut("Ctrl+2")
        options_menu.addAction(color_option)

        # create 'Shape' action, add to 'Options' button
        shape_option = QAction('Shape', self)
        # shape_option.triggered.connect()
        shape_option.setShortcut("Ctrl+3")
        options_menu.addAction(shape_option)

        # create 'Foliage' action, add to 'Options' button
        foliage_option = QAction('Foliage', self)
        # foliage_option.triggered.connect()
        foliage_option.setShortcut("Ctrl+3")
        options_menu.addAction(foliage_option)

        # Creating button for pause/play
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        videoWidget = QVideoWidget()
        self.pal = QPalette()
        self.pal.setColor(QPalette.Foreground, Qt.green)
        videoWidget.setPalette(self.pal)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                                      QSizePolicy.Maximum)

        self.songLabel = QLabel()
        self.songLabel.setSizePolicy(QSizePolicy.Preferred,
                                     QSizePolicy.Maximum)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        self.playButton.setShortcut("Space")
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.songLabel)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)

        # self.mediaPlayer.setVideoOutput(videoWidget)
        self.player.stateChanged.connect(self.mediaStateChanged)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.error.connect(self.handleError)

    def openFile(self):
        song = QFileDialog.getOpenFileName(self, "Open Song", "~", "Sound Files (*.mp3 *.ogg *.wav *.m4a)")
        songName = song[0].split("/")
        songName = songName[-1].split(".")
        self.songLabel.setText(songName[0])
        if song[0] != '':
            url = QUrl.fromLocalFile(song[0])
            if self.playlist.mediaCount() == 0:
                self.playButton.setEnabled(True)
                self.playlist.addMedia(QMediaContent(url))
                self.player.setPlaylist(self.playlist)
                self.player.setVolume(100)
                self.player.play()
            else:
                self.playlist.addMedia(QMediaContent(url))

    def exit(self):
        sys.exit()

    def play(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def mediaStateChanged(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.player.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.player.errorString())

    def show_color_dialog(self):
        QColorDialog.getColor()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AudioPlayer()
    window.show()
    sys.exit(app.exec_())
