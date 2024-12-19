import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

class PasswordApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Secure Password Entry')
        self.setGeometry(300, 300, 500, 250)
        self.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()

        # Title
        self.title = QLabel('Secure Password Entry')
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #2C3E50;
        """)
        layout.addWidget(self.title)

        # Password Input Section
        self.password_label = QLabel('Enter your password:')
        self.password_label.setStyleSheet("""
            font-size: 16px;
            color: #34495E;
        """)
        layout.addWidget(self.password_label)

        self.password_layout = QHBoxLayout()

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            padding: 10px;
            font-size: 18px;
            border: 2px solid #2980B9;
            border-radius: 5px;
            background-color: #ecf0f1;
            min-width: 300px;
        """)

        self.eye_button = QPushButton()
        self.eye_button.setIcon(QIcon(QPixmap('eye_off.png')))  # You can replace this with your own eye icon image
        self.eye_button.setIconSize(self.eye_button.size())
        self.eye_button.setStyleSheet("background: none; border: none;")
        self.eye_button.clicked.connect(self.toggle_password_visibility)

        self.password_layout.addWidget(self.password_input)
        self.password_layout.addWidget(self.eye_button)

        layout.addLayout(self.password_layout)

        # Password Strength Indicator
        self.strength_label = QLabel('Password Strength: ')
        self.strength_label.setStyleSheet("""
            font-size: 14px;
            color: #7F8C8D;
        """)
        layout.addWidget(self.strength_label)

        self.password_input.textChanged.connect(self.update_password_strength)

        # Submit Button
        self.submit_button = QPushButton('Submit')
        self.submit_button.setStyleSheet("""
            background-color: #2980B9;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
            border: none;
            margin-top: 20px;
        """)
        self.submit_button.clicked.connect(self.submit_password)
        layout.addWidget(self.submit_button)

        # Feedback Label
        self.feedback_label = QLabel('')
        self.feedback_label.setAlignment(Qt.AlignCenter)
        self.feedback_label.setStyleSheet("""
            font-size: 14px;
            color: #e74c3c;
        """)
        layout.addWidget(self.feedback_label)

        # Set layout
        self.setLayout(layout)

    def toggle_password_visibility(self):
        """Toggle the visibility of the password"""
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.eye_button.setIcon(QIcon(QPixmap('eye_on.png')))  # Replace with the 'eye on' image
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.eye_button.setIcon(QIcon(QPixmap('eye_off.png')))  # Replace with the 'eye off' image

    def update_password_strength(self):
        """Update password strength indicator"""
        password = self.password_input.text()
        strength = self.check_password_strength(password)
        self.strength_label.setText(f'Password Strength: {strength["label"]}')
        self.strength_label.setStyleSheet(f"color: {strength['color']};")

    def check_password_strength(self, password):
        """Evaluate the strength of the password"""
        if len(password) < 6:
            return {"label": "Weak", "color": "#e74c3c"}  # Red color for weak password
        elif len(password) < 10:
            return {"label": "Medium", "color": "#f39c12"}  # Yellow color for medium password
        else:
            return {"label": "Strong", "color": "#27ae60"}  # Green color for strong password

    def submit_password(self):
        """Simulate password submission and validate"""
        password = self.password_input.text()
        if password:
            self.feedback_label.setText('Password entered successfully!')
            self.feedback_label.setStyleSheet("color: #2ecc71;")  # Green success message
        else:
            self.feedback_label.setText('Please enter a valid password.')
            self.feedback_label.setStyleSheet("color: #e74c3c;")  # Red error message

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordApp()
    ex.show()
    sys.exit(app.exec_())
