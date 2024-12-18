import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

class WordCounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Counter App")
        self.setGeometry(100, 100, 500, 350)

        # Set background color
        self.setStyleSheet("background-color: #f4f6f9;")

        # Create widgets
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Type or paste your text here...")
        self.text_edit.setStyleSheet("""
            background-color: #ffffff;
            font-size: 16px;
            padding: 12px;
            border-radius: 10px;
            border: 1px solid #ccc;
            color: #333;
        """)
        
        self.result_label = QLabel("Word Count: 0", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("""
            font-size: 20px;
            color: #3e8e41;
            font-weight: bold;
            margin-top: 10px;
        """)
        
        self.count_button = QPushButton("Count Words", self)
        self.count_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s;
        """)
        self.count_button.setFixedHeight(40)
        self.count_button.clicked.connect(self.count_words)
        self.count_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s;
        """)
        self.count_button.clicked.connect(self.count_words)
        
        # Hover effect for button
        self.count_button.setStyleSheet("""
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.count_button)
        layout.addWidget(self.result_label)
        
        # Add spacing and margin to layout
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)

        self.setLayout(layout)

    def count_words(self):
        text = self.text_edit.toPlainText()
        word_count = len(text.split())
        self.result_label.setText(f"Word Count: {word_count}")

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WordCounterApp()
    window.show()
    sys.exit(app.exec_())
