import time, datetime
from datetime import timedelta


def add(dt):
    return dt + datetime.timedelta(seconds=10**9)


dt = datetime.datetime(2021, 3, 5, 14, 30, 21)
print(add(dt))
https://www.geeksforgeeks.org/python-datetime-timedelta-function/