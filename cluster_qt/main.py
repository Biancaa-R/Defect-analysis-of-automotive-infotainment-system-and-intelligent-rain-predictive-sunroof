import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QSplashScreen,QWidget
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QIcon,QMovie
from PyQt5.QtWidgets import QMessageBox
import time
import webbrowser


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
        self.login.clicked.connect(self.gotologin)
        self.register_2.clicked.connect(self.gotosignup)
        self.goto_2.clicked.connect(self.gotochoose)

    def gotologin(self):
        login=LoginScreen()
        widget.addWidget(login)
        widget.setCurrentWidget(login)

    def gotosignup(self):
        signup=SignupScreen()
        widget.addWidget(signup)
        widget.setCurrentWidget(signup)
    
    def gotochoose(self):
        # msg = QMessageBox()
        # msg.setWindowTitle("Choose your view")
        # msg.setText("Do you want to goto cluster or infotainment?")
        # msg.setIcon(QMessageBox.Question)
        # msg.exec()
        #pass

        # music=MusicScreen()
        # widget.addWidget(music)
        # widget.setCurrentWidget(music)
        menu=MenuScreen()
        widget.addWidget(menu)
        widget.setCurrentWidget(menu)
             
class LoginScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("loginscreen.ui",self)
        self.welcome_7.setIcon(QIcon('assets//angle-left.png'))
        self.email.setPlaceholderText("Enter your email ID")
        self.password.setPlaceholderText("Enter your password")

        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.welcome_7.clicked.connect(self.gotowelcome)
        self.register_2.clicked.connect(self.gotosignup)

    def gotowelcome(self):
        welcome=WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentWidget(welcome)
    
    def gotosignup(self):
        signup=SignupScreen()
        widget.addWidget(signup)
        widget.setCurrentWidget(signup)

class SignupScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("signup.ui",self)
        self.name.setPlaceholderText("Enter your name")
        self.email.setPlaceholderText("Enter your email ID")
        self.phone.setPlaceholderText("Enter your phone number")
        self.password.setPlaceholderText("Enter your password")
        self.confirm.setPlaceholderText("confirm your password")


        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login.setIcon(QIcon('assets//user.png'))
        self.welcome_7.setIcon(QIcon('assets//angle-left.png'))

        self.login.clicked.connect(self.gotologin)
        self.register_2.clicked.connect(self.signup)
        self.welcome_7.clicked.connect(self.gotowelcome)

    def gotologin(self):
        login=LoginScreen()
        widget.addWidget(login)
        widget.setCurrentWidget(login)
    
    def gotowelcome(self):
        welcome=WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentWidget(welcome)
    
    def signup(self):
        global name,email,phone
        name=self.name.text()
        email=self.email.text()
        phone=self.phone.text()
        if(name=="" or email=="" or phone==""):
            self.error.setText("Please fill in all fields")
        global password,confirm
        password=self.password.text()
        confirm=self.confirm.text()
        if (password!=confirm):
            self.error.setText("Passwords do not match")

class MusicScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("gif_render.ui",self)
        movie=QMovie("assets//music_bg.gif")
        self.bg_label.setMovie(movie)
        movie.start()

class MenuScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("menu.ui",self)
        self.google.clicked.connect(self.gotogoogle)

    def gotogoogle(self):
        google=GoogleScreen()
        widget.addWidget(google)
        widget.setCurrentWidget(google)

class GoogleScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("google.ui",self)
        self.google.clicked.connect(self.gotogoogle)
        self.youtube.clicked.connect(self.gotoyoutube)
        self.maps.clicked.connect(self.gotomaps)
        self.drive.clicked.connect(self.gotodrive)
        self.sheets.clicked.connect(self.gotosheets)
        self.voice.clicked.connect(self.gotovoice)
        self.meet.clicked.connect(self.gotomeet)
        self.docs.clicked.connect(self.gotodocs)

    def gotogoogle(self):
        # then make a url variable 
        url = "https://www.google.com"

        # then call the default open method described above 
        webbrowser.open(url)

    def gotoyoutube(self):
        # then make a url variable 
        url = "https://www.youtube.com/"

        # then call the default open method described above 
        webbrowser.open(url) 

    def gotomaps(self):
        # then make a url variable 
        url = "https://maps.google.com/"

        # then call the default open method described above 
        webbrowser.open(url)       

    def gotodrive(self):
        # then make a url variable 
        url = "https://drive.google.com/"

        # then call the default open method described above 
        webbrowser.open(url)   

    def gotosheets(self):
        # then make a url variable 
        url = "https://docs.google.com/spreadsheets/"

        # then call the default open method described above 
        webbrowser.open(url)   


    def gotovoice(self):
        # then make a url variable 
        url = "https://assistant.google.com/"

        # then call the default open method described above 
        webbrowser.open(url)   

    def gotomeet(self):
        # then make a url variable 
        url = "https://meet.google.com/"

        # then call the default open method described above 
        webbrowser.open(url)   

    def gotodocs(self):
        # then make a url variable 
        url = "https://docs.google.com/document/"

        # then call the default open method described above 
        webbrowser.open(url)   



if __name__=="__main__":
    app=QApplication(sys.argv)
    splash=SplashScreen()
    splash.show()
    splash.progress()

    welcome=WelcomeScreen()
    widget=QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(660)
    widget.setFixedWidth(1250)
    widget.show()

    splash.finish(widget)
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
