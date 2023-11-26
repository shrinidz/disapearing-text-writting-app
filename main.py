import tkinter as tk
from tkinter import ttk
import threading
import time

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")

        self.style = ttk.Style()
        self.style.configure('Danger.TButton', font=('Helvetica', 12), background='#FF5733', foreground='white')

        self.text_widget = tk.Text(self.root, wrap="word", font=('Helvetica', 18))
        self.text_widget.pack(expand=True, fill="both")

        #self.delete_button = ttk.Button(self.root, text="Delete Text", style='Danger.TButton', command=self.delete_text)
        #self.delete_button.pack(pady=10)

        self.start_timer()

    def start_timer(self):
        self.timer_thread = threading.Thread(target=self.check_inactivity, daemon=True)
        self.timer_thread.start()

    def check_inactivity(self):
        inactivity_duration = 30  # seconds

        while True:
            time.sleep(1)
            try:
                if self.text_widget.edit_modified():
                    self.text_widget.edit_modified(False)
                    self.reset_timer()
                else:
                    inactivity_duration -= 1
                    if inactivity_duration == 0:
                        self.delete_text()
                        inactivity_duration = 30  # reset timer after deleting text
            except Exception as e:
                print(f"An error occurred: {e}")

    def reset_timer(self):
        # Reset the timer when the user types
        inactivity_duration = 30

    def delete_text(self):
        # Delete all text in the text widget
        self.text_widget.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
