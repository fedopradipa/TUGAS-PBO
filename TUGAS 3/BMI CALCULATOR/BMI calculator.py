import tkinter as tk
from tkinter import Frame, Label, Entry, Button, W
from tkinter import ttk


def hitung_bmi_USunits():
    berat = float(txtweight.get())
    tinggi_kaki = float(txtheight_feet.get())
    tinggi_inci = float(txtheight_inches.get())
    usia = float(txtage.get())
    jenis_kelamin = jenis_kelamin_var.get()
    tinggi_dalam_inci = (tinggi_kaki * 12) + \
        tinggi_inci  # KOnversi tinggi ke inci
    bmi = (berat / (tinggi_dalam_inci ** 2)) * 703
    if usia <= 20:
        if jenis_kelamin == "Pria":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]
    else:
        if jenis_kelamin == "Pria":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]
    label_hasil.config(text=f"BMI: {bmi:.2f} ({kategori[0]})")


def hitung_bmi_MatricUnits():
    berat = float(txtweight1.get())
    tinggi = float(txtheight.get())
    usia = float(txtage1.get())
    jenis_kelamin = jenis_kelamin_var.get()
    bmi = berat / ((tinggi / 100) ** 2)
    if usia <= 20:
        if jenis_kelamin == "Pria":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]
    else:
        if jenis_kelamin == "Pria":
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        else:
            nilai_bmi = [18.5, 24.9, 29.9, 100]
        kategori = ["Kurus", "Berat Normal", "Kegemukan", "Obesitas"]
    label_hasil1.config(text=f"BMI: {bmi:.2f} ({kategori[0]})")


app = tk.Tk()
app.title("Kalkulator BMI")

frame = ttk.Frame(app)
frame.grid(row=0, column=0)

notebook = ttk.Notebook(frame)
notebook.grid()

frame1 = ttk.Frame(notebook)
frame1.grid()

frame2 = ttk.Frame(notebook)
frame2.grid()

notebook.add(frame1, text="US Units")
notebook.add(frame2, text="Metric Units")
# Label frame 1
Label(frame1, text="Usia:").grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
Label(frame1, text="Berat (pound):").grid(
    row=1, column=0, padx=5, pady=5, sticky=W)
Label(frame1, text="Tinggi (kaki):").grid(
    row=2, column=0, padx=5, pady=5, sticky=W)
Label(frame1, text="Tinggi (inci):").grid(
    row=2, column=2, padx=5, pady=5, sticky=W)
Label(frame1, text="Jenis Kelamin:").grid(
    row=3, column=0, padx=5, pady=5, sticky=W)

# label frame 2
Label(frame2, text="Usia:").grid(
    row=0, column=0, padx=5, pady=5, sticky=W)
Label(frame2, text="Jenis Kelamin:").grid(
    row=1, column=0, padx=5, pady=5, sticky=W)
Label(frame2, text="Tinggi (cm):").grid(
    row=2, column=0, padx=5, pady=5, sticky=W)
Label(frame2, text="Berat (kg):").grid(
    row=3, column=0, padx=5, pady=5, sticky=W)
# Textbox frame 1
txtage = Entry(frame1)
txtage.grid(row=0, column=1)

txtweight = Entry(frame1)
txtweight.grid(row=1, column=1)

txtheight_feet = Entry(frame1)
txtheight_feet.grid(row=2, column=1)

txtheight_inches = Entry(frame1)
txtheight_inches.grid(row=2, column=3)

jenis_kelamin_var = tk.StringVar()
jenis_kelamin_var.set("Pria")

pria_radio = tk.Radiobutton(
    frame1, text="Pria", variable=jenis_kelamin_var, value="Pria")
perempuan_radio = tk.Radiobutton(
    frame1, text="Perempuan", variable=jenis_kelamin_var, value="Perempuan")

pria_radio.grid(row=3, column=1, padx=5, pady=5, sticky=W)
perempuan_radio.grid(row=3, column=2, padx=5, pady=5, sticky=W)
# textbox frame2
txtage1 = Entry(frame2)
txtage1.grid(row=0, column=1)

jenis_kelamin_var = tk.StringVar()
jenis_kelamin_var.set("Pria")

pria_radio = tk.Radiobutton(
    frame2, text="Pria", variable=jenis_kelamin_var, value="Pria")
perempuan_radio = tk.Radiobutton(
    frame2, text="Perempuan", variable=jenis_kelamin_var, value="Perempuan")

pria_radio.grid(row=1, column=1, padx=5, pady=5, sticky=W)
perempuan_radio.grid(row=1, column=2, padx=5, pady=5, sticky=W)

txtheight = Entry(frame2)
txtheight.grid(row=2, column=1)

txtweight1 = Entry(frame2)
txtweight1.grid(row=3, column=1)
# Button frame 1
hitung_button = Button(frame1, text="Hitung", command=hitung_bmi_USunits)
hitung_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky=W)

# button frame 2
hitung_button = Button(frame2, text="Hitung", command=hitung_bmi_MatricUnits)
hitung_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky=W)
# label hasil frame 1
label_hasil = Label(frame1, text="BMI: ")
label_hasil.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=W)
# label hasil frame 2
label_hasil1 = Label(frame2, text="BMI: ")
label_hasil1.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky=W)

app.mainloop()
