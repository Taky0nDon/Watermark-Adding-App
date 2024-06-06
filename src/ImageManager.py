from PIL import Image, ImageTk, ImageDraw, ImageFont
from pathlib import Path
from os import environ

class ImageManager:
    def __init__(self) -> None:
        self.SAVE_DIR = Path(environ["OLDPWD"], "user_images")
        self.IMAGE_RESIZE_FACTOR = 5
        self.initial_pil_bg = None
        self.pil_bg = None
        self.imgtk_bg = None
        self.pil_fg = Image.new("RGBA", (1, 1))
        self.imgtk_fg = None
        self.pil_superimposed = None
        self.imgtk_superimposed = None
        self.fg_x_position = 0
        self.fg_y_position = 0


    def draw_text(self, text2draw):
        font_size = 100
        self.pil_bg = self.initial_pil_bg
        assert self.pil_bg is not None, "You must choose a background before\
               you can add text!"
        user_string = text2draw
        with self.pil_bg as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0)) 
            txt.resize(base.size)
            fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
            drawer = ImageDraw.Draw(txt)
            while fnt.getlength(user_string) > self.pil_bg.size[0] - 10:
                font_size -= 1
                fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
            drawer.text((10,10), user_string, font=fnt, fill=(255, 255, 255, 128), font_size=100)
            print(f"{fnt.getlength(user_string)}")
            print(self.pil_bg.size)
            self.pil_bg = Image.alpha_composite(base.convert("RGBA"), txt)



    def save_img(self) -> None:
        """ Saves the superimposed image as a file """
        if self.pil_superimposed is not None:
            self.pil_superimposed.save(fp=f"{self.SAVE_DIR}/test.png")


    def set_bg_image(self, path: str)-> None:
        """ Creates a new Image object based on a user provided path,
        and assigns it to the `pil_bg` attribute. """
        self.image_path = Path(path)
        if not path_is_valid(self.image_path):
            self.pil_bg = None
            return
        current_image = Image.open(self.image_path)
        orig_width, orig_height = current_image.size
        new_width = orig_width//self.IMAGE_RESIZE_FACTOR
        new_height = orig_height//self.IMAGE_RESIZE_FACTOR
        self.pil_bg = current_image.resize((new_width, new_height))
        self.initial_pil_bg = self.pil_bg.copy()
        self.imgtk_bg = ImageTk.PhotoImage(self.pil_bg.resize((new_width, new_height)))

    def set_fg_image(self, path: str)-> None:
        watermark_image = Image.open(Path(path))
        orig_width, orig_height = watermark_image.size
        new_width = orig_width//self.IMAGE_RESIZE_FACTOR
        new_height = orig_height//self.IMAGE_RESIZE_FACTOR
        self.pil_fg = watermark_image.resize((new_width, new_height))
        self.imgtk_fg = ImageTk.PhotoImage(self.pil_fg)


    def set_fg_position(self, pos_coords: str)-> None:
        coords = [int(e) for e in pos_coords]
        self.fg_x_position = coords[0]
        self.fg_y_position = coords[1]


    def generate_superimposed_img(self, fg_pos: str)-> None:
        if self.pil_bg is not None:
            coords = [int(e) for e in fg_pos.split(",")]
            self.fg_x_position = coords[0]
            self.fg_y_position = coords[1]
# this way the original background is preserved so the overlay can be moved
# without stamping the foreground all over it.
            pil_bg = self.pil_bg.convert(mode="RGBA")
            pil_fg = self.pil_fg.convert(mode="RGBA")
            try:
                pil_bg.paste(pil_fg, 
                             box=(self.fg_x_position, self.fg_y_position),
                             mask=pil_fg
                             )
            except AttributeError:
                pil_bg = pil_fg
            self.pil_superimposed = pil_bg
            self.imgtk_superimposed = ImageTk.PhotoImage(self.pil_superimposed)
        else:
            messagebox.showerror(title="No background selected!",
                                 message="You must choose a background image."
                                 )
        # the alpha channel is caushing all the negative space to appear the same color as
        # the blue part of the icon. Need to get paste to respect transparent parts of 
        # watermark


def path_is_valid(path: Path) -> bool:
    if not path.exists():
        return False
    return True


def get_img_display_size(img: Image.Image) -> tuple[int, int]:
    original_dim = img.size # (w, h)
    reduced_dim = original_dim[0]//4, original_dim[1]//4
    return reduced_dim
