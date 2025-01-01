import logging as log
from ttkthemes import ThemedTk

def resize(parent):
    parent.update_idletasks()
    parent.geometry("")

def restart_f(main_window, parent):
    log.info("Timer reset by user.")
    for widget in parent.winfo_children():
        widget.destroy()
    main_window(parent)


def change_theme(parent):
    if isinstance(parent, ThemedTk):
        log.info("Changing theme to equilux...")
        parent.set_theme("equilux")
        parent.after(100, lambda: parent.update_idletasks())
    else:
        log.error("parent is not an instance of ThemedTk")