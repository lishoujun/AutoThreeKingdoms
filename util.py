#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   util.py
@Time    :   2021/08/11 00:47:13
@Author  :   shoujun.li
@Version :   1.0
@Contact :   highgogo@pm.me
'''

import pyautogui


def on_move(x, y):
    # 监听鼠标移动
    # print('Pointer moved to {0}'.format((x, y)))
    ...


def on_scroll(x, y, dx, dy):
    # 监听鼠标滚轮
    # print('Scrolled {0}'.format((x, y)))
    return False


def mapmove(x, y):
    pyautogui.click(1980, 409, duration=1)
    pyautogui.click(2660, 415, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')

    pyautogui.typewrite(str(x))
    pyautogui.click(2751, 418, duration=1)
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.typewrite(str(y))
    pyautogui.click(2792, 412, duration=0.5)

def attack(x=None, y=None):
    if x == None or y == None:
        pyautogui.click(2551, 157, duration=1)


def mapattack(x, y):
    mapmove(x, y)
    attack()

if __name__ == '__main__':
    mapattack(754,1155)