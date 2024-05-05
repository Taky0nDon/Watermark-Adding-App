import tkinter as tk
from pathlib import Path
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

from LocalImage import Localimage
from Layout import Layout

def get_BitmapImage(**kwargs):
    layout.display_image()
    img_path = image_path.get()
    local_image.image_path = img_path
    img = Image.open(img_path)
    print("Accessing image located at", img_path)
    layout.show_it = True
    print(layout.show_it)
    # return ImageTk.PhotoImage(img)
    

local_image = Localimage()
root = tk.Tk()
root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
layout = Layout(mainframe)

mainframe.grid(column=0, row=0, sticky="NWES")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

image_path = tk.StringVar()
image_path_entry = ttk.Entry(mainframe, width=7, textvariable=image_path)
image_path_entry.insert(0, "/home/mike/bg/space.png")
image_path_entry.grid(column=0, row=1, columnspan=4, sticky="WE")

meters = tk.StringVar()
# ttk.Label(mainframe, textvariable=meters)\
#         .grid(column=2, row=2, sticky="WE")

ttk.Button(mainframe, text="Select", command=get_BitmapImage)\
        .grid(column=3, row=3, sticky="W")

ttk.Label(mainframe, text="Choose an image to watermark:")\
    .grid(column=2, row=0, sticky="E") 

hide = ttk.Button(mainframe, text="Hide", command=layout.hide_image)\
        .grid(column=0, row=3, sticky="E")
# ttk.Label(mainframe, text="meters")\
#         .grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

image_path_entry.focus()



root.mainloop()
