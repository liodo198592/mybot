# -*- coding: UTF-8 -*-
import random
import win32gui
import win32api, win32con
import ctypes




def relocatewindow():
    # 定义结构体，存储当前窗口坐标
    class RECT(ctypes.Structure):
        _fields_ = [('left', ctypes.c_int),
                    ('top', ctypes.c_int),
                    ('right', ctypes.c_int),
                    ('bottom', ctypes.c_int)]

    rect = RECT()
    HWND = win32gui.GetForegroundWindow()  # 获取当前窗口句柄
    ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))  # 获取当前窗口坐标
    win32gui.SetWindowPos(HWND, None, -6, 0, rect.right - rect.left, rect.bottom - rect.top,
                          win32con.SWP_NOSENDCHANGING | win32con.SWP_SHOWWINDOW)  # 将窗口恢复至初始位置

#relocatewindow()