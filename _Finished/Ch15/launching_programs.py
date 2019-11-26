import subprocess

# Runs the program
def run_calc():
    subprocess.Popen("C:\\Windows\\System32\\calc.exe")

def run_and_wait_calc():
    """Here we open a calculator process.
    while it's still running, we check if poll() returns None. It should, as the process is still running.
    Then we close the calculator program and call wait() on the terminated process.
    wait() and poll() now return 0, indicating that the process terminated without errors.
    """
    calc_proc = subprocess.Popen("C:\\Windows\\System32\\calc.exe")
    print(calc_proc.poll() == None) # True
    print(calc_proc.wait()) # 0
    print(calc_proc.poll()) # 0


def passing_command_line_arguments_to_popen():
    """Runs notepad.exe, and opens fog.log
    """
    subprocess.Popen(["C:\\Windows\\notepad.exe", 'C:\\fog.log'])

def opening_files_with_default_applications():
    file_obj = open('test.txt', 'w')
    file_obj.write('Hello World!')
    file_obj.close()
    subprocess.Popen(['start', 'hello.txt'], shell=True)

# For multitrack_Programming.py
run_calc()