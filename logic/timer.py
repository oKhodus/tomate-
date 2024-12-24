import pygame
import logging as log
from tkinter import messagebox
from logic.sound import play_sound
from ui.progress import ProgressBar
from logic.utils import resize


pygame.mixer.init()

def start_timer(work_entry, break_entry, sumround_entry, timer_label, prg_frame, label, button, work_label, break_label, sumround_label, res_btn, end_btn, parent):
    try:
        user_work = int(work_entry.get()) * 60
        user_break = int(break_entry.get()) * 60
        user_rounds = int(sumround_entry.get())
        log.info(f"Timer started at: Work - {user_work // 60} min, Break - {user_break // 60}, Rounds - {user_rounds}")

        progress = ProgressBar(prg_frame)

        tomate_timer(user_work, user_break, 1, user_rounds, timer_label, progress, label, prg_frame, res_btn, end_btn, parent)

        widgets_base = [button, work_label, break_label, sumround_label, work_entry, break_entry, sumround_entry]
        for widget in widgets_base:
            widget.destroy()

    except ValueError as e:
        log.error(f"Invalid input: {e}")
        messagebox.showerror("Error", "Please enter valid numbers!")

def tomate_timer(work_t, break_t, loop, loops, timer_label, progress, label, prg_frame, res_btn, end_btn, parent):
    play_sound()
    if loop > loops:
        log.info("All rounds completed successfuly.")

        for widget in parent.winfo_children():
            main = [label, end_btn]
            if widget not in main:
                widget.destroy()
        parent.geometry("333x75")

        play_sound()

        label.config(text="That's all, the work is done, good job!\n\
Do you wanna try it again?")
        end_btn.pack()
        return
    
    prg_frame.pack()
    progress.pack()
    progress.update_progress(loop, loops)
    res_btn.pack()
    resize(parent)

    def start_break():
        play_sound()
        if loop == loops:
            log.info(f"Last break started: {(break_t // 60) * 2} min")
            resize(parent)
            label.config(text=f"Last break! \nRelax just about - \n{(break_t // 60) * 2} minutes")
            countdown(break_t * 2, break_t * 2, progress, start_next_round, timer_label, prg_frame)
        else:
            log.info(f"Break started: {break_t // 60} min")
            resize(parent)
            label.config(text=f"Break time! \nRelax just about - \n{break_t // 60} {'minutes' if break_t > 1 else 'minute'}")
            countdown(break_t, break_t, progress, start_next_round, timer_label, prg_frame)


    def start_next_round():
        play_sound()
        tomate_timer(work_t, break_t, loop + 1, loops, timer_label, progress, label, prg_frame, res_btn, end_btn, parent)

    log.info(f"Starting round {loop}/{loops}: Work time {work_t // 60} min")
    label.config(text=f"Round {loop}/{loops}: Work time!")
    countdown(work_t, work_t, progress, start_break, timer_label, prg_frame)

def countdown(sec, total_sec, progress, callback, timer_label, prg_frame, elapsed=0):
    minutes, seconds = divmod(sec, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    progress.update_progress(elapsed, total_sec)
    if sec % 60 == 0:
        log.info(f"Time left: {minutes} min {seconds} sec")
    if sec > 0:
        timer_label.after(1000, countdown, sec - 1, total_sec, progress, callback, timer_label, prg_frame, elapsed + 1)
    else:
        callback()