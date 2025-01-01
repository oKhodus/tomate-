import tkinter as tk
from tkinter import ttk
from logic.timer import start_timer
from logic.utils import *
from data.calendar import add_event_to_calendar

def create_main_window(root):
    root.title("Tomate!")
    root.geometry("320x300")
    root.pack_propagate(False)

    root.iconbitmap("staff/tomat.ico")
    base_font = ("Helvetica", 14)

    label = tk.Label(root, text="Welcome to Tomate! \n \
Please enter duration of \n \
work and break (in minutes)", font=base_font)
    label.pack(anchor="center")

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

    restart_btn = tk.Button(root, text="Reset timer", command=lambda: restart_f(create_main_window, root))

    end_btn = tk.Button(root, text="Try Again", command=lambda: restart_f(create_main_window, root))

    button = tk.Button(root, text="Start timer", command=lambda: start_timer(work_entry, break_entry, sumround_entry, timer_label, progress_frame, label, button, work_label, break_label, sumround_label, restart_btn, end_btn, root))
    button.pack()

    theme_btn = tk.Button(root, text="Dark theme", command=lambda: change_theme(root))
    theme_btn.pack()

    return work_entry, break_entry, sumround_entry, button, work_label, break_label, sumround_label, label, timer_label, progress_frame, restart_btn