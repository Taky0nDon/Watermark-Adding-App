import io
import tkinter as tk
from pathlib import Path
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

from LocalImage import Localimage
from Layout import Layout

def get_Image_object(path: Path):
    img = Image.open(path)
    return img


def get_BitmapImage(**kwargs):
    tk_compatible_image = tk.PhotoImage(file=image_path.get())
    img_label = ttk.Label(image=tk_compatible_image)
    img_label['image'] = tk_compatible_image
    img_label.grid(row=0, column=2)
    
    
SUBSAMPLE_FACTOR = 3
TEST_PHOTO_PATH = "/home/mike/bg/space.png"
PIL_TEST_PHOTO_PATH = "/home/mike/bg/cyberpunkcity.jpg"
pil_test_img = Image.open(PIL_TEST_PHOTO_PATH).resize((480,270))



root = tk.Tk()
tk_image = ImageTk.PhotoImage(pil_test_img)

root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWES")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

local_image = Localimage()
layout = Layout(mainframe)

image_path = tk.StringVar()
image_path_entry = ttk.Entry(mainframe, width=7, textvariable=image_path)
image_path_entry.insert(0,TEST_PHOTO_PATH)
image = tk.PhotoImage(file=Path(image_path.get())).subsample(SUBSAMPLE_FACTOR)
# test_image_label = ttk.Label(image=image, width=200)
test_image_label = ttk.Label(image=tk_image, width=200)

hidden_label = ttk.Label(mainframe, text="I have not used my grid method")
select_button = ttk.Button(mainframe, text="Select",
                           command=lambda x=test_image_label: layout.display_widget(x))

entry_label = ttk.Label(mainframe, text="Choose an image to watermark:")

hide = ttk.Button(mainframe, text="Hide", command= lambda x=test_image_label:
                  layout.hide_image(x))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

entry_label.grid(column=2, row=0, sticky="E")
hide.grid(column=1, row=3, sticky="E")
select_button.grid(column=3, row=3, sticky="W")
image_path_entry.grid(column=0, row=1, columnspan=4, sticky="WE")
test_image_label.grid(column=0, row=4, columnspan=4)
hidden_label.grid_remove()
image_path_entry.focus()



root.mainloop()
