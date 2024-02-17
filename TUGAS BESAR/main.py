import tkinter as tk
from tkinter import messagebox
from database import create_database_connection
from register import RegisterForm
from menu_utama import Menu
import bcrypt
from PIL import Image, ImageTk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
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

        # Label judul
        label_judul = tk.Label(self, text="F'do.NET",
                               font=('Helvetica', 25, 'bold'), bg="#282c35", fg="white")
        label_judul.pack(pady=10)

        # Formulir Login
        self.label_username = tk.Label(
            self, text="Username:", bg="#282c35", fg="white")
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(
            self, text="Password:", bg="#282c35", fg="white")
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(
            self, text="Login", command=self.process_login, bg="#136C38", fg="white")
        self.button_login.pack(pady=10)

        self.button_register = tk.Button(
            self, text="Register", command=self.show_register, bg="#136C38", fg="white")
        self.button_register.pack(pady=10)

        # Membuat ukuran jendela tidak dapat diubah
        self.resizable(width=False, height=False)

        self.logged_in = False
        self.username_value = ""  # Menambahkan atribut untuk menyimpan nilai entry_username

    def set_icon(self):
        icon_image = Image.open("icon3.jpg")
        tk_icon = ImageTk.PhotoImage(icon_image)
        self.iconphoto(False, tk_icon)

    def process_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                "SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()

            if user:
                # Mengasumsikan kata sandi ada di indeks 5 pada database Anda
                hashed_password = user[5].encode('utf-8')
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    tk.messagebox.showinfo(
                        "Success", f"Login berhasil, Selamat datang {username}!")
                    self.logged_in = True
                    self.username_value = username  # Menyimpan nilai entry_username
                    self.withdraw()  # Menyembunyikan jendela utama
                    self.show_menu()
                else:
                    tk.messagebox.showerror(
                        "Error", "Login gagal. Periksa kembali username dan password Anda.")
            else:
                tk.messagebox.showerror(
                    "Error", "Login gagal. Periksa kembali username dan password Anda.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def show_menu(self):
        if self.logged_in:
            open_menu = Menu(self)
            open_menu.protocol("WM_DELETE_WINDOW", self.on_menu_close)
            open_menu.mainloop()

    def show_register(self):
        form_daftar = RegisterForm(self)
        self.wait_window(form_daftar)

    def on_menu_close(self):
        self.logged_in = False
        self.deiconify()


if __name__ == "__main__":
    aplikasi = MainApp()
    aplikasi.mainloop()
