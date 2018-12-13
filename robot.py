# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
#import sys
import random
from PIL import ImageGrab
import pyautogui
from PIL import Image
import pytesseract
import compareimg
import locatewindow
#import mylog
from ctypes import *


dd_dll = windll.LoadLibrary('DD\\dd85590\\DD85590\\DD85590.64.dll')

oritgx1 =0
oritgy1 =0
oritgx2 =2048
oritgy2 =1596
destgx1 =0
destgy1 =0
destgx2 =1024
destgy2 =798
grate = 0.5
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
        res = checkitem(462*2, 144*2, 575*2, 172*2, target, 1,0)
        if res is True:
            cancelDialog(909*2, 163*2)
            time.sleep(1)
        

        #请组逞或加入队伍
        target = [u'请', u'组', u'建',u'或', u'加',u'入', u'队', u'伍']
        res = checkitem(827*2, 319*2, 1007*2, 351*2, target, 9,0)
        if res is True:
            cancelDialog(863*2, 158*2)
            time.sleep(1)


        target = [u'队', u'伍', u'沼',u'任', u'务']
        res = checkitem(441*2, 113*2, 556*2, 142*2, target, 9,0)
        if res is True:
            cancelDialog(924*2, 134*2)
            time.sleep(1)


        #check shanggushenfu
        target = [u'激活', u'护符']
        res = checkitem(430 * 2, 212 * 2, 603 * 2, 240 * 2, target, 1)
        if res is True:
            clickB(764 * 2, 223 * 2)
            time.sleep(1)

        # check use
        target = [u'使', u'用']
        res = checkitem(1618, 1290, 1817, 1381, target, 4, 1)
        if res is True:
            cnt = 0

    return


def clearmap():
    clickA(36*2,73*2)
    time.sleep(1)
    clickB(962 * 2, 412 * 2)
    time.sleep(2)
    clickB(801*2, 623*2)
    time.sleep(1)

def move(xx,xy):
    xx = int(xx +  random.random() * 5 - 2)
    #xy = int(xy + random.random() * 10 - 5)
    dd_dll.DD_mov(int(xx), int(xy))


def moveex(xx,xy):
    dd_dll.DD_mov(int(xx), int(xy))


def botrandom():
    return random.random()*1


def checkimg(x1, y1, x2, y2, url, click=True, times=1):
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


def clicknow():
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)


def clickRight():
    dd_dll.DD_btn(4)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(8)


def clickB(cx, xy):
    cx = int(cx * grate)
    xy = int(xy * grate)
    move(cx, xy)
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)


def cancelDialog(cx, xy):
    #检查是否有对话框
    res = checkimg(357 * 2, 44 * 2, 412 * 2, 75 * 2, "res2//paihang.png", False, 0)
        if res is False:
            cx = int(cx * grate)
            xy = int(xy * grate)
            move(cx, xy)
            dd_dll.DD_btn(1)
            time.sleep(1 + botrandom())
            dd_dll.DD_btn(2)


def clickA(cx, xy):
    cx = int(cx * grate)
    xy = int(xy * grate)
    move(cx, xy)
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)
    dd_dll.DD_btn(1)
    time.sleep(1 + botrandom())
    dd_dll.DD_btn(2)


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
                time.sleep(1+ botrandom())
                dd_dll.DD_btn(2)
            if times >= 2:
                dd_dll.DD_btn(1)
                time.sleep(1+botrandom())
                dd_dll.DD_btn(2)
            return True
    return False

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
            if key == 7:
                # yellow
                if t < 7877308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 8:
                # yellow
                if t > 10877308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
            if key == 9:
                # yellow
                if t > 12877308:
                    rmg.putpixel((i, j), (255, 255, 255))
                else:
                    rmg.putpixel((i, j), (0, 0, 0))
    #rmg.show()
    rmg.save("gray.png")
    text = pytesseract.image_to_string(rmg, lang='chi_sim')
    return text

