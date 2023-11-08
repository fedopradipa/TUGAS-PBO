import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W


def hitung_luas():
    pas = float(txtpajang_alas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tl = float(txttinggi_limas.get())
    hasil = round(pas+3*(pas*ts/2), 2)

    txtluas.delete(0, END)
    txtluas.insert(END, hasil)


def hitung_volume():
    pas = float(txtpajang_alas_segitiga.get())
    ts = float(txttinggi_segitiga.get())
    tl = float(txttinggi_limas.get())
    hasil = round((pas*ts/2)*tl/3, 2)

    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil)


def hitung():
    hitung_luas()
    hitung_volume()


# create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("kalkulator menghitung luas dan volume LIMAS SEGITGA")

# Windows
frame = Frame(app)
frame.pack(padx=30, pady=30)

# label Panjang alas segitiga
panjang_alas_segitiga = Label(frame, text="panjang alas segitiga: ").grid(
    row=0, column=0, sticky=W, padx=5, pady=5)
# Label tinggi segitiga
tinggi_segitiga = Label(frame, text="tinggi segitiga: ").grid(
    row=1, column=0, sticky=W, padx=5, pady=5)
# Label tinggi limas
tinggi_limas = Label(frame, text="tinggi limas: ").grid(
    row=2, column=0, sticky=W, padx=5, pady=5)


# textbox
txtpajang_alas_segitiga = Entry(frame)
txtpajang_alas_segitiga.grid(row=0, column=1)

txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=1, column=1)

txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=2, column=1)

# button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# output label luas
luas = Label(frame, text="luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# output label volume
volume = Label(frame, text="volume")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# output textbox luas
txtluas = Entry(frame)
txtluas.grid(row=4, column=1, sticky=W, padx=5, pady=5)
# output textbox volume
txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)


app.mainloop()
