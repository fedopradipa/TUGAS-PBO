import tkinter as tk
from tkinter import ttk
from modulFungsi import *


def tampilkan_input():
    bentuk = combo_bentuk.get()

    # Menyembunyikan tombol dan Combobox setelah pemilihan bentuk
    button_confirm.grid_forget()
    combo_bentuk.grid_forget()

    # Menampilkan label dan entri berdasarkan bentuk yang dipilih
    if bentuk == "Kubus":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan rusuk:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        button_hitung.grid(row=4, column=0, columnspan=2, pady=10)
    elif bentuk == "Balok":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan panjang balok:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        label_input2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_input2.config(text="Masukan lebar balok:")
        entry_input2.grid(row=2, column=1, padx=10, pady=5)
        label_input3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        label_input3.config(text="Masukan tinggi balok")
        entry_input3.grid(row=3, column=1, padx=10, pady=5)
        button_hitung.grid(row=4, column=0, columnspan=2, pady=10)
    elif bentuk == "Bola":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan jari-jari bola:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        button_hitung.grid(row=4, column=0, columnspan=2, pady=10)
    elif bentuk == "Kerucut":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan jari-jari kerucut:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        label_input2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_input2.config(text="Masukan Garis pelukis:")
        entry_input2.grid(row=2, column=1, padx=10, pady=5)
        label_input3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        label_input3.config(text="Masukan tinggi kerucut:")
        entry_input3.grid(row=3, column=1, padx=10, pady=5)
        button_hitung.grid(row=4, column=0, columnspan=2, pady=10)
    elif bentuk == "Limas segiempat":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan panjang alas limas:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        label_input2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_input2.config(text="Masukan lebar alas limas:")
        entry_input2.grid(row=2, column=1, padx=10, pady=5)
        label_input3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        label_input3.config(text="Masukan tinggi limas:")
        entry_input3.grid(row=3, column=1, padx=10, pady=5)
        button_hitung.grid(row=4, column=0, columnspan=2, pady=10)
    elif bentuk == "Limas segitiga":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan panjang alas segitiga:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        label_input2.grid(
            row=2, column=0, padx=10, pady=5, sticky="w")
        label_input2.config(text="Masukan tinggi segitiga:")
        entry_input2.grid(
            row=2, column=1, padx=10, pady=5)
        label_input3.grid(
            row=3, column=0, padx=10, pady=5, sticky="w")
        label_input3.config(text="Masukan tinggi limas:")
        entry_input3.grid(
            row=3, column=1, padx=10, pady=5)
        button_hitung.grid(row=4, column=0, columnspan=2, pady=10)
    elif bentuk == "Prisma segitiga":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan sisi 1:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)

        label_input2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_input2.config(text="Masukan sisi 2:")
        entry_input2.grid(row=2, column=1, padx=10, pady=5)

        label_input3.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        label_input3.config(text="Masukan sisi 3:")
        entry_input3.grid(row=3, column=1, padx=10, pady=5)

        label_input4.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        label_input4.config(text="Masukan tinggi prisma")
        entry_input4.grid(row=4, column=1, padx=10, pady=5)

        label_input5.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        label_input5.config(text="Masukan alas:")
        entry_input5.grid(row=5, column=1, padx=10, pady=5)

        label_input6.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        label_input6.config(text="Masukan tinggi:")
        entry_input6.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        button_hitung.grid(row=7, column=0, columnspan=2, pady=10)
    elif bentuk == "Silinder":
        label_bentuk.grid_forget()
        label_input1.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        label_input1.config(text="Masukan jari-jari silinder:")
        entry_input1.grid(row=1, column=1, padx=10, pady=5)
        label_input2.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        label_input2.config(text="Masukan tinggi silinder:")
        entry_input2.grid(row=2, column=1, padx=10, pady=5)
        button_hitung.grid(row=3, column=0, columnspan=2, pady=10)


