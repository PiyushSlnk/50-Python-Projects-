import tkinter as tk
from tkinter import scrolledtext
import datetime

# Function to handle the chatbot response
def respond():
    user_input = entry.get().lower()
    chat_window.config(state=tk.NORMAL)
    
    # Display user input
    chat_window.insert(tk.END, "You: " + user_input + '\n')
    
    # Get today's date, time, day, year, etc.
    now = datetime.datetime.now()
    if 'hello' in user_input:
        bot_response = "Hello! How can I help you today?"
    elif 'bye' in user_input:
        bot_response = "Goodbye! Have a great day!"
    elif 'how are you' in user_input:
        bot_response = "I'm good, thank you for asking!"
    elif 'date' in user_input:
        bot_response = "Today's date is " + now.strftime("%B %d, %Y") + "."
    elif 'time' in user_input:
        bot_response = "The current time is " + now.strftime("%H:%M:%S") + "."
    elif 'day' in user_input:
        bot_response = "Today is " + now.strftime("%A") + "."
    elif 'year' in user_input:
        bot_response = "The current year is " + now.strftime("%Y") + "."
    elif 'month' in user_input:
        bot_response = "This month is " + now.strftime("%B") + "."
    elif 'hour' in user_input:
        bot_response = "It is currently " + str(now.hour) + " hours."
    elif 'minute' in user_input:
        bot_response = "It is currently " + str(now.minute) + " minutes past the hour."
    elif 'second' in user_input:
        bot_response = "It is currently " + str(now.second) + " seconds into the minute."
    else:
        bot_response = "Sorry, I don't understand that. Please ask something like 'What is the date?' or 'What is the time?'"
    
    # Display bot response
    chat_window.insert(tk.END, "Bot: " + bot_response + '\n')
    
    # Scroll to the bottom
    chat_window.yview(tk.END)
    
    # Clear the entry field for the next input
    entry.delete(0, tk.END)
    
    chat_window.config(state=tk.DISABLED)

# Set up the main window
root = tk.Tk()
root.title("Modern Chatbot")
root.geometry("500x600")
root.config(bg="#2b2b2b")

# Create a chat window (Scrolled Text Widget)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=20, state=tk.DISABLED, bg="#1e1e1e", fg="#fff", font=("Segoe UI", 12), borderwidth=0)
chat_window.grid(row=0, column=0, padx=15, pady=15)

# Create an entry field for user input with rounded corners
entry = tk.Entry(root, width=40, font=("Segoe UI", 14), bd=0, relief="solid", highlightthickness=1, highlightbackground="#444", fg="#fff", bg="#333", insertbackground="white")
entry.grid(row=1, column=0, padx=15, pady=10)

# Create a send button with modern styling
send_button = tk.Button(root, text="Send", width=15, height=2, command=respond, bg="#4CAF50", fg="white", font=("Segoe UI", 14), relief="flat", activebackground="#45a049", activeforeground="white")
send_button.grid(row=2, column=0, padx=15, pady=15)

# Run the Tkinter event loop
root.mainloop()
