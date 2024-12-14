import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import aspose.words as aw

class WordToPDFConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Word to PDF Converter')
        self.setGeometry(100, 100, 400, 300)

        # Set up the main layout
        main_layout = QVBoxLayout()

        # Title label
        self.title_label = QLabel('Word to PDF Converter')
        self.title_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Instruction label
        self.instruction_label = QLabel('Select a Word file and convert it to PDF:')
        self.instruction_label.setFont(QFont('Arial', 12))
        self.instruction_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.instruction_label)

        # Buttons layout
        button_layout = QHBoxLayout()

        self.button_select = QPushButton('Select Word File')
        self.button_select.setFont(QFont('Arial', 10))
        self.button_select.clicked.connect(self.select_file)
        button_layout.addWidget(self.button_select)

        self.button_convert = QPushButton('Convert to PDF')
        self.button_convert.setFont(QFont('Arial', 10))
        self.button_convert.clicked.connect(self.convert_file)
        button_layout.addWidget(self.button_convert)

        main_layout.addLayout(button_layout)

        # Status label
        self.status_label = QLabel('')
        self.status_label.setFont(QFont('Arial', 10))
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Set the main layout
        self.setLayout(main_layout)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Word File", "", "Word Files (*.docx);;All Files (*)", options=options)

        if file_name:
            self.word_file = file_name
            self.status_label.setText(f"Selected File: {file_name}")

    def convert_file(self):
        if not hasattr(self, 'word_file') or not self.word_file:
            QMessageBox.warning(self, 'Error', 'Please select a Word file first.')
            return

        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        save_path, _ = QFileDialog.getSaveFileName(self, "Save PDF File As", "", "PDF Files (*.pdf)", options=options)

        if save_path:
            try:
                doc = aw.Document(self.word_file)
                doc.save(save_path)
                QMessageBox.information(self, 'Success', f'File converted successfully and saved as {save_path}')
                self.status_label.setText('Conversion successful!')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to convert the file: {e}')
                self.status_label.setText('Conversion failed.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = WordToPDFConverterApp()
    converter.show()
    sys.exit(app.exec_())
