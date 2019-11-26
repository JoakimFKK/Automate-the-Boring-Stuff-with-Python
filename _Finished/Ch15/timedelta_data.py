import datetime
import time

"""To create a timedelta object:
Use datetime.timedelta() function, the function takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds.
There is no month or year keyword argument because 'a month', and 'a year', is a variable amount of time depending on the particular month or year.
A timedelta object has the total duration represented in days, seconds, and microseconds.
these numbers are stoered in days, seconds, and microseconds attributes respectively.
The total_seconds() method will return the duration in number of seconds alone. 
"""

def func1():
    delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    print(delta.days, delta.seconds, delta.microseconds)    # 11 36548 0
    print(delta.total_seconds())    # 986948.0
    print(str(delta))   # 11 days, 10:09:08
    print(delta)    # 11 days, 10:09:08

def func2():
    oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
    about_thirty_years = datetime.timedelta(days=365 * 30)
    print(oct21st) # 2015-10-21 16:29:00
    print(oct21st - about_thirty_years) # 1985-10-28 16:29:00
    print(oct21st - (2 * about_thirty_years)) # 1955-11-05 16:29:00

