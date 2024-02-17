import tkinter as tk
from tkinter import ttk, messagebox, StringVar
from database import create_database_connection
from pesan import Pesan
from datetime import datetime
from PIL import Image, ImageTk


class Menu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Warnet.NET")
        self.set_icon()
        # Mendapatkan lebar dan tinggi layar
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Mengatur ukuran jendela dan posisinya di tengah
        window_width = 950
        window_height = 500
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.configure(bg="#282c35")

        # Judul
        label_judul = tk.Label(self, text="F'do.NET", font=(
            'Helvetica', 25, 'bold'), bg="#282c35", fg="white")
        label_judul.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Waktu terkini
        self.label_waktu = tk.Label(self, text="", font=(
            'Helvetica', 12), bg="#282c35", fg="white")
        self.label_waktu.grid(row=0, column=4, padx=10, pady=10, sticky='e')

        # Tombol Logout
        button_logout = tk.Button(
            self, text="Logout", command=self.logout, bg="#136C38", fg="white")
        button_logout.grid(row=0, column=5, padx=(10, 20), pady=10, sticky='e')

        # Frame untuk Treeview
        treeview_frame = ttk.LabelFrame(
            self, text="Informasi Penyewa Warnet", labelanchor='n', padding=(10, 5))
        treeview_frame.grid(row=1, column=0, columnspan=5,
                            padx=20, pady=(5, 10), sticky='we')

        # Treeview
        columns = ("ID Pesanan", "Nama", "PC", "Waktu", "Harga",
                   "Jam Main", "Jam Habis", "Tanggal", "Status Bayar")
        self.treeview = ttk.Treeview(
            treeview_frame, columns=columns, show="headings", style="Custom.Treeview", height=10)
        for col in columns:
            self.treeview.heading(col, text=col)

        # Set the column widths
        col_widths = (80, 100, 120, 50, 80, 80, 80, 80, 100)
        for col, width in zip(columns, col_widths):
            self.treeview.column(col, width=width)

        self.treeview.grid(row=0, column=0, columnspan=5,
                           pady=(5, 10), sticky='we')

        # Scrollbar untuk Treeview
        scrollbar = ttk.Scrollbar(
            treeview_frame, orient="vertical", command=self.treeview.yview)
        scrollbar.grid(row=0, column=5, sticky="ns", pady=(5, 10))
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Kotak pencarian dan tombol pencarian
        self.entry_search = tk.Entry(self, width=20)
        self.entry_search.grid(row=4, column=4, padx=10, pady=10)
        button_search = tk.Button(
            self, text="Search", command=self.search_user, bg="#136C38", fg="white")
        button_search.grid(row=4, column=3, padx=10, pady=10)

        # Tombol update, delete, dan pesan
        button_update = tk.Button(
            self, text="Update", command=self.show_update_window, bg="#136C38", fg="white")
        button_update.grid(row=4, column=0, padx=10)

        button_delete = tk.Button(
            self, text="Delete", command=self.delete_user, bg="#136C38", fg="white")
        button_delete.grid(row=4, column=1, padx=10)

        button_pesan = tk.Button(
            self, text="Order", command=self.pesan, bg="#136C38", fg="white")
        button_pesan.grid(row=4, column=2, padx=10)

        # Refresh informasi saat dashboard dibuka
        self.refresh_info()
        # Update waktu setiap detik
        self.update_clock()

        # Variable untuk status pembayaran
        self.status_pembayaran_var = StringVar()
        self.status_pembayaran_var.set("LUNAS")  # Default: LUNAS

        # Membuat ukuran jendela tidak dapat diubah
        self.resizable(width=False, height=False)

    def set_icon(self):
        icon_image = Image.open("icon3.jpg")
        tk_icon = ImageTk.PhotoImage(icon_image)
        self.iconphoto(False, tk_icon)

    def update_clock(self):
        # Update waktu
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.label_waktu.config(text=current_time)
        self.after(1000, self.update_clock)

    def refresh_info(self):
        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                "SELECT id_pesan, name, computer, duration, price, order_time, end_time, order_date, status_pembayaran FROM rentals")
            rentals = cursor.fetchall()

            # Hapus data di Treeview
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            # Tambahkan data baru
            for rental in rentals:
                self.treeview.insert("", "end", values=rental)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def search_user(self):
        search_term = self.entry_search.get()
        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                f"SELECT id_pesan, name, computer, duration, price, order_time, end_time, order_date, status_pembayaran FROM rentals WHERE name LIKE '%{search_term}%'")
            rentals = cursor.fetchall()

            # Hapus data di Treeview
            for row in self.treeview.get_children():
                self.treeview.delete(row)

            # Tambahkan data baru
            for rental in rentals:
                self.treeview.insert("", "end", values=rental)

            # Pesan jika tidak ada hasil
            if not rentals:
                messagebox.showinfo("Info", "Tidak ada hasil yang ditemukan.")
                # Refresh Treeview
                self.refresh_info()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def show_update_window(self):
        selected_user_id = self.get_selected_user_id()
        if selected_user_id:
            # Dapatkan data terkait dari database
            connection = create_database_connection()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    f"SELECT id_pesan, name, computer, duration, price, order_time, end_time, order_date, status_pembayaran FROM rentals WHERE id_pesan = {selected_user_id}")
                rental_data = cursor.fetchone()

                if rental_data:
                    # Jendela update status pembayaran
                    update_window = tk.Toplevel(self)
                    update_window.title("Warnet.NET")
                    update_window.geometry("820x400")
                    update_window.configure(bg="#282c35")

                    icon_image = Image.open("icon3.jpg")
                    tk_icon = ImageTk.PhotoImage(icon_image)
                    update_window.iconphoto(False, tk_icon)

                    # LabelFrame untuk menampilkan data
                    info_frame = ttk.LabelFrame(
                        update_window, text="Data yang Akan Diupdate", padding=(10, 5))
                    info_frame.grid(row=0, column=0, padx=10,
                                    pady=10, sticky='we')

                    columns = ("ID Pesanan", "Nama", "PC", "Waktu", "Harga",
                               "Jam Main", "Jam Habis", "Tanggal", "Status Bayar")
                    treeview_info = ttk.Treeview(
                        info_frame, columns=columns, show="headings", style="Custom.Treeview", height=1)
                    for col in columns:
                        treeview_info.heading(col, text=col)

                    # Set the column widths
                    col_widths = (80, 100, 120, 50, 80, 80, 80, 80, 100)
                    for col, width in zip(columns, col_widths):
                        treeview_info.column(col, width=width)

                    treeview_info.grid(
                        row=0, column=0, pady=(5, 10), sticky='we')

                    # Mengisi data ke dalam Treeview
                    treeview_info.insert("", "end", values=rental_data)

                    # Label dan Combobox untuk status pembayaran
                    label_status = tk.Label(update_window, text="Status Pembayaran:", font=(
                        'Helvetica', 12), bg="#282c35", fg="white")
                    # Menempel di sisi kiri
                    label_status.grid(row=1, column=0, pady=(
                        5, 10), padx=(10, 5), sticky='w')

                    options = ["LUNAS", "BELUM LUNAS"]
                    combobox_status = ttk.Combobox(
                        update_window, textvariable=self.status_pembayaran_var, values=options, state="readonly")
                    combobox_status.set("BELUM LUNAS")  # Default: BELUM LUNAS
                    # Menempel di sisi kanan
                    combobox_status.grid(row=1, column=0, pady=(
                        5, 10), padx=(5, 10))

                    # Tombol untuk mengonfirmasi perubahan status pembayaran
                    button_confirm = tk.Button(update_window, text="Update Status", command=lambda: self.update_status_pembayaran(
                        selected_user_id, update_window), bg="#136C38", fg="white")
                    button_confirm.grid(row=2, column=0, columnspan=2, pady=10)

            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def update_status_pembayaran(self, selected_user_id, update_window):
        # Dapatkan status pembayaran yang dipilih
        new_status_pembayaran = self.status_pembayaran_var.get()

        # Update status pembayaran di database
        connection = create_database_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                f"UPDATE rentals SET status_pembayaran = '{new_status_pembayaran}' WHERE id_pesan = {selected_user_id}")
            connection.commit()

            messagebox.showinfo("Info", "Status Pembayaran berhasil diupdate.")
            self.refresh_info()

            # Tutup jendela update setelah berhasil diupdate
            update_window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def delete_user(self):
        selected_user_id = self.get_selected_user_id()
        if selected_user_id:
            # Hapus user berdasarkan user_id
            connection = create_database_connection()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    f"DELETE FROM rentals WHERE id_pesan = {selected_user_id}")
                connection.commit()

                messagebox.showinfo(
                    "Info", f"User with ID {selected_user_id} deleted successfully.")
                self.refresh_info()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
            finally:
                cursor.close()
                connection.close()

    def pesan(self):
        connection = create_database_connection()
        cursor = connection.cursor()
        try:
            # Sembunyikan jendela Menu
            self.withdraw()

            # Tampilkan Pesan
            menu_utama_window = Pesan(self)
            menu_utama_window.wait_window()  # Tunggu hingga Pesan ditutup

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

    def logout(self):
        # Logika untuk logout
        self.destroy()
        messagebox.showinfo("Info", "Logout berhasil")

    def get_selected_user_id(self):
        selected_item = self.treeview.selection()
        if selected_item:
            # Ambil user_id dari data yang terpilih di Treeview
            user_id = self.treeview.item(selected_item, 'values')[0]
            return user_id
        else:
            messagebox.showinfo("Info", "Pilih baris terlebih dahulu.")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Menu(root)
    root.mainloop()
