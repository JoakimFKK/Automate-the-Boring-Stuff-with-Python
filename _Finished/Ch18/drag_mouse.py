import pyautogui

start = (500, 400)
end = (1000, 800)

pyautogui.dragTo(start, duration=0.5)
pyautogui.dragTo(end, duration=0.5)

# pyautogui.dragTo(start)
# pyautogui.dragTo(end)