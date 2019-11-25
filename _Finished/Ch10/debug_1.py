import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
"""Logging to a file"""
# logging.basicConfig(filename="01_logging.txt", level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)
logging.debug("Start of program!")
def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(n + 1):
        """The problem is:
            for i in range(n + 1):
            Since range(n) starts by default at 0, 5 * 0 is 0, and is gonna stay at 0.
            The fix:
            for i in range(1, n + 1):
        """

        total *= i
        logging.debug(f"i is {i}, total is {total}")
    logging.debug(f"End of factorial {n}")
    return total

print(factorial(5))
logging.debug("End of program!")

""" Output:
 2019-11-12 13:46:43,078 - DEBUG - Start of program!
 2019-11-12 13:46:43,078 - DEBUG - Start of factorial(5%)
 2019-11-12 13:46:43,078 - DEBUG - i is 0, total is 0
 2019-11-12 13:46:43,078 - DEBUG - i is 1, total is 0
 2019-11-12 13:46:43,078 - DEBUG - i is 2, total is 0
 2019-11-12 13:46:43,078 - DEBUG - i is 3, total is 0
 2019-11-12 13:46:43,078 - DEBUG - i is 4, total is 0
 2019-11-12 13:46:43,078 - DEBUG - i is 5, total is 0
 2019-11-12 13:46:43,078 - DEBUG - End of factorial 5
0
 2019-11-12 13:46:43,078 - DEBUG - End of program!

"""