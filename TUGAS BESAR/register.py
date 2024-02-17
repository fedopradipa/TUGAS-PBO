import tkinter as tk
from tkinter import ttk, messagebox
from database import create_database_connection
import bcrypt
from PIL import Image, ImageTk


class RegisterForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Warnet.NET")
        self.set_icon()
        # Mendapatkan lebar dan tinggi layar
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Mengatur ukuran jendela dan posisinya di tengah
        window_width = 400
        window_height = 300
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Ganti warna latar belakang dan warna teks sesuai keinginan
        self.configure(bg="#282c35")

        # Label Nama Lengkap
        self.label_fullname = tk.Label(
            self, text="Nama Lengkap:", bg="#282c35", fg="white")
        self.label_fullname.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        # Entry Nama Lengkap
        self.entry_fullname = tk.Entry(self)
        self.entry_fullname.grid(row=0, column=1, padx=10, pady=5)

        # Label Jenis Kelamin
        self.label_gender = tk.Label(
            self, text="Jenis Kelamin:", bg="#282c35", fg="white")
        self.label_gender.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        # Combobox Jenis Kelamin
        self.combobox_gender = ttk.Combobox(
            self, values=["Laki-laki", "Perempuan"])
        self.combobox_gender.grid(row=1, column=1, padx=10, pady=5)

        # Label Umur
        self.label_age = tk.Label(
            self, text="Umur:", bg="#282c35", fg="white")
        self.label_age.grid(row=2, column=0, sticky="e", padx=10, pady=5)

        # Entry Umur
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=2, column=1, padx=10, pady=5)

        # Label Username
        self.label_username = tk.Label(
            self, text="Username:", bg="#282c35", fg="white")
        self.label_username.grid(row=3, column=0, sticky="e", padx=10, pady=5)

        # Entry Username
        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=3, column=1, padx=10, pady=5)

        # Label Password
        self.label_password = tk.Label(
            self, text="Password:", bg="#282c35", fg="white")
        self.label_password.grid(row=4, column=0, sticky="e", padx=10, pady=5)

        # Entry Password
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=4, column=1, padx=10, pady=5)

        # Tombol Register
        self.button_register = tk.Button(
            self, text="Register", command=self.register_user, bg="#136C38", fg="white")
        self.button_register.grid(row=5, column=0, columnspan=2, pady=10)

        # Membuat ukuran jendela tidak dapat diubah
        self.resizable(width=False, height=False)

    def set_icon(self):
        icon_image = Image.open("icon3.jpg")
        tk_icon = ImageTk.PhotoImage(icon_image)
        self.iconphoto(False, tk_icon)

    def register_user(self):
        fullname = self.entry_fullname.get()
        gender = self.combobox_gender.get()
        age = self.entry_age.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not all([fullname, gender, age, username, password]):
            tk.messagebox.showerror("Error", "Semua kolom harus diisi.")
            return

         # Hash password menggunakan bcrypt
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO users (fullname, gender, age, username, password) VALUES (%s, %s, %s, %s, %s)",
                           (fullname, gender, age, username, hashed_password))
            connection.commit()
            tk.messagebox.showinfo("Success", "Registrasi berhasil!")
            self.destroy()  # Menutup jendela registrasi setelah berhasil
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = RegisterForm(root)
    root.mainloop()
