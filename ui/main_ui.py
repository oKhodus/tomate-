import tkinter as tk
from tkinter import ttk
from logic.timer import start_timer

def create_main_window(root):
    root.title("Tomate!")
    root.geometry("320x300")
    size = root.geometry("320x300")

    root.iconbitmap("staff/tomat.ico")

    base_font = ("Helvetica", 14)

    label = tk.Label(root, text="Welcome to Tomate! \n \
Please enter duration of \n \
work and break (in minutes)", font=base_font)
    label.pack()

    work_label = tk.Label(root, text="Duration of work")
    work_entry = tk.Entry(root)
    work_label.pack()
    work_entry.pack()

    break_label = tk.Label(root, text="Duration of break")
    break_entry = tk.Entry(root)
    break_label.pack()
    break_entry.pack()

    sumround_label = tk.Label(root, text="Amount of rounds")
    sumround_entry = tk.Entry(root)
    sumround_label.pack()
    sumround_entry.pack()

    timer_label = tk.Label(root, text="", font=("Helvetica", 18))
    timer_label.pack()

    progress_frame = tk.Frame(root)
    progress_frame.pack()

    button = tk.Button(root, text="Start timer", command=lambda: start_timer(work_entry, break_entry, sumround_entry, timer_label, progress_frame, label, button, work_label, break_label, sumround_label))
    button.pack()
