from PyQt5 import QtWidgets, QtGui

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLabel widget
        self.label = QtWidgets.QLabel(self)
        #from PyQt5.QtGui import QPixmap

        # Load QPixmap from an image file
        #pixmap = QPixmap("path/to/image.png")

        # Load the image using QPixmap
        pixmap = QtGui.QPixmap(":C:\Users\Biancaa. R\Downloads\cluster\Smart-CAR-Dashboard-GUI-in-Python-main\bg1.jpg")

        # Set the pixmap on the QLabel
        self.label.setPixmap(pixmap)

        # Resize the window to fit the image
        self.resize(pixmap.width(), pixmap.height())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
