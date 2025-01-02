import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFormLayout
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt


class ProfileCard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Profile Card")
        self.setGeometry(300, 100, 400, 500)

        # Set window style
        self.setStyleSheet("""
            QWidget {
                background-color: #e0f7fa;
            }
            .profile-card {
                background-color: #ffffff;
                border-radius: 15px;
                padding: 20px;
                width: 350px;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
                text-align: center;
            }
            QLabel {
                font-size: 18px;
                color: #333;
            }
            .bio {
                color: #777;
                font-size: 14px;
                margin-bottom: 15px;
            }
            .button {
                background-color: #42a5f5;
                border-radius: 10px;
                color: white;
                padding: 10px;
                font-weight: bold;
                margin-top: 10px;
            }
            .button:hover {
                background-color: #1e88e5;
            }
            .social-button {
                background-color: #00796b;
                border-radius: 10px;
                color: white;
                padding: 10px;
                font-weight: bold;
                margin-top: 10px;
                width: 100px;
            }
            .social-button:hover {
                background-color: #004d40;
            }
            .social-button.linkedin {
                background-color: #0077b5;
            }
            .social-button.linkedin:hover {
                background-color: #004f87;
            }
            .social-button.github {
                background-color: #333;
            }
            .social-button.github:hover {
                background-color: #1c1c1c;
            }
            .skills {
                background-color: #f1f8e9;
                padding: 10px;
                border-radius: 10px;
                font-size: 14px;
                color: #333;
            }
            .profile-card h2 {
                color: #00796b;
                font-size: 24px;
                margin-top: 15px;
                font-weight: bold;
            }
        """)

        # Set up layout
        layout = QVBoxLayout()

        # Create profile card
        profile_card = QWidget()
        profile_layout = QVBoxLayout()

        # Profile image
        self.profile_image = QLabel(self)
        pixmap = QPixmap("profile_image.jpg")  # Replace with your image file
        self.profile_image.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
        self.profile_image.setAlignment(Qt.AlignCenter)
        self.profile_image.setStyleSheet("border-radius: 50%; border: 5px solid #00796b; margin-bottom: 15px;")

        # Name
        self.name_label = QLabel("Piyush Singh")
        self.name_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")

        # Bio
        self.bio_label = QLabel("Software Engineer | Web Developer | AI Enthusiast")
        self.bio_label.setStyleSheet("color: #777; font-size: 14px; margin-bottom: 15px;")

        # Social Media Buttons
        self.social_button_layout = QHBoxLayout()
        self.github_button = QPushButton("GitHub")
        self.github_button.setStyleSheet("background-color: #333; color: white; font-weight: bold; padding: 10px; border-radius: 10px;")
        self.github_button.setFixedWidth(100)

        self.linkedin_button = QPushButton("LinkedIn")
        self.linkedin_button.setStyleSheet("background-color: #0077b5; color: white; font-weight: bold; padding: 10px; border-radius: 10px;")
        self.linkedin_button.setFixedWidth(100)

        self.social_button_layout.addWidget(self.github_button)
        self.social_button_layout.addWidget(self.linkedin_button)

        # Skills
        skills_label = QLabel("Skills:")
        skills_label.setStyleSheet("font-weight: bold; color: #333;")
        skills = QLabel("Python, JavaScript, Web Development, AI, Machine Learning")
        skills.setStyleSheet("color: #333; font-size: 14px;")
        
        # Skills container
        skills_container = QWidget()
        skills_container.setStyleSheet("background-color: #f1f8e9; padding: 15px; border-radius: 10px;")
        skills_container.setLayout(QVBoxLayout())
        skills_container.layout().addWidget(skills_label)
        skills_container.layout().addWidget(skills)

        # Add all elements to the profile layout
        profile_layout.addWidget(self.profile_image)
        profile_layout.addWidget(self.name_label)
        profile_layout.addWidget(self.bio_label)
        profile_layout.addLayout(self.social_button_layout)
        profile_layout.addWidget(skills_container)

        # Apply to the main layout
        profile_card.setLayout(profile_layout)
        layout.addWidget(profile_card)

        # Set the layout of the window
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileCard()
    window.show()
    sys.exit(app.exec_())
