import time, subprocess, os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

time_left = 60
while time_left > 0:
    print(time_left, end="")
    time.sleep(1)
    time_left -= 1

## More boring way to show ^ 
# time.sleep(60)

subprocess.Popen(['start', 'Workfiles/alarm.wav'], shell=True)