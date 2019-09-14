import pyautogui
import time
import random
import Alarm
import sys
import Check as ch

z = int(input("How many follows? "))

##clicks on firefox window
pyautogui.click(1342,93)



##opens the firefox console.  make sure it's docked right.
pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')

time.sleep(0.5)
pyautogui.press('k')

pyautogui.keyUp('shift')
pyautogui.keyUp('ctrl')

time.sleep(4)

##check to see that the console opened
if pyautogui.pixel(1342,93) != (237, 237, 240):
    if Alarm.alarm() != 'c':
        sys.exit()

        
pyautogui.click(901,715)

time.sleep(1)




if pyautogui.pixel(825, 718) == (255, 255, 255):
    x = 809
    j = 0
else:
    x = 691
    j = 1

    
##type out and enter javascript functions.  These function names are short to avoid issues.


##find all user images and scroll to a particular one
pyautogui.typewrite("function I(m) {document.getElementsByClassName('user-image l')[m].scrollIntoView();}")

time.sleep(2.5)

pyautogui.press('enter')

##find all blue buttons that are active
pyautogui.typewrite("function K() {return document.querySelectorAll('a.auth-required.btn.blue:not(.f-hide)');}")

time.sleep(2.5)

pyautogui.press('enter')

##scroll to a button and scroll the window up
pyautogui.typewrite("function F(m) {x[m].scrollIntoView(); window.scrollBy(0, -56);}")

time.sleep(2.5)

pyautogui.press('enter')

##scroll to a button
pyautogui.typewrite("function B(m) {x[m].scrollIntoView(false);}")

time.sleep(2.5)

pyautogui.press('enter')





y = 143

n = j
z += j

pyautogui.typewrite("x = K();")

time.sleep(0.1)

pyautogui.press('enter')


while n < 6 and n < z:

    n -= ch.follow()

    pyautogui.typewrite("F({});".format(n))

    time.sleep(0.1)

    pyautogui.press('enter')

    l = 0
    while True:    #########    check for blue
        time.sleep(0.1)
        if pyautogui.pixel(x, y) == (65, 166, 222):
            break
        if l == 30:
            n -= ch.follow()
            pyautogui.typewrite("F({});".format(n))
            time.sleep(0.1)
            pyautogui.press('enter')
            l = 0
            while True:    #########    check for blue
                time.sleep(0.1)
                if pyautogui.pixel(x, y) == (65, 166, 222):
                    break
                if l == 30:
                    n = 6
                    break
                l += 1
            break
        l += 1


    if n == 6:
        break


    pyautogui.click(x,y)

    a = random.gauss(0.6, 0.05)
    if a < 0.35:
        a = 0.35
    if a > 0.85:
        a = 0.85
    time.sleep(a)

    pyautogui.click(901,715)

    time.sleep(0.5)

    n += 1



z -= j

y = 711

w = 48 + j

while True:  ##############  n < z

    k = j

    pyautogui.typewrite("x = K();")

    time.sleep(0.1)

    pyautogui.press('enter')


    while True:    ########   k < 48 and m < 1

        k -= ch.follow()

        pyautogui.typewrite("B({});".format(k))

        time.sleep(0.1)

        pyautogui.press('enter')

        l = 0
        while True:    #########    check for blue
            time.sleep(0.1)
            if pyautogui.pixel(x, y) == (65, 166, 222):
                break
            if l == 30:
                k -= ch.follow()
                pyautogui.typewrite("B({});".format(k))
                time.sleep(0.1)
                pyautogui.press('enter')
                l = 0
                while True:    #########    check for blue
                    time.sleep(0.1)
                    if pyautogui.pixel(x, y) == (65, 166, 222):
                        break
                    if l == 30:
                        k = w
                        break
                    l += 1
                break
            l += 1


        if k == w:
            break


        pyautogui.click(x,y)

        a = random.gauss(0.6, 0.05)
        if a < 0.35:
            a = 0.35
        if a > 0.85:
            a = 0.85
        time.sleep(a)

        pyautogui.click(901,715)
        pyautogui.click(901,715)

        time.sleep(0.5)

        k += 1


    if n == 6:
        n = 47
        pyautogui.typewrite("x = K();")
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.typewrite("F({});".format(j))
        time.sleep(0.1)
        pyautogui.press('enter')
        l = 0
        while True:    #########    check for blue
            time.sleep(0.1)
            if pyautogui.pixel(x, y) == (65, 166, 222):
                j += 1
                w += 1
                break
            if l == 30:
                break
            l += 1
    else:
        n += 48

    if n >= z:
        break


    pyautogui.typewrite("I({});".format(n))
    time.sleep(0.1)
    pyautogui.press('enter')
    a = random.gauss(3, 0.1)
    if a < 2.5:
        a = 2.5
    if a > 3.5:
        a = 3.5
    time.sleep(a)

    l = 0
    while pyautogui.pixel(63, 710) == (248, 246, 243):
        a = random.gauss(0.45, 0.05)
        if a < 0.2:
            a = 0.2
        if a > 0.7:
            a = 0.7
        time.sleep(a)
        l += 1
        if l == 25:
            print('new stuff did not appear.')
            if Alarm.alarm() == 'c':
                pyautogui.click(901,715)
            else:
                sys.exit()

pyautogui.click(463, 746)
