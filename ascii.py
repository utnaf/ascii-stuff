import os
import time
import sys

from src import Char

rows, columns = os.popen('stty size', 'r').read().split()

count = 0

try:
    while 1:
        for x in range(int(rows)):
            count += 1
            for y in range(int(columns)):
                sys.stdout.write(str(Char()))
            if count < int(rows):
                sys.stdout.write('\n')
        sys.stdout.write('\033[H')
        sys.stdout.flush()
        time.sleep(0.2)
except KeyboardInterrupt:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
