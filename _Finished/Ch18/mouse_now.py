import pyautogui

print('Press CTRL-C to quit.')

try:
    while True:
        x, y = pyautogui.position()
        position_string = f'X: {str(x).rjust(4)} Y: {str(y).rjust(4)}'
        print(position_string, end='')
        print('\b' * len(position_string), end='', flush=True)
except:
    print("\nFinished")