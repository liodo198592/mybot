# -*- coding: UTF-8 -*-
import sys
import Tkinter
import tkMessageBox
import robot
import robotzhuagui
from Tkinter import *
from robot import *
from mylog import *
from robotzhuagui import *
reload(sys)
sys.setdefaultencoding('utf-8')

sys.stdout = Logger("mylog.txt")
#引用Tk模块

def startaction():
    print("开始单人任务"+str(finishbaotu.get())+str(finishyabiao.get())+
                          str(finishmijing.get())+str(finishsanjie.get())+str(finishkeju.get())
                          +str(finishbangpairenwu.get())+str(finishshimen.get()))
    robot.doone(finishbaotu.get(), finishyabiao.get(), finishmijing.get(), finishsanjie.get(), finishkeju.get(), finishbangpairenwu.get(), finishshimen.get())


def getzhuagui():
    print("开始抓鬼")
    robotzhuagui.startguagui()


# 进入消息循环
print("ruarua start!")
top = Tkinter.Tk("ruarua")
top.geometry('400x500+500+200')
top.title('ruarua')
finishbaotu = IntVar()
finishyabiao = IntVar()
finishmijing = IntVar()
finishsanjie = IntVar()
finishkeju = IntVar()
finishbangpairenwu = IntVar()
finishshimen = IntVar()

CheckVar2 = IntVar()
C1 = Checkbutton(top, text="NO宝图", variable=finishbaotu, onvalue=1, offvalue=0, height=5, width=20)
C2 = Checkbutton(top, text="NO押镖", variable=finishyabiao, onvalue=1, offvalue=0, height=5, width=20)
C3 = Checkbutton(top, text="NO秘境", variable=finishmijing, onvalue=1, offvalue=0, height=5, width=20)
C4 = Checkbutton(top, text="NO三界", variable=finishsanjie, onvalue=1, offvalue=0, height=5, width=20)
C5 = Checkbutton(top, text="NO科举", variable=finishkeju, onvalue=1, offvalue=0, height=5, width=20)
C6 = Checkbutton(top, text="NO帮派任务", variable=finishbangpairenwu, onvalue=1, offvalue=0, height=5, width=20)
C7 = Checkbutton(top, text="NO师门", variable=finishshimen, onvalue=1, offvalue=0, height=5, width=20)
B1 = Tkinter.Button(top, text ="所有单人任务", command = startaction)
B2 = Tkinter.Button(top, text ="开始抓鬼", command = getzhuagui)
C1.grid(row=0, column=0)
C2.grid(row=0, column=1)
C3.grid(row=1, column=0)
C4.grid(row=1, column=1)
C5.grid(row=2, column=0)
C6.grid(row=2, column=1)
C7.grid(row=3, column=0)
B1.grid(row=4, column=0)
B2.grid(row=4, column=1)
top.mainloop()
