import io
import tkinter as tk
from pathlib import Path
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

from LocalImage import Localimage
from Layout import Layout

class State:
    def __init__(self) -> None:
        self.chosen_image_path = ""

    def update_image_path(self):
        self.chosen_image_path = image_path.get()


SUBSAMPLE_FACTOR = 3
TEST_PHOTO_PATH = "/home/mike/bg/space.png"
PIL_TEST_PHOTO_PATH = "/home/mike/bg/cyberpunkcity.jpg"

pil_test_img = Image.open(PIL_TEST_PHOTO_PATH).resize((480,270))


root = tk.Tk()

root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWES")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

local_image = Localimage()
layout = Layout(mainframe)

image_path = tk.StringVar()
image_path_entry = ttk.Entry(mainframe, textvariable=image_path)
image_path_entry.insert(0,TEST_PHOTO_PATH)
tk_image = ImageTk.PhotoImage(pil_test_img)

test_image_label = ttk.Label(image=tk_image, borderwidth=10, relief="solid")
hidden_label = ttk.Label(mainframe, text="I have not used my grid method")
select_button = ttk.Button(mainframe, text="Select",
                           command=lambda x=test_image_label: layout.display_widget(x))
entry_label = ttk.Label(mainframe, text="Choose an image to watermark:", borderwidth=10, border=10, relief="groove")
hide_button = ttk.Button(mainframe, text="Hide", command= lambda x=test_image_label:
                  layout.hide_image(x))
test_text_label = ttk.Label(mainframe, text="here i am")

for child in mainframe.winfo_children():
    pass
    # child.grid_configure(padx=5, pady=5)

entry_label.grid(column=0, row=1)
image_path_entry.grid(column=0, row=2)
hide_button.grid(column=0, row=3)
select_button.grid(column=0, row=4)
test_image_label.grid(column=0, row=5, pady=1)


image_path_entry.focus()



root.mainloop()
