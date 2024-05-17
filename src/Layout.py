import tkinter as tk
from pathlib import Path
from tkinter import PhotoImage, ttk, messagebox
from PIL import Image, ImageTk

IMAGE_RESIZE_FACTOR = 5

class Layout:
    def __init__(self, frame):
        self.frame = frame
        self.watermark_path_var = tk.StringVar()
        self.image_path_var = tk.StringVar()
        self.image_path_entry = ttk.Entry(frame, textvariable=self.image_path_var)
        self.watermark_path_entry = ttk.Entry(frame,
                                              textvariable=self.watermark_path_var
                                              )
        self.select_image_button = ttk.Button(frame,
                                        text="Choose an image to display",
                                        command=self.display_image)
        self.select_watermark_button = ttk.Button(frame,
                                                  text="Choose a watermark",
                                                  command=self.display_watermark
                                                  )
        self.image_display = ttk.Label(frame)
        self.watermark_display_label = ttk.Label(frame)
        self.image_description_label = ttk.Label(frame,
                                                 text="Image:"
                                                 )
        self.watermark_description_label = ttk.Label(frame,
                                                 text="Watermark:"
                                                 )
        self.current_image = None
        self.current_imagetk = None

    def set_image(self):
        self.image_path_str = self.image_path_var.get()
        self.image_path = Path(self.image_path_str)
        if not path_is_valid(self.image_path):
            messagebox.showerror(self.frame,
                               message=f"The path {self.image_path_str} does not exit"
                                 )
            return
        self.current_image = Image.open(self.image_path_var.get())
#            .resize(get_img_display_size(self.current_image))
        orig_width, orig_height = self.current_image.size
        new_width = orig_width//IMAGE_RESIZE_FACTOR
        new_height = orig_height//IMAGE_RESIZE_FACTOR
        self.current_imagetk = ImageTk.PhotoImage(self.current_image.resize((new_width, new_height)))


    def display_image(self):
        self.set_image()
        self.image_display.configure(image=self.current_imagetk)


    def set_watermark(self, watermark_path_var):
        self.watermark_path = Path(watermark_path_var)
        if not path_is_valid(self.watermark_path):
            messagebox.showerror(self.frame,
                               message=f"The path {self.watermark_path.as_posix()} does not exit"
                                 )
            return
        self.watermark_image = Image.open(self.watermark_path)
        orig_width, orig_height = self.watermark_image.size
        new_width = orig_width//IMAGE_RESIZE_FACTOR
        new_height = orig_height//IMAGE_RESIZE_FACTOR
        self.watermark_photoimage = ImageTk.PhotoImage(self.watermark_image.resize((new_width, new_height)))


    def display_watermark(self):
        self.set_watermark(self.watermark_path_var.get())
        self.watermark_display_label.configure(image=self.watermark_photoimage)


def path_is_valid(path: Path) -> bool:
    if not path.exists():
        return False
    return True

def get_img_display_size(img: Image.Image) -> tuple[int, int]:
    original_dim = img.size # (w, h)
    reduced_dim = original_dim[0]//4, original_dim[1]//4
    return reduced_dim
