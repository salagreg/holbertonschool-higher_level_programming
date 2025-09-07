#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    n = len(argv) - 1
    
    if n == 0:
        print("0 argument(s).")
    elif n == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
