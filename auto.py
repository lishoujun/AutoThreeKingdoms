"""
https://blog.csdn.net/longgb123/article/details/79090559 pynput
https://zhuanlan.zhihu.com/p/302592540  pyautogui
"""
import time
import pyautogui
from pynput.mouse import Listener
from util import on_move, on_scroll


STARTWAIT = 0  # 开始时可能还在占领倒计时，不能直接开始
time.sleep(STARTWAIT)
# 攻击按钮与点击位置的偏移量
ATTACKBUTTONX = 120
ATTACKBUTTONY = -74
# 选将  默认选择第三个
SELECTX = 2387
SELECTY = 475
# 攻击确认按钮位置
ATTACKCONFIMX = 2643
ATTACKCONFIMY = 379
POSITIONFIXX = 2385
POSITIONFIXY = 232


# 攻击取消  两步操作
ATTACKCANCELX = 2714
ATTACKCANCELY = 101
ATTACKBACKX = 2790
ATTACKBACKY = 63

DEBUG = True


def getsleeptime():
    if DEBUG:
        return 1
    # TODO 根据当前时间自行计算等待时间。    规则是  占领时间+ 行军时间  默认假设行军时间在100s内
    return 400


def getpositions():
    """
    点击鼠标记录位置，滚动鼠标结束
    """
    positions = []

    def on_click(x, y, button, pressed):
        # 监听鼠标点击事件
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        if pressed:
            positions.append((x, y))

    # 连接事件以及释放
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
    print(positions)
    return positions


def atteck():
    ...
    pyautogui.click()
    pyautogui.moveRel(ATTACKBUTTONX, ATTACKBUTTONY, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(SELECTX, SELECTY, duration=1)
    pyautogui.click()
    if DEBUG:
        # 取消  方便调试
        pyautogui.click(ATTACKCANCELX, ATTACKCANCELY, duration=0.5)
        pyautogui.click(ATTACKBACKX, ATTACKBACKY, duration=0.5)
    else:
        # 真打
        pyautogui.click(ATTACKCONFIMX, ATTACKCONFIMY, duration=0.5)


def pointpos(positions=[(2317, 533)]):
    lastpos = None
    for item in positions:
        print(item[0], item[1])
        if not lastpos:
            pyautogui.moveTo(item[0], item[1], duration=1)
        else:
            pyautogui.moveTo(item[0]-lastpos[0]+POSITIONFIXX,
                             item[1]-lastpos[1]+POSITIONFIXY, duration=1)
        lastpos = item
        atteck()
        time.sleep(getsleeptime())


"""
pyautogui.moveTo(2563, 494, duration=1)
print(pyautogui.position())
pointpos([(2317, 533)])
a=[123];print(a[-1])
"""

if __name__ == '__main__':
    positions = getpositions()
    pointpos(positions)
