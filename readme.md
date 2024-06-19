This is my project for day 85 of the Angela Yu 100 Days of Code course. My goal
is to construct an application in python that will add a watermark to an image
file provided by the user.

## [Tkinter refresher](https://tkdocs.com/tutorial/index.html)


## How it Works:

1. If you don't already have Python installed, install it. [Latest version here]
(https://www.python.org/downloads/release/python-3124/)
2. Clone this repository and install the required third party libraries:
```
git clone https://github.com/Taky0nDon/Watermark-Adding-App.git
cd Watermark-Adding-App
python3 -m pip install -r requirements.txt
```
(If you are having trouble with this process, open an
issue and I will do my best to be of assistance.)
3. Run `python3 src/main.py` to start the program.
4. Click on 'choose background image'. Navigate to the picture you wish to make your background.
5. Do the same after clicking 'choose the foreground.'
6. Type some text into the box next to the 'Add text' button. The text will be 
superimposed over your background.
7. Click 'Superimpose image' to apply the foreground to the background and text
combination. If you wish for the text to be above the foreground, simply click
'Add text' again, and the new text will appear on top of the foreground and the
background.
