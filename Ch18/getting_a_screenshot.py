# from PIL import Image
import pyautogui

im = pyautogui.screenshot()
print(type(im))

print(im.getpixel((0, 0))) # (40, 44, 52)
print(im.getpixel((50, 200))) # (33, 37, 43)
 


im.save('FOOBAR.png')

