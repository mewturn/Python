import pyautogui as pag
import random
import sys

text = sys.argv[1]
scale = 5

while True:
    pag.press("enter")
    pag.typewrite(text, interval=scale*random.random())
    pag.press("enter")
    
    