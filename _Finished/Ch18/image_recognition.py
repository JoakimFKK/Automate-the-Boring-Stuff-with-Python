import pyautogui
import os

"""
Søgningen går fra pos(0, 0) til pos(x, 0), pos(0, 1) osv.
"""

os.chdir(os.path.dirname(os.path.realpath(__file__)))

img_file = 'image_recognition.png'

recognition_pos = pyautogui.locateOnScreen(img_file)
print(recognition_pos)

# pyautogui.moveTo(((recognition_pos[0] + int(recognition_pos[2] / 2)), (recognition_pos[1] + int(recognition_pos[3] / 2))), duration=1)
"""SAME AS"""
x, y = pyautogui.center(recognition_pos)
pyautogui.moveTo((x, y))