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



def change_image():
    test_image_label.configure(image=new_tk_image)

TEST_PHOTO_PATH = "/home/mike/bg/space.png"
PIL_TEST_PHOTO_PATH = "/home/mike/bg/cyberpunkcity.jpg"
pil_test_img = Image.open(PIL_TEST_PHOTO_PATH).resize((480,270))
# why does the resize method call behave differently when i inline it
# instead of doing pil_test_img.resize() on a separate line?


root = tk.Tk()

root.title("Watermark Me")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky="NWES")

layout = Layout(mainframe)

image_path = tk.StringVar()
image_path_entry = ttk.Entry(mainframe, textvariable=image_path)
image_path_entry.insert(0,TEST_PHOTO_PATH)
tk_image = ImageTk.PhotoImage(pil_test_img)
test_image_label = ttk.Label(image=tk_image)
new_image = Image.open(image_path.get()).resize((480, 270))
new_tk_image = ImageTk.PhotoImage(new_image)

entry_label = ttk.Label(mainframe, text="Choose an image to watermark:")
select_button = ttk.Button(mainframe, text="Select",
                           command=change_image)
hide_button = ttk.Button(mainframe, text="Hide", command= lambda x=test_image_label:
                  layout.hide_image(x))
test_text_label = ttk.Label(mainframe, text="here i am")
empty_label = ttk.Label(mainframe, text="")

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

entry_label.grid(column=0, row=0)
image_path_entry.grid(column=1, row=0)
hide_button.grid(column=0, row=3)
select_button.grid(column=0, row=4)
test_image_label.grid(column=0, row=5)
empty_label.grid(column=0, row=6)


image_path_entry.focus()
breakpoint()



root.mainloop()
