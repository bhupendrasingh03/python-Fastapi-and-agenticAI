import sys

from myapis import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])