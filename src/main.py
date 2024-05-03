from pathlib import Path
from tkinter import *
from tkinter import ttk

from PIL import Image

def calculate(*arg):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Watermark Me")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

image_path = StringVar()
image_path_entry = ttk.Entry(mainframe, width=7, textvariable=image_path)
image_path_entry.grid(column=0, row=1, columnspan=4, sticky="WE")

meters = StringVar()
# ttk.Label(mainframe, textvariable=meters)\
#         .grid(column=2, row=2, sticky="WE")

ttk.Button(mainframe, text="Select", command=calculate)\
        .grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Choose an image to watermark:")\
    .grid(column=2, row=0, sticky=E) 

# ttk.Label(mainframe, text="meters")\
#         .grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

image_path_entry.focus()
root.bind("<Return>", calculate)



root.mainloop()
