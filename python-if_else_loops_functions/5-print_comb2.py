#!/usr/bin/python3
for number in range(100):
    if number <= 98:
        print("{:02d}".format(number), end=", ")
    else:
        print("{:02d}".format(number))
