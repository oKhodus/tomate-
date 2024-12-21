import pygame
from tkinter import messagebox
from logic.sound import play_sound

pygame.mixer.init()

def start_timer(work_entry, break_entry, sumround_entry, timer_label, progress, label, button, work_label, break_label, sumround_label):
    try:
        user_work = int(work_entry.get()) * 60
        user_break = int(break_entry.get()) * 60
        user_rounds = int(sumround_entry.get())

        # progress.pack()
        tomate_timer(user_work, user_break, 1, user_rounds, timer_label, progress, label)
        widgets = [work_entry, break_entry, sumround_entry, button, work_label, break_label, sumround_label]
        for widget in widgets:
            widget.destroy()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

def tomate_timer(work_t, break_t, loop, loops, timer_label, progress, label):
    if loop > loops:
        play_sound()
        label.config(text="That's all, the work is done, good job!")
        timer_label.config(text="")
        return

    # update_progress(progress, loop, loops)

    def start_break():
        play_sound()
        if loop == loops:
            label.config(text=f"Break time! \nYou can relax just about - \n{(break_t // 60) * 2} minutes")
            countdown((break_t * 2), start_next_round, timer_label)
        else:
            label.config(text=f"Break time! \nYou can relax just about - \n{break_t // 60} {'minutes' if break_t > 1 else 'minute'}")
            countdown(break_t, start_next_round, timer_label)

    def start_next_round():
        play_sound()
        tomate_timer(work_t, break_t, loop + 1, loops, timer_label, progress, label)

    label.config(text=f"Round {loop}/{loops}: Work time!")
    countdown(work_t, start_break, timer_label)

def countdown(sec, callback, timer_label):
    minutes, seconds = divmod(sec, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    if sec > 0:
        timer_label.after(1000, countdown, sec - 1, callback, timer_label)
    else:
        callback()

# def update_progress(progress, current_round, total_rounds):
#     progress_value = (current_round / total_rounds) * 100
#     progress["value"] = progress_value
#     progress.update()
