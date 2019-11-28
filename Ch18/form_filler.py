import pyautogui
import time


def fill_form():
    name_field_pos = (552, 389)
    pyautogui.click(name_field_pos)
    pyautogui.click(name_field_pos)




if __name__ == "__main__":
    intro_text = 'Starting in '
    countdown_timer = 3
    for i in range(countdown_timer):
        print(intro_text + str(countdown_timer - i), end='')
        time.sleep(1)
        print('\b' * (len(intro_text) + 1), end='', flush=True)
    fill_form()