import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk


class AplikasiPemutarVideo:
    def __init__(self, master):
        self.master = master
        self.master.title("Pemutar Video")
        self.master.geometry("800x600")
        self.master.configure(bg="#282c35")

        self.video_path = ""
        self.vid = None
        self.canvas = None
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        # Canvas untuk menampilkan video
        self.canvas = tk.Canvas(self.master, bg="#212121")
        self.canvas.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Buttons
        button_frame = tk.Frame(self.master, bg="#282c35")
        button_frame.pack(pady=10)

        self.load_button = tk.Button(
            button_frame, text="Muat Video", command=self.load_video, bg="#136C38", fg="white")
        self.load_button.grid(row=0, column=0, padx=10)

        self.play_button = tk.Button(
            button_frame, text="Main", command=self.play_video, bg="#136C38", fg="white")
        self.play_button.grid(row=0, column=1, padx=10)

        self.pause_button = tk.Button(
            button_frame, text="Pause", command=self.pause_video, bg="#136C38", fg="white")
        self.pause_button.grid(row=0, column=2, padx=10)

        self.stop_button = tk.Button(
            button_frame, text="Berhenti", command=self.stop_video, bg="#136C38", fg="white")
        self.stop_button.grid(row=0, column=3, padx=10)

    def load_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("File Video", "*.mp4")])
        if self.video_path:
            self.vid = cv2.VideoCapture(self.video_path)
            self.show_frame()

    def play_video(self):
        self.paused = False
        self.show_frame()

    def pause_video(self):
        self.paused = True

    def stop_video(self):
        self.paused = True
        self.vid.release()
        self.canvas.delete("all")

    def show_frame(self):
        if not self.paused and self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (800, 600))

                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=image)

                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.canvas.photo = photo

                self.master.after(10, self.show_frame)
            else:
                self.paused = True


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPemutarVideo(root)
    root.mainloop()
