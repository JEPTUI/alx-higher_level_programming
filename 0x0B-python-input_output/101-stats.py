#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints the following statistics since beginning:
    Total file size: File size: <total size>
    Number of lines by status code
"""

import sys


def print_stats(size, stat_codes):
    """
    prints accumulated statistics
    """
    print("File size: {:d}".format(size))
    for i, j in sorted(stat_codes.items()):
        if j:
            print("{:s}: {:d}".format(i, j))

def parse_stdin_and_compute():
    size = 0
    counts = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for count in sys.stdin:
            fields = list(map(str, count.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            counts += 1
            if counts % 10 == 0:
                print_stats(size, stat_codes)
    except KeyboardInterrupt:
        print_stats(size, stat_codes)
        raise
    print_stats(size, stat_codes)

parse_stdin_and_compute()
