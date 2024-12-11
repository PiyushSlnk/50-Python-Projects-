import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QFormLayout, QInputDialog, QTableWidget, QTableWidgetItem, QDateEdit
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt, QDate

class AttendanceApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Attendance Checker")
        self.setGeometry(100, 100, 800, 600)

        # List of students with their details (name, email, phone, attendance, image)
        self.students = [
            {"name": "John", "email": "john@example.com", "phone": "1234567890", "attendance": {"2024-12-11": "Absent"}, "image": "student.png"},
            {"name": "Jane", "email": "jane@example.com", "phone": "0987654321", "attendance": {"2024-12-11": "Absent"}, "image": "student.png"},
            {"name": "Sam", "email": "sam@example.com", "phone": "1122334455", "attendance": {"2024-12-11": "Absent"}, "image": "student.png"},
            {"name": "Alice", "email": "alice@example.com", "phone": "2233445566", "attendance": {"2024-12-11": "Absent"}, "image": "student.png"},
            {"name": "Bob", "email": "bob@example.com", "phone": "5566778899", "attendance": {"2024-12-11": "Absent"}, "image": "student.png"}
        ]

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header Label (Attendance Book)
        header = QLabel("Attendance Book")
        header.setStyleSheet("font-size: 36px; font-weight: bold; color: white; background-color: #4CAF50; padding: 20px; text-align: center;")
        layout.addWidget(header)

        # Date picker widget to select the date
        self.date_picker = QDateEdit(self)
        self.date_picker.setDate(QDate.currentDate())  # Default date is today's date
        self.date_picker.setDisplayFormat("yyyy-MM-dd")  # Display format as YYYY-MM-DD
        self.date_picker.setStyleSheet("font-size: 14px; padding: 5px; margin: 10px;")
        layout.addWidget(self.date_picker)

        # Table for displaying student details (name, email, phone, attendance)
        self.table = QTableWidget()
        self.table.setRowCount(len(self.students))
        self.table.setColumnCount(6)  # Now with a date column
        self.table.setHorizontalHeaderLabels(["Image", "Name", "Email", "Phone", "Attendance", "Date"])

        # Set the table to stretch across the entire window width
        self.table.horizontalHeader().setSectionResizeMode(0, 1)  # For image column, make it auto resize
        self.table.horizontalHeader().setSectionResizeMode(1, 3)  # Name column should take up a significant portion of the width
        self.table.horizontalHeader().setSectionResizeMode(2, 2)  # Email column
        self.table.horizontalHeader().setSectionResizeMode(3, 2)  # Phone column
        self.table.horizontalHeader().setSectionResizeMode(4, 1)  # Attendance column
        self.table.horizontalHeader().setSectionResizeMode(5, 1)  # Date column

        # Set the background color of the table and rows
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f9f9f9;
                color: #333;
                font-size: 14px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
            }
            QTableWidget::item:hover {
                background-color: #e0e0e0;
            }
        """)

        self.update_table()

        layout.addWidget(self.table)

        # Buttons to mark attendance and add new student
        button_layout = QHBoxLayout()

        self.present_button = QPushButton("Mark Present")
        self.absent_button = QPushButton("Mark Absent")
        self.update_details_button = QPushButton("Update Student Details")
        self.add_student_button = QPushButton("Add New Student")

        # Style buttons
        self.present_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 10px;")
        self.absent_button.setStyleSheet("background-color: #F44336; color: white; font-size: 14px; padding: 10px;")
        self.update_details_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 14px; padding: 10px;")
        self.add_student_button.setStyleSheet("background-color: #FFC107; color: white; font-size: 14px; padding: 10px;")

        button_layout.addWidget(self.present_button)
        button_layout.addWidget(self.absent_button)
        button_layout.addWidget(self.update_details_button)
        button_layout.addWidget(self.add_student_button)

        self.present_button.clicked.connect(self.mark_present)
        self.absent_button.clicked.connect(self.mark_absent)
        self.update_details_button.clicked.connect(self.update_student_details)
        self.add_student_button.clicked.connect(self.add_new_student)

        layout.addLayout(button_layout)

        # Setting layout to the window
        self.setLayout(layout)

    def mark_present(self):
        student, ok = self.select_student()
        if ok:
            selected_date = self.date_picker.date().toString("yyyy-MM-dd")
            student["attendance"][selected_date] = "Present"
            self.update_table()

    def mark_absent(self):
        student, ok = self.select_student()
        if ok:
            selected_date = self.date_picker.date().toString("yyyy-MM-dd")
            student["attendance"][selected_date] = "Absent"
            self.update_table()

    def select_student(self):
        """ Pop-up to select a student """
        student_names = [s["name"] for s in self.students]
        student, ok = QInputDialog.getItem(self, "Select Student", "Choose a student:", student_names, 0, False)
        if ok:
            # Find selected student details
            selected_student = next(s for s in self.students if s["name"] == student)
            return selected_student, ok
        return None, False

    def update_student_details(self):
        """ Pop-up to update student details """
        student, ok = self.select_student()
        if ok:
            # Get new email and phone
            email, ok_email = QInputDialog.getText(self, "Update Email", "Enter new email:", text=student["email"])
            phone, ok_phone = QInputDialog.getText(self, "Update Phone", "Enter new phone number:", text=student["phone"])
            if ok_email and ok_phone:
                student["email"] = email
                student["phone"] = phone
                self.update_table()

    def add_new_student(self):
        """ Pop-up to add a new student """
        name, ok_name = QInputDialog.getText(self, "New Student", "Enter student's name:")
        if ok_name and name:
            email, ok_email = QInputDialog.getText(self, "New Student", "Enter student's email:")
            if ok_email and email:
                phone, ok_phone = QInputDialog.getText(self, "New Student", "Enter student's phone number:")
                if ok_phone and phone:
                    # Add new student to the list
                    new_student = {"name": name, "email": email, "phone": phone, "attendance": {self.date_picker.date().toString("yyyy-MM-dd"): "Absent"}, "image": "student.png"}
                    self.students.append(new_student)
                    self.update_table()

    def update_table(self):
        """ Update the displayed student details in the table """
        self.table.setRowCount(len(self.students))
        selected_date = self.date_picker.date().toString("yyyy-MM-dd")
        for row, student in enumerate(self.students):
            # Set the image for each student (example: placeholder image)
            img_label = QLabel()
            img_pixmap = QPixmap(student["image"])
            img_label.setPixmap(img_pixmap.scaled(50, 50, Qt.KeepAspectRatio))

            self.table.setCellWidget(row, 0, img_label)  # Add image to the first column
            self.table.setItem(row, 1, QTableWidgetItem(student["name"]))
            self.table.setItem(row, 2, QTableWidgetItem(student["email"]))
            self.table.setItem(row, 3, QTableWidgetItem(student["phone"]))
            self.table.setItem(row, 4, QTableWidgetItem(student["attendance"].get(selected_date, "Absent")))
            self.table.setItem(row, 5, QTableWidgetItem(selected_date))

# Main Application
def main():
    app = QApplication(sys.argv)
    window = AttendanceApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
