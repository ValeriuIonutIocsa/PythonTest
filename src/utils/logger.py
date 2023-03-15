import sys


def printError(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
