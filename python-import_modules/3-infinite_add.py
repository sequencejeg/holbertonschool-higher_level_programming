#!/usr/bin/python3

import sys

if __name__ == "__main__":

    qty = sys.argv
    lenght = len(qty)
    totalSum = 0

    if lenght > 0:
        for i in range(1, lenght):
            totalSum += int(qty[i])
    print(totalSum)
