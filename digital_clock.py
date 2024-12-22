import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import QTimer, QTime, Qt  # Added Qt import
from PyQt5.QtGui import QFont, QPalette, QColor

class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set up the main window
        self.setWindowTitle("Digital Clock")
        self.setGeometry(100, 100, 400, 200)

        # Set up the clock display
        self.clock_label = QLabel(self)
        self.clock_label.setAlignment(Qt.AlignCenter)  # Align text to center
        self.clock_label.setFont(QFont("Helvetica", 40, QFont.Bold))
        self.clock_label.setStyleSheet("color: white;")
        self.setCentralWidget(self.clock_label)  # Ensure proper alignment

        # Set up the main window background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        self.setPalette(palette)

        # Timer to update the clock
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