def waitbaotu():
    print("wait waitbaotu")
    baotuindex = 0
    isinit = 0
    cnt = 0
    while True:
        target = [u'听', u'听',u'无', u'妨']
        res = checkitem(1471, 1117, 1903, 1198, target, 1)
        if res is True:
            isinit = 1

        print("find baotu task")
        if baotuindex != 0:
            lastindex = checktaskbaotu(n)
            if lastindex != 0:
                baotuindex = lastindex
            else:
                baotuindex = 0
        else:
            for n in range(1, 5):
                lastindex = checktaskbaotu(n)
                if lastindex != 0:
                    baotuindex = lastindex
                else:
                    baotuindex = 0

        if baotuindex == 0:
            cnt += 1
            print("cnt = "+str(cnt))
            if cnt > 10:
                print("baotu finish")
                break
        else:
            cnt = 0

        res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
                if res is False:
                    falsecount = falsecount + 1
                    if falsecount > 2:
                        print("退出战斗")
                        cnt = 0
                        break

                time.sleep(2)

        checkdialog()
        time.sleep(1)
    return


def waitsanjie():
    print("wait waitsanjie")
    while True:
        checkdialog()
        time.sleep(1)
        target = [u'求', u'助']
        res = checkitem(804*2, 497*2, 932*2, 528*2, target, 1,0)
        if res is True:
            clickB(650*2, 339*2)
            isinit = 1
        else:
            cancelDialog(960 * 2, 141 * 2)
            break
    return


def waitkeju():
    print("wait waitkeju")

    while True:
        checkdialog()
        time.sleep(1)
        target = [u'求', u'助']
        res = checkitem(794*2, 624*2, 906*2, 651*2, target, 1,0)
        if res is True:
            clickB(516*2, 417*2)
            isinit = 1
        else:
            cancelDialog(960 * 2, 151 * 2)
            break

    return


def waitbangpai():
    print("wait waitbangpai")
    cntbangpai = 0
    while True:
        #findtask
        hasbangpai = 0
        print("find bangpai task")
        for n in range(1, 5):
            print("find task")
            lastindex = checktaskbangpai(n)
            time.sleep(0.1)
            if lastindex != 0:
                hasbangpai = 1
                cntin = 0
                while True:
                    cntin = cntin + 1
                    print("find task" + str(lastindex) + "cnt in" + str(cntin))
                    nowindex = checktaskbangpai(lastindex)
                    time.sleep(0.1)
                    if nowindex != 0:
                        hasbangpai = 1
                    if nowindex == 0 and cntin > 10:
                        break
        if hasbangpai == 0:
            cntbangpai = cntbangpai + 1
            print("cntbangpai" + str(cntbangpai))
            doingbangpai()
            clearmap()
            if cntbangpai > 2:
                break
        else:
            cntbangpai = 0

        checkdialog()
        time.sleep(1)
    return


def doingbangpai():
    print("doingbangpai")
    cnt = 0
    while True:
        cnt = cnt + 1
        print(cnt)
        if cnt > 2:
            break

        #do task
        # hanghui
        target = [u'购', u'买']
        res = checkitem(769 * 2, 663 * 2, 885 * 2, 699 * 2, target, 2, 1)
        if res is True:
            time.sleep(0.5)
            cnt = 0
            res2 = checkitem(769 * 2, 663 * 2, 885 * 2, 699 * 2, target, 2, 0)
            if res2 is True:
                cancelDialog(927 * 2, 152 * 2)

        #宝石购买
        target = [u'晌']
        res = checkitem(718 * 2, 664 * 2, 859 * 2, 697 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'派任务']
        res = checkitem(770 * 2, 443 * 2, 922 * 2, 471 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'派任务']
        res = checkitem(765 * 2, 561 * 2, 930 * 2, 590 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'派任务']
        res = checkitem(765 * 2, 261 * 2, 919 * 2, 293 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'派任务']
        res = checkitem(775 * 2, 380 * 2, 924 * 2, 409 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'派任务']
        res = checkitem(774 * 2, 320 * 2, 921 * 2, 352 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'切',u'磋']
        res = checkitem(769 * 2, 560 * 2, 924 * 2, 592 * 2, target, 8, 1)
        if res is True:
            cnt = 0

        target = [u'上', u'交']
        res = checkitem(772 * 2, 601 * 2, 882 * 2, 629 * 2, target, 3, 2)
        if res is True:
            break

        target = [u'上', u'交']
        res = checkitem(1244, 1183, 1548, 1268, target, 3, 2)
        if res is True:
            break

        # check use
        target = [u'使', u'用']
        res = checkitem(1618, 1290, 1817, 1381, target, 4, 1)
        if res is True:
            break

        target = [u'购', u'买']
        res = checkitem(746 * 2, 598 * 2, 863 * 2, 632 * 2, target, 3, 1)
        if res is True:
            time.sleep(0.5)
            cnt = 0
            res2 = checkitem(746 * 2, 598 * 2, 863 * 2, 632 * 2, target, 3, 0)
            if res2 is True:
                cancelDialog(927*2,152*2)

        res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
                if res is False:
                    falsecount = falsecount + 1
                    if falsecount > 2:
                        print("退出战斗")
                        cnt = 0
                        break
                time.sleep(2)
            break

        checkdialog()
        time.sleep(1)

        target = [u'领', u'取']
        res = checkitem(750 * 2, 499 * 2, 939 * 2, 530 * 2, target, 1, 1)
        if res is True:
            cnt = 0
    return


