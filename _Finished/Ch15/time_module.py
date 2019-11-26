import time

def intro():
    print(time.time()) # 1574066563.5332215
    """Explanation:
    Here I'm calling time.time() on 18th of November, 09:43.
    The value is how many seconds have passed between the Unix epoch and the moment time.time() was called.

    Epoch timestamps can be used to profile code, that is, to measure how long a piece of code takes to run.
    If you call time.time() at the beginning of the code block you want to measure and again at the end,
    you can subtract the first timestamp from the secnod to find the elapsed time between those two calls.
    For example, (continued in calc_prod())
    """


def how_get_time_func_takes():
    def calc_prod():
        # Calculate the product of the first 100.000 numbers.
        product = 1
        for i in range(1, 100000):
            product = product * i
        return product

    start_time = time.time()
    prod = calc_prod()
    end_time = time.time()
    print(f"The result is {len(str(prod))} digits long.") # The result is 456569 digits long.
    print(f"Took {end_time - start_time} seconds to calculate.") # Took 2.092365264892578 seconds to calculate.

def time_dot_sleep_func():
    for i in range(3):
        print("Tick")
        time.sleep(1)
        print("Tock")
        time.sleep(1)

def rounding_numbers():
    now = time.time()
    print(now) # 1574070708.6545494
    print(round(now, 2)) # 1574070708.65
    print(round(now, 4)) # 1574070708.6545
    print(round(now))  # 1574070709
