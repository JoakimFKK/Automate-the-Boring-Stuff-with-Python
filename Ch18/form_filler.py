import pyautogui as ghost
import time

def fill_form():
    # PyAutoGUI measurements
    ghost.FAILSAFE = True
    ghost.PAUSE = 1
    # Values
    START_POS = (1925, 62)
    MY_NAME = "Timmy Shitgrin"
    GREATEST_FEAR = "Being waterboarded by mayo."
    WIZARD_POWERS = 2
    ROBOCOP_RATING = 3
    ADD_COMMENTS = "I have a need. A need for speed."
    
    # Focus on textbox
    ghost.click(START_POS)
    ghost.click(START_POS)

    # Name
    textbox_input(MY_NAME)

    # Greatest fear
    textbox_input(GREATEST_FEAR)

    # What is the source of your wizard powers? Dropdown
    for i in range(WIZARD_POWERS):
        ghost.typewrite(['down'])
    ghost.press('enter')
    ghost.press('tab')

    # RoboCop Togglebuttons
    ghost.typewrite(['right', 'left'])
    for i in range(ROBOCOP_RATING - 1):
        ghost.press('right')
    ghost.press('tab')

    # TXT Additional comments
    textbox_input(ADD_COMMENTS)

    # Submit.
    ghost.press('enter')


def textbox_input(tb_input):
    ghost.typewrite(tb_input)
    ghost.press('tab')

if __name__ == "__main__":
    intro_text = 'Starting in '
    countdown_timer = 3
    for i in range(countdown_timer):
        print(intro_text + str(countdown_timer - i), end='')
        time.sleep(1)
        print('\b' * (len(intro_text) + 1), end='', flush=True)
    fill_form()