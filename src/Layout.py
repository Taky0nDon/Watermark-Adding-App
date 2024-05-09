import tkinter as tk
from tkinter import ttk
from PIL import Image


class Layout:
    def __init__(self, frame):
        self.show_it = False
        self.frame = frame
        self.the_label = ttk.Label(self.frame, text="Showing it")


    def display_widget(self, widget: ttk.Widget):
        widget.grid(row=1, column=1)

    def hide_image(self, widget: ttk.Widget):
        widget.grid_remove()
