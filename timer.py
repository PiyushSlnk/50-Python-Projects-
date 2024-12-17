import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Timer variables
        self.time_left = 0
        self.running = False

        # Background color
        self.root.config(bg="#333333")

        # Timer Display
        self.time_label = tk.Label(self.root, text="00:00", font=("Helvetica", 40), width=8, fg="#FFFFFF", bg="#333333")
        self.time_label.pack(pady=30)

        # Button Frame
        button_frame = tk.Frame(self.root, bg="#333333")
        button_frame.pack(pady=20)

        # Start button
        self.start_button = tk.Button(button_frame, text="Start", font=("Helvetica", 14), width=8, height=2, bg="#4CAF50", fg="#FFFFFF", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        # Stop button
        self.stop_button = tk.Button(button_frame, text="Stop", font=("Helvetica", 14), width=8, height=2, bg="#FF5733", fg="#FFFFFF", command=self.stop_timer)
        self.stop_button.grid(row=0, column=1, padx=10)

        # Reset button
        self.reset_button = tk.Button(button_frame, text="Reset", font=("Helvetica", 14), width=8, height=2, bg="#2196F3", fg="#FFFFFF", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)

        # Timer loop
        self.update_timer()

    def start_timer(self):
        """Start the timer or continue it if already running"""
        if not self.running:
            self.running = True
            self.countdown()

    def stop_timer(self):
        """Stop the timer"""
        self.running = False

    def reset_timer(self):
        """Reset the timer to 0"""
        self.time_left = 0
        self.running = False
        self.update_label()

    def update_timer(self):
        """Update the time every second"""
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_label()
        elif self.running and self.time_left == 0:
            messagebox.showinfo("Time's Up", "Time is up!")
            self.reset_timer()

        # After every 1000 ms, call this function again
        self.root.after(1000, self.update_timer)

    def countdown(self):
        """Start a countdown for the timer"""
        self.time_left = 5 * 60  # Set timer for 5 minutes
        self.running = True

    def update_label(self):
        """Update the label with formatted time"""
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        time_str = f"{minutes:02}:{seconds:02}"
        self.time_label.config(text=time_str)

# Main window setup
root = tk.Tk()
app = TimerApp(root)
root.mainloop()
