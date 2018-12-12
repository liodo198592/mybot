import time
from PIL import ImageGrab

try:
    while True:
        img = ImageGrab.grab(bbox=(1613, 377, 2013, 537))
        img.show()
        time.sleep(5)
        img = ImageGrab.grab(bbox=(1613, 537, 2013, 697))
        img.show()
        time.sleep(5)
        img = ImageGrab.grab(bbox=(1613, 697, 2013, 857))
        img.show()
        time.sleep(5)
except KeyboardInterrupt:
    print('\nExit.')

