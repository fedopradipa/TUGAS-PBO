import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W


def hitung_luas():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    hasil = round((2*3.14*r*t) + (2*3.14*r**2), 2)

    txtluas.delete(0, END)
    txtluas.insert(END, hasil)


def hitung_volume():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    hasil = round(3.14*r**2*t, 2)

    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil)


def hitung():
    hitung_luas()
    hitung_volume()


# create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("kalkulator menghitung luas dan volume SILINDER")

# Windows
frame = Frame(app)
frame.grid()

# label jari jari silinder
jari_jari = Label(frame, text="Jari-jari: ").grid(
    row=0, column=0, sticky=W, padx=5, pady=5)
# Label tinggi silinder
tinggi = Label(frame, text="tinggi: ").grid(
    row=1, column=0, sticky=W, padx=5, pady=5)


# textbox
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# output label luas
luas = Label(frame, text="luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# output label volume
volume = Label(frame, text="volume")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# output textbox luas
txtluas = Entry(frame)
txtluas.grid(row=3, column=1, sticky=W, padx=5, pady=5)
# output textbox volume
txtvolume = Entry(frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)


app.mainloop()
