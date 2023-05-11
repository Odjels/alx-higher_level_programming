#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    a = len(sys.argv)
    add = 0

    for i in range(1, a):
        add += int(sys.argv[i])
    print("{:d}".format(add))
