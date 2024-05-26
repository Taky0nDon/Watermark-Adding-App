import os
import tkinter as tk
from pathlib import Path
from tkinter import PhotoImage, ttk, messagebox
from PIL import Image, ImageTk


from ImageManager import ImageManager

SAVE_DIR = Path(os.environ["OLDPWD"], "user_images")
img_mgr = ImageManager()
class Layout:
    def __init__(self, frame):
        self.frame = frame
        self.fg_path_stringvar = tk.StringVar()
        self.bg_path_stringvar = tk.StringVar()
        self.fg_position = tk.StringVar(value="0,0")

        self.entry_bg_path = ttk.Entry(frame, textvariable=self.bg_path_stringvar)
        self.entry_fg_path = ttk.Entry(frame,
                                              textvariable=self.fg_path_stringvar
                                              )
        self.entry_fg_position = ttk.Entry(frame, textvariable=self.fg_position)

        self.btn_select_bg = ttk.Button(frame,
                                        text="Choose an image to display",
                                        command=self.display_bg_img)
        self.btn_select_fg = ttk.Button(frame, text="Choose a watermark",
                                        command=self.display_fg_img
                                       )
        self.button_exit_app = ttk.Button(frame, text="Exit", command=exit)

        self.label_fg_position = ttk.Label(frame,
                                           text="Overlay position (x, y)"
                                           )
        self.btn_superimpose = ttk.Button(frame, text="Overlay image",
                                          command=lambda x=self.fg_position.get(): self.display_superimposed_image(x)
                                         )
        self.label_bg_display = ttk.Label(frame)
        self.label_fg_display = ttk.Label(frame)
        self.image_description_label = ttk.Label(frame, text="Image:")
        self.watermark_description_label = ttk.Label(frame, text="Watermark:")
        self.superimposed_img_display = ttk.Label(frame)
        self.button_save = ttk.Button(frame, text="Save.", command=img_mgr.save_img)


    def display_bg_img(self)-> None:
        img_mgr.set_bg_image(self.bg_path_stringvar.get())
        if img_mgr.pil_bg:
            self.label_bg_display.configure(image=img_mgr.imgtk_bg)
        else:
            self.show_error("no_path")


    def display_fg_img(self)-> None:
        img_mgr.set_fg_image(self.fg_path_stringvar.get())
        if img_mgr.pil_fg:
            self.label_fg_display.configure(image=img_mgr.imgtk_fg)
        else:
            self.show_error("no_path")


    def display_superimposed_image(self, pos) -> None:
        img_mgr.generate_superimposed_img(pos)
        self.superimposed_img_display.configure(image=img_mgr.imgtk_superimposed)

    def show_error(self, err, path=None):
        msg = "Something went wrong."
        if err == "no_path":
            msg = f"The path {path} does not exit"
        messagebox.showerror(self.frame,
                             message=msg
                            )
