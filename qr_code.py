import sys
import qrcode
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from PIL import Image

class QRCodeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QR Code Generator')
        self.setGeometry(200, 200, 400, 300)

        # Layout and widgets
        self.layout = QVBoxLayout()

        # URL input field
        self.link_input = QLineEdit(self)
        self.link_input.setPlaceholderText("Enter website URL here")

        # Generate button
        self.generate_btn = QPushButton("Generate QR Code", self)

        # Label to show the QR code
        self.qr_label = QLabel(self)

        # Add widgets to layout
        self.layout.addWidget(self.link_input)
        self.layout.addWidget(self.generate_btn)
        self.layout.addWidget(self.qr_label)

        # Set layout to window
        self.setLayout(self.layout)

        # Connect button to function
        self.generate_btn.clicked.connect(self.generate_qr_code)

    def generate_qr_code(self):
        # Get URL from input field
        url = self.link_input.text()
        if url:
            # Generate QR code
            qr_img = qrcode.make(url)

            # Convert the QR code to a QImage object that PyQt can display
            qr_img = qr_img.convert("RGBA")  # Convert to RGBA for color support
            img_data = qr_img.tobytes("raw", "RGBA")
            qimage = QImage(img_data, qr_img.width, qr_img.height, QImage.Format_RGBA8888)

            # Create a pixmap from the QImage and display it
            pixmap = QPixmap.fromImage(qimage)
            self.qr_label.setPixmap(pixmap)
            self.qr_label.setScaledContents(True)

# Entry point to start the app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec_())
