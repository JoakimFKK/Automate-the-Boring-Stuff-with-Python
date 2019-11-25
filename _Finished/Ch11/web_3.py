"""You need to write binary data instead of text data in order to maintain the unicode encoding of the text."""
"""To write the webpage to a file you can use a for loop with the Reponse object's iter_content() method."""
import requests
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Start of program.")

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
with open("RomeoAndJuliet.txt", 'wb') as romeo_juliet:
    for chunk in res.iter_content(100000):
        romeo_juliet.write(chunk)
"""When iter_content() method returns "chunks" of the content on each iteration through the loop.
Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain.
One hundred thousand bytes is generally a good size.
"""


logging.critical("End of program.")