def hitung():
    bentuk = combo_bentuk.get()

    if bentuk == "Kubus":
        rusuk = float(entry_input1.get())
        luas_permukaan, volume = hitung_kubus(rusuk)
        hasil_text.set(
            f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")

    elif bentuk == "Balok":
        panjang = float(entry_input1.get())
        tinggi = float(entry_input2.get())
        lebar = float(entry_input3.get())
        luas_permukaan, volume = hitung_balok(panjang, tinggi, lebar)
        hasil_text.set(
            f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    elif bentuk == "Bola":
        jari_jari = float(entry_input1.get())
        luas_permukaan, volume = hitung_bola(jari_jari)
        hasil_text.set(
            f"luas permukaan: {luas_permukaan:.2f}\nvolume: {volume:.2f}")
    elif bentuk == "Kerucut":
        jari_jari = float(entry_input1.get())
        garis_pelukis = float(entry_input2.get())
        tinggi = float(entry_input3.get())
        luas_permukaan, volume = hitung_kerucut(
            jari_jari, garis_pelukis, tinggi)
        hasil_text.set(
            f"luas permukaan: {luas_permukaan:.2f}\nvolume: {volume:.2f}")
    elif bentuk == "Limas segiempat":
        panjang_alas_limas = float(entry_input1.get())
        tinggi_limas = float(entry_input2.get())
        lebar_alas_limas = float(entry_input3.get())
        luas_permukaan, volume = hitung_limas_segiempat(
            panjang_alas_limas, tinggi_limas, lebar_alas_limas)
        hasil_text.set(
            f"luas permukaan: {luas_permukaan:.2f}\nvolume: {volume:.2f}")
    elif bentuk == "Limas segitiga":
        panjang_alas_segitiga = float(entry_input1.get())
        tinggi_limas = float(entry_input2.get())
        tinggi_segitiga = float(entry_input3.get())
        luas_permukaan, volume = hitung_limas_segitiga(
            panjang_alas_segitiga, tinggi_segitiga, tinggi_limas)
        hasil_text.set(
            f"luas permukaan: {luas_permukaan:.2f}\nvolume: {volume:.2f}")
    elif bentuk == "Prisma segitiga":
        s1 = float(entry_input1.get())
        s2 = float(entry_input2.get())
        s3 = float(entry_input3.get())
        tinggi_prisma = float(entry_input4.get())
        alas = float(entry_input5.get())
        tinggi = float(entry_input6.get())
        luas_permukaan, volume = hitung_prisma_segitiga(
            s1, s2, s3, alas, tinggi_prisma, tinggi)
        hasil_text.set(
            f"luas permukaan: {luas_permukaan:.2f}\nvolume: {volume:.2f}")
    elif bentuk == "Silinder":
        jari_jari = float(entry_input1.get())
        tinggi = float(entry_input2.get())
        luas_permukaan, volume = hitung_silinder(jari_jari, tinggi)
        hasil_text.set(
            f"luas permukaan: {luas_permukaan:.2f}\nvolume: {volume:.2f}")


# Membuat window
window = tk.Tk()
window.title("Kalkulator Bangun Ruang")

# Membuat Combobox untuk memilih bentuk
label_bentuk = tk.Label(window, text="Pilih Bentuk:")
label_bentuk.grid(row=0, column=0, padx=10, pady=10, sticky="w")

bentuk_var = tk.StringVar()
combo_bentuk = ttk.Combobox(
    window, textvariable=bentuk_var, values=["Kubus", "Balok", "Bola", "Kerucut", "Limas segiempat", "Limas segitiga", "Prisma segitiga", "Silinder"])
combo_bentuk.grid(row=0, column=1, padx=10, pady=10)

# Tombol untuk menampilkan input
button_confirm = tk.Button(window, text="Confirm", command=tampilkan_input)
button_confirm.grid(row=1, column=2, padx=10, pady=5)

# Membuat input dan label untuk masing-masing bentuk
label_input1 = tk.Label(window, text="Masukan:")
entry_input1 = tk.Entry(window)

label_input2 = tk.Label(window, text="Masukan:")
entry_input2 = tk.Entry(window)

label_input3 = tk.Label(window, text="Masukan:")
entry_input3 = tk.Entry(window)

label_input4 = tk.Label(window, text="Masukan")
entry_input4 = tk.Entry(window)

label_input5 = tk.Label(window, text="Masukan:")
entry_input5 = tk.Entry(window)

label_input6 = tk.Label(window, text="Masukan jari-jari:")
entry_input6 = tk.Entry(window)
# Tombol untuk menghitung
button_hitung = tk.Button(window, text="Hitung", command=hitung)

# Menampilkan hasil
hasil_text = tk.StringVar()
hasil_label = tk.Label(window, textvariable=hasil_text)
hasil_label.grid(row=8, column=0, columnspan=2, pady=10)

# Menjalankan loop utama Tkinter
window.mainloop()
