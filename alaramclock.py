import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QComboBox, QTimeEdit, QWidget, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QTimer, QTime, Qt
import pytz
from datetime import datetime


class AlarmClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alarm Clock with Time Zone")
        self.setGeometry(100, 100, 500, 500)

        # Apply background color
        self.setStyleSheet("background-color: #ffffff;")  # White background

        # Main layout
        self.layout = QVBoxLayout()

        # Title label
        self.title_label = QLabel("⏰ Alarm Clock with Time Zone")
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setStyleSheet("color: #4A90E2;")  # Blue
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Current time label
        self.current_time_label = QLabel("Current Time: Loading...")
        self.current_time_label.setFont(QFont("Arial", 14))
        self.current_time_label.setStyleSheet("color: #333333;")  # Dark gray
        self.layout.addWidget(self.current_time_label)

        # Time Zone selection
        self.time_zone_label = QLabel("🌐 Select Time Zone:")
        self.time_zone_label.setFont(QFont("Arial", 14))
        self.time_zone_label.setStyleSheet("color: #4A90E2;")  # Blue
        self.layout.addWidget(self.time_zone_label)

        self.time_zone_combo = QComboBox()
        self.time_zone_combo.addItems(pytz.all_timezones)
        self.time_zone_combo.setStyleSheet(
            """
            background-color: #f9f9f9; 
            border: 1px solid #dddddd; 
            padding: 8px; 
            font-size: 12px;
            """
        )
        self.layout.addWidget(self.time_zone_combo)

        # Alarm time selector
        self.alarm_label = QLabel("⏱️ Set Alarm Time:")
        self.alarm_label.setFont(QFont("Arial", 14))
        self.alarm_label.setStyleSheet("color: #4A90E2;")  # Blue
        self.layout.addWidget(self.alarm_label)

        self.alarm_time = QTimeEdit()
        self.alarm_time.setDisplayFormat("HH:mm:ss")
        self.alarm_time.setStyleSheet(
            """
            background-color: #f9f9f9; 
            border: 1px solid #dddddd; 
            padding: 8px; 
            font-size: 14px;
            """
        )
        self.layout.addWidget(self.alarm_time)

        # Set alarm button
        self.set_alarm_button = QPushButton("🔔 Set Alarm")
        self.set_alarm_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.set_alarm_button.setStyleSheet(
            """
            background-color: #28a745; 
            color: white; 
            border-radius: 5px; 
            padding: 10px;
            """
        )
        self.set_alarm_button.clicked.connect(self.set_alarm)
        self.layout.addWidget(self.set_alarm_button)

        # Alarm status
        self.alarm_status = QLabel("🚫 Alarm Status: Not Set")
        self.alarm_status.setFont(QFont("Arial", 14))
        self.alarm_status.setStyleSheet("color: #ff6347;")  # Red
        self.layout.addWidget(self.alarm_status)

        # Timer for updating the current time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        # Main widget setup
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # Variables for alarm
        self.alarm_set_time = None
        self.alarm_time_zone = None

    def update_time(self):
        """Update current time based on selected time zone."""
        selected_time_zone = self.time_zone_combo.currentText()
        time_zone = pytz.timezone(selected_time_zone)
        current_time = datetime.now(time_zone).strftime("%H:%M:%S")
        self.current_time_label.setText(f"🕒 Current Time: {current_time}")

        # Check if alarm is due
        if self.alarm_set_time and self.alarm_time_zone:
            alarm_tz = pytz.timezone(self.alarm_time_zone)
            current_time_in_alarm_tz = datetime.now(alarm_tz).strftime("%H:%M:%S")
            if current_time_in_alarm_tz == self.alarm_set_time:
                self.trigger_alarm()

    def set_alarm(self):
        """Set the alarm time."""
        self.alarm_set_time = self.alarm_time.time().toString("HH:mm:ss")
        self.alarm_time_zone = self.time_zone_combo.currentText()
        self.alarm_status.setText(
            f"✅ Alarm Set for {self.alarm_set_time} in {self.alarm_time_zone}"
        )
        QMessageBox.information(
            self,
            "Alarm Set",
            f"Alarm has been set for {self.alarm_set_time} in {self.alarm_time_zone}",
        )

    def trigger_alarm(self):
        """Trigger the alarm."""
        self.alarm_set_time = None  # Reset the alarm
        self.alarm_status.setText("🚫 Alarm Status: Not Set")
        QMessageBox.warning(self, "Alarm", "⏰ Time's up!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set application icon (optional)
    app.setWindowIcon(QIcon("alarm_icon.png"))  # Add a custom icon if available

    clock = AlarmClock()
    clock.show()
    sys.exit(app.exec_())
