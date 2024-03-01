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
import timeit
import sqlite3

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel
import subprocess

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

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
        start=time.time()
        login=LoginScreen()
        widget.addWidget(login)
        widget.setCurrentWidget(login)
        global login_bool
        login_bool=1
        stop=time.time()
        login_load=stop-start
        print(login_load)
        #0.10786724090576172

    def gotosignup(self):
        start=time.time()
        signup=SignupScreen()
        widget.addWidget(signup)
        widget.setCurrentWidget(signup)
        global signup_bool
        signup_bool=1
        #Check if the next frame is the clicked screen
        stop=time.time()
        signup_load=stop-start
        print(signup_load)
    
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
        start=time.time()
        menu=MenuScreen()
        widget.addWidget(menu)
        widget.setCurrentWidget(menu)
        global menu_bool
        menu_bool=1
        stop=time.time()
        menu_load=stop-start
        print(menu_load)
             
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
        self.login.clicked.connect(self.gotologin)

    def gotowelcome(self):
        welcome=WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentWidget(welcome)
    
    def gotosignup(self):
        signup=SignupScreen()
        widget.addWidget(signup)
        widget.setCurrentWidget(signup)

    def gotologin(self):
        global username
        email = self.email.text()
        password = self.password.text()

        if len(email)==0 or len(password)==0:
            self.error.setText("Please fill in all fields")
        
        else:
            conn = sqlite3.connect("mahindra.db")
            cur = conn.cursor()
            query = "SELECT password FROM login_info WHERE email = '"+email+"'"
            cur.execute(query)    
            result_pass = cur.fetchone()

            if result_pass is not None:
                if result_pass[0] == password:
                    print("Successfully logged in.")
                    dashboard = MenuScreen()
                    widget.addWidget(dashboard)
                    widget.setCurrentWidget(dashboard)
                else:
                    self.error.setText("Invalid username or password")
            else:
                self.error.setText("Invalid username or password")


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

        global password,confirm
        password=self.password.text()
        confirm=self.confirm.text()

        if(name=="" or email=="" or phone==""):
            self.error.setText("Please fill in all fields")

        if (password!=confirm):
            self.error.setText("Passwords do not match")

        # conn=sqlite3.connect("mahindra.db")
        # cur=conn.cursor()
        # query= "INSERT INTO login_info (name,password,email,phone) VALUES (''{}'',''{}'',''{}'',{})".format(name,password,email,phone)
        # cur.execute(query)
        # conn.commit()
        # conn.close()
        # self.error.setText("Account created successfully")
        else:
            conn = sqlite3.connect("mahindra.db")
            cur = conn.cursor()
            query = "INSERT INTO login_info (name, password, email, phone) VALUES ('{}', '{}', '{}', {})".format(name, password, email, phone)
            cur.execute(query)
            conn.commit()
            conn.close()
            self.error.setText("Account created successfully")


class MusicScreen(QDialog):
    def __init__(self): 
        super(QDialog,self).__init__()
        loadUi("gif_render.ui",self)
        movie=QMovie("assets//music_bg.gif")
        self.bg_label.setMovie(movie)
        movie.start()
        self.dial.setRange(0, 100) 
        self.dial.valueChanged.connect(self.display) 
        #Directa pota getting error uh


    def display(self):
        print("Value = " + str(self.dial.value()))

        def set_system_volume(volume_level):
            # Get the speakers (default audio endpoint)
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            # Set the volume level (0.0 to -65.25 dB)
            volume.SetMasterVolumeLevel(volume_level, None)

            #    Set the volume level (0.0 to -65.25 dB)
            # 0.0 dB is the maximum volume, -65.25 dB is the minimum volume
            # For example, to set the volume to 50%:
        volume_percentage = int(self.dial.value() )# Adjust this value as per your requirement

        volume_db = ((volume_percentage / 100) * 65.25)-65.25
        set_system_volume(volume_db)


class MenuScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("menu.ui",self)
        self.google.clicked.connect(self.gotogoogle)
        self.music.clicked.connect(self.gotomusic)
        self.wifi.clicked.connect(self.gotowifi)
        self.gps.clicked.connect(self.gotomaps)

    def gotogoogle(self):
        google=GoogleScreen()
        widget.addWidget(google)
        widget.setCurrentWidget(google)
    
    def gotomusic(self):
        music=MusicScreen()
        widget.addWidget(music)
        widget.setCurrentWidget(music)
    
    def gotowifi(self):
        wifi_dialog = QDialog()  # Create a new dialog
        wifi_widget = WiFiNetworksWidget()  # Create instance of WiFiNetworksWidget
        layout = QVBoxLayout()
        layout.addWidget(wifi_widget)
        wifi_dialog.setLayout(layout)
        wifi_dialog.exec_()

    def gotomaps(self):
        # then make a url variable 
        url = "https://maps.google.com/"

        # then call the default open method described above 
        webbrowser.open(url)   

class GoogleScreen(QDialog):
    def __init__(self):
        super(QDialog,self).__init__()
        loadUi("google.ui",self)
        self.google.clicked.connect(self.gotogoogle)
        self.google.setIcon(QIcon('assets//google.png'))
        self.youtube.clicked.connect(self.gotoyoutube)
        self.youtube.setIcon(QIcon('assets//youtube.png'))
        self.maps.clicked.connect(self.gotomaps)
        self.maps.setIcon(QIcon('assets//google-maps.png'))
        self.drive.clicked.connect(self.gotodrive)
        self.drive.setIcon(QIcon('assets//drive.png'))
        self.sheets.clicked.connect(self.gotosheets)
        self.sheets.setIcon(QIcon('assets//sheets.png'))
        self.voice.clicked.connect(self.gotovoice)
        self.voice.setIcon(QIcon('assets//google-voice.png'))
        self.meet.clicked.connect(self.gotomeet)
        self.meet.setIcon(QIcon('assets//meet.png'))
        self.docs.clicked.connect(self.gotodocs)
        self.docs.setIcon(QIcon('assets//docs.png'))

        self.menu.clicked.connect(self.gotomenu)
        self.menu.setIcon(QIcon('assets//angle-left.png'))

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
    
    def gotomenu(self):
        menu=MenuScreen()
        widget.addWidget(menu)
        widget.setCurrentWidget(menu)

class WiFiNetworksWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Available WiFi Networks')
        self.layout = QVBoxLayout()

        # Combo box to display network names
        self.combo_networks = QComboBox()
        self.layout.addWidget(self.combo_networks)

        # Button to refresh network list
        self.btn_refresh = QPushButton('Refresh')
        self.btn_refresh.clicked.connect(self.display_networks)
        self.layout.addWidget(self.btn_refresh)

        # Button to connect to selected network
        self.btn_connect = QPushButton('Connect')
        self.btn_connect.clicked.connect(self.connect_to_network)
        self.layout.addWidget(self.btn_connect)

        # Label to display connection status
        self.lbl_status = QLabel()
        self.layout.addWidget(self.lbl_status)

        self.setLayout(self.layout)

        # Scan and display available networks
        self.display_networks()

    def display_networks(self):
        try:
            # Clear previous network names
            self.combo_networks.clear()

            # Execute netsh command to get available networks
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
            output = output.decode('utf-8')

            # Extract network names
            networks = [line.strip().split(': ')[-1] for line in output.split('\n') if 'SSID' in line]

            # Update combo box with network names
            if networks:
                self.combo_networks.addItems(networks)
            else:
                self.combo_networks.addItem('No WiFi networks found.')
        except Exception as e:
            print("Error:", e)
            self.combo_networks.addItem('Error occurred while fetching networks.')

    def connect_to_network(self):
        selected_network = self.combo_networks.currentText()
        if selected_network:
            try:
                # Connect to the selected network
                output = subprocess.check_output(['netsh', 'wlan', 'connect', 'name=' + selected_network])
                output = output.decode('utf-8')
                if "successfully" in output:
                    self.lbl_status.setText(f"Successfully connected to '{selected_network}'.")
                else:
                    self.lbl_status.setText(f"Failed to connect to '{selected_network}'.")
            except Exception as e:
                print("Error:", e)
                self.lbl_status.setText(f"Error occurred while connecting to '{selected_network}'.")

class BatteryScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen,self).__init__()
        loadUi("battery.ui",self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        pixmap=QPixmap("assets//bg_splash.jpg")
        self.setPixmap(pixmap)


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


# Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
# Check your Python version and be sure it is installed on your machine

# Check the path environment variable

# Go to -> "start" and type "Manage App Execution Aliases". Go to it and turn off "Python"
