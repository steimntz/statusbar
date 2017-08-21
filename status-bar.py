import sys
import time
from colorize.printer import Printer

while (1 == 1):
    bar = time.strftime("%c")
    p = Printer()
    p.printc("FF0000", bar)
    time.sleep(1)
