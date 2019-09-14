def follow():

    import pyautogui
    import time
    import random
    import Alarm
    import sys



    Problem = 0

    if pyautogui.pixel(840, 715) != (252, 251, 251):
        Problem = 1
        l = 0
        while True:
            a = random.gauss(2, 0.1)
            if a < 1.5:
                a = 1.5
            if a > 2.5:
                a = 2.5
            time.sleep(a)
            if pyautogui.pixel(840, 715) == (252, 251, 251):
                pyautogui.click(901,715)
                time.sleep(1)
                break
            if pyautogui.pixel(206, 261) == (255,255,255):
                pyautogui.click(206, 261)
            if l == 10:
                if Alarm.alarm() == 'c':
                    pyautogui.click(901,715)
                    time.sleep(1)
                    break
                else:
                    sys.exit()
            l += 1

    return Problem
