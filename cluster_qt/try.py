import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap = QPixmap("assets//bg_splash.jpg")
        self.setPixmap(pixmap)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(50)  # milliseconds
        self.progress_value = 0

    def progress(self):
        self.progress_value += 1
        self.progressBar.setValue(self.progress_value)
        if self.progress_value >= 100:
            self.timer.stop()

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    welcome = WelcomeScreen()
    widget = QStackedWidget()
    widget.addWidget(welcome)
    widget.show()

    splash.finish(welcome)

    sys.exit(app.exec_())
