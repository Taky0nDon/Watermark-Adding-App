from pathlib import PurePath


from Layout import Layout


DEFAULT_FOLDER = PurePath("/home", "mike", "bg")
WATERMARK_DIR = Path(Path(os.getcwd()).parent, "assets", "img")


def main() -> Layout:
    return Layout()

if __name__ == "__main__":
    main()
