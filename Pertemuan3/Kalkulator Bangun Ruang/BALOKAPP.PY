import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W


def hitung_luas():
    p = float(txtpanjang.get())
    L = float(txtlebar.get())
    T = float(txttinggi.get())
    hasil = round(2*((p*L) + (p*T) + (L*T)), 2)

    txtluas.delete(0, END)
    txtluas.insert(END, hasil)


def hitung_volume():
    p = float(txtpanjang.get())
    L = float(txtlebar.get())
    T = float(txttinggi.get())
    hasil = round(p*L*T, 2)

    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil)


def hitung():
    hitung_luas()
    hitung_volume()


# create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("kalkulator menghitung luas dan volume Balok")

# Windows
frame = Frame(app)
frame.pack(padx=30, pady=30)

# label Panjang
panjang = Label(frame, text="Panjang:").grid(
    row=0, column=0, sticky=W, padx=5, pady=5)
# Label Lebar
lebar = Label(frame, text="Lebar:").grid(
    row=1, column=0, sticky=W, padx=5, pady=5)
# Label Tinggi
tinggi = Label(frame, text="Tinggi:").grid(
    row=2, column=0, sticky=W, padx=5, pady=5)

# textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)
# textbox lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)
# textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

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
