from PIL import Image, ImageTk, ImageDraw, ImageFont
from pathlib import Path
from os import environ


from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showinfo,showerror

class ImageManager:
    def __init__(self) -> None:
        self.SAVE_DIR = Path(environ["OLDPWD"], "user_images")
        self.IMAGE_RESIZE_FACTOR = 5
        self.pil_bg = None
        self.pil_bg_notext = self.pil_bg
        self.imgtk_bg = None
        self.pil_fg = Image.new("RGBA", (1, 1))
        self.imgtk_fg = None
        self.pil_superimposed = None
        self.imgtk_superimposed = None
        self.fg_x_position = 0
        self.fg_y_position = 0
        self.text_exists = False


    def draw_text(self, text2draw):
        print(f"{type(self.pil_bg)=}")
        assert self.pil_bg is not None, "You must choose a background before\
               you can add text!"
        font_size = 100
        if self.text_exists:
            self.pil_bg = self.pil_bg_notext
        user_string = text2draw
        with self.pil_bg as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0)) 
            fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
            drawer = ImageDraw.Draw(txt)
            while fnt.getlength(user_string) > self.pil_bg.size[0] - 10:
                font_size -= 1
                fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
            drawer.text((10,10), user_string, font=fnt, fill=(255, 255, 255, 128), font_size=100)
            self.pil_bg = Image.alpha_composite(base.convert("RGBA"), txt)
            self.imgtk_bg = self.tkize_image(self.pil_bg)
            self.text_exists = True



    def save_img(self) -> None:
        """ Saves the superimposed image as a file """
        SAVE_DIR = Path(Path(environ["PWD"]).parent,
                        "assets",
                        "imgs",
                        "user_images")
        if self.pil_superimposed is None:
            showinfo(title="No selection", message="You have no image to save!")
        else:
            new_file_path = asksaveasfilename(initialdir=SAVE_DIR)
            self.pil_superimposed.save(fp=f"{new_file_path}.tiff", format='tiff')
            


    def set_bg_image(self, path: str)-> None:
        """ Creates a new Image object based on a user provided path,
        and assigns it to the `pil_bg` attribute. """
        image_path = Path(path)
        assert path_is_valid(image_path), "File does not exist!"
        new_bg_img = Image.open(image_path)
        orig_width, orig_height = new_bg_img.size
        new_width = orig_width//self.IMAGE_RESIZE_FACTOR
        new_height = orig_height//self.IMAGE_RESIZE_FACTOR
        self.pil_bg = new_bg_img.resize((new_width, new_height))
        self.pil_bg_notext = self.pil_bg.copy()
        self.imgtk_bg = self.tkize_image(self.pil_bg)

    def set_fg_image(self, path: str)-> None:
        fg_path = Path(path)
        assert path_is_valid(fg_path), "File does not exist!"
        new_watermark_image = Image.open(fg_path)
        orig_width, orig_height = new_watermark_image.size
        new_width = orig_width//self.IMAGE_RESIZE_FACTOR
        new_height = orig_height//self.IMAGE_RESIZE_FACTOR
        self.pil_fg = new_watermark_image.resize((new_width, new_height))
        self.imgtk_fg = self.tkize_image(self.pil_fg)


    def set_fg_position(self, pos_coords: str)-> None:
        coords = [int(e) for e in pos_coords]
        self.fg_x_position = coords[0]
        self.fg_y_position = coords[1]


    def generate_superimposed_img(self, fg_pos: str)-> None:
        if self.pil_bg is None:
            showerror(title="No background selected!",
                                 message="You must choose a background image."
                                 )
            return
        coords = [int(e) for e in fg_pos.split(",")]
        self.fg_x_position = coords[0]
        self.fg_y_position = coords[1]
        pil_bg = self.pil_bg.convert(mode="RGBA")
        pil_fg = self.pil_fg.convert(mode="RGBA")
        pil_bg.paste(pil_fg, 
                     box=(self.fg_x_position, self.fg_y_position),
                     mask=pil_fg
                     )
        self.pil_bg_notext.paste(pil_fg,
                                 box=(self.fg_x_position, self.fg_y_position),
                                 mask=pil_fg)
        self.pil_superimposed = pil_bg
        self.imgtk_superimposed = self.tkize_image(self.pil_superimposed)
        # the alpha channel is caushing all the negative space to appear the same color as
        # the blue part of the icon. Need to get paste to respect transparent parts of 
        # watermark


    def tkize_image(self, image: Image.Image):
        return ImageTk.PhotoImage(image)


def path_is_valid(path: Path) -> bool:
    if not path.exists():
        return False
    return True


def get_img_display_size(img: Image.Image) -> tuple[int, int]:
    original_dim = img.size # (w, h)
    reduced_dim = original_dim[0]//4, original_dim[1]//4
    return reduced_dim
