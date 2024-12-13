import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox, QLabel
from PyQt5.QtCore import QProcess

class CodeCompiler(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Code Compiler')
        
        layout = QVBoxLayout()

        # Label for instructions
        self.label = QLabel('Enter your code and select the language:')
        layout.addWidget(self.label)

        # Text editor for code input
        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)

        # Language selection
        self.languageCombo = QComboBox(self)
        self.languageCombo.addItem("Python")
        self.languageCombo.addItem("C")
        self.languageCombo.addItem("Java")
        self.languageCombo.addItem("JavaScript")
        layout.addWidget(self.languageCombo)

        # Compile button
        self.compileButton = QPushButton('Compile and Run', self)
        self.compileButton.clicked.connect(self.compileCode)
        layout.addWidget(self.compileButton)

        # Output display area
        self.outputArea = QTextEdit(self)
        self.outputArea.setReadOnly(True)
        layout.addWidget(self.outputArea)

        self.setLayout(layout)

    def compileCode(self):
        code = self.textEdit.toPlainText()
        language = self.languageCombo.currentText()
        output = ""

        if language == "Python":
            # Save the Python code to a file and execute it
            with open("temp.py", "w") as file:
                file.write(code)
            output = self.runPython()

        elif language == "C":
            # Save the C code to a file, compile, and execute
            with open("temp.c", "w") as file:
                file.write(code)
            output = self.runC()

        elif language == "Java":
            # Save the Java code to a file, compile, and execute
            with open("temp.java", "w") as file:
                file.write(code)
            output = self.runJava()

        elif language == "JavaScript":
            # Save the JavaScript code to a file and execute
            with open("temp.js", "w") as file:
                file.write(code)
            output = self.runJavaScript()

        self.outputArea.setText(output)

    def runPython(self):
        try:
            result = subprocess.run(['python', 'temp.py'], capture_output=True, text=True)
            return result.stdout + result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

    def runC(self):
        try:
            # Compile C code
            subprocess.run(['gcc', 'temp.c', '-o', 'temp.out'], check=True)
            # Run the compiled code
            result = subprocess.run(['./temp.out'], capture_output=True, text=True)
            return result.stdout + result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

    def runJava(self):
        try:
            # Compile Java code
            subprocess.run(['javac', 'temp.java'], check=True)
            # Run the compiled Java code
            result = subprocess.run(['java', 'temp'], capture_output=True, text=True)
            return result.stdout + result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

    def runJavaScript(self):
        try:
            result = subprocess.run(['node', 'temp.js'], capture_output=True, text=True)
            return result.stdout + result.stderr
        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CodeCompiler()
    window.show()
    sys.exit(app.exec_())
