import time, datetime


def add(dt):
    now = dt.timestamp()
    now_plus_gs = now + (10**9)
    now_plus_gs_date = datetime.datetime.fromtimestamp(now_plus_gs)
    return now_plus_gs_date


dt = datetime.datetime(2021, 3, 5, 14, 30, 21)
print(add(dt))
