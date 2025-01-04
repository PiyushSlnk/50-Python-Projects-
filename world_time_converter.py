import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QTime, Qt
import pytz
from datetime import datetime

class WorldTimeConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("World Time Converter")
        self.setGeometry(300, 300, 500, 300)  # Set the window size to medium

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f8ff;
                font-size: 16px;
                color: #333;
            }
            QLabel {
                font-weight: bold;
                color: #005f6b;
            }
            QComboBox {
                background-color: #e0f7fa;
                border: 1px solid #00796b;
                color: #00796b;
            }
            QLineEdit {
                background-color: #e8f5e9;
                border: 1px solid #388e3c;
                color: #388e3c;
            }
            QPushButton {
                background-color: #64b5f6;
                border: 1px solid #1976d2;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #42a5f5;
            }
        """)

        # Create layout
        layout = QVBoxLayout()
        time_layout = QHBoxLayout()

        # Widgets
        self.time_input = QLineEdit(self)
        self.time_input.setPlaceholderText("Enter time (HH:MM)")
        self.time_zone_from = QComboBox(self)
        self.time_zone_to = QComboBox(self)
        self.result_label = QLabel("Converted Time: ", self)
        self.convert_button = QPushButton("Convert", self)

        # Add items to combo boxes
        self.time_zone_from.addItems(pytz.all_timezones)
        self.time_zone_to.addItems(pytz.all_timezones)

        # Add widgets to layout
        time_layout.addWidget(QLabel("From Time Zone: "))
        time_layout.addWidget(self.time_zone_from)
        time_layout.addWidget(QLabel("To Time Zone: "))
        time_layout.addWidget(self.time_zone_to)

        layout.addLayout(time_layout)
        layout.addWidget(self.time_input)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.result_label)

        # Set the layout to the window
        self.setLayout(layout)

        # Connect the button
        self.convert_button.clicked.connect(self.convert_time)

    def convert_time(self):
        try:
            # Get input time and time zones
            input_time_str = self.time_input.text()
            from_zone = self.time_zone_from.currentText()
            to_zone = self.time_zone_to.currentText()

            # Parse the input time
            input_time = datetime.strptime(input_time_str, "%H:%M")

            # Get time zones
            from_tz = pytz.timezone(from_zone)
            to_tz = pytz.timezone(to_zone)

            # Localize input time
            localized_time = from_tz.localize(input_time)

            # Convert to target time zone
            converted_time = localized_time.astimezone(to_tz)

            # Display the result
            self.result_label.setText(f"Converted Time: {converted_time.strftime('%H:%M %p')}")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WorldTimeConverter()
    window.show()
    sys.exit(app.exec_())
