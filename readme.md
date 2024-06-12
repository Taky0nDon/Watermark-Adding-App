This is my project for day 85 of the Angela Yu 100 Days of Code course. My goal
is to construct an application in python that will add a watermark to an image
file provided by the user.

## [Tkinter refresher](https://tkdocs.com/tutorial/index.html)


## How it Works:

1. Make sure python is installed on your sytem.
2. Pillow 10.3.0 is the only third party requirement for this program. In order
to download it, navigate to the `watermark_me` parent directory and run
`py -m pip install -r requirements.txt`
This will install pip. If you wish, you may activate a virtual environment
for this step.
3. Navigate to ./src/ and run `python3 main.py`. this will open the tkinter GUI.
4. Click on 'choose background image'. The default folder most likely doesn't
exist on your system. Navigate to the picture you wish to make your background.
5. Do the same after clicking 'choose the foreground.'
6. Type some text into the box next to the 'Add text' button. The text will be 
superimposed over your background.
7. Click 'Superimpose image' to apply the foreground to the background and text
combination. If you wish for the text to be above the foreground, simply click
'Add text' again, and the new text will appear on top of the foreground and the
background.
