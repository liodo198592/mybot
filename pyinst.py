# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = [r'C:\Users\zhouyu\PycharmProjects\mybot\ruaruawindow.py',\
            '-F','-w',\
            r'--distpath=C:\Users\zhouyu\PycharmProjects\dist',\
            r'--workpath=C:\Users\zhouyu\PycharmProjects\mybot',\
            r'--specpath=C:\Users\zhouyu\PycharmProjects\mybot',\
            r'--icon=C:\Users\zhouyu\PycharmProjects\mybot\rua.ico',\
            r'--upx-dir','upx393w']
    run(opts)
