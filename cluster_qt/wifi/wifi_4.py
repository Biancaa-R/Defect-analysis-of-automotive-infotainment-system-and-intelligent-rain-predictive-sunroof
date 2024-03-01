import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QDialog, QLineEdit, QHBoxLayout
import subprocess

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Enter Password')
        self.layout = QVBoxLayout()

        # Label for password entry
        self.label_password = QLabel('Enter the password:')
        self.layout.addWidget(self.label_password)

        # Password input field
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        # Button to confirm password
        self.btn_confirm = QPushButton('Connect')
        self.btn_confirm.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_confirm)

        self.setLayout(self.layout)

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
            output = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=bssid'])
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
                # Check if the network requires a password
                output = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'name=' + selected_network])
                output = output.decode('utf-8')
                if "Security key           : Absent" not in output:
                    # Password required, show dialog
                    dialog = PasswordDialog()
                    if dialog.exec_():
                        password = dialog.password_input.text()
                        if password:
                            # Connect to the network with the provided password
                            command = ['netsh', 'wlan', 'connect', 'name=' + selected_network, 'password=' + password]
                            output = subprocess.check_output(command)
                            output = output.decode('utf-8')
                            if "successfully" in output:
                                self.lbl_status.setText(f"Successfully connected to '{selected_network}'.")
                            else:
                                self.lbl_status.setText(f"Failed to connect to '{selected_network}'.")
                        else:
                            self.lbl_status.setText("Please enter a password.")
                else:
                    # No password required
                    output = subprocess.check_output(['netsh', 'wlan', 'connect', 'name=' + selected_network])
                    output = output.decode('utf-8')
                    if "successfully" in output:
                        self.lbl_status.setText(f"Successfully connected to '{selected_network}'.")
                    else:
                        self.lbl_status.setText(f"Failed to connect to '{selected_network}'.")
            except subprocess.CalledProcessError as e:
                print("Error:", e)
                self.lbl_status.setText(f"Error occurred while connecting to '{selected_network}'.")
            except Exception as e:
                print("Unexpected error:", e)
                self.lbl_status.setText("An unexpected error occurred.")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WiFiNetworksWidget()
    ex.show()
    sys.exit(app.exec_())
