import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QSplashScreen,QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time


import warnings
from requests.exceptions import ConnectionError

def custom_excepthook(type, value, traceback):
    # Handle exceptions and warnings here
    # You can display a message or log the issue
    print("Exception or warning occurred:", type, value)


# Install the custom excepthook
sys.excepthook = custom_excepthook

def show_warning():
    warnings.warn("This is a sample warning!")

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen,self).__init__()
        loadUi("splash.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap=QPixmap("assets//bg_splash.jpg")
        self.setPixmap(pixmap)
    
    def progress(self):
        for i in range (0,100):
            time.sleep(0.05)
            self.progressBar.setValue(i)
    # def progress(self):
    #     self.progress_value = 0
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.update_progress)
    #     self.timer.start(50)  # milliseconds

    # def update_progress(self):
    #     self.progress_value += 1
    #     self.progressBar.setValue(self.progress_value)
    #     if self.progress_value >= 100:
    #         self.timer.stop()

class WelcomeScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("welcome.ui",self)
        # self.login.clicked.connect(self.gotologin)
        # self.register_2.clicked.connect(self.gotosignup)
        # self.goto_2.clicked.connect(self.gotochoose)

        # def gotologin(self):
        #     login=LoginScreen()
        #     widget.addWidget(login)
        #     widget.setCurrentWidget(login)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()
    splash.progress()

    stacked_widget = QStackedWidget()
    welcome_screen = WelcomeScreen()
    stacked_widget.addWidget(welcome_screen)
    stacked_widget.setFixedHeight(1600)
    stacked_widget.setFixedWidth(2200)
    stacked_widget.show()

    splash.finish(stacked_widget)

    sys.exit(app.exec_())
