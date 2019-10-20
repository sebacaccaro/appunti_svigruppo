import os
import sys


def fake_cat(fileName):
    print(open(fileName).read())


if __name__ == "__main__":
    fake_cat(sys.argv[1])
