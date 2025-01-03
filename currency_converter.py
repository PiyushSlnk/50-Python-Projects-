import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTabWidget, QHBoxLayout
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

# Fetch exchange rates from API
def fetch_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except Exception as e:
        print("Error fetching exchange rates:", e)
        return None

class CurrencyConverterTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # Fetch exchange rates
        self.rates = fetch_exchange_rates()
        if not self.rates:
            QMessageBox.critical(self, "Error", "Failed to fetch exchange rates!")
            sys.exit()

        # Populate currencies in dropdowns
        self.base_currency.addItems(self.rates.keys())
        self.target_currency.addItems(self.rates.keys())

    def initUI(self):
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #34495e;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #34495e;
                border-radius: 8px;
                background: #ecf0f1;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                padding: 8px;
                border: none;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel#resultLabel {
                font-size: 16px;
                color: #2c3e50;
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout()

        self.label_amount = QLabel("Enter Amount:")
        self.amount_input = QLineEdit()
        self.label_base_currency = QLabel("Base Currency:")
        self.base_currency = QComboBox()
        self.label_target_currency = QLabel("Target Currency:")
        self.target_currency = QComboBox()
        self.result_label = QLabel("Converted Amount: -")
        self.result_label.setObjectName("resultLabel")

        self.convert_button = QPushButton("Convert Currency")
        self.convert_button.clicked.connect(self.convert_currency)

        layout.addWidget(self.label_amount)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.label_base_currency)
        layout.addWidget(self.base_currency)
        layout.addWidget(self.label_target_currency)
        layout.addWidget(self.target_currency)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            base = self.base_currency.currentText()
            target = self.target_currency.currentText()

            if base in self.rates and target in self.rates:
                converted = amount * (self.rates[target] / self.rates[base])
                self.result_label.setText(f"Converted Amount: {converted:.2f} {target}")
            else:
                QMessageBox.warning(self, "Invalid Input", "Invalid currency selected!")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid amount!")

class AboutTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        about_text = QLabel(
            "💸 Welcome to the Currency Converter App! 💸\n\n"
            "Features:\n"
            "- Convert between 150+ currencies\n"
            "- Real-time exchange rates\n"
            "- Easy-to-use interface\n\n"
            "Designed By ❤️ Piyush "
        )
        about_text.setFont(QFont("Arial", 12))
        about_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(about_text)
        self.setLayout(layout)

class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Converter - Tabbed Interface")
        self.setGeometry(100, 100, 400, 300)

        # Add tabs
        self.addTab(CurrencyConverterTab(), "Currency Converter")
        self.addTab(AboutTab(), "About App")

        # Add app icon
        self.setWindowIcon(QIcon("currency_icon.png"))  # Optional: Add an icon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
