# -*- coding: UTF-8 -*-
import Tkinter as tk
from ttk import *
import time
import datetime
import Queue, threading
import sys
import Tkinter
import tkMessageBox
import robot
import robotzhuagui
import getcursor
import predealimg
from Tkinter import *
from robot import *
from mylog import *
from robotzhuagui import *
from getcursor import *
import inspect
import ctypes
reload(sys)
sys.setdefaultencoding('utf-8')

sys.stdout = Logger("mylog.txt")


def _async_raise(tid, exctype):
   """raises the exception, performs cleanup if needed"""
   tid = ctypes.c_long(tid)
   if not inspect.isclass(exctype):
      exctype = type(exctype)
   res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
   if res == 0:
      raise ValueError("invalid thread id")
   elif res != 1:
      # """if it returns a number greater than one, you're in trouble,
      # and you should call it again with exc=NULL to revert the effect"""
      ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
      raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
   _async_raise(thread.ident, SystemExit)

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x500+500+200')
        self.root.title('ruarua')
        self.textlenth  = 0
        self.startloc = 0
        self.nowtask = 0

    def show(self):
        self.finishbaotu = IntVar()
        self.finishyabiao = IntVar()
        self.finishmijing = IntVar()
        self.finishsanjie = IntVar()
        self.finishkeju = IntVar()
        self.finishbangpairenwu = IntVar()
        self.finishshimen = IntVar()

        self.locationtext = tk.Text(self.root, width=10, height=4)

        self.x1 = Tkinter.Entry(width=4)
        self.y1 = Tkinter.Entry(width=4)
        self.x2 = Tkinter.Entry(width=4)
        self.y2 = Tkinter.Entry(width=4)
        self.namelist = Tkinter.Entry(width=20)
        self.namelist.insert(0,u"热闹 轩岚 粉 软 果")
        self.param = Tkinter.Entry(width=10)
        self.param.insert(0, '9877308')
        self.C1 = Checkbutton(self.root, text="NO宝图", variable=self.finishbaotu, onvalue=1, offvalue=0, height=4, width=10)
        self.C2 = Checkbutton(self.root, text="NO押镖", variable=self.finishyabiao, onvalue=1, offvalue=0, height=4, width=10)
        self.C3 = Checkbutton(self.root, text="NO秘境", variable=self.finishmijing, onvalue=1, offvalue=0, height=4, width=10)
        self.C4 = Checkbutton(self.root, text="NO三界", variable=self.finishsanjie, onvalue=1, offvalue=0, height=4, width=10)
        self.C5 = Checkbutton(self.root, text="NO科举", variable=self.finishkeju, onvalue=1, offvalue=0, height=4, width=10)
        self.C6 = Checkbutton(self.root, text="NO帮派任务", variable=self.finishbangpairenwu, onvalue=1, offvalue=0, height=4, width=10)
        self.C7 = Checkbutton(self.root, text="NO师门", variable=self.finishshimen, onvalue=1, offvalue=0, height=4, width=10)
        self.B1 = Tkinter.Button(self.root, text="所有单人任务", command=self.startaction)
        self.B11 = Tkinter.Button(self.root, text="单人任务", command=self.startaction11)
        self.B2 = Tkinter.Button(self.root, text="开始抓鬼", command=self.getzhuagui)
        self.Blocation = Tkinter.Button(self.root, text="开始获取坐标", command=self.getlocation)
        self.Blocationend = Tkinter.Button(self.root, text="停止获取坐标", command=self.getlocationend)
        self.Blocationcancel = Tkinter.Button(self.root, text="停止自动任务", command=self.gettaskcancel)
        self.Bcap = Tkinter.Button(self.root, text="分析内容", command=self.getCap)
        self.showtext = tk.Text(self.root,width=35, height=30)
        self.C1.grid(row=0, column=1)
        self.C2.grid(row=0, column=2)
        self.C3.grid(row=1, column=1)
        self.C4.grid(row=1, column=2)
        self.C5.grid(row=2, column=1)
        self.C6.grid(row=2, column=2)
        self.C7.grid(row=3, column=1)
        self.B1.grid(row=4, column=1)
        self.B11.grid(row=5, column=1)
        self.namelist.grid(row=5,column=0)
        self.B2.grid(row=4, column=2)
        self.Blocationcancel.grid(row=4, column=0)
        self.showtext.grid(row=0, column=0, rowspan=4)
        self.locationtext.grid(row=0, column=3)
        self.Blocation.grid(row=1, column=3)
        self.Blocationend.grid(row=1, column=4)
        self.x1.grid(row=2, column=3)
        self.y1.grid(row=2, column=4)
        self.x2.grid(row=3, column=3)
        self.y2.grid(row=3, column=4)
        self.param.grid(row=4, column=3)
        self.Bcap.grid(row=4, column=4)
        self.root.mainloop()

    def startaction(self):
        self.nowtask = 1
        self.B1.config(state=tk.DISABLED)
        print("开始单人任务" + str(self.finishbaotu.get()) + str(self.finishyabiao.get()) +
              str(self.finishmijing.get()) + str(self.finishsanjie.get()) + str(self.finishkeju.get())
              + str(self.finishbangpairenwu.get()) + str(self.finishshimen.get()))

        #self.thread_queue = Queue.Queue()  # used to communicate between main thread (UI) and worker thread
        self.new_thread = threading.Thread(target=self.run_loop_startaction, kwargs={'param1': 100, 'param2': 20})
        self.new_thread.setDaemon(True)
        self.new_thread.start()
        self.root.after(100, self.listen_for_result)

    def startaction11(self):
        self.nowtask = 3
        self.B11.config(state=tk.DISABLED)
        print("单人任务" + str(self.finishbaotu.get()) + str(self.finishyabiao.get()) +
              str(self.finishmijing.get()) + str(self.finishsanjie.get()) + str(self.finishkeju.get())
              + str(self.finishbangpairenwu.get()) + str(self.finishshimen.get()))

        #self.thread_queue = Queue.Queue()  # used to communicate between main thread (UI) and worker thread
        self.new_thread = threading.Thread(target=self.run_loop_startaction11, kwargs={'param1': 100, 'param2': 20})
        self.new_thread.setDaemon(True)
        self.new_thread.start()
        self.root.after(100, self.listen_for_result)

    def getzhuagui(self):
        self.nowtask = 2
        self.B2.config(state=tk.DISABLED)
        print("开始抓鬼")
        #self.thread_queue = Queue.Queue()  # used to communicate between main thread (UI) and worker thread
        self.new_thread = threading.Thread(target=self.run_loop_getzhuagui, kwargs={'param1': 100, 'param2': 20})
        self.new_thread.setDaemon(True)
        self.new_thread.start()
        self.root.after(100, self.listen_for_result)


    def getlocation(self):
        if self.startloc == 0:
            self.startloc = 1
            self.Blocation.config(state=tk.DISABLED)
            self.new_thread_loc = threading.Thread(target=self.run_loop_getlocation, kwargs={'param1': 100, 'param2': 20})
            self.new_thread_loc.setDaemon(True)
            self.new_thread_loc.start()
            self.root.after(100, self.listen_for_result)


    def getlocationend(self):
        if self.startloc == 1:
            stop_thread(self.new_thread_loc)
            self.locationtext.delete(0.0, END)
            self.Blocation.config(state=tk.NORMAL)
            self.startloc = 0


    def gettaskcancel(self):
        if self.nowtask == 1:
            stop_thread(self.new_thread)
            self.B1.config(state=tk.NORMAL)
            self.nowtask = 0
        if self.nowtask == 2:
            stop_thread(self.new_thread)
            self.B2.config(state=tk.NORMAL)
            self.nowtask = 0
        if self.nowtask == 3:
            stop_thread(self.new_thread)
            self.B11.config(state=tk.NORMAL)
            self.nowtask = 0


    def getCap(self):
        predealimg.cap(self.x1.get(),self.y1.get(),self.x2.get(),self.y2.get(),self.param.get())


    def run_loop_getlocation(self, param1, param2):
        getcursor.getloc()
        pass


    def run_loop_getzhuagui(self, param1, param2):
        robotzhuagui.startguagui()
        while True:
            time.sleep(1)
        pass

    def run_loop_startaction(self, param1, param2):
        #target = [u'热闹', u'轩岚',u'粉',u'软',u'果']
        #target = [u'轩岚', u'粉', u'软', u'果']
        target = self.namelist.get().split(' ')
        for name in target:
            res = robot.checktabforUser(name)
            if res is True:
                print("成功切换 开始任务 " + name)
                robot.doone(self.finishbaotu.get(), self.finishyabiao.get(), self.finishmijing.get(), self.finishsanjie.get(),
                            self.finishkeju.get(),
                            self.finishbangpairenwu.get(), self.finishshimen.get())
                print("任务结束 " + name)
        while True:
            time.sleep(1)
        pass


    def run_loop_startaction11(self, param1, param2):

        robot.doone(self.finishbaotu.get(), self.finishyabiao.get(), self.finishmijing.get(), self.finishsanjie.get(),
                    self.finishkeju.get(),
                    self.finishbangpairenwu.get(), self.finishshimen.get())

        while True:
            time.sleep(1)
        pass


    def listen_for_result(self):
        '''
        Check if there is something in the queue.
        Must be invoked by self.root to be sure it's running in main thread
        '''
        content1 = ""
        contentloc = ""
        try:
            while True:
                if g_thread_queue.empty() is False:
                    content1 += g_thread_queue.get(False)
                    break
                if g_thread_loc.empty() is False:
                    contentloc += g_thread_loc.get(False)
                    break
                if g_thread_queue.empty() is True and g_thread_loc.empty() is True:
                    break
        except Queue.Empty:  # must exist to avoid trace-back
            pass
        finally:
            #
            self.textlenth += len(content1)
            if self.textlenth > 500:
                self.showtext.delete(0.0, END)
                self.textlenth = 0
            self.showtext.insert(0.0, content1)
            if contentloc != '':
                self.locationtext.delete(0.0, END)
                self.locationtext.insert(0.0, contentloc)
            self.root.after(100, self.listen_for_result)


def log_loop(param1, param2):
    while True:
        try:
            img = ImageGrab.grab(bbox=(0, 0, 1440, 900))
            img.save(
                "imglog/{ss}.png".format(ss=str(datetime.datetime.now().strftime("%Y%m%d %H%M%S")).replace(" ", "#")))
        except IOError:
            print("IO ImageGrab.grab ERROR")
        else:
            pass

        time.sleep(10)


if __name__ == '__main__':
    #log_thread = threading.Thread(target=log_loop, kwargs={'param1': 100, 'param2': 20})
    #log_thread.setDaemon(True)
    #log_thread.start()

    '''
    while True:
        robot.checkdialog()
        time.sleep(2)
    '''
    win = MainWindow()
    win.show()

