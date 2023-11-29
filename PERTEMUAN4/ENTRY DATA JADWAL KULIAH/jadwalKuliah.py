import tkinter as tk
from tkinter import Label, Entry, Button, Text, END
from tkinter.ttk import Combobox


class AplikasiJadwalKuliah:
    def __init__(self, master):
        self.master = master
        master.title("Jadwal Kuliah App")
        master.geometry("400x500")
        master.configure(bg="black")

        self.label_judul = Label(master, text="Jadwal Kuliah", font=(
            "Arial", 16, "bold"), bg="black", fg="white")
        self.label_judul.pack(pady=10)

        self.label_hari = Label(master, text="Hari:", font=(
            "Arial", 12), bg="black", fg="white")
        self.label_hari.pack()

        self.combo_hari = Combobox(master, values=[
                                   "Senin", "Selasa", "Rabu", "Kamis", "Jumat"], state="readonly", font=("Arial", 12))
        self.combo_hari.pack(pady=5)

        self.label_instruksi = Label(master, text="Masukkan jadwal kuliah di bawah:", font=(
            "Arial", 12), bg="black", fg="white")
        self.label_instruksi.pack(pady=5)

        self.entry_jadwal = Entry(
            master, bg="#212121", fg="white", font=("Arial", 12), width=40)
        self.entry_jadwal.pack(pady=10)

        self.btn_tambah = Button(master, text="Tambah Jadwal", command=self.tambah_jadwal,
                                 bg="#136C38", fg="white", font=("Arial", 12, "bold"))
        self.btn_tambah.pack(pady=10)

        self.btn_tampilkan = Button(master, text="Tampilkan Jadwal", command=self.tampilkan_jadwal,
                                    bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
        self.btn_tampilkan.pack(pady=10)

        self.txt_jadwal = Text(master, height=10, width=40, wrap=tk.WORD,
                               bg="#212121", fg="white", font=("Arial", 12))
        self.txt_jadwal.pack(pady=10)
        self.txt_jadwal.config(state=tk.DISABLED)

    def tambah_jadwal(self):
        hari = self.combo_hari.get()
        jadwal = self.entry_jadwal.get()

        if hari and jadwal:
            with open("jadwal.txt", "a") as file:
                file.write(f"{hari}:\n{jadwal}\n\n")
            self.combo_hari.set("")  # Reset ComboBox
            self.entry_jadwal.delete(0, END)
            self.txt_jadwal.config(state=tk.DISABLED)
            print("Jadwal berhasil ditambahkan.")
        else:
            print("Pilih hari dan isi jadwal terlebih dahulu!")

    def tampilkan_jadwal(self):
        self.txt_jadwal.config(state=tk.NORMAL)
        self.txt_jadwal.delete(1.0, END)
        try:
            with open("jadwal.txt", "r") as file:
                jadwal = file.read()
            self.txt_jadwal.insert(tk.END, jadwal)
        except FileNotFoundError:
            print("File jadwal tidak ditemukan.")
        self.txt_jadwal.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiJadwalKuliah(root)
    root.mainloop()
