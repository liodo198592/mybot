# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import robot
import random
from PIL import ImageGrab
import pyautogui
from PIL import Image
import pytesseract
import compareimg
import locatewindow
from ctypes import *

dd_dll = robot.dd_dll
grate = robot.grate
g_lasttime = 0


def checkdialog():
    global g_lasttime
    if(time.time() - g_lasttime) > 40:
        # check dialog
        print("check dialog")
        g_lasttime = time.time()

        # teamview
        target = [u'确', u'定']
        res2 = checkitem(879 * 2, 481 * 2, 927 * 2, 497 * 2, target, 1, 1)
        if res2 is True:
            pass


        target = [u'取', u'消']
        res = checkitem(359 * 2, 465 * 2, 474 * 2, 495 * 2, target, 6)
        if res is True:
            print("checkdialog 取消")


        target = [u'福', u'利']
        res = checkitem(462*2, 144*2, 575*2, 172*2, target, 1)
        if res is True:
            clickB(909*2, 163*2)
            time.sleep(1)

        # check use
        target = [u'使', u'用']
        res = checkitem(1618, 1290, 1817, 1381, target, 4, 1)
        if res is True:
            cnt = 0

    return



def checkimg(x1, y1, x2, y2, url, click=True):
    x1 = int(x1 * grate)
    y1 = int(y1 * grate)
    x2 = int(x2 * grate)
    y2 = int(y2 * grate)
    try:
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save("tmp.png")
    except IOError:
        print("IO ImageGrab.grab ERROR")
    else:
        pass
    percent = compareimg.compimg("tmp.png", url)
    if percent > 70:
        #print("match: ")
        if click is True:
            dd_dll.DD_mov((x1 + x2) / 2, (y1 + y2) / 2)
            dd_dll.DD_btn(1)
            time.sleep(1 + botrandom())
            dd_dll.DD_btn(2)
        return True
    return False


def botrandom():
    return random.random()*2


def getText(x1, y1, x2, y2, key):
    x1 = int(x1 * grate)
    y1 = int(y1 * grate)
    x2 = int(x2 * grate)
    y2 = int(y2 * grate)

    try:
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save("out.png")
    except IOError:
        print("IO ImageGrab.grab ERROR")
    else:
        pass
    strtask = getstrfromimg(img, key)
    print(strtask)
    #strtask.encode("gb2312")
    return strtask



def clearmap():
    clickA(36 * 2, 73 * 2)
    time.sleep(1)
    clickB(962 * 2, 412 * 2)
    time.sleep(2)
    clickB(801 * 2, 623 * 2)
    time.sleep(1)


def getstrfromimg(img, key):
    img = img.convert("RGB")
    w, h = img.size
    rmg = Image.new("RGB", img.size, (255, 255, 255, 255))
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            t = r*255*255 + g * 255 + b
            if key == 1:
                #yellow
                if t > 9877308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 2:
                #write
                if t > 14406655:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 3:
                # write
                if t < 14077308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 4:
                #yellow
                if t > 14077308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 5:
                #yellow
                if t > 14477308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 6:
                # yellow
                if t < 12877308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
    #rmg.show()
    rmg.save("gray.png")
    text = pytesseract.image_to_string(rmg, lang='chi_sim')
    return text


def checkitem(x1, y1, x2, y2, strlist, key, times=1):
    x1 = int(x1 * grate)
    y1 = int(y1 * grate)
    x2 = int(x2 * grate)
    y2 = int(y2 * grate)

    try:
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save("out.png")
    except IOError:
        print("IO ImageGrab.grab ERROR")
    else:
        pass
    strtask = getstrfromimg(img, key)
    if strtask.strip() != "":
        print("checkitem :" + strtask)
    for substr in strlist:
        if substr in strtask:
            print(u'find: ' + str(substr) + u' in :' + str(strtask))
            move((x1 + x2) / 2, (y1 + y2) / 2)
            if times >= 1:
                dd_dll.DD_btn(1)
                time.sleep(1 + botrandom())
                dd_dll.DD_btn(2)
            if times >= 2:
                dd_dll.DD_btn(1)
                time.sleep(1 + botrandom())
                dd_dll.DD_btn(2)
            return True
    return False

def clickB(cx, xy):
    cx = int(cx * grate)
    xy = int(xy * grate)

    dd_dll.DD_mov(cx, xy)
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)


def clickA(cx, xy):
    cx = int(cx * grate)
    xy = int(xy * grate)

    dd_dll.DD_mov(cx, xy)
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)


