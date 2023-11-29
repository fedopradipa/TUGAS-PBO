import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract


class AplikasiAmbilTeksDariGambar:
    def __init__(self, master):
        self.master = master
        self.master.title("Ambil Teks dari Gambar")
        self.master.geometry("600x400")
        self.master.configure(bg="#2C2F33")

        self.label_judul = tk.Label(
            self.master, text="Ambil Teks dari Gambar", bg="#2C2F33", fg="#7289DA", font=("Helvetica", 18, "bold"))
        self.label_judul.pack(pady=10)

        self.canvas_gambar = tk.Canvas(
            self.master, bg="white", width=300, height=200)
        self.canvas_gambar.pack(pady=10)

        self.tombol_ambil_gambar = tk.Button(
            self.master, text="Ambil Gambar", command=self.ambil_gambar, bg="#43B581", fg="white")
        self.tombol_ambil_gambar.pack(pady=10)

        self.tombol_ambil_teks = tk.Button(
            self.master, text="Ambil Teks", command=self.ambil_teks, bg="#43B581", fg="white")
        self.tombol_ambil_teks.pack(pady=10)

        self.label_hasil_teks = tk.Label(
            self.master, text="", bg="#2C2F33", fg="white", font=("Helvetica", 12))
        self.label_hasil_teks.pack()

    def ambil_gambar(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 300))
            photo = ImageTk.PhotoImage(image)
            self.canvas_gambar.config(
                width=photo.width(), height=photo.height())
            self.canvas_gambar.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas_gambar.image = photo  # to prevent garbage collection
            self.image_path = file_path

    def ambil_teks(self):
        if hasattr(self, 'image_path'):
            image = Image.open(self.image_path)
            teks = pytesseract.image_to_string(image)
            self.label_hasil_teks.config(text=teks)
        else:
            self.label_hasil_teks.config(text="Ambil gambar terlebih dahulu.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiAmbilTeksDariGambar(root)
    root.mainloop()
