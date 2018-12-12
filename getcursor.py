import pyautogui
import time
import Queue

g_thread_loc = Queue.Queue()

def getloc():
    try:
        while True:
            x, y = pyautogui.position()
            #print(x,y)
            g_thread_loc.put(str(x)+","+str(y)+"\n")
            #img = ImageGrab.grab(bbox=(x, y, x+400, y+200))
            #img.show()
            time.sleep(2)
    except KeyboardInterrupt:
        print('\nExit.')

