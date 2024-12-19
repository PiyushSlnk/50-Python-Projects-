import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QListWidget, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QColor


class PasswordManagerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Colorful Password Manager')
        self.setGeometry(300, 300, 500, 350)
        self.setStyleSheet("background-color: #f2f2f2;")

        self.passwords = {}  # Dictionary to store passwords
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title
        self.title = QLabel('Colorful Password Manager')
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #2C3E50;
        """)
        layout.addWidget(self.title)

        # Website/Service Input Section
        self.website_label = QLabel('Website/Service:')
        self.website_label.setStyleSheet("""
            font-size: 16px;
            color: #34495E;
        """)
        layout.addWidget(self.website_label)

        self.website_input = QLineEdit()
        self.website_input.setStyleSheet("""
            padding: 10px;
            font-size: 18px;
            border: 2px solid #2980B9;
            border-radius: 5px;
            background-color: #ecf0f1;
        """)
        layout.addWidget(self.website_input)

        # Password Input Section
        self.password_label = QLabel('Password:')
        self.password_label.setStyleSheet("""
            font-size: 16px;
            color: #34495E;
        """)
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            padding: 10px;
            font-size: 18px;
            border: 2px solid #2980B9;
            border-radius: 5px;
            background-color: #ecf0f1;
        """)
        layout.addWidget(self.password_input)

        # Eye Button to Show/Hide Password
        self.eye_button = QPushButton()
        self.eye_button.setIcon(QIcon('eye_off.png'))  # Eye icon for visibility toggle
        self.eye_button.setIconSize(self.eye_button.size())
        self.eye_button.setStyleSheet("background: none; border: none;")
        self.eye_button.clicked.connect(self.toggle_password_visibility)

        # Layout for the Password Input and Eye Button
        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_input)
        self.password_layout.addWidget(self.eye_button)
        layout.addLayout(self.password_layout)

        # Add Password Button
        self.add_button = QPushButton('Add Password')
        self.add_button.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
            border: none;
            margin-top: 20px;
        """)
        self.add_button.clicked.connect(self.add_password)
        layout.addWidget(self.add_button)

        # Saved Passwords List
        self.saved_passwords_label = QLabel('Saved Passwords:')
        self.saved_passwords_label.setStyleSheet("""
            font-size: 16px;
            color: #34495E;
        """)
        layout.addWidget(self.saved_passwords_label)

        self.saved_passwords_list = QListWidget()
        self.saved_passwords_list.setStyleSheet("""
            font-size: 14px;
            background-color: #ecf0f1;
            border: 1px solid #2980B9;
            border-radius: 5px;
        """)
        layout.addWidget(self.saved_passwords_list)

        # Set layout
        self.setLayout(layout)

    def toggle_password_visibility(self):
        """Toggle the visibility of the password"""
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.eye_button.setIcon(QIcon('eye_on.png'))  # Change to eye on icon
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.eye_button.setIcon(QIcon('eye_off.png'))  # Change to eye off icon

    def add_password(self):
        """Add the entered password to the password list"""
        website = self.website_input.text()
        password = self.password_input.text()

        if website and password:
            self.passwords[website] = password  # Store password
            self.saved_passwords_list.addItem(f"{website}: {password}")  # Add to list display
            self.clear_inputs()
        else:
            self.show_error_message()

    def clear_inputs(self):
        """Clear input fields after saving a password"""
        self.website_input.clear()
        self.password_input.clear()

    def show_error_message(self):
        """Show an error message if inputs are missing"""
        error_dialog = QInputDialog(self)
        error_dialog.setWindowTitle('Input Error')
        error_dialog.setLabelText('Both website and password are required!')
        error_dialog.setStyleSheet("""
            background-color: #e74c3c;
            color: white;
        """)
        error_dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec_())
