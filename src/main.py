import time


def print_pause(string: str, delay=2)->None:
    """Print a passed in string after a
    delay of passed in seconds. Default
    delay is of 2 seconds.
    """
    time.sleep(delay)
    print(string)
