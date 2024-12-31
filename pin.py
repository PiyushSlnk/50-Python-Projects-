from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class PinnedNoteApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pinned Note")
        self.setGeometry(200, 200, 500, 400)
        self.setStyleSheet("background-color: #FAF3E0;")

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Title Label
        title_label = QLabel("Pinned Note Application")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #3E497A; margin: 10px;")
        main_layout.addWidget(title_label)

        # Note Editor
        self.note_editor = QTextEdit()
        self.note_editor.setPlaceholderText("Write your note here...")
        self.note_editor.setStyleSheet(
            "padding: 10px; font-size: 14px; border: 1px solid #CCCCCC; border-radius: 5px; background-color: #FFFFFF;"
        )
        input_layout.addWidget(self.note_editor)

        # Buttons
        pin_button = QPushButton("Pin Note")
        pin_button.setStyleSheet(
            "background-color: #2ECC71; color: white; font-size: 14px; padding: 10px; border-radius: 5px;"
        )
        pin_button.clicked.connect(self.pin_note)

        clear_button = QPushButton("Clear Note")
        clear_button.setStyleSheet(
            "background-color: #E74C3C; color: white; font-size: 14px; padding: 10px; border-radius: 5px;"
        )
        clear_button.clicked.connect(self.clear_note)

        button_layout.addWidget(pin_button)
        button_layout.addWidget(clear_button)
        input_layout.addLayout(button_layout)
        main_layout.addLayout(input_layout)

        # Pinned Note Display
        self.pinned_note_label = QLabel("No pinned note yet!")
        self.pinned_note_label.setFont(QFont("Arial", 16))
        self.pinned_note_label.setAlignment(Qt.AlignCenter)
        self.pinned_note_label.setStyleSheet(
            "padding: 15px; font-size: 16px; color: #34495E; border: 2px solid #95A5A6; border-radius: 5px; background-color: #ECF0F1;"
        )
        main_layout.addWidget(self.pinned_note_label)

        # Footer
        footer = QLabel("Developed with ❤️ by Pijush Singh")
        footer_font = QFont("Arial", 10)
        footer_font.setItalic(True)
        footer.setFont(footer_font)
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #7F8C8D; margin-top: 20px;")
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

    def pin_note(self):
        note_text = self.note_editor.toPlainText().strip()

        if not note_text:
            QMessageBox.warning(self, "Error", "Please write something to pin!")
            return

        self.pinned_note_label.setText(note_text)
        self.note_editor.clear()
        QMessageBox.information(self, "Pinned", "Your note has been pinned!")

    def clear_note(self):
        self.note_editor.clear()
        QMessageBox.information(self, "Cleared", "The note editor has been cleared!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = PinnedNoteApp()
    window.show()
    sys.exit(app.exec_())
