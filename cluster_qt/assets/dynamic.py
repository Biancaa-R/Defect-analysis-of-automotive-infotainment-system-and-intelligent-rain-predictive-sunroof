from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(250, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Define a label for displaying GIF
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(2000, 2000))
        self.label.setMaximumSize(QtCore.QSize(2000, 2000))
        self.label.setObjectName("label")

        # Embed the label into the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Integrate QMovie to the label and initiate the GIF
        self.movie = QMovie("saving.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())