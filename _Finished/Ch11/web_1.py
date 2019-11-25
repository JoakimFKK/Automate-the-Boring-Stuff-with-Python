#! python3
#01_map_it.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser
import sys
import pyperclip

"""change directory to where the python script is located.
'01_map_it.py [arguments]'
Program should execute.
"""
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '. join(sys.argv[1:])
#TODO: get address from clipboard.
else:
     address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)