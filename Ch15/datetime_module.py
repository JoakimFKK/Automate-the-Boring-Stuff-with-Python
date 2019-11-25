import datetime
import time

def intro():
    print(datetime.datetime.now()) # 2019-11-18 11:53:24.274469
    dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
    print(dt.year, dt.month, dt.day) # 2015 10 21
    print(dt.hour, dt.minute, dt.second) # 16 29 0

def get_todays_date():
    print(datetime.datetime.fromtimestamp(1000000)) # 1970-01-12 14:46:40
    """Calling datetime.datetime.fromtimestamp() and passing it 10000000,
    returns a datetime object for the moment 1.000.000 seconds after the Unix epoch.
    Passing time.time(), the Unix epoch timestamp for the current moment,
    returns a datetime object for the current moment.
    So the expressions datetime.datetime.now() and datetime.datetime.fromtimestamp(time.time())
    do the same thing. They both give you a datetime object for the present moment.
    """
    print(datetime.datetime.fromtimestamp(time.time())) # 2019-11-18 11:56:39.006614

def comparing_dates():
    halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
    newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
    oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
    print(halloween2015 == oct31_2015) # True
    print(halloween2015 > newyears2016) # False
    print(newyears2016 > halloween2015) # True
    print(newyears2016 != oct31_2015) # True