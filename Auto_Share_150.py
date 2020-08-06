def share(Initial_Shares):
    import pyautogui
    import time
    import random
    import subprocess
    import Stats_Scrape as SS


    subprocess.call(['C:\\Program Files\\Mozilla Firefox\\firefox.exe'])


####Open Mozilla Window --- Homepage = Mozilla.org
    l = 0
    while True:

        if pyautogui.pixel(569, 100) == (255, 255, 255):
            break
        time.sleep(1)
        l += 1
        if l == 15:

            pyautogui.click(1350, 13)
            share(Initial_Shares)
            return 0






##Dev Tool

    l = 0
    while True:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')

        time.sleep(1)
        pyautogui.press('k')

        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')

        rgb = pyautogui.pixel(882, 189)

        if rgb == (255, 251, 214):
            time.sleep(1)
            break
        l += 1
        if l == 15:

            pyautogui.click(1350, 13)
            share(Initial_Shares)
            return 0



#####Stats

    l = 0
    while True:

        pyautogui.typewrite(\"#######\",\"_self\");")  ####### = website

        time.sleep(2)

        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(5)

####click login button
        if pyautogui.pixel(593, 603) == (65, 166, 222):
            l = 0
            while True:
                pyautogui.typewrite("document.getElementsByClassName('btn blue btn-primary')[0].click(); ")

                time.sleep(5)

                pyautogui.press('enter')
                pyautogui.press('enter')

                if pyautogui.pixel(498, 100) == (130, 36, 50):
                    break

                l += 1
                if l == 4:

                    pyautogui.click(1350, 13)
                    share(Initial_Shares)
                    return 0
            break

#####already logged in
        if pyautogui.pixel(498, 100) == (130, 36, 50):
            break

        l += 1
        if l == 3:

            pyautogui.click(1350, 13)
            share(Initial_Shares)
            return 0

    l = 0
    while True:
        Stats = SS.scrape()
        if Stats != []:
            break
        l += 1
        if l == 4:

            pyautogui.click(1350, 13)
            share(Initial_Shares)
            return 0


    pyautogui.click(901,715)
    time.sleep(1)
    pyautogui.click(901,715)
    time.sleep(1)
    pyautogui.click(901,715)

    if Initial_Shares == 0:
        Initial_Shares = int(Stats[2])

    Current_Shares = int(Stats[2])
#changed to random
#    Available_Listings = int(Stats[0])
    Available_Listings = random.randint(143,157)

################ + 5
    z = Available_Listings - 1 + 5

    last = Current_Shares - Initial_Shares





##Closet

    l = 0
    while True:

#        pyautogui.typewrite("window.open(\"#######\",\"_self\");")  ####### = website
        pyautogui.typewrite("window.open(\"#######\",\"_self\");")  ####### = website

        time.sleep(2)

        pyautogui.press('enter')
        pyautogui.press('enter')

        time.sleep(5)

        if pyautogui.pixel(498, 100) == (130, 36, 50):
            break

        l += 1
        if l == 3:

            pyautogui.click(1350, 13)
            share(Initial_Shares)
            return 0





    pyautogui.click(605, 100)
    time.sleep(1)
    pyautogui.click(605, 100)
    time.sleep(1)
    pyautogui.click(605, 100)


    while True:
        pyautogui.press('end')
        time.sleep(0.1)
        pyautogui.press('end')
        l = 0
        while pyautogui.pixel(63, 500) == (248, 246, 243):
            time.sleep(0.2)
            l += 1
            if l == 20:
                break
        if l == 20:
            break


    time.sleep(1)
    pyautogui.press('home')
    time.sleep(0.1)
    pyautogui.press('home')
    time.sleep(1)

    pyautogui.click(901,715)
    time.sleep(1)
    pyautogui.click(901,715)
    time.sleep(1)
    pyautogui.click(901,715)







    pyautogui.typewrite("x = document.getElementsByClassName('icon share-gray'); function C(m) { x[m].click(); }; y = document.getElementsByClassName('share-wrapper-con'); function S() { y[0].click(); };; ")

    time.sleep(1)

    pyautogui.press('enter')
    pyautogui.press('enter')







    while last <= z:





        pyautogui.typewrite("C({});; ".format(z))

        time.sleep(1)

        pyautogui.press('enter')
        pyautogui.press('enter')

        l = 0
        while pyautogui.pixel(622, 93) == (252, 251, 251):
            time.sleep(0.2)
            l += 1
            if l == 25:
                pyautogui.typewrite("C({});; ".format(z))
                time.sleep(1.5)
                pyautogui.press('enter')
                pyautogui.press('enter')
            if l == 50:

                pyautogui.click(1350, 13)
                share(Initial_Shares)
                return 0





        pyautogui.typewrite("S();; ")
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('enter')

        l = 0
        while True:
            if pyautogui.pixel(622, 93) == (252, 251, 251):
                time.sleep(1)
                if pyautogui.pixel(622, 93) == (252, 251, 251):
                    break
            time.sleep(0.2)
            l += 1
            if l == 35:
                a = random.gauss(1, 0.1)
                if a < 0.5:
                    a = 0.5
                if a > 1.5:
                    a = 1.5
                time.sleep(a)
                if pyautogui.pixel(214, 260) == (255,255,255):
                    z += 1
                    a = random.randint(-12, 12)
                    b = random.randint(-12, 12)
                    pyautogui.click(214 + a, 260 + b)
                    print('captcha')

                    time.sleep(2)
                    pyautogui.click(901,715)
                    time.sleep(1)
                    pyautogui.click(901,715)
                    time.sleep(1)
                    pyautogui.click(901,715)
            if l == 70:
                print('hard captcha')
                pyautogui.hotkey('win','prtsc')
                time.sleep(random.uniform(587, 643))############

                pyautogui.click(1350, 13)
                share(Initial_Shares)
                return 0


        a = random.gauss(1, 0.1)
        if a < 0.5:
            a = 0.5
        if a > 1.5:
            a = 1.5
        time.sleep(a)

        z -= 1


    time.sleep(4)


    pyautogui.click(1350, 13)
