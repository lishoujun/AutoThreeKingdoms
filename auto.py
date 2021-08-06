import pyautogui

sizex,sizey=pyautogui.size()
print(sizex,sizey)
pyautogui.moveTo(sizex/2,sizey/2,duration=1)
pyautogui.moveTo(0,0,duration=1)  # 左上角
pyautogui.moveTo(sizex - 1,sizey - 1,duration=1)  # 右下角
pyautogui.moveTo(0,0,duration=1)  # 左上角
pyautogui.moveTo(0,0,duration=1)  # 左上角
pyautogui.moveTo(1921,0,duration=1) # 外置显示器左上角
pyautogui.moveTo(1921,0,duration=1) # 外置显示器左上角
pyautogui.moveRel(100, -200, duration=0.5)

i = 10
while i > 0:
    print(pyautogui.position())
    i = i - 1 
