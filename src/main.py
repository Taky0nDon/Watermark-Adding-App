import io
import os
import tkinter as tk
from pathlib import Path, PurePath
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

from Layout import Layout

DEFAULT_FOLDER = PurePath("/home", "mike", "bg")
WATERMARK_DIR = Path(Path(os.getcwd()).parent, "assets", "img")
TEST_BG = PurePath(DEFAULT_FOLDER, "space.png")
TEST_FG = Path(WATERMARK_DIR, "python-watermark.png") 
# why does the resize method call behave differently when i inline it
# instead of doing pil_test_img.resize() on a separate line?


root = tk.Tk()

root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWES")

layout = Layout(mainframe)
layout.entry_bg_path.insert(0,TEST_BG.as_posix())
layout.entry_fg_path.insert(0, TEST_FG.as_posix())


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

layout.btn_select_bg.grid(column=0, row=0, sticky="W")
layout.entry_bg_path.grid(column=1, row=0)
layout.btn_select_bg_file.grid(column=5, row=0)
layout.btn_select_fg_file.grid(column=5, row=1)
layout.label_fg_position.grid(column=3, row=0)
layout.entry_fg_position.grid(column=4, row=0)
layout.btn_superimpose.grid(column=3, row=1)
layout.btn_select_fg.grid(column=0, row=1, sticky="W")
layout.entry_fg_path.grid(column=1, row=1)
layout.image_description_label.grid(column=0, row=2)
layout.watermark_description_label.grid(column=1, row=2)
layout.label_bg_display.grid(column=0, row=3)
layout.label_fg_display.grid(column=1, row=3)
layout.superimposed_img_display.grid(column=0, columnspan=2, row=4)
layout.button_exit_app.grid(column=0, columnspan=3, row=5)


layout.entry_bg_path.focus()



root.mainloop()