def waitshimen():
    print("wait shimen")
    cnt = 0
    while True:
        cnt = cnt + 1
        print(cnt)
        if cnt > 8:
            break

        #check use
        target = [u'使',u'用']
        res = checkitem(1618,1290,1817,1381,target, 4,1)
        if res is True:
            break

        #check buy daoju

        target = [u'购', u'买']
        res = checkitem(768*2, 666*2, 880*2, 698*2, target, 2, 1)
        if res is True:
            time.sleep(0.5)
            res2 = checkitem(768 * 2, 666 * 2, 880 * 2, 698 * 2, target, 2, 0)
            if res2 is True:
                cancelDialog(927 * 2, 152 * 2)

        #hanghui
        target = [u'购', u'买']
        res = checkitem(769 * 2, 663 * 2, 885 * 2, 699 * 2, target, 2,1)
        if res is True:
            time.sleep(0.5)
            res2 = checkitem(769 * 2, 663 * 2, 885 * 2, 699 * 2, target, 2, 0)
            if res2 is True:
                cancelDialog(927 * 2, 152 * 2)

        #chongwu
        target = [u'购', u'买']
        res = checkitem(1553, 1290, 1900, 1383, target, 2,1)


        target = [u'购', u'买']
        res = checkitem(752 * 2, 599 * 2, 862 * 2, 632 * 2, target, 4,1)
        if res is True:
            print("check buy teshusshimen success")


        target = [u'上', u'交']
        res = checkitem(772*2, 601*2, 882*2, 629*2, target, 3,1)
        if res is True:
            break

        target = [u'上', u'交']
        res = checkitem(1244, 1183, 1548, 1268, target, 3,1)
        if res is True:
            break

        target = [u'额', u'外']
        checkitem(752*2, 318*2, 944*2, 351*2, target, 1,1)


        target = [u'额', u'外']
        checkitem(752 * 2, 500 * 2, 944 * 2, 533 * 2, target, 1,1)

        target = [u'抽', u'奖']
        checkitem(468 * 2, 324 * 2, 544 * 2, 367 * 2, target, 2,1)


        target = [u'我', u'要', u'收', u'服', u'了', u'你', u'进', u'入', u'战', u'斗']
        res = checkitem(1445, 1100, 1950, 1192, target, 1,1)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
                if res is False:
                    falsecount = falsecount+1
                    if falsecount > 3:
                        print("退出战斗")
                        break

                time.sleep(2)
            break

        res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
                if res is False:
                    falsecount = falsecount + 1
                    if falsecount > 3:
                        print("退出战斗")
                        break

                time.sleep(2)
            break

        checkdialog()
        time.sleep(0.1)
    return

def checktaskmijing():
    checkdialog()
    x, y = pyautogui.position()
    print(x, y)
    x1 = 1574
    y1 = 503
    x2 = 1989
    y2 = 660

    print(x1, y1, x2, y2)
    target = [u'秘', u'境', u'降', u'妖', u'第', u'关', u'挑', u'战']
    res = checkitem(x1, y1, x2, y2, target, 1)
    if res is True:
        return True
    return False


def checktaskbaotu(index):
    checkdialog()
    x, y = pyautogui.position()
    print(x, y)
    x1 = 1613
    y1 = 377 + (index - 1) * 160
    x2 = 2013
    y2 = 377 + index * 160

    print(x1, y1, x2, y2, index)
    target = [u'宝', u'图', u'任', u'务', u'前', u'往', u'战', u'胜']
    res = checkitem(x1, y1, x2, y2, target, 1)
    if res is True:
        return index
    return 0


