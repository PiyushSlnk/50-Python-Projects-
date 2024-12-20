import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QWidget,
)
from bs4 import BeautifulSoup


class WebScraperApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setWindowTitle("Web Scraper")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.url_label = QLabel("Enter URL:")
        self.layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        self.layout.addWidget(self.url_input)

        self.scrape_button = QPushButton("Scrape Website")
        self.scrape_button.clicked.connect(self.scrape_website)
        self.layout.addWidget(self.scrape_button)

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        self.layout.addWidget(self.result_area)

        self.setLayout(self.layout)

    def scrape_website(self):
        url = self.url_input.text().strip()
        if not url:
            self.result_area.setText("Please enter a valid URL.")
            return

        try:
            # Fetch the webpage content
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract data: title and first 5 paragraphs
            title = soup.title.string if soup.title else "No title available"
            paragraphs = [p.get_text() for p in soup.find_all("p")][:5]

            # Display the results
            result = f"Website: {url}\n\nTitle: {title}\n\nContent:\n"
            for i, paragraph in enumerate(paragraphs, start=1):
                result += f"{i}. {paragraph}\n"

            self.result_area.setText(result)

        except requests.exceptions.RequestException as e:
            self.result_area.setText(f"Error fetching the webpage: {e}")
        except Exception as e:
            self.result_area.setText(f"An error occurred: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scraper_app = WebScraperApp()
    scraper_app.show()
    sys.exit(app.exec_())
