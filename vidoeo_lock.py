import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox, QHBoxLayout, QProgressBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class VideoLockerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Video Locker & Unlocker")
        self.setGeometry(300, 300, 500, 400)
        self.setStyleSheet("""
            QWidget {
                background-color: #f9f9f9;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QLineEdit {
                font-size: 14px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            QPushButton {
                font-size: 14px;
                padding: 10px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)

        # UI Elements
        self.label = QLabel("Select a video file and enter a password:")
        self.label.setAlignment(Qt.AlignCenter)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.select_button = QPushButton("Select Video")
        self.select_button.setIcon(QIcon("icons/select.png"))

        self.lock_button = QPushButton("Lock Video")
        self.lock_button.setIcon(QIcon("icons/lock.png"))

        self.unlock_button = QPushButton("Unlock Video")
        self.unlock_button.setIcon(QIcon("icons/unlock.png"))

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.select_button)
        button_layout.addWidget(self.lock_button)
        button_layout.addWidget(self.unlock_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        # Button Click Events
        self.select_button.clicked.connect(self.select_video)
        self.lock_button.clicked.connect(self.lock_video)
        self.unlock_button.clicked.connect(self.unlock_video)

        # Variables
        self.video_file = None

    def select_video(self):
        file_dialog = QFileDialog()
        self.video_file, _ = file_dialog.getOpenFileName(self, "Select Video", "", "Video Files (*.mp4 *.avi *.mkv)")
        if self.video_file:
            self.label.setText(f"Selected: {self.video_file}")

    def xor_encrypt_decrypt(self, file_path, key):
        """Encrypts or decrypts a file using XOR cipher."""
        try:
            self.progress_bar.setValue(25)
            output_file = file_path + ".tmp"
            key_bytes = bytearray(key.encode('utf-8'))
            with open(file_path, "rb") as f_in, open(output_file, "wb") as f_out:
                data = bytearray(f_in.read())
                for i in range(len(data)):
                    data[i] ^= key_bytes[i % len(key_bytes)]
                f_out.write(data)
            os.remove(file_path)
            os.rename(output_file, file_path)
            self.progress_bar.setValue(100)
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    def lock_video(self):
        if not self.video_file:
            QMessageBox.warning(self, "Error", "No video selected!")
            return

        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Error", "Password cannot be empty!")
            return

        try:
            self.xor_encrypt_decrypt(self.video_file, password)
            QMessageBox.information(self, "Success", "Video locked successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.progress_bar.setValue(0)

    def unlock_video(self):
        if not self.video_file:
            QMessageBox.warning(self, "Error", "No video selected!")
            return

        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Error", "Password cannot be empty!")
            return

        try:
            self.xor_encrypt_decrypt(self.video_file, password)
            QMessageBox.information(self, "Success", "Video unlocked successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.progress_bar.setValue(0)


if __name__ == "__main__":
    app = QApplication([])
    window = VideoLockerApp()
    window.show()
    app.exec_()
