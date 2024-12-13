import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
)
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 350, 500)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")
        self.initUI()

    def initUI(self):
        # Main layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)

        # Display widget
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            "font-size: 32px; padding: 10px; border: 2px solid #00ADB5; border-radius: 10px; background-color: #393E46;"
        )
        self.layout.addWidget(self.display)

        # Buttons layout
        self.buttons_layout = QGridLayout()

        # Button labels
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Add buttons to the grid
        row, col = 0, 0
        for button in buttons:
            button_widget = QPushButton(button)
            button_widget.setFixedSize(75, 75)
            button_widget.setStyleSheet(
                """
                QPushButton {
                    font-size: 20px;
                    color: #EEEEEE;
                    background-color: #00ADB5;
                    border: 2px solid #00ADB5;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #007B7F;
                }
                QPushButton:pressed {
                    background-color: #006B6F;
                }
                """
            )
            button_widget.clicked.connect(lambda checked, b=button: self.on_button_click(b))
            self.buttons_layout.addWidget(button_widget, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)

    def on_button_click(self, button):
        if button == 'C':
            self.display.clear()
        elif button == '=':
            try:
                expression = self.display.text()
                result = eval(expression)  # Evaluate the expression
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
