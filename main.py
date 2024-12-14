import time as t
import tkinter as tk

root = tk.Tk()

root.title("Tomate!")
root.geometry("490x270")
# 1920x1080 / 4

label = tk.Label(root, text="Welcome to Tomate! \n \
Please enter duration of work and break (in minutes)")

label.pack()

work_entry = tk.Entry(root)
work_entry.pack()

break_entry = tk.Entry(root)
break_entry.pack()


def start_timer():
    try:
        user_work = int(work_entry.get() * 60)
        user_break = int(break_entry.get() * 60)
        tomate_timer(user_work, user_break, 1)
        
    except ValueError:
        label.config(text="Please enter valid number!")


def tomate_timer(work_t, break_t, loop, loops = 4):
    if loop > loops:
        label.config(text="That's all the work is done, good job!")
        return

    label.config(text=f"Round number {loop}: work time is - {work_t // 60} min")
    root.after(work_t * 1000, start_break, break_t, loop, loops)

    def start_break(break_t, loop, loops):
        label.config(text="Break time!")
        root.after(break_t * 1000,tomate_timer, break_t, break_t, loop + 1, loops)
        

button = tk.Button(root, text="Push", command=start_timer)
button.pack()

root.mainloop()