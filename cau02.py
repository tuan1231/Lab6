import tkinter as tk
from tkinter import messagebox

class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AtarBals Modern Antivirus")
        self.root.geometry("800x500")
        self.root.configure(bg='#ffffff')  # Màu nền tùy chỉnh cho khu vực chính

        # Khung chính chia thành thanh bên và khu vực nội dung chính
        self.sidebar_frame = tk.Frame(root, bg='#3366ff', width=200, height=500)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.main_frame = tk.Frame(root, bg='#ffffff')
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Thanh bên
        self.add_sidebar_buttons()

        # Khu vực chính
        self.add_main_content()

    def add_sidebar_buttons(self):
        buttons = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
        for btn_text in buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, font=("Arial", 12), bg='#3366ff', fg='white', relief=tk.FLAT)
            btn.pack(pady=10, padx=10, anchor='w')

        scan_now_button = tk.Button(self.sidebar_frame, text="Scan Now", font=("Arial", 14), bg='#00ff00', fg='white', relief=tk.FLAT)
        scan_now_button.pack(pady=20, padx=10, anchor='w')

    def add_main_content(self):
        self.title_label = tk.Label(self.main_frame, text="Scan", font=("Arial", 24), bg='#ffffff')
        self.title_label.pack(pady=20)

        self.subtitle_label = tk.Label(self.main_frame, text="Premium will be free forever. You just need to click button.", font=("Arial", 14), bg='#ffffff')
        self.subtitle_label.pack(pady=10)

        self.button_frame = tk.Frame(self.main_frame, bg='#ffffff')
        self.button_frame.pack(pady=20)

        buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
        for btn_text in buttons:
            btn = tk.Button(self.button_frame, text=btn_text, font=("Arial", 12), bg='#ff00ff', fg='black', relief=tk.FLAT)
            btn.pack(side=tk.LEFT, padx=10, pady=10)

        self.status_label = tk.Label(self.main_frame, text="Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)", font=("Arial", 12), bg='#ffffff', fg='#ff00ff')
        self.status_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = AntivirusApp(root)
    root.mainloop()
