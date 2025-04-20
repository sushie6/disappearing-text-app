import tkinter as tk
from tkinter import scrolledtext

class WriteAndGoneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Write and Gone")
        self.root.configure(bg="#FFE2E2")
        self.root.state('zoomed')

        self.heading_label = tk.Label(root, text="WRITE & GONE", font=("Arial", 80, "bold"), fg="#2C2C2C", bg="#FFE2E2")
        self.heading_label.pack(side="top", pady=40)

        self.instruction_label = tk.Label(root, text="Don’t stop writing, or all progress will be lost", font=("courier", 23), fg="#2C2C2C", bg="#FFE2E2")
        self.instruction_label.pack()

        self.countdown_label = tk.Label(root, text="", font=("courier", 18), fg="#FFFDEC", bg="#2C2C2C")
        self.countdown_label.pack(pady=20)  # Increased padding below the timer

        self.text_area = scrolledtext.ScrolledText(root, font=("courier", 24), bg="#2C2C2C", fg="#FFE2E2", width=60, height=8)  # Reduced height
        self.text_area.pack(pady=20, padx=20, fill="both", expand=True)
        self.text_area.focus_set()
        self.text_area.bind("<KeyRelease>", self.reset_timer)
        self.text_area.bind("<Key>", self.start_initial_timer)

        self.countdown_timer = None
        self.remaining_time = 10
        self.timer_started = False

    def start_initial_timer(self, event=None):
        if not self.timer_started:
            self.timer_started = True
            self.reset_timer()
            self.text_area.unbind("<Key>", self.start_initial_timer)

    def reset_timer(self, event=None):
        if self.timer_started:
            self.remaining_time = 10
            self.update_countdown_label()
            if self.countdown_timer:
                self.root.after_cancel(self.countdown_timer)
            self.countdown_timer = self.root.after(1000, self.countdown)

    def countdown(self):
        if self.timer_started:
            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.update_countdown_label()
                self.countdown_timer = self.root.after(1000, self.countdown)
            else:
                self.clear_text()

    def update_countdown_label(self):
        if self.timer_started:
            if self.remaining_time > 0:
                self.countdown_label.config(text=f"Erasing in: {self.remaining_time} seconds")
            else:
                self.countdown_label.config(text="Text erased!")
        else:
            self.countdown_label.config(text="")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.remaining_time = 10
        self.timer_started = False
        self.update_countdown_label()
        self.text_area.bind("<Key>", self.start_initial_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = WriteAndGoneApp(root)
    root.mainloop()