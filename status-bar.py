import sys
import time

class Printer:
    def __init__(self):
        sys.stdout.flush()

    def hi(self):
        print("hi")

    def printc(self, hex_color, text):
        r, g, b = [int(hex_color[i:i+2], 16) for i in range(1, len(hex_color), 2)]
        print(f"\x1b[38;2;{r};{g};{b}m{text}\x1b\n")

while (1 == 1):
    bar = time.strftime("%c")
    p = Printer()
    p.printc("FF0000", bar)
    time.sleep(1)

sys.stdout.flush()
