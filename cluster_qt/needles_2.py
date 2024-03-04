import sys
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QRadialGradient, QPolygonF

import math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTimer, Qt, QPointF
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QRadialGradient


class CircularNeedleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(30)  # Update every 30 milliseconds (33 fps)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
        painter.setWindow(-50, -50, 100, 100)
        
        # Draw main circle
        gradient = QRadialGradient(0, 0, 45)
        gradient.setColorAt(0, Qt.lightGray)
        gradient.setColorAt(1, Qt.darkGray)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(-45, -45, 90, 90)
        
        # Draw needle
        painter.save()
        painter.translate(0, -3)
        painter.rotate(self.angle)
        gradient = QRadialGradient(0, 0, 35)
        gradient.setColorAt(0, Qt.green)
        gradient.setColorAt(1, Qt.darkGreen)
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        
        # Define needle shape
        needle = QPolygonF([
            QPointF(-3, 0),
            QPointF(3, 0),
            QPointF(0, -30)
        ])
        painter.drawConvexPolygon(needle)
        
        painter.restore()
    
    def updateAnimation(self):
        self.angle += 1  # Adjust the speed of rotation here
        if self.angle >= 360:
            self.angle = 0
        self.update()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Fancy Circular Needle")
        self.setGeometry(100, 100, 400, 400)
        
        self.circularNeedleWidget = CircularNeedleWidget(self)
        self.circularNeedleWidget.setGeometry(50, 50, 300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