def checktaskzhuagui(index):
    x, y = pyautogui.position()
    print(x, y)
    x1 = 1613
    y1 = 377 + (index - 1) * 160
    x2 = 2013
    y2 = 377 + index * 160
    print(x1, y1, x2, y2, index)
    target = [u'捉', u'鬼', u'捉', u'拿']
    res = checkitem(x1, y1, x2, y2, target, 1)
    if res is True:
        return index
    return 0



def clicknow():
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)


def move(xx,xy):
    xx = int(xx +  random.random() * 5 - 2)
    #xy = int(xy + random.random() * 10 - 5)
    dd_dll.DD_mov(int(xx), int(xy))

def scrollaction():
    dd_dll.DD_mov(1175, 958)
    dd_dll.DD_btn(1)
    starty = 958
    while starty > 338:
        randomy = random.random()*20
        sleepy = random.random()/5
        time.sleep(sleepy)
        starty = int(starty-randomy)
        if starty < 338:
            starty = 338
        dd_dll.DD_mov(1175, starty)
        if starty == 338:
            break
    dd_dll.DD_btn(2)


def findzhuaguitask():
    robot.checkdialog()
    print("click task")
    clickA(863 * 2, 158 * 2)
    time.sleep(4 + botrandom())
    print("click 可接")
    clickA(967 * 2, 356 * 2)
    time.sleep(2+botrandom())
    print("click 常规任务")
    clickB(186 * 2, 224 * 2)
    time.sleep(2 + botrandom())
    startx = 103
    starty = 203
    weight = 140
    hight = 45
    intervaly = 80
    haszhuaguitask = 0

    for n in range(0,6):
        nowsx = startx
        nowsy = starty + intervaly*(n)
        nowex = nowsx+ weight
        nowey = nowsy + hight
        target = [u'抓', u'鬼',u'呱', u'嵬']
        res = checkitem(nowsx*2,nowsy*2,nowex*2,nowey*2,target*2,1,1)
        if res is True:
            time.sleep(2)
            clickB(805 * 2, 666 * 2)
            haszhuaguitask = 1
            break
    if haszhuaguitask == 0:
        clickB(942 * 2, 140 * 2)
    time.sleep(5)
    print("finish findzhuaguitask")


def startguagui():
    baotuindex = 0
    clickB(600, 600)
    time.sleep(1)
    locatewindow.relocatewindow()
    #findzhuaguitask()


    while True:
        lastnobattlecnt = 0
        needfindtask = 0
        while True:
            lastnobattlecnt += 1
            print("lastnobattlecnt: " + str(lastnobattlecnt))

            target = [u'少侠巳经']
            res = checkitem(323 * 2, 355 * 2, 703 * 2, 432 * 2, target, 2, 0)
            if res is True:
                target = [u'确', u'定']
                res2 = checkitem(562 * 2, 465 * 2, 653 * 2, 496 * 2, target, 1)
                if res2 is True:
                    lastnobattlecnt = 0
            else:
                # 取消
                target = [u'取', u'消']
                res2 = checkitem(360*2, 465*2, 473*2, 499*2, target, 1)
                if res2 is True:
                    print("startguagui 取消")
                    lastnobattlecnt = 0

            target = [u'抓', u'鬼', u'任', u'务']
            res = checkitem(1473, 751, 1874, 821, target, 1)
            if res is True:
                lastnobattlecnt = 0

            target = [u'抓', u'鬼', u'任', u'务']
            res = checkitem(782*2, 322*2, 917*2, 352*2, target, 1)
            if res is True:
                lastnobattlecnt = 0

            #target = [u'使', u'用']
            #res = checkitem(819*2, 655*2, 897*2, 688*2, target, 2)
            #if res is True:
                #lastnobattlecnt = 0

            if lastnobattlecnt > 5:
                print("find 抓鬼 task")
                checkdialog()
                needfindtask += 1
                if needfindtask > 1:
                    break
                lastnobattlecnt = 0
                clearmap()

                if baotuindex != 0:
                    lastindex = checktaskzhuagui(n)
                    if lastindex != 0:
                        baotuindex = lastindex
                    else:
                        baotuindex = 0
                else:
                    for n in range(1, 5):
                        lastindex = checktaskzhuagui(n)
                        if lastindex != 0:
                            baotuindex = lastindex
                        else:
                            baotuindex = 0

            res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False)
            if res is True:
                lastnobattlecnt  = 0
                needfindtask = 0
                print("进入战斗")
                falsecount = 0
                while True:
                    res = checkimg(578*2, 55*2, 623*2,82*2, "res2//tianzhen.png", False)
                    if res is False:
                        falsecount = falsecount + 1
                        if falsecount > 2:
                            print("退出战斗")
                            break

                    time.sleep(1)
            time.sleep(1)

        findzhuaguitask()

