import logging as log

def resize(parent):
    parent.update_idletasks()
    parent.geometry("")

def restart_f(main_window, parent):
        log.info("Timer reset by user.")
        for widget in parent.winfo_children():
            widget.destroy()
        main_window(parent)