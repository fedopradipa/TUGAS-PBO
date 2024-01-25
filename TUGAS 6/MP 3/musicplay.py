import tkinter as tk
from tkinter import filedialog
import pygame


class AplikasiPemutarMusik:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemutar Musik")
        self.master.geometry("700x500")
        self.master.configure(bg="#282c35")

        self.playlist = []
        self.lagu_sekarang = 0
        self.terjeda = True

        pygame.mixer.init()

        self.buat_widget()

    def buat_widget(self):
        # Daftar lagu
        self.daftar_lagu = tk.Listbox(self.master, selectmode=tk.SINGLE, bg="#212121", selectbackground="#3a3f4a",
                                      fg="white", font=("Helvetica", 12))
        self.daftar_lagu.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Tombol
        frame_tombol = tk.Frame(self.master, bg="#282c35")
        frame_tombol.pack(pady=10)

        self.tombol_muat = tk.Button(
            frame_tombol, text="Muat Lagu", command=self.muat_lagu, bg="#136C38", fg="white")
        self.tombol_muat.grid(row=0, column=0, padx=10)

        self.tombol_main = tk.Button(
            frame_tombol, text="Main", command=self.mainkan_musik, bg="#136C38", fg="white")
        self.tombol_main.grid(row=0, column=1, padx=10)

        self.tombol_terjeda = tk.Button(
            frame_tombol, text="Terjeda", command=self.terjeda_musik, bg="#136C38", fg="white")
        self.tombol_terjeda.grid(row=0, column=2, padx=10)

        self.tombol_berhenti = tk.Button(
            frame_tombol, text="Berhenti", command=self.berhenti_musik, bg="#136C38", fg="white")
        self.tombol_berhenti.grid(row=0, column=3, padx=10)

        self.tombol_selanjutnya = tk.Button(
            frame_tombol, text="Selanjutnya", command=self.lagu_berikutnya, bg="#136C38", fg="white")
        self.tombol_selanjutnya.grid(row=0, column=4, padx=10)

        # volume
        self.skala_volume = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume",
                                     command=self.atur_volume, bg="#212121", troughcolor="#136C38", fg="white")
        self.skala_volume.set(50)  # Volume default
        self.skala_volume.pack(pady=10, padx=20, fill=tk.X)

        # Label informasi lagu
        self.label_info_lagu = tk.Label(
            self.master, text="", bg="#282c35", fg="white", font=("Helvetica", 12))
        self.label_info_lagu.pack()

    def muat_lagu(self):
        lagu = filedialog.askopenfilenames(filetypes=[("File MP3", "*.mp3")])
        if lagu:
            self.playlist.extend(lagu)
            for lagu in lagu:
                self.daftar_lagu.insert(tk.END, lagu)

    def mainkan_musik(self):
        if not self.playlist:
            return

        if self.terjeda:
            pygame.mixer.music.unpause()
            self.terjeda = False
        else:
            pygame.mixer.music.load(self.playlist[self.lagu_sekarang])
            pygame.mixer.music.play()
            self.terjeda = False

        self.perbarui_info_lagu()

    def terjeda_musik(self):
        if not self.terjeda:
            pygame.mixer.music.pause()
            self.terjeda = True

    def berhenti_musik(self):
        pygame.mixer.music.stop()
        self.terjeda = True

    def lagu_berikutnya(self):
        if not self.playlist:
            return

        self.lagu_sekarang = (self.lagu_sekarang + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.lagu_sekarang])
        pygame.mixer.music.play()
        self.terjeda = False

        self.perbarui_info_lagu()

    def atur_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume) / 100)

    def perbarui_info_lagu(self):
        if self.playlist:
            info_lagu = f"Sedang Diputar: {self.playlist[self.lagu_sekarang]}"
            self.label_info_lagu.config(text=info_lagu)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPemutarMusik(root)
    root.mainloop()
