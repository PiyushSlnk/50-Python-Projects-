import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, \
    QTableWidgetItem, QLineEdit, QComboBox
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QColor, QPalette
from twilio.rest import Client  # Import Twilio client to send SMS

class RestaurantBillingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Restaurant Billing System')
        self.setGeometry(100, 100, 800, 700)

        # Initialize menu items and other variables
        self.menu_items = {
            1: {"name": "Burger", "price": 100},
            2: {"name": "Pizza", "price": 300},
            3: {"name": "Pasta", "price": 150},
            4: {"name": "Coke", "price": 50},
            5: {"name": "Fries", "price": 80}
        }

        self.items_ordered = []
        self.platform_fee_percentage = 5  # Example platform fee (5%)

        # Twilio API credentials
        self.account_sid = 'your_account_sid'  # Replace with your Twilio Account SID
        self.auth_token = 'your_auth_token'  # Replace with your Twilio Auth Token
        self.twilio_phone_number = 'your_twilio_phone_number'  # Replace with your Twilio phone number

        self.init_ui()

    def init_ui(self):
        # Set background color for a professional look
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(245, 245, 245))  # Light grey background
        self.setPalette(palette)

        # Shop Name Label
        self.shop_name_label = QLabel("Restaurant RED CHILIES", self)
        self.shop_name_label.setStyleSheet("font-size: 24px; color: #333333; font-weight: bold; background-color: #FF6F61; padding: 10px; border-radius: 5px;")
        self.shop_name_label.setAlignment(Qt.AlignCenter)

        # GST Number Label
        self.gst_label = QLabel("GST Number: 29ABCDE1234F1Z5", self)
        self.gst_label.setStyleSheet("font-size: 1px; color: #333333; font-weight: bold; background-color: #FF6F61; padding: 5px; border-radius: 5px;")

        # Location Label
        self.location_label = QLabel("Location:India, WestBengal,Kolkata", self)
        self.location_label.setStyleSheet("font-size: 16px; color: #333333; font-weight: bold;")

        # Date and Time Label
        self.datetime_label = QLabel(self)
        self.update_datetime()
        self.datetime_label.setStyleSheet("font-size: 16px; color: #8b0000; font-weight: bold;")

        # Customer Details (Name, Email, Phone)
        self.customer_name_input = QLineEdit(self)
        self.customer_name_input.setPlaceholderText("Customer Name")
        self.customer_name_input.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            background-color: #FFF7E6;
            border-radius: 5px;
            border: 2px solid #FF6F61;
        """)
        
        self.customer_email_input = QLineEdit(self)
        self.customer_email_input.setPlaceholderText("Customer Email")
        self.customer_email_input.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            background-color: #FFF7E6;
            border-radius: 5px;
            border: 2px solid #FF6F61;
        """)
        
        self.customer_phone_input = QLineEdit(self)
        self.customer_phone_input.setPlaceholderText("Customer Phone (+91 XXXXX XXXXX)")
        self.customer_phone_input.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            background-color: #FFF7E6;
            border-radius: 5px;
            border: 2px solid #FF6F61;
        """)

        # Menu Section
        self.menu_label = QLabel("Select Items:")
        self.menu_label.setStyleSheet("font-size: 18px; color: #333333; font-weight: bold;")

        # ComboBox for Menu with increased size and colorful look
        self.menu_combo = QComboBox(self)
        for item_number, item_details in self.menu_items.items():
            self.menu_combo.addItem(f"{item_details['name']} - ₹{item_details['price']}", item_number)
        self.menu_combo.setFixedSize(250, 40)  # Increased size for better readability
        self.menu_combo.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            background-color: #FF6F61;
            color: white;
            border-radius: 5px;
        """)

        # Quantity Input Field with a focus effect (highlight when selected)
        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Quantity")
        self.quantity_input.setStyleSheet("""
            font-size: 16px;
            padding: 10px;
            background-color: #FFF7E6;
            border-radius: 5px;
            border: 2px solid #FF6F61;
        """)
        self.quantity_input.setFixedSize(120, 30)  # Increased size
        self.quantity_input.setStyleSheet(self.quantity_input.styleSheet() + """
            QLineEdit:focus {
                border: 2px solid #4CAF50;  # Highlight border color when focused
            }
        """)

        # Add Item Button with Colorful Style
        self.add_item_button = QPushButton("Add Item", self)
        self.add_item_button.setStyleSheet("""
            background-color: #4CAF50; 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 18px;
        """)
        self.add_item_button.clicked.connect(self.add_item)

        # Send SMS Button
        self.send_sms_button = QPushButton("Send Bill to Phone", self)
        self.send_sms_button.setStyleSheet("""
            background-color: #FF6F61; 
            color: white; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 18px;
        """)
        self.send_sms_button.clicked.connect(self.send_sms)

        # Bill Display Table
        self.bill_table = QTableWidget(self)
        self.bill_table.setColumnCount(5)
        self.bill_table.setHorizontalHeaderLabels(["Item", "Quantity", "Price", "Tax", "Total"])
        self.bill_table.setStyleSheet("font-size: 14px; color: #333333; background-color: #ffffff;")

        # Bill Summary Section
        self.total_label = QLabel("Total: ₹0.00", self)
        self.total_label.setStyleSheet("font-size: 18px; color: #4CAF50; font-weight: bold;")
        self.platform_fee_label = QLabel("Platform Fee: ₹0.00", self)
        self.platform_fee_label.setStyleSheet("font-size: 16px; color: #333333;")
        self.gst_label2 = QLabel("GST (9%): ₹0.00", self)
        self.gst_label2.setStyleSheet("font-size: 16px; color: #333333;")
        self.sgst_label2 = QLabel("SGST (9%): ₹0.00", self)
        self.sgst_label2.setStyleSheet("font-size: 16px; color: #333333;")
        self.final_total_label = QLabel("Final Total: ₹0.00", self)
        self.final_total_label.setStyleSheet("font-size: 18px; color: #4CAF50; font-weight: bold;")

        # Layouts
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.shop_name_label)
        self.main_layout.addWidget(self.gst_label)
        self.main_layout.addWidget(self.location_label)
        self.main_layout.addWidget(self.datetime_label)

        self.main_layout.addWidget(self.customer_name_input)
        self.main_layout.addWidget(self.customer_email_input)
        self.main_layout.addWidget(self.customer_phone_input)

        self.menu_layout = QHBoxLayout()
        self.menu_layout.addWidget(self.menu_label)
        self.menu_layout.addWidget(self.menu_combo)
        self.menu_layout.addWidget(self.quantity_input)
        self.main_layout.addLayout(self.menu_layout)

        self.main_layout.addWidget(self.add_item_button)
        self.main_layout.addWidget(self.bill_table)

        self.main_layout.addWidget(self.total_label)
        self.main_layout.addWidget(self.platform_fee_label)
        self.main_layout.addWidget(self.gst_label2)
        self.main_layout.addWidget(self.sgst_label2)
        self.main_layout.addWidget(self.final_total_label)

        self.main_layout.addWidget(self.send_sms_button)

        self.setLayout(self.main_layout)

    def update_datetime(self):
        current_time = QDateTime.currentDateTime().toString()
        self.datetime_label.setText(f"Date & Time: {current_time}")

    def add_item(self):
        try:
            selected_item_index = self.menu_combo.currentIndex()
            item = self.menu_items[selected_item_index + 1]
            quantity = int(self.quantity_input.text())
            item_total = item['price'] * quantity
            item_tax = self.calculate_tax(item_total)
            total_item_price = item_total + item_tax

            row_position = self.bill_table.rowCount()
            self.bill_table.insertRow(row_position)
            self.bill_table.setItem(row_position, 0, QTableWidgetItem(item['name']))
            self.bill_table.setItem(row_position, 1, QTableWidgetItem(str(quantity)))
            self.bill_table.setItem(row_position, 2, QTableWidgetItem(f"₹{item_total:.2f}"))
            self.bill_table.setItem(row_position, 3, QTableWidgetItem(f"₹{item_tax:.2f}"))
            self.bill_table.setItem(row_position, 4, QTableWidgetItem(f"₹{total_item_price:.2f}"))

            self.items_ordered.append({
                'item': item['name'],
                'quantity': quantity,
                'item_total': item_total,
                'item_tax': item_tax,
                'total': total_item_price
            })

            self.update_bill_summary()
            self.clear_input_fields()
        except ValueError:
            pass

    def calculate_tax(self, item_total):
        gst = item_total * 0.09
        sgst = gst
        return gst + sgst

    def update_bill_summary(self):
        total_amount = sum([item['total'] for item in self.items_ordered])
        platform_fee = total_amount * (self.platform_fee_percentage / 100)
        gst_total = total_amount * 0.09
        sgst_total = gst_total

        self.total_label.setText(f"Total: ₹{total_amount:.2f}")
        self.platform_fee_label.setText(f"Platform Fee: ₹{platform_fee:.2f}")
        self.gst_label2.setText(f"GST (9%): ₹{gst_total:.2f}")
        self.sgst_label2.setText(f"SGST (9%): ₹{sgst_total:.2f}")
        self.final_total_label.setText(f"Final Total: ₹{total_amount + platform_fee + gst_total + sgst_total:.2f}")

    def clear_input_fields(self):
        self.quantity_input.clear()

    def send_sms(self):
        # Get customer phone number
        phone_number = self.customer_phone_input.text()

        # Check if phone number is valid
        if phone_number.startswith("+91") and len(phone_number) == 13:
            # Format the bill details as a message
            bill_details = "Restaurant XYZ Bill\n"
            bill_details += "\n".join([f"{item['item']} - {item['quantity']} x ₹{item['item_total']:.2f}" for item in self.items_ordered])
            bill_details += f"\n\nTotal: ₹{self.total_label.text()[7:]}\nGST (9%): ₹{self.gst_label2.text()[12:]}\nSGST (9%): ₹{self.sgst_label2.text()[12:]}\nFinal Total: ₹{self.final_total_label.text()[12:]}\n"

            # Send SMS using Twilio
            client = Client(self.account_sid, self.auth_token)
            try:
                message = client.messages.create(
                    body=bill_details,
                    from_=self.twilio_phone_number,
                    to=phone_number
                )
                print(f"Message sent to {phone_number}")
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("Invalid phone number. Please enter a valid phone number starting with +91.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RestaurantBillingApp()
    window.show()
    sys.exit(app.exec_())
