#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lenght = len(sys.argv) - 1
    count = 0

    if lenght == 0:
        print("{} arguments.".format(lenght))
    elif lenght == 1:
        print("{} argument:".format(lenght))
    else:
        print("{} arguments:".format(lenght))

    if lenght > 0:
        for i in sys.argv:
            if count != 0:
                print("{}: {}".format(count, i))
            count += 1
