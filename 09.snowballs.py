import sys

snowballs = int(input())
value = - sys.maxsize
max_quality = None
max_time = None
max_snow = None
while snowballs > 0:

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > value:
        value = snowball_value
        max_quality = snowball_quality
        max_time = snowball_time
        max_snow = snowball_snow

    snowballs -= 1

print(f"{max_snow} : {max_time} = {int(value)} ({max_quality})")