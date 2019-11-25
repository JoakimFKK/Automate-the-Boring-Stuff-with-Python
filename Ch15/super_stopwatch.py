#! python3
import time

input('Press ENTER to begin. Afterwards press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
print('Started.')
start_time = time.time()
last_time = start_time

lap_counter = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap #{lap_counter}: {total_time} ({lap_time})", end='')
        lap_counter += 1
        last_time = time.time() # Reset the last lap time.
# except (KeyboardInterrupt, EOFError):
except EOFError:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print("\n\nDone.")
""" OUTPUT:
    Press ENTER to begin. Afterwards press ENTER to "click" the stopwatch. Press Ctrl-C to quit.

    Started.

    Lap #1: 3.15 (3.15)
    Lap #2: 6.84 (3.68)
    Lap #3: 10.05 (3.22)
    Lap #4: 12.7 (2.65)
    Lap #5: 16.04 (3.34)
    Lap #6: 19.26 (3.21)
    Lap #7: 22.44 (3.18)
    Lap #8: 26.11 (3.67)
    Lap #9: 29.84 (3.73)
    Lap #10: 33.17 (3.34)
    Lap #11: 36.36 (3.18)
    Done.
"""