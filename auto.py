"""
https://blog.csdn.net/longgb123/article/details/79090559 pynput
https://zhuanlan.zhihu.com/p/302592540  pyautogui
"""
import time
import pyautogui
from pynput.mouse import Listener
from util import on_move, on_scroll


# sizex,sizey=pyautogui.size()
# print(sizex,sizey)
# pyautogui.moveTo(sizex/2,sizey/2,duration=1)
# pyautogui.moveTo(0,0,duration=1)  # 左上角
# pyautogui.moveTo(sizex - 1,sizey - 1,duration=1)  # 右下角
# pyautogui.moveTo(0,0,duration=1)  # 左上角
# pyautogui.moveTo(0,0,duration=1)  # 左上角
# pyautogui.moveTo(1921,0,duration=1) # 外置显示器左上角
# pyautogui.moveTo(1921,0,duration=1) # 外置显示器左上角
# pyautogui.moveRel(100, -200, duration=0.5)

STARTWAIT = 0  # 开始时可能还在占领倒计时，不能直接开始
time.sleep(STARTWAIT)


def getsleeptime():
    return 700


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
    pyautogui.moveRel(246, -105, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(2484, 561, duration=1)
    pyautogui.click()

    # 取消  方便调试
    # pyautogui.click(2923, 115, duration=0.5)
    # pyautogui.click(3002, 70, duration=0.5)
    # 真打
    pyautogui.click(2830, 477, duration=0.5)

    # pyautogui.moveTo(3004, 579, duration=1)
    # pyautogui.click()


def pointpos(positions=[(2317, 533)]):
    lastpos = None
    for item in positions:
        print(item[0], item[1])
        if not lastpos:
            pyautogui.moveTo(item[0], item[1], duration=1)
        else:
            pyautogui.moveTo(item[0]-lastpos[0]+2497,
                             item[1]-lastpos[1]+288, duration=1)
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
