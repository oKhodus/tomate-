import tkinter as tk
from ui.main_ui import create_main_window
import logging as log

log.basicConfig(
    filename="tomate.log", 
    level=log.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    log.info("App started...")
    root = tk.Tk()
    create_main_window(root)
    try:
        root.mainloop()
    except Exception as e:
        log.error(f"App crashed: ///{e}///")
    finally:
        log.info("App closed.")
