import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W


def hitung_luas_segitiga():
    s1 = float(txtsisi1.get())
    s2 = float(txtsisi2.get())
    s3 = float(txtsisi3.get())
    T = float(txttinggi_prisma.get())
    hasil = round((s1+s2+s3)*T, 2)

    txtluas_segitiga.delete(0, END)
    txtluas_segitiga.insert(END, hasil)


def hitung_luas_prisma():
    s1 = float(txtsisi1.get())
    s2 = float(txtsisi2.get())
    s3 = float(txtsisi3.get())
    a = float(txtalas.get())
    T = float(txttinggi_prisma.get())
    t = float(txttinggi.get())
    hasil = round((s1+s2+s3)*T*a*t, 2)

    txtluas_prisma.delete(0, END)
    txtluas_prisma.insert(END, hasil)


def hitung_volume():
    a = float(txtalas.get())
    T = float(txttinggi_prisma.get())
    t = float(txttinggi.get())
    hasil = round(a*t*T/2, 2)

    txtvolume.delete(0, END)
    txtvolume.insert(END, hasil)


def hitung():
    hitung_luas_segitiga()
    hitung_luas_prisma()
    hitung_volume()


# create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("kalkulator menghitung luas dan volume Prsima segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=30, pady=30)

# label sisi
sisi_1 = Label(frame, text="sisi 1: ").grid(
    row=0, column=0, sticky=W, padx=5, pady=5)
sisi_2 = Label(frame, text="sisi 2: ").grid(
    row=1, column=0, sticky=W, padx=5, pady=5)
sisi_3 = Label(frame, text="sisi 3: ").grid(
    row=2, column=0, sticky=W, padx=5, pady=5)
# Label Alas
alas = Label(frame, text="Alas:").grid(
    row=3, column=0, sticky=W, padx=5, pady=5)
# label tinggi Prisma
tinggi_prisma = Label(frame, text="Tinggi Prisma: ").grid(
    row=4, column=0, sticky=W, padx=5, pady=5)
# Label Tinggi
tinggi = Label(frame, text="Tinggi:").grid(
    row=5, column=0, sticky=W, padx=5, pady=5)

# textbox sisi
txtsisi1 = Entry(frame)
txtsisi1.grid(row=0, column=1)

txtsisi2 = Entry(frame)
txtsisi2.grid(row=1, column=1)

txtsisi3 = Entry(frame)
txtsisi3.grid(row=2, column=1)
# textbox alas
txtalas = Entry(frame)
txtalas.grid(row=3, column=1)
# textbox Tinggi prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=4, column=1)
# textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=5, column=1)
# button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# output label luas
luas_segitiga = Label(frame, text="luas segitiga: ")
luas_segitiga.grid(row=7, column=0, sticky=W, padx=5, pady=5)

luas_prisma = Label(frame, text="luas prisma: ")
luas_prisma.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# output label volume
volume = Label(frame, text="volume")
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# output textbox luas
txtluas_segitiga = Entry(frame)
txtluas_segitiga.grid(row=7, column=1, sticky=W, padx=5, pady=5)
txtluas_prisma = Entry(frame)
txtluas_prisma.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# output textbox volume
txtvolume = Entry(frame)
txtvolume.grid(row=9, column=1, sticky=W, padx=5, pady=5)


app.mainloop()