def checktaskbangpai(index):
    checkdialog()
    nextkey = 0
    x, y = pyautogui.position()
    print(x, y)
    x1 = 1613
    y1 = 377 + (index - 1) * 160
    x2 = 2013
    y2 = 377 + index * 160

    target = [u'青龙堂']
    res = checkitem(98 * 2, 751 * 2, 251 * 2, 775 * 2, target, 1, 0)
    if res is True:
        nextkey = 2
    else:
        nextkey = 1

    print(x1, y1, x2, y2, index)
    target = [u'青', u'龙', u'白', u'朱', u'雀', u'玄', u'武']
    res = checkitem(x1, y1, x2, y2, target, 1,nextkey)
    if res is True:
        doingbangpai()
        return index
    return 0


def checktask(index):
    checkdialog()
    x, y = pyautogui.position()
    print(x,y)
    strtask = ""
    x1 = 1613
    y1 = 377 + (index - 1) * 160
    x2 = 2013
    y2 = 377 + index * 160

    print(x1, y1, x2, y2, index)
    target = [u'门', u'巡', u'逻', u'购', u'买', u'战', u'胜', u'强', u'盗', u'去', u'采', u'集', u'收', u'服', u'的']
    res = checkitem(x1, y1, x2, y2, target, 1)
    if res is True:
        waitshimen()
        return index
    return 0

#shimen
def runshimen():
    print("check shimen")
    cntshimen = 0
    while True:
        hasshimen = 0
        lastindex = 0
        clearmap()
        for n in range(1, 5):
            print("find task")
            lastindex = checktask(n)
            time.sleep(0.1)
            if lastindex != 0:
                hasshimen = 1
                cntin = 0
                while True:
                    cntin = cntin+1
                    print("find task" + str(lastindex) + "cnt in" + str(cntin))
                    nowindex = checktask(lastindex)
                    time.sleep(0.1)
                    if nowindex != 0:
                        hasshimen = 1
                    if nowindex == 0 and cntin > 10:
                        break
        print("extra check shimen")
        waitshimen()
        if hasshimen == 0:
            cntshimen = cntshimen+1
            if cntshimen > 2:
                break


def waitmijing():
    print("wait waitmijing")
    cnt = 0
    while True:
        cnt = cnt + 1
        print(cnt)
        if cnt > 20:
            clickA(1917, 729)
            break

        # check use
        target = [u'秘', u'境',u'降', u'妖']
        res = checkitem(1462, 871, 1875, 938, target, 1,1)
        if res is True:
            time.sleep(1)
            target = [u'狱', u'法']
            res2 = checkitem(707*2, 174*2, 888*2, 209*2, target, 9, 0)
            if res2 is True:
                clickA(414, 777)
                botrandom()
                clickA(1093, 1099)
            else:
                target = [u'池', u'仙']
                res3 = checkitem(707 * 2, 174 * 2, 888 * 2, 209 * 2, target, 9, 0)
                if res3 is True:
                    clickA(225*2, 358*2)
                    botrandom()
                    clickA(1093, 1099)



        target = [u'点', u'击', u'空', u'白', u'处', u'返', u'回', u'主',u'界', u'面']
        res = checkitem(774, 1175, 1212, 1228, target, 7)
        if res is True:
            clickA(1917, 729)
            clickA(1917, 729)
            break;

        print("find mijing task")
        res = checktaskmijing()
        if res is True:
            time.sleep(3)
            cnt = 0

        target = [u'进', u'入', u'战', u'斗']
        res = checkitem(1543, 996, 1849, 1056, target, 1)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
                if res is False:
                    falsecount = falsecount + 1
                    if falsecount > 3:
                        print("退出战斗")
                        break

                time.sleep(2)

        res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False, 0)
                if res is False:
                    falsecount = falsecount + 1
                    if falsecount > 2:
                        print("退出战斗")
                        break

                time.sleep(2)
        checkdialog()
        time.sleep(1)


