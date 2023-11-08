import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W


def hitung_luas():
    r = float(txtjari_jari.get())
    L = round(4*3.14*r**2, 2)

    txtluas.delete(0, END)
    txtluas.insert(END, L)


def hitung_volume():
    r = float(txtjari_jari.get())
    L = round((4/3)*3.14*r**3, 2)

    txtvolume.delete(0, END)
    txtvolume.insert(END, L)


def hitung():
    hitung_luas()
    hitung_volume()


# create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("kalkulator menghitung luas dan volume kubus")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# label jari-jari
jari_jari = Label(frame, text="jari_jari:")
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# textbox jari-jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

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
