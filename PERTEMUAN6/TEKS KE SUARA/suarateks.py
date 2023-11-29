import tkinter as tk
from gtts import gTTS
from playsound import playsound


class AplikasiTeksKeSuara:
    def __init__(self, master):
        self.master = master
        self.master.title("Konversi Teks ke Suara")
        self.master.geometry("400x250")
        self.master.configure(bg="#2C2F33")

        self.label_judul = tk.Label(
            self.master, text="Konversi Teks ke Suara", bg="#2C2F33", fg="#7289DA", font=("Helvetica", 18, "bold"))
        self.label_judul.pack(pady=10)

        self.label_petunjuk = tk.Label(
            self.master, text="Masukkan teks di bawah ini:", bg="#2C2F33", fg="white", font=("Helvetica", 12))
        self.label_petunjuk.pack()

        self.entry_teks = tk.Entry(
            self.master, font=("Helvetica", 14), bg="#7289DA", fg="white", width=30)
        self.entry_teks.pack(pady=10)

        self.tombol_konversi = tk.Button(
            self.master, text="Konversi", command=self.konversi_teks, bg="#7289DA", fg="white")
        self.tombol_konversi.pack(pady=10)

    def konversi_teks(self):
        teks_konversi = self.entry_teks.get()

        if teks_konversi:
            # Ganti "id" sesuai dengan bahasa yang diinginkan
            tts = gTTS(text=teks_konversi, lang="id")
            tts.save("output.mp3")
            playsound("output.mp3")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTeksKeSuara(root)
    root.mainloop()
