import Xlib
import Xlib.display

class Display:
    def width(self):
        display = Xlib.display.Display(':0')
        return display.screen()['width_in_pixels']
