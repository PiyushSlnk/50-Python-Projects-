import tkinter as tk
from tkinter import ttk
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Spelling Checker")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")

        self.spellchecker = SpellChecker()

        # Title Label
        title_label = tk.Label(
            self.root, text="Professional Spelling Checker", font=("Helvetica", 20, "bold"), bg="#0078D7", fg="white", pady=15
        )
        title_label.pack(fill=tk.X)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#ffffff")
        input_frame.pack(pady=20)

        input_label = tk.Label(
            input_frame, text="Enter your text below for spell checking:", font=("Helvetica", 14), bg="#ffffff", anchor="w"
        )
        input_label.pack(anchor="w", padx=15)

        self.text_area = tk.Text(
            input_frame, height=12, width=80, font=("Courier", 12), relief="groove", bd=2, highlightbackground="#0078D7", highlightthickness=1
        )
        self.text_area.pack(pady=10, padx=15)

        # Button Frame
        button_frame = tk.Frame(self.root, bg="#ffffff")
        button_frame.pack(pady=10)

        self.check_button = tk.Button(
            button_frame,
            text="Check Spelling",
            font=("Helvetica", 14, "bold"),
            bg="#0078D7",
            fg="white",
            padx=15,
            pady=8,
            command=self.check_spelling,
            relief="flat",
            cursor="hand2",
        )
        self.check_button.pack(pady=5)

        # Output Frame
        output_frame = tk.Frame(self.root, bg="#f4f4f4", relief="groove", bd=2)
        output_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        output_label = tk.Label(
            output_frame, text="Results:", font=("Helvetica", 14, "bold"), bg="#f4f4f4", anchor="w"
        )
        output_label.pack(anchor="w", padx=15, pady=5)

        # Scrollable Text Area for Results
        self.result_text = tk.Text(
            output_frame,
            wrap="word",
            height=15,
            font=("Helvetica", 12),
            bg="#f4f4f4",
            fg="#333333",
            relief="flat",
            state="disabled",
        )
        self.result_text.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(output_frame, command=self.result_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_text["yscrollcommand"] = scrollbar.set

    def check_spelling(self):
        text = self.text_area.get("1.0", tk.END).strip()
        if not text:
            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", "Please enter some text to check.")
            self.result_text.config(state="disabled", fg="red")
            return

        words = text.split()
        misspelled = self.spellchecker.unknown(words)

        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)

        if not misspelled:
            self.result_text.insert("1.0", "No spelling mistakes found!\n")
            self.result_text.config(fg="green")
        else:
            corrections = {word: self.spellchecker.correction(word) for word in misspelled}
            result_text = "Spelling corrections:\n"
            for word, correction in corrections.items():
                result_text += f"- {word} -> {correction}\n"

            self.result_text.insert("1.0", result_text)
            self.result_text.config(fg="#0078D7")

        self.result_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
