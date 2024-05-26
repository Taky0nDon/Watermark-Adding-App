from PIL import Image, ImageTk
from pathlib import Path
from os import environ

class ImageManager:
    def __init__(self) -> None:
        self.SAVE_DIR = Path(environ["OLDPWD"], "user_images")
        self.IMAGE_RESIZE_FACTOR = 5
        self.pil_bg = None
        self.imgtk_bg = None
        self.pil_fg = Image.new("RGBA", (1, 1))
        self.imgtk_fg = None
        self.pil_superimposed = None
        self.imgtk_superimposed = None
        self.fg_x_position = 0
        self.fg_y_position = 0

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
        self.imgtk_bg = ImageTk.PhotoImage(self.pil_bg.resize((new_width, new_height)))

    def set_fg(self, watermark_path_var)-> None:
        self.watermark_path = Path(watermark_path_var)
        if not path_is_valid(self.watermark_path):
            messagebox.showerror(self.frame,
                               message=f"The path {self.watermark_path.as_posix()} does not exit"
                                 )
            return
        watermark_image = Image.open(self.watermark_path)
        orig_width, orig_height = watermark_image.size
        new_width = orig_width//IMAGE_RESIZE_FACTOR
        new_height = orig_height//IMAGE_RESIZE_FACTOR
        self.pil_fg = watermark_image.resize((new_width, new_height))
        self.imgtk_fg = ImageTk.PhotoImage(self.pil_fg)


def path_is_valid(path: Path) -> bool:
    if not path.exists():
        return False
    return True

