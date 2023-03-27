#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError, TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info(9)[1]), file=sys.stderr)
        return None