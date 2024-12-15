import tkinter as tk
import pygame

root = tk.Tk()
pygame.mixer.init()

root.title("Tomate!")
root.geometry("320x250")

root.iconbitmap("staff/tomat.ico")

base_font = ("Helvetica", 14)

label = tk.Label(root, text="Welcome to Tomate! \n \
Please enter duration of \n \
work and break (in minutes)",
font= base_font)
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

widgets = [work_entry, break_entry, work_label, break_label, sumround_label, sumround_entry]

def countdown(sec, callback):
    minutes, seconds = divmod(sec, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    if sec > 0:
        root.after(1000, countdown, sec - 1, callback)
    else:
        callback()

def play_sound():
    pygame.mixer.music.load("staff/ms/pop_sound(break).mp3")
    pygame.mixer.music.play()

def start_timer():
    try:
        user_work = int(work_entry.get()) * 60
        user_break = int(break_entry.get()) * 60
        user_rounds = int(sumround_entry.get())
        tomate_timer(user_work, user_break, 1, user_rounds)

        for widget in widgets:
            widget.destroy()
        button.destroy()

    except ValueError:
        label.config(text="Please enter valid numbers!")

def tomate_timer(work_t, break_t, loop, loops):
    if loop > loops:
        label.config(text="That's all, the work is done, good job!")
        timer_label.destroy()
        return

    def start_break():
        play_sound()
        if loop == loops:
            label.config(text=f"Break time! \nYou can relax just about - \n\
{(break_t // 60) * 2} minutes")
            countdown((break_t * 2), start_next_round)
        else:
            label.config(text=f"Break time! \nYou can relax just about - \n\
{break_t // 60} {'minutes' if break_t > 1 else 'minute'}")
            countdown(break_t, start_next_round)

    def start_next_round():
        tomate_timer(work_t, break_t, loop + 1, loops)

    label.config(text=f"Round {loop}/{loops}: Work time!")
    countdown(work_t, start_break)

button = tk.Button(root, text="Start timer", command=start_timer)
button.pack()

root.mainloop()