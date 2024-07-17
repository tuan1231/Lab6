import tkinter as tk
from tkinter import messagebox

class DataEntryForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry Form")
        self.root.geometry("500x400")
        
        # Khung thông tin người dùng
        self.user_info_frame = tk.LabelFrame(root, text="User Information", padx=10, pady=10)
        self.user_info_frame.pack(padx=10, pady=10, fill="x")

        self.create_user_info_frame()

        # Khung đăng ký
        self.registration_frame = tk.LabelFrame(root, text="Registration Status", padx=10, pady=10)
        self.registration_frame.pack(padx=10, pady=10, fill="x")

        self.create_registration_frame()

        # Khung Điều khoản và Điều kiện
        self.terms_frame = tk.LabelFrame(root, text="Terms & Conditions", padx=10, pady=10)
        self.terms_frame.pack(padx=10, pady=10, fill="x")

        self.create_terms_frame()

        # Nút Gửi
        self.submit_button = tk.Button(root, text="Enter data", command=self.submit_data)
        self.submit_button.pack(pady=20)

    def create_user_info_frame(self):
        tk.Label(self.user_info_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.user_info_frame, text="Last Name").grid(row=0, column=2, padx=5, pady=5)
        self.last_name_entry = tk.Entry(self.user_info_frame)
        self.last_name_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.user_info_frame, text="Title").grid(row=0, column=4, padx=5, pady=5)
        self.title_var = tk.StringVar()
        self.title_combobox = tk.OptionMenu(self.user_info_frame, self.title_var, "Mr.", "Mrs.", "Ms.", "Dr.")
        self.title_combobox.grid(row=0, column=5, padx=5, pady=5)

        tk.Label(self.user_info_frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
        self.age_spinbox = tk.Spinbox(self.user_info_frame, from_=18, to=100)
        self.age_spinbox.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.user_info_frame, text="Nationality").grid(row=1, column=2, padx=5, pady=5)
        self.nationality_entry = tk.Entry(self.user_info_frame)
        self.nationality_entry.grid(row=1, column=3, padx=5, pady=5)

    def create_registration_frame(self):
        self.registration_var = tk.IntVar()
        self.registration_check = tk.Checkbutton(self.registration_frame, text="Currently Registered", variable=self.registration_var)
        self.registration_check.grid(row=0, column=0, padx=5, pady=5)

        tk.Label(self.registration_frame, text="# Completed Courses").grid(row=0, column=1, padx=5, pady=5)
        self.courses_spinbox = tk.Spinbox(self.registration_frame, from_=0, to=50)
        self.courses_spinbox.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.registration_frame, text="# Semesters").grid(row=0, column=3, padx=5, pady=5)
        self.semesters_spinbox = tk.Spinbox(self.registration_frame, from_=0, to=20)
        self.semesters_spinbox.grid(row=0, column=4, padx=5, pady=5)

    def create_terms_frame(self):
        self.terms_var = tk.IntVar()
        self.terms_check = tk.Checkbutton(self.terms_frame, text="I accept the terms and conditions.", variable=self.terms_var)
        self.terms_check.pack(anchor='w', padx=5, pady=5)

    def submit_data(self):
        if self.terms_var.get() == 0:
            messagebox.showwarning("Terms & Conditions", "You must accept the terms and conditions to proceed.")
            return

        data = {
            "First Name": self.first_name_entry.get(),
            "Last Name": self.last_name_entry.get(),
            "Title": self.title_var.get(),
            "Age": self.age_spinbox.get(),
            "Nationality": self.nationality_entry.get(),
            "Currently Registered": self.registration_var.get(),
            "# Completed Courses": self.courses_spinbox.get(),
            "# Semesters": self.semesters_spinbox.get(),
        }

        for key, value in data.items():
            print(f"{key}: {value}")

        messagebox.showinfo("Data Submitted", "Your data has been submitted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataEntryForm(root)
    root.mainloop()
