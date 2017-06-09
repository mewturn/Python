### Milton Li, 2017 #################
### A simple auto-clicking program :)
#####################################

## You need the PyAutoGUI module installed. 
## For more information, I used this guide: https://automatetheboringstuff.com/chapter18/
import pyautogui as pag
import random

while True:
    ## Get x and y coordinates of the current cursor position
    x, y = pag.position()
    
    ## Click at the current cursor position with a random interval of 0 seconds to 1 second
    pag.click(x=x, y=y, interval=random.random())