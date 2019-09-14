import pyautogui
import time
import random
import Alarm
import sys
import Check as ch



z = int(input("How many shares? "))

direction = input("Enter b to go backwards.  Any other entry will go forward. ")

##clicks on firefox window

pyautogui.click(1342,93)


##presses the down arrow a few times

if z <= 3 and direction == 'b':
    for i in range (0,9):
        pyautogui.press('down')
        time.sleep(0.2)

if direction != 'b':
    for i in range (0,6):
        pyautogui.press('down')
        time.sleep(0.2)



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

## click on the console command line
pyautogui.click(901,715)

time.sleep(2)


##type out and enter javascript functions.  These function names are short to avoid issues.

##find all visible share buttons
pyautogui.typewrite("function K() {return document.getElementsByClassName('icon share-gray');}")

time.sleep(2)

pyautogui.press('enter')

##scroll to button
pyautogui.typewrite("function R(m) { x[m].scrollIntoView(); }")

time.sleep(2)

pyautogui.press('enter')

## click on button
pyautogui.typewrite("function C(m) { x[m].click(); }")

time.sleep(2)

pyautogui.press('enter')

##find click-on-share button
pyautogui.typewrite("function W() {return document.getElementsByClassName('share-wrapper-con');}")

time.sleep(2)

pyautogui.press('enter')

## assign click-on-share button to a variable
pyautogui.typewrite("y = W()")

time.sleep(2)

pyautogui.press('enter')

##activate click-on-share button
pyautogui.typewrite("function S() { y[0].click(); }")

time.sleep(2)

pyautogui.press('enter')



## set up to go backwards
if direction == 'b':
    k = 47
    while k + 1 < z:
        pyautogui.typewrite("x = K();")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite("R({});".format(k))
        time.sleep(0.3)
        pyautogui.press('enter')
        l = 0
        time.sleep(3)
        while pyautogui.pixel(63, 237) == (248, 246, 243):
            a = random.gauss(0.45, 0.05)
            if a < 0.2:
                a = 0.2
            if a > 0.7:
                a = 0.7
            time.sleep(a)
            l += 1
            if l == 25:
                if Alarm.alarm() == 'c':
                    pyautogui.click(901,715)
                else:
                    sys.exit()
        k += 48

    if z >= 4:
        pyautogui.typewrite("x = K();")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite("R({});".format(z-4))
        time.sleep(0.3)
        pyautogui.press('enter')





time.sleep(1)

n = 0

while n < z: #############   n < z


    if direction == 'b':
        z += ch.follow()
        if z <= n:
            break
    else:
        n -= ch.follow()
        if z <= n:
            break


    if direction == 'b':
        if z%3 == 0 and z >= 4:
            pyautogui.typewrite("R({});".format(z-4))
            time.sleep(0.3)######## 6
            pyautogui.press('enter')
        if z == 3:
            pyautogui.click(215, 710)
            time.sleep(0.5)
            for i in range (0,3):
                pyautogui.press('up')
                time.sleep(0.2)
            time.sleep(0.5)
            pyautogui.click(901,715)
            time.sleep(0.5)

        pyautogui.typewrite("C({});".format(z-1))
    else:
        if n%48 == 0:
            pyautogui.typewrite("x = K();")
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(3)
        if n%3 == 0 and n >= 3:
            pyautogui.typewrite("R({});".format(n-3))
            time.sleep(0.3)######## 6
            pyautogui.press('enter')

        pyautogui.typewrite("C({});".format(n))


    time.sleep(0.3)########  1
    pyautogui.press('enter')

    l = 0
    while pyautogui.pixel(840, 715) == (252, 251, 251):
        time.sleep(0.2)
        l += 1
        if l == 25:
            print('share did not appear')
            pyautogui.press('enter')
            time.sleep(0.3)########  1
            if direction == 'b':
                pyautogui.typewrite("C({});".format(z-1))
                time.sleep(1)########  1
                pyautogui.press('enter')
            else:
                pyautogui.typewrite("C({});".format(n))
                time.sleep(1)######## 0.5
                pyautogui.press('enter')




    time.sleep(0.3)######## 0.5
    pyautogui.typewrite("S();")
    time.sleep(0.3)########  1
    pyautogui.press('enter')


    l = 0
    while pyautogui.pixel(221, 135) == (255, 255, 255):
        time.sleep(0.2)
        l += 1
        if l == 25:
            print('share still there')
            pyautogui.press('enter')
            time.sleep(0.3)########  1
            pyautogui.typewrite("S();")
            time.sleep(1)########  1
            pyautogui.press('enter')





    a = random.gauss(1, 0.1)
    if a < 0.5:
        a = 0.5
    if a > 1.5:
        a = 1.5
    time.sleep(a)




    if direction == 'b':
        z -= 1
    else:
        n += 1


pyautogui.click(463, 746)
