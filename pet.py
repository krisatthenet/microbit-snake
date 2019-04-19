# Add your Python code here. E.g.
from microbit import *


display.show(Image.SNAKE)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SILLY)
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.CONFUSED)
    else:
        display.show(Image.SAD)