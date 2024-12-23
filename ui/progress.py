import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ProgressBar:
    def __init__(self, parent, max_tomatoes=10, tomato_size=(15, 15)):
        self.frame = tk.Frame(parent)
        self.canvas = tk.Canvas(
            self.frame, 
            width=max_tomatoes * (tomato_size[0] + 5), 
            height=tomato_size[1] + 20
        )
        self.canvas.pack()

        self.tomato_img = Image.open("staff/tom.png")
        self.tomato_img = self.tomato_img.resize(tomato_size, Image.LANCZOS)
        self.tomato_photo = ImageTk.PhotoImage(self.tomato_img)

        self.slice_width = self.tomato_img.width // 10
        self.slice_height = self.tomato_img.height

        self.max_tomatoes = max_tomatoes
        self.current_tomatoes = 0

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def update_progress(self, elapsed_time, total_time):
        value = elapsed_time / total_time
        total_slices = int(value * self.max_tomatoes * 10)
        full_tomatoes = total_slices // 10
        remaining_slices = total_slices % 10

        self.canvas.delete("all")

        for tomate in range(full_tomatoes):
            x = 10 + tomate * (self.tomato_photo.width() + 5)
            y = 10
            self.canvas.create_image(x, y, image=self.tomato_photo, anchor="nw")

        if remaining_slices > 0:
            slice_img = self.tomato_img.crop((0, 0, self.slice_width * remaining_slices, self.slice_height))
            slice_photo = ImageTk.PhotoImage(slice_img)

            x = 10 + full_tomatoes * (self.tomato_photo.width() + 5)
            y = 10
            self.canvas.create_image(x, y, image=slice_photo, anchor="nw")
        
        self.canvas.delete("percent_text")
        self.canvas.create_text(
            self.canvas.winfo_width() // 2,
            self.tomato_photo.height() + 15,
            text=f"{int(value * 100)}%",
            font=("Helvetica", 12),
            fill="black",
            tags="percent_text"
        )

    def destroy(self):
        self.frame.destroy()