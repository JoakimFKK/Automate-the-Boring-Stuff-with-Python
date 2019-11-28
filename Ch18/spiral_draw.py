import pyautogui as ghost
import time

# Get paint in focus
time.sleep(5)

distance = 200
while distance > 0:
    ghost.dragRel(distance, 0, duration=0.2)
    distance -= 5
    ghost.dragRel(0, distance, duration=0.2)
    ghost.dragRel(-distance, 0, duration=0.2)
    distance -= 5
    ghost.dragRel(0, -distance, duration=0.2)