def waityabiao():
    print("wait waitmijing")
    cnt = 0
    while True:
        cnt = cnt + 1
        print(cnt)
        if cnt > 10:
            break

        res = checkimg(357*2, 44*2, 412*2, 75*2, "res2//paihang.png", False, 0)
        if res is True:
            target = [u'押', u'送', u'普', u'通', u'镖', u'银']
            res2 = checkitem(1497, 990, 1885, 1061, target, 1)
            if res2 is True:
                print("开始押镖")
                cnt = 0
        else:
            cnt = 0
            print("押镖中")

        target = [u'确', u'定']
        checkitem(1105, 893, 1321, 960, target, 1)

        checkdialog()
        time.sleep(1)
    return True

 #waitbaotu()
#点击打开活动列表

finishshimen = 0

def getactionlist(finishbaotu, finishyabiao, finishmijing, finishsanjie, finishkeju, finishbangpairenwu):

    noactioncnt = 0
    time.sleep(2)

    while True:
        checkdialog()

        target = [u'活', u'动']
        res = checkitem(940, 227, 1123, 291, target, 1)
        if res is True:
            cancelDialog(1912, 272)
            time.sleep(1)

        clickB(629, 113)
        while True:
            target = [u'活', u'动']
            res = checkitem(940, 227, 1123, 291, target, 1)
            if res is True:
                clickA(141*2, 210*2)
                time.sleep(0.3*botrandom())
                break
            else:
                time.sleep(1)
        resstr = []
        clickx = []
        clicky = []
        str1=getText(615, 390, 906, 466, 1)
        str2=getText(615, 390, 906, 466, 2)
        resstr.append(str1+str2)
        clickx.append(1070)
        clicky.append(451)
        str1 = getText(1337, 397, 1614, 472, 1)
        str2 = getText(1337, 397, 1614, 472, 2)
        resstr.append(str1 + str2)
        clickx.append(1799)
        clicky.append(451)
        str1 = getText(612, 599, 872, 668, 1)
        str2 = getText(612, 599, 872, 668, 2)
        resstr.append(str1 + str2)
        clickx.append(1065)
        clicky.append(656)
        str1 = getText(1335, 600, 1569, 671, 1)
        str2 = getText(1335, 600, 1569, 671, 2)
        resstr.append(str1 + str2)
        clickx.append(1796)
        clicky.append(660)
        str1 = getText(613, 806, 887, 881, 1)
        str2 = getText(613, 806, 887, 881, 2)
        resstr.append(str1 + str2)
        clickx.append(1066)
        clicky.append(857)
        str1 = getText(1335, 800, 1566, 877, 1)
        str2 = getText(1335, 800, 1566, 877, 2)
        resstr.append(str1 + str2)
        clickx.append(1801)
        clicky.append(861)
        doflag = 0
        for n in range(0, 6):
            print("check action:" + str(n))

            if finishyabiao == 0:
                strlist = [u'蓬', u'票', u'押', u'镖', u'运', u'锺']
                for substr in strlist:
                    if substr in resstr[n]:
                        clickB(clickx[n], clicky[n])
                        waityabiao()
                        finishyabiao = 1
                        doflag = 1
                        break
            if finishbaotu == 0:
                strlist = [u'宝', u'图']
                for substr in strlist:
                    if substr in resstr[n]:
                        clickB(clickx[n], clicky[n])
                        waitbaotu()
                        finishbaotu = 1
                        doflag = 1
                        break

            if finishsanjie == 0:
                strlist = [u'界']
                for substr in strlist:
                    if substr in resstr[n]:
                        clickB(clickx[n], clicky[n])
                        waitsanjie()
                        finishsanjie = 1
                        doflag = 1
                        break

            if finishkeju == 0:
                strlist = [u'乡', u'试']
                for substr in strlist:
                    if substr in resstr[n]:
                        clickB(clickx[n], clicky[n])
                        waitkeju()
                        finishkeju = 1
                        doflag = 1
                        break

            if finishbangpairenwu == 0:
                strlist = [u'派任务']
                for substr in strlist:
                    if substr in resstr[n]:
                        clickB(clickx[n], clicky[n])
                        waitbangpai()
                        finishbangpairenwu = 1
                        doflag = 1
                        break

            if finishmijing == 0:
                strlist2 = [u'秘', u'境',u'降']
                for substr2 in strlist2:
                    if substr2 in resstr[n]:
                        clickB(clickx[n], clicky[n])
                        time.sleep(2)
                        waitmijing()
                        doflag = 1
                        finishmijing = 1
                        break
            if doflag == 1:
                break

        if doflag == 0:
            noactioncnt += 1
            print("noactioncnt :" + str(noactioncnt))
            if noactioncnt > 3:
                target = [u'活', u'动']
                res = checkitem(940, 227, 1123, 291, target, 1)
                if res is True:
                    cancelDialog(1912, 272)
                    time.sleep(1)
                break
        else:
            noactioncnt = 0
        time.sleep(botrandom())


