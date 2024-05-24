import os
import tkinter as tk
from pathlib import Path
from tkinter import PhotoImage, ttk, messagebox
from PIL import Image, ImageTk

IMAGE_RESIZE_FACTOR = 5
SAVE_DIR = Path(os.environ["OLDPWD"], "user_images")

class Layout:
    def __init__(self, frame):
        self.frame = frame
        self.pil_bg = None
        self.imgtk_bg = None
        self.pil_fg = Image.new("RGBA", (1, 1))
        self.imgtk_fg = None
        self.pil_superimposed = None
        self.imgtk_superimposed = None
        self.fg_x_position = 0
        self.fg_y_position = 0
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
                                        command=self.display_fg
                                       )
        self.button_exit_app = ttk.Button(frame, text="Exit", command=exit)

        self.label_fg_position = ttk.Label(frame,
                                           text="Overlay position (x, y)"
                                           )
        self.btn_superimpose = ttk.Button(frame, text="Overlay image",
                                          command=self.generate_superimposed_img
                                         )
        self.image_display = ttk.Label(frame)
        self.watermark_display_label = ttk.Label(frame)
        self.image_description_label = ttk.Label(frame, text="Image:")
        self.watermark_description_label = ttk.Label(frame, text="Watermark:")
        self.superimposed_img_display = ttk.Label(frame)
        self.button_save = ttk.Button(frame, text="Save.", command=self.save_img)

    def save_img(self) -> None:
        if self.pil_superimposed is not None:
            self.pil_superimposed.save(fp=f"{SAVE_DIR}/test.png")

    def set_bg_image(self)-> None:
        self.image_path_str = self.bg_path_stringvar.get()
        self.image_path = Path(self.image_path_str)
        if not path_is_valid(self.image_path):
            messagebox.showerror(self.frame,
                               message=f"The path {self.image_path_str} does not exit"
                                 )
            return
        current_image = Image.open(self.bg_path_stringvar.get())
#            .resize(get_img_display_size(self.current_image))
        orig_width, orig_height = current_image.size
        new_width = orig_width//IMAGE_RESIZE_FACTOR
        new_height = orig_height//IMAGE_RESIZE_FACTOR
        self.pil_bg = current_image.resize((new_width, new_height))
        self.imgtk_bg = ImageTk.PhotoImage(self.pil_bg.resize((new_width, new_height)))


    def set_fg_position(self)-> None:
        coords = [int(e) for e in self.fg_position.get().split(",")]
        self.fg_x_position = coords[0]
        self.fg_y_position = coords[1]

    def display_bg_img(self)-> None:
        self.set_bg_image()
        print(type(self.imgtk_bg))
        self.image_display.configure(image=self.imgtk_bg)


    def set_fg(self, watermark_path_var)-> None:
        self.watermark_path = Path(watermark_path_var)
        if not path_is_valid(self.watermark_path):
            messagebox.showerror(self.frame,
                               message=f"The path {self.watermark_path.as_posix()} does not exit"
                                 )
            return
        watermark_image = Image.open(self.watermark_path)
        orig_width, orig_height = watermark_image.size
        new_width = orig_width//IMAGE_RESIZE_FACTOR
        new_height = orig_height//IMAGE_RESIZE_FACTOR
        self.pil_fg = watermark_image.resize((new_width, new_height))
        self.imgtk_fg = ImageTk.PhotoImage(self.pil_fg)


    def display_fg(self)-> None:
        if self.pil_bg is not None:
            self.set_fg(self.fg_path_stringvar.get())
        self.watermark_display_label.configure(image=self.imgtk_fg)

    def generate_superimposed_img(self)-> None:
        if self.pil_bg is not None:
            coords = [int(e) for e in self.fg_position.get().split(",")]
            self.fg_x_position = coords[0]
            self.fg_y_position = coords[1]
# this way the original background is preserved so the overlay can be moved
# without stamping the foreground all over it.
            pil_bg = self.pil_bg.convert(mode="RGBA")
            pil_fg = self.pil_fg.convert(mode="RGBA")
            mask = pil_fg.copy().convert("L")
            try:
                pil_bg.paste(pil_fg, 
                             box=(self.fg_x_position, self.fg_y_position),
                             mask=mask
                             )
            except AttributeError:
                pil_bg = pil_fg
            self.pil_superimposed = pil_bg
            self.imgtk_superimposed = ImageTk.PhotoImage(self.pil_superimposed)
            self.superimposed_img_display.configure(image=self.imgtk_superimposed)
        else:
            messagebox.showerror(title="No background selected!",
                                 message="You must choose a background image."
                                 )
        # the alpha channel is caushing all the negative space to appear the same color as
        # the blue part of the icon. Need to get paste to respect transparent parts of 
        # watermark


def path_is_valid(path: Path) -> bool:
    if not path.exists():
        return False
    return True

def get_img_display_size(img: Image.Image) -> tuple[int, int]:
    original_dim = img.size # (w, h)
    reduced_dim = original_dim[0]//4, original_dim[1]//4
    return reduced_dim
