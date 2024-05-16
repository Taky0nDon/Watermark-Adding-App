import io
import os
import tkinter as tk
from pathlib import Path, PurePath
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

from Layout import Layout

DEFAULT_FOLDER = PurePath("/home", "mike", "bg")
WATERMARK_DIR = Path(os.getcwd(), "..", "assets", "img")
print(DEFAULT_FOLDER.as_posix())
# why does the resize method call behave differently when i inline it
# instead of doing pil_test_img.resize() on a separate line?


root = tk.Tk()

root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWES")

layout = Layout(mainframe)
layout.image_path_entry.insert(0,DEFAULT_FOLDER.as_posix())
layout.watermark_path_entry.insert(0, WATERMARK_DIR.as_posix())


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

layout.select_image_button.grid(column=0, row=0, sticky="W")
layout.image_path_entry.grid(column=1, row=0)
layout.select_watermark_button.grid(column=0, row=1, sticky="W")
layout.watermark_path_entry.grid(column=1, row=1)
layout.image_description_label.grid(column=0, row=2)
layout.watermark_description_label.grid(column=1, row=2)
layout.image_display.grid(column=0, row=3)
layout.watermark_display_label.grid(column=1, row=3)


layout.image_path_entry.focus()



root.mainloop()
