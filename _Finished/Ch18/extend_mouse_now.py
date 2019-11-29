"""Program crashes when going to a different monitor.
the screenshot that's taken doesn't extend to other monitors.

When used on a vertical monitor the range goes further than the size of the screen, but as if pyautogui sees it as horizontal.
"""
import pyautogui

print('Press CTRL-C to quit.')

try:
    while True:
        x, y = pyautogui.position()
        position_string = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        pixel_color = pyautogui.screenshot().getpixel((x, y))
        position_string += f" RGB: ({str(pixel_color[0]).rjust(3)}"
        position_string += f", {str(pixel_color[1]).rjust(3)}"
        position_string += f", {str(pixel_color[2]).rjust(3)})"
        print(position_string, end='')
        print('\b' * len(position_string), end='', flush=True)
except KeyboardInterrupt:
    print("\nFinished")