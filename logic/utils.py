def delete_widget(widget, parent):
    widget.destroy()
    parent.update_idletasks()
    parent.geometry("")
