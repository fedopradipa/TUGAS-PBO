import tkinter as tk
from tkinter import ttk


def konversi_suhu():
    suhu_awal = float(entry_suhu.get())
    satuan_awal = combo_suhu_awal.get()
    satuan_tujuan = combo_suhu_tujuan.get()

    if satuan_awal == satuan_tujuan:
        hasil_konversi.set(f"{suhu_awal}{satuan_awal}")
    else:
        if satuan_awal == "Celsius":
            if satuan_tujuan == "Fahrenheit":
                hasil_konversi.set(f"{(suhu_awal * 9/5) + 32} °F")
            elif satuan_tujuan == "Kelvin":
                hasil_konversi.set(f"{suhu_awal + 273.15} K")
        elif satuan_awal == "Fahrenheit":
            if satuan_tujuan == "Celsius":
                hasil_konversi.set(f"{(suhu_awal - 32) * 5/9} °C")
            elif satuan_tujuan == "Kelvin":
                hasil_konversi.set(f"{(suhu_awal - 32) * 5/9 + 273.15} K")
        elif satuan_awal == "Kelvin":
            if satuan_tujuan == "Celsius":
                hasil_konversi.set(f"{suhu_awal - 273.15} °C")
            elif satuan_tujuan == "Fahrenheit":
                hasil_konversi.set(f"{(suhu_awal - 273.15) * 9/5 + 32} °F")


app = tk.Tk()
app.title("Aplikasi Konversi Suhu")
app.geometry("500x300")
app.configure(bg="black")

label_masukan_suhu = tk.Label(
    app, text="Masukkan Suhu", bg="black", fg="red", font=12)
label_masukan_suhu.grid(row=0, column=0, padx=10, pady=10)

label_suhu = tk.Label(app, text="Suhu", bg="black", fg="red")
label_suhu.grid(row=1, column=0, padx=10, pady=10)

entry_suhu = tk.Entry(app)
entry_suhu.grid(row=1, column=1, padx=10, pady=10)

combo_suhu_awal = ttk.Combobox(app, values=["Celsius", "Fahrenheit", "Kelvin"], width=8)
combo_suhu_awal.set("Celsius")
combo_suhu_awal.grid(row=1, column=2, padx=10, pady=10)

label_konversi_ke = tk.Label(app, text="Konversi ke", bg="black", fg="red")
label_konversi_ke.grid(row=3, column=0, padx=10, pady=10)

combo_suhu_tujuan = ttk.Combobox(app, values=["Celsius", "Fahrenheit", "Kelvin"])
combo_suhu_tujuan.grid(row=3, column=1, padx=10, pady=10)

button_konversi = tk.Button(app, text="Konversi", bg="red", fg="black", command=konversi_suhu)
button_konversi.grid(row=4, column=1, padx=10, pady=10)

hasil_konversi = tk.StringVar()
label_hasil_konversi = tk.Label(
    app, textvariable=hasil_konversi, bg="black", fg="red", font=12)
label_hasil_konversi.grid(row=5, column=1, padx=10, pady=10)

app.mainloop()
