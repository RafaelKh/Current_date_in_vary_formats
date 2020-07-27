from datetime import datetime

now = datetime.now()
num = int(input())


def current_date(n):
    if n == 1:
        print(now.strftime("%Y.%m.%d"))
    elif n == 2:
        print(now.strftime("%Y.%m.%d %H:%M:%S"))
    elif n == 3:
        print(now.strftime("%a %b %d %Y %H:%M:%S GMT +0400 (Armenian Standard Time)"))


current_date(num)