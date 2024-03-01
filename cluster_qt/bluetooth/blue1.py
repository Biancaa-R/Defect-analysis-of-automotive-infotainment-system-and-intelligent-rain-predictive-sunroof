import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QDialog
import bluetooth

class BluetoothDevicesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Nearby Bluetooth Devices')
        self.layout = QVBoxLayout()

        # Combo box to display nearby Bluetooth devices
        self.combo_devices = QComboBox()
        self.combo_devices.activated.connect(self.connect_to_device)  # Connect the activated signal to connect_to_device function
        self.layout.addWidget(self.combo_devices)

        # Button to refresh list of nearby Bluetooth devices
        self.btn_refresh = QPushButton('Refresh')
        self.btn_refresh.clicked.connect(self.refresh_devices)
        self.layout.addWidget(self.btn_refresh)

        self.setLayout(self.layout)

        # Refresh list of nearby Bluetooth devices
        self.refresh_devices()

    def refresh_devices(self):
        self.combo_devices.clear()

        # Discover nearby Bluetooth devices
        nearby_devices = bluetooth.discover_devices()

        # Add discovered devices to the combo box
        for bdaddr in nearby_devices:
            device_name = bluetooth.lookup_name(bdaddr)
            self.combo_devices.addItem(device_name, bdaddr)

    def connect_to_device(self, index):
        # Get the selected Bluetooth device's address from the combo box
        device_address = self.combo_devices.itemData(index)

        # Attempt to connect to the selected Bluetooth device
        try:
            socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            socket.connect((device_address, 1))
            print(f"Successfully connected to {self.combo_devices.currentText()}")
            # Add your further logic here after successful connection
        except Exception as e:
            print(f"Failed to connect to {self.combo_devices.currentText()}: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BluetoothDevicesWidget()
    ex.show()
    sys.exit(app.exec_())
