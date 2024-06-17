import os
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfile, askopenfilename

from PIL import ImageTk


from ImageManager import ImageManager


IMG_HOME = Path("/home/mike/code/100_days_of_code/final_projects/watermark_me/assets/imgs/")
BG_STARTING_DIR = Path(IMG_HOME, "bg")
FG_STARTING_DIR = Path(IMG_HOME, "fg")
img_mgr = ImageManager()

class Layout:
    def __init__(self, frame: tk.Frame):
        self.frame = frame
        self.total_columns, self.total_rows = 0, 0
        self.strvar_fg_path = tk.StringVar()
        self.strvar_bg_path = tk.StringVar()
        self.strvar_fg_position = tk.StringVar(value="0,0")
        self.strvar_fg_text = tk.StringVar()

        self.entry_bg_path = ttk.Entry(frame, textvariable=self.strvar_bg_path)
        self.entry_fg_path = ttk.Entry(frame, textvariable=self.strvar_fg_path)
        self.entry_fg_position = ttk.Entry(frame, textvariable=self.strvar_fg_position)
        self.entry_text = ttk.Entry(frame, textvariable=self.strvar_fg_text)

        self.btn_select_bg = ttk.Button(frame,
                                        text="choose background image",
                                        command=self.display_bg_img)
        self.btn_select_fg = ttk.Button(frame, text="choose the foreground",
                                        command=self.display_fg_img)
        self.btn_superimpose = ttk.Button(frame, text="Superimpose image",
                                          command=self.display_superimposed_image)
        self.btn_drawtxt = ttk.Button(frame, text="Add text",
                                      command=self.display_superimposed_text)
        self.btn_save = ttk.Button(frame, text="Save.", command=img_mgr.save_img)
        self.btn_exit = ttk.Button(frame, text="exit", command=exit)

        self.label_bg_indicator = ttk.Label(frame, text="Background:")
        self.label_fg_indicator = ttk.Label(frame, text="Foreground:")
        self.label_fg_position = ttk.Label(frame, text="Foreground position (x, y)")
        self.label_bg_display = ttk.Label(frame)
        self.label_fg_display = ttk.Label(frame)
        self.label_finalimg_display = ttk.Label(frame)

    def create_ui(self)-> None:

        self.btn_select_bg.grid(column=0, row=0, sticky="WE")
        self.entry_bg_path.grid(column=1, row=0)
        self.btn_select_fg.grid(column=0, row=1, sticky="WE")
        self.entry_fg_path.grid(column=1, row=1)
        self.label_fg_position.grid(column=0, row=2)
        self.entry_fg_position.grid(column=1, row=2)
        self.entry_text.grid(column=1, row=3, columnspan=7, sticky="WE")
        self.btn_drawtxt.grid(column=0, row=3, sticky="WE")
        self.btn_superimpose.grid(column=0, row=6, sticky="EW")
        self.label_bg_indicator.grid(column=0, row=4)
        self.label_fg_indicator.grid(column=1, row=4)
        self.label_fg_display.grid(column=1, row=5)
        self.label_bg_display.grid(column=0, row=5)
        self.label_finalimg_display.grid(column=0, row=7, columnspan=8)
        self.btn_save.grid(column=0, row=8, sticky="WE")
        self.btn_exit.grid(column=1, row=8, sticky="EW")


    def choose_bg_file(self) -> None:
        """ Inserts path of file chosen by user into background entry widget
        """
        bg_img_path = askopenfilename(parent=self.frame,
                              title="Choose background image",
                              initialdir="/home/mike/idontexist",
                              initialfile=sorted(os.listdir(BG_STARTING_DIR))[0]
                                      )
        self.entry_bg_path.delete(0, tk.END)
        self.entry_bg_path.insert(0, bg_img_path)
        self.entry_bg_path.xview(len(bg_img_path))

    def choose_fg_file(self):
        fg_img_path = askopenfilename(parent=self.frame,
                              title="Choose foreground image",
                              initialdir=FG_STARTING_DIR,
                              initialfile=sorted(os.listdir(FG_STARTING_DIR))[0]
                                      )
        self.entry_fg_path.delete(0, tk.END)
        self.entry_fg_path.insert(0, fg_img_path)
        self.entry_fg_path.xview(len(fg_img_path))


    def display_bg_img(self)-> None:
        self.choose_bg_file()
        img_mgr.set_bg_image(self.strvar_bg_path.get())
        self.label_bg_display.configure(
                                        image=img_mgr.imgtk_bg
                                        )


    def display_fg_img(self)-> None:
        self.choose_fg_file()
        img_mgr.set_fg_image(self.strvar_fg_path.get())
        self.label_fg_display.configure(image=img_mgr.imgtk_fg)


    def display_superimposed_image(self) -> None:
        pos = self.strvar_fg_position.get()
        img_mgr.generate_superimposed_img(pos)
        if self.entry_text is not None:
            img_mgr.draw_text(self.entry_text.get())
        self.label_finalimg_display.configure(image=img_mgr.imgtk_superimposed)


    def display_superimposed_text(self) -> None:
        img_mgr.draw_text(self.entry_text.get())
        self.label_finalimg_display.configure(image=img_mgr.imgtk_bg)

    def display_drawn_text(self):
        img_mgr.draw_text(self.entry_text.get())
        self.label_finalimg_display.configure(image=img_mgr.imgtk_bg)


    def get_frame_size(self):
        if self.frame.grid_size() is not None:
            self.total_columns, self.total_rows = self.frame.grid_size()
