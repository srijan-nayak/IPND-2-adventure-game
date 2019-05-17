import time


def print_pause(string: str, seconds: int):
    """Print a passed in string after a
    delay of passed in seconds.
    """
    time.sleep(seconds)
    print(string)