def checkbag():

    while True:
        print("check baoguo")
        res = checkimg(965 * 2, 648 * 2, 1015 * 2, 683 * 2, "res2//baoguo.png", False, 0)
        if res is True:
            clickA(1976, 1333)
            time.sleep(botrandom())
            clickA(1691, 1352)
            break
        checkdialog()
        time.sleep(1)

    for row in range(1, 6):
        for col in range(1, 6):
            x1l = 1046 + (col - 1)*160
            y1l = 488 + (row - 1)*160
            x1r = x1l + 120
            ylr = y1l + 120
            res = checkimg(x1l, y1l, x1r, ylr, "res2//baotu.png")
            if res is True:
                clickA(775, 990)
                waitwabao()
                return True
    return False


def checktabforUser(name):

    xstart = 170
    ystart = 880
    while True:
        findFlag = False
        for i in range(0,5):
            #clear scream
            moveex(1169, 881)
            clickRight()
            time.sleep(1)
            moveex(1279, 736)
            clicknow()
            time.sleep(1)
            moveex(1169, 881)
            # cllick
            moveex(xstart+i*50, ystart)
            clicknow()
            # change
            clickB(600, 600)
            time.sleep(1)
            try:
                locatewindow.relocatewindow()
            except:
                print (" locatewindow.relocatewindow() error")
                pass
            time.sleep(1)
            #确认主界面
            res = checkimg(357 * 2, 44 * 2, 412 * 2, 75 * 2, "res2//paihang.png", False, 0)
            if res is True:
                clickA(982*2,77*2)
                time.sleep(1)
                target = list(name)
                res2 = checkitem(140*2, 167*2, 413*2, 198*2, target, 9,0)
                if res2 is True:
                    cancelDialog(924*2, 136*2)
                    findFlag = True
                    break
                else:
                    cancelDialog(924 * 2, 136 * 2)
            else:
                cancelDialog(924 * 2, 136 * 2)
        if findFlag is True:
            print("find exit break")
            break
    return True




def waitwabao():
    print("wait wabao")
    cnt = 0
    while True:
        cnt = cnt + 1
        print(cnt)
        if cnt > 20:
            break

        # check use
        target = [u'使', u'用']
        res = checkitem(1618, 1290, 1817, 1381, target, 4, 1)
        if res is True:
            cnt = 0

        res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False,0)
        if res is True:
            print("进入战斗")
            falsecount = 0
            while True:
                res = checkimg(578*2, 55*2, 623*2,82*2 , "res2//tianzhen.png", False,0)
                if res is False:
                    falsecount = falsecount + 1
                    if falsecount > 2:
                        print("退出战斗")
                        break

                time.sleep(2)
        checkdialog()
        time.sleep(1)


def doone(finishbaotu,finishyabiao,finishmijing,finishsanjie,finishkeju,finishbangpairenwu,finishshimen):
    clickB(600, 600)
    time.sleep(1)
    locatewindow.relocatewindow()
    print("run shimen")
    if finishshimen == 0:
        runshimen()
    print("check action")
    getactionlist(finishbaotu, finishyabiao, finishmijing, finishsanjie, finishkeju, finishbangpairenwu)
    print("check wabao")
    checkbag()
    print("finish  单人任务")

if __name__ == '__main__':
    #热闹 轩岚  粉 软 果
    checktabforUser(u"热闹")
#doone()
'''
#sys.stdout = mylog.Logger("mylog.txt")
#baotu
listx = [ 215, 267, 317, 362]
listy = [ 879, 879, 879, 879]

time.sleep(2)
#close A
for num in range(1,4):
    move(listx[num], listy[num])
    time.sleep(1)
    clicknow()
    time.sleep(1)
    doone()
    time.sleep(1)
    move(listx[num], listy[num])
    time.sleep(1)
    clicknow()

'''


