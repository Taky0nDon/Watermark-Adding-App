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


root = tk.Tk()

root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWES")

layout = Layout(mainframe)
layout.create_ui()


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Establish rows and columns before adjusting span

# Adjust spans
# Could I do this in a loop? 
layout.get_frame_size()
for child in mainframe.winfo_children():
    if isinstance(child, ttk.Entry):
        child.grid(columnspan=layout.total_columns, sticky="WE")
layout.btn_superimpose.grid(columnspan=layout.total_columns)
layout.entry_bg_path.focus()



root.mainloop()
