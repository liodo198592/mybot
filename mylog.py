# -*- coding: UTF-8 -*-
import sys
import datetime
import Queue
g_thread_queue = Queue.Queue()


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        writeStr = ''
        if  message != '\n':
            writeStr = ' 【' + str(datetime.datetime.now()) + '】\n' + message
        else:
            writeStr = message
        self.terminal.write(writeStr)
        g_thread_queue.put(writeStr)
        self.log.write(writeStr)
        self.flush()

    def flush(self):
        self.log.flush()


#sys.stdout = Logger("mylog.txt")
#print("Hello world55 !")
