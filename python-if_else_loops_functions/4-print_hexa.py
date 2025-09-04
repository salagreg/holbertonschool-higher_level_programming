#!/usr/bin/python3
print("{}".format(
    ''.join("{} = {}\n".format(i, hex(i)) for i in range(99))
), end='')
