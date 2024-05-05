import tkinter as tk
from tkinter import ttk
from PIL import Image


class Layout:
    def __init__(self, frame):
        self.show_it = False
        self.frame = frame
        self.the_label = None


    def display_image(self):
        self.the_label = ttk.Label(self.frame, text="Showing it")
        self.the_label.grid(column=0, row=4, columnspan=4)

    def hide_image(self):
        self.the_label.grid_remove()
