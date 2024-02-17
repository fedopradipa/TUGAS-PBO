import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime, timedelta
from database import create_database_connection
from PIL import Image, ImageTk


class Pesan(tk.Toplevel):
    def __init__(self, menu_window, *args, **kwargs):
        super().__init__(menu_window, *args, **kwargs)
        self.menu_window = menu_window
        self.title("Warnet.NET")
        self.set_icon()
        # Mendapatkan lebar dan tinggi layar
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Mengatur ukuran jendela dan posisinya di tengah
        window_width = 500
        window_height = 350
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Ganti warna latar belakang dan warna teks sesuai keinginan
        self.configure(bg="#282c35")

        # Label Order Date
        self.label_order_date = tk.Label(
            self, text="Order Date:", bg="#282c35", fg="white")
        self.label_order_date.grid(row=0, column=0, padx=10, pady=5)
        self.label_order_date_value = tk.Label(
            self, text=datetime.now().strftime("%Y-%m-%d"), bg="#282c35", fg="white")
        self.label_order_date_value.grid(row=0, column=1, padx=10, pady=5)

        # Label Order Time
        self.label_order_time = tk.Label(
            self, text="Order Time:", bg="#282c35", fg="white")
        self.label_order_time.grid(row=0, column=2, padx=10, pady=5)
        self.label_order_time_value = tk.Label(
            self, text=datetime.now().strftime("%H:%M:%S"), bg="#282c35", fg="white")
        self.label_order_time_value.grid(row=0, column=3, padx=10, pady=5)

        # Label Pesanan
        self.label_pesanan = tk.Label(
            self, text="PESANAN:", bg="#282c35", fg="white")
        self.label_pesanan.grid(row=1, column=0, pady=10, columnspan=4)

        # Label ID Pesanan
        self.label_id = tk.Label(
            self, text="ID Pesanan:", bg="#282c35", fg="white")
        self.label_id.grid(row=2, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(self, state="readonly")
        self.entry_id.grid(row=2, column=1, padx=10, pady=5)

        # Label Username
        self.label_username = tk.Label(
            self, text="Username:", bg="#282c35", fg="white")
        self.label_username.grid(row=3, column=0, padx=10, pady=5)
        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=3, column=1, padx=10, pady=5)

        # Label Billing
        self.label_billing = tk.Label(
            self, text="Billing:", bg="#282c35", fg="white")
        self.label_billing.grid(row=4, column=0, pady=10, columnspan=4)

        # Checkbuttons Billing
        self.var_billing = tk.StringVar(value="")
        self.checkbox_billing_1 = tk.Checkbutton(
            self, text="1 Jam", variable=self.var_billing, onvalue="1", offvalue="", command=self.calculate_price, bg="#282c35", fg="white", selectcolor="#136C38")
        self.checkbox_billing_1.grid(row=5, column=0, padx=10, pady=5)

        self.checkbox_billing_2 = tk.Checkbutton(
            self, text="2 Jam", variable=self.var_billing, onvalue="2", offvalue="", command=self.calculate_price, bg="#282c35", fg="white", selectcolor="#136C38")
        self.checkbox_billing_2.grid(row=5, column=1, padx=10, pady=5)

        self.checkbox_billing_3 = tk.Checkbutton(
            self, text="3 Jam", variable=self.var_billing, onvalue="3", offvalue="", command=self.calculate_price, bg="#282c35", fg="white", selectcolor="#136C38")
        self.checkbox_billing_3.grid(row=5, column=2, padx=10, pady=5)

        # Combobox Computer
        self.label_computer = tk.Label(
            self, text="Komputer:", bg="#282c35", fg="white")
        self.label_computer.grid(row=6, column=0, padx=10, pady=5)

        computer_values = ["PC1", "PC2", "PC3", "PC4", "PC5"]
        self.combobox_computer = ttk.Combobox(self, values=computer_values)
        self.combobox_computer.set("PC1")  # Set nilai default
        self.combobox_computer.grid(row=6, column=1, padx=10, pady=5)

        # Label Harga
        self.label_harga = tk.Label(
            self, text="Harga:", bg="#282c35", fg="white")
        self.label_harga.grid(row=7, column=0, padx=10, pady=5)
        self.entry_harga = tk.Entry(self, state="readonly")
        self.entry_harga.grid(row=7, column=1, padx=10, pady=5)

        # Label Waktu Habis
        self.label_waktu_habis = tk.Label(
            self, text="Waktu Habis:", bg="#282c35", fg="white")
        self.label_waktu_habis.grid(row=7, column=2, padx=10, pady=5)
        self.entry_waktu_habis = tk.Entry(self, state="readonly")
        self.entry_waktu_habis.grid(row=7, column=3, padx=10, pady=5)

        # Tombol Reset
        self.button_reset = tk.Button(
            self, text="Reset", command=self.reset_form, bg="#136C38", fg="white")
        self.button_reset.grid(row=8, column=0, pady=10)

        # Tombol Pesan
        self.button_pesan = tk.Button(
            self, text="Booked", command=self.submit_order, bg="#136C38", fg="white")
        self.button_pesan.grid(row=8, column=1, pady=10)

        # Tombol Dashboard
        self.button_cancel = tk.Button(
            self, text="Cancel", command=self.show_menu, bg="#136C38", fg="white")
        self.button_cancel.grid(row=8, column=2, pady=10)

        # Membuat ukuran jendela tidak dapat diubah
        self.resizable(width=False, height=False)

        # Initialize the harga and waktu_habis
        self.calculate_price()

        # Populate otomatis ID Pesanan
        self.populate_order_id()

    def set_icon(self):
        icon_image = Image.open("icon3.jpg")
        tk_icon = ImageTk.PhotoImage(icon_image)
        self.iconphoto(False, tk_icon)

    def calculate_price(self):
        duration = int(self.var_billing.get()) if self.var_billing.get() else 0

        # Hitung harga berdasarkan durasi (contoh: 5000 per jam)
        harga = 5000 * duration
        self.entry_harga.config(state="normal")
        self.entry_harga.delete(0, tk.END)
        self.entry_harga.insert(0, harga)
        self.entry_harga.config(state="readonly")

        # Hitung waktu habis berdasarkan durasi penyewaan
        order_time = self.label_order_time_value.cget("text")
        end_time = (datetime.strptime(order_time, "%H:%M:%S") +
                    timedelta(hours=duration)).strftime("%H:%M:%S")

        self.entry_waktu_habis.config(state="normal")
        self.entry_waktu_habis.delete(0, tk.END)
        self.entry_waktu_habis.insert(0, end_time)
        self.entry_waktu_habis.config(state="readonly")

    def reset_form(self):
        # Reset semua elemen formulir
        self.entry_id.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.var_billing.set("")  # Reset StringVar
        self.combobox_computer.set("")  # Reset combobox
        self.entry_harga.config(state="normal")
        self.entry_harga.delete(0, tk.END)
        self.entry_harga.config(state="readonly")
        self.entry_waktu_habis.config(state="normal")
        self.entry_waktu_habis.delete(0, tk.END)
        self.entry_waktu_habis.config(state="readonly")

        # Populate otomatis ID Pesanan setelah reset
        self.populate_order_id()

    def submit_order(self):
        # Ambil nilai dari elemen formulir
        order_date = self.label_order_date_value.cget("text")
        order_time = self.label_order_time_value.cget("text")
        id_pesan = self.entry_id.get()
        name = self.entry_username.get()
        duration = self.var_billing.get()
        computer = self.combobox_computer.get()
        harga = self.entry_harga.get()
        waktu_habis = self.entry_waktu_habis.get()

        # Validasi isian formulir
        if not (name and duration and computer and harga and waktu_habis):
            messagebox.showwarning(
                "Peringatan", "Harap isi semua kolom formulir.")
            return
        # Simpan data ke database
        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO rentals (id_pesan, name, order_date, order_time, duration, computer, price, end_time)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (id_pesan, name, order_date, order_time, duration, computer, harga, waktu_habis))
            connection.commit()
            messagebox.showinfo("Sukses", "Order berhasil!")

            # Reset formulir setelah submit
            self.reset_form()
           # Refresh informasi pada Treeview Dashboard
            self.menu_window.refresh_info()
            self.show_menu()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def show_menu(self):
        # Kembali ke dashboard
        self.menu_window.deiconify()
        self.destroy()  # Menutup jendela Pesan

    def populate_order_id(self):
        # Mengambil ID Pesanan terbaru dari database
        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT MAX(id_pesan) FROM rentals")
            max_id = cursor.fetchone()[0]

            # Menyusun ID Pesanan baru (ID terbaru + 1)
            new_order_id = max_id + 1 if max_id else 1

            # Memasukkan nilai ke dalam kotak ID Pesanan
            self.entry_id.config(state="normal")
            self.entry_id.delete(0, tk.END)
            self.entry_id.insert(0, new_order_id)
            self.entry_id.config(state="readonly")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    menu_utama = Pesan(root)
    root.mainloop()
