"""
Analyzes number of logs by keyword at id and log message of logs by every day. Saves statistics to DB(default sqlite3).

In Future:
    1. Generates diagrams based on data from stored statistics.
"""

import sys

from utils import bcolors
from base import analyze


def main():
    args = sys.argv[1:]
    if not args:
        print(bcolors.WARNING + 'Usage: path_to_log_file' + bcolors.ENDC)
        sys.exit(1)

    path = args[0]
    del args[0]

    if len(args) != 0:
        print(bcolors.FAIL + "Error: must specify one path" + bcolors.ENDC)
        sys.exit(1)

    analyze(path)


if __name__ == '__main__':
    main()
