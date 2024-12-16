import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QHBoxLayout, QLabel, QListWidgetItem, QDialog, QFormLayout, QDateTimeEdit, QTextEdit
)
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QFont


class TaskDetailsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Task Details")
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")

        # Form layout for details
        self.form_layout = QFormLayout()

        # Task description input
        self.description_input = QTextEdit()
        self.description_input.setStyleSheet(
            "font-size: 16px; padding: 10px; border: 2px solid #00ADB5; border-radius: 5px; background-color: #393E46;"
        )
        self.form_layout.addRow("Description:", self.description_input)

        # Due date and time input
        self.due_date_input = QDateTimeEdit()
        self.due_date_input.setDateTime(QDateTime.currentDateTime())
        self.due_date_input.setCalendarPopup(True)
        self.due_date_input.setStyleSheet(
            "font-size: 16px; padding: 10px; border: 2px solid #00ADB5; border-radius: 5px; background-color: #393E46;"
        )
        self.form_layout.addRow("Due Date & Time:", self.due_date_input)

        # Buttons
        self.buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet(
            "background-color: #00ADB5; color: white; border-radius: 5px; padding: 8px;"
        )
        self.ok_button.clicked.connect(self.accept)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet(
            "background-color: #FF3E4D; color: white; border-radius: 5px; padding: 8px;"
        )
        self.cancel_button.clicked.connect(self.reject)

        self.buttons_layout.addWidget(self.ok_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.form_layout.addRow(self.buttons_layout)
        self.setLayout(self.form_layout)

    def get_details(self):
        return self.description_input.toPlainText(), self.due_date_input.dateTime()


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced To-Do List")
        self.setGeometry(100, 100, 500, 700)
        self.setStyleSheet("background-color: #2E2E2E; color: white;")
        self.initUI()

    def initUI(self):
        # Main layout
        self.layout = QVBoxLayout()

        # Heading
        self.heading = QLabel("My To-Do List")
        self.heading.setFont(QFont("Arial", 20, QFont.Bold))
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("color: #00ADB5; margin-bottom: 10px;")
        self.layout.addWidget(self.heading)

        # Input field and add button layout
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task title")
        self.task_input.setStyleSheet(
            "font-size: 18px; padding: 10px; border: 2px solid #00ADB5; border-radius: 10px; background-color: #393E46;"
        )
        self.add_button = QPushButton("Add Task")
        self.add_button.setStyleSheet(
            """
            QPushButton {
                font-size: 16px; color: white; background-color: #00ADB5; 
                border: 2px solid #00ADB5; border-radius: 10px; padding: 8px;
            }
            QPushButton:hover {
                background-color: #007B7F;
            }
            QPushButton:pressed {
                background-color: #006B6F;
            }
            """
        )
        self.add_button.clicked.connect(self.add_task)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)
        self.layout.addLayout(input_layout)

        # Task list
        self.task_list = QListWidget()
        self.task_list.setStyleSheet(
            "font-size: 18px; border: none; padding: 10px; background-color: #393E46; color: white;"
        )
        self.layout.addWidget(self.task_list)

        # Remove task button
        self.remove_button = QPushButton("Remove Selected")
        self.remove_button.setStyleSheet(
            """
            QPushButton {
                font-size: 16px; color: white; background-color: #FF3E4D; 
                border: 2px solid #FF3E4D; border-radius: 10px; padding: 8px;
            }
            QPushButton:hover {
                background-color: #FF1E3D;
            }
            QPushButton:pressed {
                background-color: #FF0E2D;
            }
            """
        )
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)

    def add_task(self):
        task_title = self.task_input.text().strip()
        if not task_title:
            return

        dialog = TaskDetailsDialog()
        if dialog.exec_() == QDialog.Accepted:
            description, due_date = dialog.get_details()
            task_item = QListWidgetItem(f"{task_title}\nDescription: {description}\nDue: {due_date.toString('yyyy-MM-dd hh:mm AP')}")
            task_item.setFlags(task_item.flags() | Qt.ItemIsUserCheckable)
            task_item.setCheckState(Qt.Unchecked)
            self.task_list.addItem(task_item)
            self.task_input.clear()

    def remove_task(self):
        for item in self.task_list.selectedItems():
            self.task_list.takeItem(self.task_list.row(item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())
