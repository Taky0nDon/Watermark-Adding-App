import os
import tkinter as tk
from pathlib import Path
from tkinter import PhotoImage, ttk, messagebox
from PIL import Image, ImageTk

IMAGE_RESIZE_FACTOR = 5
SAVE_DIR = Path(os.environ["OLDPWD"], "user_images")

class Layout:
    def __init__(self, frame):
        self.save_path = os.environ
        print(self.save_path)
        self.frame = frame
        self.current_image = None
        self.current_imagetk = None
        self.watermark_image = Image.new("RGBA", (1, 1))
        self.superimposed_img = None
        self.superimposed_img_tk = None
        self.watermark_photoimage = None
        self.fg_x_position = 0
        self.fg_y_position = 0
        self.watermark_path_var = tk.StringVar()
        self.image_path_var = tk.StringVar()
        self.fg_position = tk.StringVar(value="0,0")
        self.image_path_entry = ttk.Entry(frame, textvariable=self.image_path_var)
        self.watermark_path_entry = ttk.Entry(frame,
                                              textvariable=self.watermark_path_var
                                              )
        self.btn_select_bg = ttk.Button(frame,
                                        text="Choose an image to display",
                                        command=self.display_image)
        self.select_watermark_button = ttk.Button(frame,
                                                  text="Choose a watermark",
                                                  command=self.display_watermark
                                                  )
        self.entry_fg_position = ttk.Entry(frame,
                                           textvariable=self.fg_position
                                           )
        self.label_fg_position = ttk.Label(frame,
                                           text="Overlay position (x, y)"
                                           )
        self.btn_superimpose = ttk.Button(frame,
                                             text="Overlay image",
                                             command=self.generate_super_imposed_img
                                             )
        self.image_display = ttk.Label(frame)
        self.watermark_display_label = ttk.Label(frame)
        self.image_description_label = ttk.Label(frame,
                                                 text="Image:"
                                                 )
        self.watermark_description_label = ttk.Label(frame,
                                                 text="Watermark:"
                                                 )
        self.superimposed_img_display = ttk.Label(frame)
        self.button_save = ttk.Button(frame,
                                      text="Save.",
                                      command=self.save_img
                                      )
        self.button_exit_app = ttk.Button(frame, text="Exit", command=exit)

    def save_img(self):
        self.superimposed_img.save(fp=f"{SAVE_DIR}/test.png")

    def set_image(self):
        self.image_path_str = self.image_path_var.get()
        self.image_path = Path(self.image_path_str)
        if not path_is_valid(self.image_path):
            messagebox.showerror(self.frame,
                               message=f"The path {self.image_path_str} does not exit"
                                 )
            return
        current_image = Image.open(self.image_path_var.get())
#            .resize(get_img_display_size(self.current_image))
        orig_width, orig_height = current_image.size
        new_width = orig_width//IMAGE_RESIZE_FACTOR
        new_height = orig_height//IMAGE_RESIZE_FACTOR
        self.current_image = current_image.resize((new_width, new_height))
        self.current_imagetk = ImageTk.PhotoImage(self.current_image.resize((new_width, new_height)))


    def set_foreground_position(self):
        coords = [int(e) for e in self.fg_position.get().split(",")]
        self.fg_x_position = coords[0]
        self.fg_y_position = coords[1]

    def display_image(self):
        self.set_image()
        print(type(self.current_imagetk))
        self.image_display.configure(image=self.current_imagetk)


    def set_watermark(self, watermark_path_var):
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
        self.watermark_image = watermark_image.resize((new_width, new_height))
        self.watermark_photoimage = ImageTk.PhotoImage(self.watermark_image)


    def display_watermark(self):
        self.set_watermark(self.watermark_path_var.get())
        self.watermark_display_label.configure(image=self.watermark_photoimage)

    def generate_super_imposed_img(self):
        coords = [int(e) for e in self.fg_position.get().split(",")]
        self.fg_x_position = coords[0]
        self.fg_y_position = coords[1]
# this way the original background is preserved so the overlay can be moved
# without stamping the foreground all over it.
        pil_bg = self.current_image.copy()
        pil_fg = self.watermark_image
        try:
            pil_bg.paste(pil_fg, 
                         box=(self.fg_x_position, self.fg_y_position)
                         )
        except AttributeError:
            pil_bg = pil_fg
        self.superimposed_img = pil_bg
        self.superimposed_img_tk = ImageTk.PhotoImage(self.superimposed_img)
        self.superimposed_img_display.configure(image=self.superimposed_img_tk)
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
