import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# Extended sample sentences categorized by levels
LEVEL_SENTENCES = {
    "Easy": [
        "The sun rises in the east.",
        "I love programming.",
        "Python is fun to learn.",
        "Cats are small and fluffy animals.",
        "Reading books improves your knowledge.",
    ],
    "Medium": [
        "The quick brown fox jumps over the lazy dog.",
        "Typing speed test measures your words per minute.",
        "Artificial intelligence is shaping the future.",
        "Regular exercise keeps the body fit and healthy.",
        "Learning new skills enhances career opportunities.",
    ],
    "Hard": [
        "Practice makes perfect, especially in coding and typing.",
        "Machine learning algorithms require extensive datasets.",
        "The complexity of neural networks can be overwhelming.",
        "Quantum computing is revolutionizing computer science.",
        "Understanding differential equations is essential in engineering.",
    ],
}

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.start_time = None
        self.remaining_time = 60  # Default 60 seconds
        self.test_sentence = ""
        self.level = "Easy"

        # Create GUI elements
        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        # Heading
        ttk.Label(
            self.root, text="Typing Speed Test", font=("Arial", 20, "bold")
        ).pack(pady=10)

        # Level selection
        level_frame = ttk.Frame(self.root)
        level_frame.pack(pady=10)
        ttk.Label(level_frame, text="Select Level:", font=("Arial", 14)).pack(side=tk.LEFT, padx=5)
        self.level_var = tk.StringVar(value="Easy")
        self.level_menu = ttk.OptionMenu(
            level_frame, self.level_var, *LEVEL_SENTENCES.keys(), command=self.set_level
        )
        self.level_menu.pack(side=tk.LEFT, padx=5)

        # Timer display
        self.timer_label = ttk.Label(
            self.root, text="Time Left: 60s", font=("Arial", 14, "bold"), foreground="red"
        )
        self.timer_label.pack(pady=10)

        # Test sentence display
        self.sentence_label = ttk.Label(
            self.root, text="", font=("Arial", 16), wraplength=600, justify="center"
        )
        self.sentence_label.pack(pady=20)

        # Input field
        self.input_text = tk.Text(self.root, height=5, width=60, font=("Arial", 14))
        self.input_text.pack(pady=10)

        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(
            button_frame, text="Start", command=self.start_test
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.submit_button = ttk.Button(
            button_frame, text="Submit", command=self.end_test, state=tk.DISABLED
        )
        self.submit_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = ttk.Button(
            button_frame, text="Reset", command=self.reset_test
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def set_level(self, selected_level):
        """Set the difficulty level and update the test sentence."""
        self.level = selected_level
        self.test_sentence = random.choice(LEVEL_SENTENCES[self.level])
        self.sentence_label.config(text=self.test_sentence)

    def start_test(self):
        """Start the typing test and the timer."""
        if not self.test_sentence:
            self.set_level(self.level_var.get())  # Set the sentence if not already set

        self.start_time = time.time()
        self.remaining_time = 60  # Reset timer
        self.update_timer()
        self.input_text.delete(1.0, tk.END)  # Clear the input field
        self.input_text.focus_set()  # Focus on input field
        self.submit_button.config(state=tk.NORMAL)  # Enable the submit button
        self.start_button.config(state=tk.DISABLED)  # Disable the start button

    def update_timer(self):
        """Update the timer every second."""
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time Left: {self.remaining_time}s")
            self.root.after(1000, self.update_timer)  # Schedule next update
        else:
            self.end_test()  # End the test when the timer reaches zero

    def end_test(self):
        """End the typing test and calculate the results."""
        if not self.start_time:
            messagebox.showerror("Error", "You need to start the test first!")
            return

        end_time = time.time()
        elapsed_time = end_time - self.start_time  # Time in seconds

        # Get user input and calculate typing speed
        user_input = self.input_text.get(1.0, tk.END).strip()
        word_count = len(user_input.split())
        typing_speed = word_count / (elapsed_time / 60)  # Words per minute (WPM)

        # Calculate accuracy
        correct_words = sum(
            1 for a, b in zip(user_input.split(), self.test_sentence.split()) if a == b
        )
        total_words = len(self.test_sentence.split())
        accuracy = (correct_words / total_words) * 100 if total_words else 0

        # Display results
        result_message = (
            f"Typing Speed: {typing_speed:.2f} WPM\n"
            f"Accuracy: {accuracy:.2f}%\n"
            f"Time Taken: {elapsed_time:.2f} seconds"
        )
        messagebox.showinfo("Test Results", result_message)

        # Reset state
        self.start_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)
        self.timer_label.config(text="Time Left: 60s")
        self.start_time = None

    def reset_test(self):
        """Reset the test to its initial state."""
        self.start_button.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.DISABLED)
        self.timer_label.config(text="Time Left: 60s")
        self.input_text.delete(1.0, tk.END)
        self.test_sentence = ""
        self.sentence_label.config(text="")

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
