import tkinter as tk
from tkinter import ttk, Frame

class ProgressBar:
    def __init__(self, parent, length = 200):
        self.frame = Frame(parent)
        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=length, mode="determinate", maximum=100)
        self.progress.pack()

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def update_progress(self, elapsed_time, total_time):
        value = (elapsed_time / total_time) * 100
        self.progress["value"] = value
        self.progress.update()

    def destroy(self):
        self.frame.destroy()